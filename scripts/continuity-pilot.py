#!/usr/bin/env python3
"""Read and verify this bounded pilot's portable checkpoint, without mutations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parents[1]
    record = json.loads((root / 'docs/ops/continuity-pilot/mission.json').read_text())
    artifact = record['checkpoint']['artifact']
    path = Path(artifact)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('checkpoint path must be relative to this repository')
    payload = subprocess.check_output(
        ['git', 'show', 'HEAD:' + artifact], cwd=root)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != record['checkpoint']['sha256']:
        raise ValueError('committed checkpoint hash mismatch')
    if (root / artifact).read_bytes() != payload:
        raise ValueError('working artifact differs from the committed checkpoint')
    print(json.dumps({
        'outcome': record['outcome'],
        'owner': record['owner'],
        'state': record['state'],
        'checkpoint_sha256': digest,
        'next_action': record['next_action'],
        'handoff': record['handoff'],
        'verification_seconds': round(time.monotonic() - started, 4),
        'scope': 'Git artifact verification only; no agent-session recovery claimed'
    }, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print('Checkpoint recovery failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
