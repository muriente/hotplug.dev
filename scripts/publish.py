#!/usr/bin/env python3
"""Publish locally validated main to GitHub Pages, using a fast-forward branch."""
import json,os,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
REPO='https://github.com/muriente/hotplug.dev.git'
def run(*a,cwd=ROOT):return subprocess.check_output(a,cwd=cwd,text=True).strip()
if run('git','branch','--show-current')!='main' or run('git','status','--porcelain'):raise SystemExit('Publish from a clean main checkout.')
sha=run('git','rev-parse','HEAD')
if run('git','ls-remote',REPO,'refs/heads/main').split()[0]!=sha:raise SystemExit('Local main differs from remote main.')
checks=json.loads(run('gh','api','repos/muriente/hotplug.dev/commits/'+sha+'/status'))
check=next((s for s in checks['statuses'] if s['context']=='MINI / site checks'),None)
if not check or check['state']!='success' or check['creator']['login']!='muriente':raise SystemExit('Run python3 scripts/check-local.py for this exact main SHA first.')
# Temp checkout is isolated. History and prior deployment commits remain intact.
with tempfile.TemporaryDirectory(prefix='hotplug-publish-') as temp:
 target=Path(temp);run('git','init','-b','gh-pages',cwd=target);run('git','remote','add','origin',REPO,cwd=target)
 existing=run('git','ls-remote',REPO,'refs/heads/gh-pages')
 if existing:
  run('git','fetch','origin','gh-pages',cwd=target);run('git','checkout','-B','gh-pages','FETCH_HEAD',cwd=target)
  # Remove only tracked files in this disposable checkout, then copy current site.
  run('git','rm','-r','--ignore-unmatch','.',cwd=target)
 if any(p.is_symlink() for p in (ROOT/'site').rglob('*')):raise SystemExit('Symlinks are not allowed in public output.')
 shutil.copytree(ROOT/'site',target,dirs_exist_ok=True)
 (target/'version.json').write_text(json.dumps({'sha':sha,'repository':'muriente/hotplug.dev','publication':'local MINI to native GitHub Pages'})+'\n')
 run('git','add','.',cwd=target)
 staged=subprocess.run(['git','diff','--cached','--quiet'],cwd=target).returncode
 if staged:
  run('git','-c','user.name=Juan Muriente','-c','user.email=658064+muriente@users.noreply.github.com','commit','-m','Publish website source '+sha,cwd=target)
 # Last check avoids silently publishing a superseded main during a concurrent merge.
 if run('git','ls-remote',REPO,'refs/heads/main').split()[0]!=sha:raise SystemExit('Main changed; publication stopped before push.')
 run('git','push','origin','HEAD:refs/heads/gh-pages',cwd=target)
 print('Published source',sha,'as gh-pages commit',run('git','rev-parse','HEAD',cwd=target))
print('Now verify the native Pages deployment and live /version.json; a push is not acceptance.')
