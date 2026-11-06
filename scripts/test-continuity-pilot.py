#!/usr/bin/env python3
"""Reproduce a synthetic interruption and corruption checks in a disposable clone."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='hotplug-continuity-') as directory:
    recovery = Path(directory) / 'recovery'
    subprocess.run(['git', 'clone', '--quiet', '--no-hardlinks', str(root),
                    str(recovery)], check=True)
    # A disposable producer exits after its durable checkpoint already exists.
    # This is a process-boundary fixture, not a live agent/session interruption.
    interrupted = subprocess.run([
        sys.executable, '-c',
        'import os,pathlib; '
        'assert pathlib.Path("docs/ops/continuity-pilot/mission.json").exists(); '
        'os._exit(23)'], cwd=recovery)
    assert interrupted.returncode == 23
    start = time.monotonic()
    verified = subprocess.run([sys.executable, 'scripts/continuity-pilot.py'],
                              cwd=recovery, capture_output=True, text=True)
    seconds = time.monotonic() - start
    assert verified.returncode == 0, verified.stderr
    data = json.loads(verified.stdout)
    assert data['handoff']['state'] == 'pending; not acknowledged'
    artifact = recovery / 'docs/ops/continuity-pilot/sample.txt'
    original = artifact.read_bytes()
    artifact.write_bytes(original + b'\nsynthetic corruption\n')
    altered = subprocess.run([sys.executable, 'scripts/continuity-pilot.py'],
                             cwd=recovery, capture_output=True, text=True)
    assert altered.returncode == 1 and 'differs' in altered.stderr
    artifact.unlink()
    missing = subprocess.run([sys.executable, 'scripts/continuity-pilot.py'],
                             cwd=recovery, capture_output=True, text=True)
    assert missing.returncode == 1 and 'failed' in missing.stderr
    print(json.dumps({'synthetic_interruption_exit': interrupted.returncode,
                      'fresh_process_recovery_seconds': round(seconds, 4),
                      'altered_artifact_rejected': True,
                      'missing_artifact_rejected': True,
                      'pending_handoff_preserved': True}, indent=2))
