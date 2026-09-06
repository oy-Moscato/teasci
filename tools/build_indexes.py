#!/usr/bin/env python3
"""Build traceable literature/query/problem indexes from preserved reports.

Python standard library only. Historical records are not upgraded to newly verified
sources; repeated DOI records deliberately retain their separate provenance.
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'archive' / 'reports'


def write_csv(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean_title(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text.replace('**', '').strip()


def identifier(text):
    match = re.search(r'10\.\d{4,9}/[A-Za-z0-9._;()/:-]+', text)
    return match.group().rstrip(').;,') if match else ''


def urls(text):
    return re.findall(r'https?://[^\s<>）]+', text)


def historical_records(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    for i, line in enumerate(lines):
        row = re.match(r'^\|\s*([JCPTR]\d{2})\s*\|(.+)', line)
        block = re.match(r'^\*\*([R]\d{2})(?:｜| — )(.+)\*\*$', line)
        if row and ('http' in line or 'DOI' in line):
            cols = [p.strip() for p in line.strip('|').split('|')]
            yield row[1], clean_title(cols[1]), line, i + 1
        elif block:
            end = i + 1
            while end < len(lines) and not re.match(r'^\*\*[^*].*\*\*$', lines[end]):
                end += 1
            yield block[1], clean_title(block[2]), '\n'.join(lines[i:end]).strip(), i + 1


def build():
    literature, searches, problems = [], [], []
    old_ids = {}
    index_path = ROOT/'literature/literature_index.csv'
    if index_path.exists():
        with index_path.open(encoding='utf-8', newline='') as f:
            old_ids = {r['source_record']:r['id'] for r in csv.DictReader(f) if r['id'].startswith('H')}
    next_id = max([int(v[1:]) for v in old_ids.values()] + [0]) + 1
    for path in sorted(REPORTS.glob('*.md')):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding='utf-8')
        for local_id, title, record, line in historical_records(path):
            doi = identifier(record)
            found = urls(record)
            primary = found[0].rstrip(').;,') if found else ''
            provenance = f'{rel}::{local_id}'
            record_id = old_ids.get(provenance)
            if record_id is None:
                record_id = f'H{next_id:03d}'
                next_id += 1
            literature.append(dict(
                id=record_id, canonical_key=doi.lower() or primary,
                title=title, identifier=doi, primary_url=primary,
                kind='historical_record', evidence_level='HISTORY',
                verification_scope='历史报告原条目迁移；具体F/A/S等与范围见record_text，本次不自动升级核查深度',
                supported_claim_and_limit='', source_record=provenance,
                source_line=line, recorded_at='2026-09-05', record_text=record))
        lines = text.splitlines()
        markers = [i for i,l in enumerate(lines) if l.startswith('**') and '检索' in l]
        if markers:
            for line in lines[markers[-1]+1:]:
                q = re.match(r'^\d+[.、]\s+(.+)$', line)
                if q:
                    searches.append(dict(date='2026-09-05', query=q[1].strip().strip('`').strip(),
                                         provenance=rel))
        for match in re.finditer(r'^\*\*([A-G]\d{2})｜(.+?)\*\*$', text, re.M):
            problems.append(dict(id=match[1], question=match[2], source_record=rel,
                                 status='historical_candidate_not_committed',
                                 current_priority='以docs/CURRENT_STATE.md与docs/DECISIONS.md为准'))
    for row in json.loads((ROOT/'literature/current_sources.json').read_text()):
        literature.append(dict(
            id=row['id'], canonical_key=row['identifier'].lower() or row['primary_url'] or row['id'],
            title=row['title'], identifier=row['identifier'], primary_url=row['primary_url'],
            kind=row['kind'], evidence_level=row['evidence_level'],
            verification_scope=row['verification_scope'],
            supported_claim_and_limit=row['supported_claim_and_limit'],
            source_record=f'literature/current_sources.json::{row["id"]}', source_line='',
            recorded_at=row['recorded_at'], record_text=json.dumps(row,ensure_ascii=False)))
    for name in ['recovered_searches.json','additional_searches.json']:
        searches.extend(json.loads((ROOT/'literature'/name).read_text()))
    # Keep each exact query once, retaining all known source locations and dates.
    unique = {}
    for row in searches:
        key = re.sub(r'\s+', ' ', row['query'].strip())
        if key not in unique:
            unique[key] = dict(query=key, dates=set(), provenance=set(), occurrences=0)
        entry = unique[key]
        entry['dates'].add(row['date'])
        entry['provenance'].add(row['provenance'])
        entry['occurrences'] += 1
    old_queries = {}
    query_path = ROOT/'literature/search_log.csv'
    if query_path.exists():
        with query_path.open(encoding='utf-8', newline='') as f:
            old_queries = {r['query']:r['id'] for r in csv.DictReader(f)}
    next_query = max([int(v[1:]) for v in old_queries.values()] + [0]) + 1
    for k in unique:
        if k not in old_queries:
            old_queries[k] = f'Q{next_query:03d}'
            next_query += 1
    query_rows = [dict(id=old_queries[k], query=k, dates=';'.join(sorted(v['dates'])),
                       provenance=';'.join(sorted(v['provenance'])),
                       recovered_occurrences=v['occurrences'])
                  for k,v in unique.items()]
    write_csv(ROOT/'literature/literature_index.csv', list(literature[0]), literature)
    write_csv(ROOT/'literature/search_log.csv', list(query_rows[0]), query_rows)
    write_csv(ROOT/'literature/question_index.csv', ['id','question','source_record','status','current_priority'], problems)
    print(f'{len(literature)} literature records; {len(query_rows)} distinct recovered queries; {len(problems)} historical questions.')


if __name__ == '__main__':
    build()
