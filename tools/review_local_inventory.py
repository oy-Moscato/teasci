#!/usr/bin/env python3
"""Offline review of the uploaded evidence; no camera, ROS or training runs.

Requires already available numpy and Pillow. Prints JSON to stdout.
Saved axes support aggregate recalculation; refitting saved points is a
separate, explicitly parameterized check, not a recreation of the experiment.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys

import numpy as np
from PIL import Image

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'evidence/local_inventory'
SOURCE_COMMIT = '4c03ab1b49685e8a6d34341d63861736446141d2'
MAIN_COMMIT = '4b9e436320edd187326884b16e1a8e6f9f47af6d'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(ref, path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], cwd=ROOT)


def review():
    hashes = []
    for line in (EVIDENCE / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        hashes.append({'path': name, 'matches': digest((EVIDENCE / name).read_bytes()) == expected.lower()})
    archives = []
    for row in json.loads(git_blob(MAIN_COMMIT, 'archive/manifest.json')):
        data = git_blob(MAIN_COMMIT, row['path'])
        archives.append({'path': row['path'], 'matches': digest(data) == row['sha256'] and len(data) == row['bytes']})

    geometry_path = EVIDENCE / 'abot_proxy/geometry/stem_axis_geometry.py'
    spec = importlib.util.spec_from_file_location('reviewed_geometry', geometry_path)
    geometry = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(geometry)
    result = json.loads((EVIDENCE / 'abot_proxy/geometry/final_30frames.json').read_text())
    accepted = [row for row in result['frames'] if row['accepted']]
    aggregate = geometry.summarize_axis_frames([row['axis'] for row in accepted], result['attempted_frames'])
    refits = []
    # Function default and live-script default; the original invocation is absent.
    for threshold in (0.015, 0.020):
        differences = []
        for row in accepted:
            fitted = geometry.fit_oriented_axis(row['keypoints_xyz'], order=np.arange(4), residual_threshold_m=threshold)
            angle = float(np.degrees(np.arccos(np.clip(np.dot(row['axis'], fitted['axis']), -1, 1))))
            residual_delta = abs(row['residual_p95_m'] - fitted['residual_p95_m'])
            if angle > 1e-5 or residual_delta > 1e-9:
                differences.append({'frame_index': row['index'], 'axis_difference_deg': angle,
                                    'saved_residual_p95_mm': row['residual_p95_m'] * 1000,
                                    'refitted_residual_p95_mm': fitted['residual_p95_m'] * 1000})
        refits.append({'threshold_m': threshold, 'different_frames': len(differences), 'differences': differences})

    code = geometry_path.read_bytes()
    lf = code.replace(b'\r\n', b'\n')
    historical_hash = '8e7c692a6de6fe6656883af23077ab6f0042c4e0aa8c8d09c68c81ca9cb928de'
    frames = [json.loads(line) for line in (EVIDENCE / 'camera_session_82_frames/frames_first3_last3_EXCERPT.jsonl').read_text().splitlines()]
    sample = EVIDENCE / 'camera_session_82_frames/frame_00000000'
    rgb = np.asarray(Image.open(sample / 'rgb_00000000.png'))
    depth = np.asarray(Image.open(sample / 'depth_00000000.png'))
    mask = np.asarray(Image.open(sample / 'invalid_mask_00000000.png'))
    scan = json.loads((EVIDENCE / 'abot_proxy/scan/manifest.json').read_text())
    views = sorted(scan['ranked'], key=lambda row: row['index'])
    return {
        'source_evidence_commit': SOURCE_COMMIT, 'checked_main_commit': MAIN_COMMIT,
        'scope': 'offline_uploaded_files_only_no_new_experiment',
        'runtime': {'numpy': np.__version__, 'pillow': Image.__version__},
        'evidence_hashes': hashes, 'main_archive_git_blob_hashes': archives,
        'geometry': {
            'accepted_frames': len(accepted), 'attempted_frames': result['attempted_frames'],
            'unique_accepted_stamps': len({row['stamp'] for row in accepted}),
            'accepted_span_s': max(row['stamp'] for row in accepted) - min(row['stamp'] for row in accepted),
            'angular_median_deg': aggregate['angular_median_deg'],
            'angular_p95_deg': aggregate['angular_p95_deg'],
            'frame_residual_p95_median_mm': float(np.median([row['residual_p95_m'] for row in accepted]) * 1000),
            'rejected_frames': [row for row in result['frames'] if not row['accepted']],
            'historical_code_hash': historical_hash, 'uploaded_code_hash': digest(code),
            'historical_hash_matches_either_line_ending': historical_hash in (digest(lf), digest(lf.replace(b'\n', b'\r\n'))),
            'refit_checks': refits,
        },
        'camera_sample': {
            'rgb_shape': list(rgb.shape), 'depth_shape': list(depth.shape), 'depth_dtype': str(depth.dtype),
            'nonzero_depth_ratio': float((depth > 0).mean()),
            'mask_values': np.unique(mask).tolist(), 'mask_valid_ratio': float((mask == 0).mean()),
            'mask_zero_depth_disagreement_pixels': int(((depth == 0) != (mask > 0)).sum()),
            'stored_valid_ratio': frames[0]['depth_valid_ratio'],
            'excerpt_frame_ids': [row['frame_id'] for row in frames],
            'excerpt_sync_delta_ms': [row['sync_delta_ms'] for row in frames],
            'excerpt_qc_pass': [row['qc_pass'] for row in frames],
            'domain_tags': sorted({row['domain_tag'] for row in frames}),
        },
        'scan': {
            'count': len(views), 'unique_angles': len({(row['yaw'], row['pitch']) for row in views}),
            'unique_stamps': len({row['stamp'] for row in views}),
            'span_s': views[-1]['stamp'] - views[0]['stamp'],
            'records_with_raw_file': sum('raw_file' in row for row in views),
            'records_with_depth_field': sum(any('depth' in key for key in row) for row in views),
            'manifest_order': 'score_ranked_use_index_for_time_order',
        },
    }


if __name__ == '__main__':
    print(json.dumps(review(), ensure_ascii=False, indent=2, allow_nan=False))
