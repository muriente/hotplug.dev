#!/usr/bin/env python3
"""Run quality checks on MINI and attest the exact clean commit to GitHub."""
import json,os,subprocess,socket
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
def run(*args,**kwargs):return subprocess.check_output(args,text=True,**kwargs).strip()
if run('git','status','--porcelain'):raise SystemExit('Commit task changes before validating an exact source SHA.')
sha=run('git','rev-parse','HEAD')
host=run('scutil','--get','ComputerName')
if host.upper()!='MINI':raise SystemExit('Run this project quality gate on MINI; observed '+host)
context='MINI / site checks'
def status(state,description):
 subprocess.run(['gh','api','--method','POST','repos/muriente/hotplug.dev/statuses/'+sha,'-f','state='+state,'-f','context='+context,'-f','description='+description,'-f','target_url=https://github.com/muriente/hotplug.dev/commit/'+sha],check=True,stdout=subprocess.DEVNULL)
status('pending','MINI local HTML, browser/accessibility and dependency checks running')
env=os.environ.copy();env.pop('SITE_URL',None)
try:
 for cmd in [['npm','ci','--ignore-scripts'],['npm','test'],['npm','run','test:browser'],['npm','audit','--audit-level=high']]:subprocess.run(cmd,check=True,env=env)
 if run('git','rev-parse','HEAD')!=sha or run('git','status','--porcelain'):raise RuntimeError('Source changed during validation')
 status('success','MINI: HTML, 12 browser/axe checks and dependency audit passed')
except BaseException:
 status('failure','MINI checks failed or were interrupted; see local output')
 raise
print('Local validation attested:',sha)
