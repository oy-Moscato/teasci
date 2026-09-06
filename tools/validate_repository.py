#!/usr/bin/env python3
"""Validate documentation links, source inputs, CSV shape and archive hashes.

No network requests or scientific claims verification are performed.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

for row in json.loads((ROOT/'archive/manifest.json').read_text()):
    path = ROOT/row['path']
    if not path.is_file():
        errors.append(f'Missing archive: {row["path"]}')
        continue
    raw = path.read_bytes()
    if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
        errors.append(f'Archive changed: {row["path"]}')

for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    if 'archive/reports' not in path.as_posix():
        # Remove code blocks before checking ordinary Markdown file links.
        clean = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', clean):
            if re.match(r'^(https?://|mailto:|#)', target):
                continue
            target = target.split('#')[0]
            if target and not (path.parent/target).exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
        if re.search(r'(?:cite|genui)|sandbox:/', text):
            errors.append(f'Chat-only citation/path in current Markdown: {path.relative_to(ROOT)}')

sources = json.loads((ROOT/'literature/current_sources.json').read_text())
ids = [row['id'] for row in sources]
if len(ids) != len(set(ids)):
    errors.append('Duplicate current source IDs')
for row in sources:
    if not row['primary_url'] and row['evidence_level'] != 'PENDING':
        errors.append(f'Missing source URL: {row["id"]}')

for path in ROOT.rglob('*.csv'):
    with path.open(encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))
    if not rows or any(len(r) != len(rows[0]) for r in rows):
        errors.append(f'Invalid CSV shape: {path.relative_to(ROOT)}')
    if 'templates' in path.parts and len(rows) != 1:
        errors.append(f'Template contains unexpected data: {path.relative_to(ROOT)}')

generated = [ROOT/'literature'/name for name in ['literature_index.csv','search_log.csv','question_index.csv']]
before = {p: p.read_bytes() for p in generated}
subprocess.run([sys.executable, str(ROOT/'tools/build_indexes.py')], check=True, stdout=subprocess.DEVNULL)
for path in generated:
    if before[path] != path.read_bytes():
        errors.append(f'Generated index was stale: {path.relative_to(ROOT)} (now regenerated)')

with (ROOT/'literature/question_index.csv').open(newline='',encoding='utf-8') as f:
    questions = list(csv.DictReader(f))
if len(questions) != 38 or len({r['id'] for r in questions}) != 38:
    errors.append('Historical question index does not preserve 38 unique questions')

with (ROOT/'literature/literature_index.csv').open(newline='',encoding='utf-8') as f:
    records = list(csv.DictReader(f))
if len({r['id'] for r in records}) != len(records):
    errors.append('Duplicate literature index IDs')
region_refs = [r for r in records if 'tea_region_38_' in r['source_record']]
if len(region_refs) != 38 or any(not r['source_record'].split('::')[-1].startswith('R') for r in region_refs):
    errors.append('Region report literature extraction contains missing references or problem rows')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: local links, source IDs, CSV schema, generated indexes, 38 questions and original archive hashes.')
