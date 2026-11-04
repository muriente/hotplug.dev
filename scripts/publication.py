"""Copy only regular website blobs from one immutable Git source tree."""
import subprocess
from pathlib import PurePosixPath

def copy_commit_site(repo,sha,target):
    tree=subprocess.check_output(['git','ls-tree','-rz',sha,'site'],cwd=repo)
    count=0
    for entry in tree.split(b'\0'):
        if not entry:continue
        metadata,name=entry.split(b'\t',1)
        mode,kind,oid=metadata.decode('ascii').split()
        path=PurePosixPath(name.decode('utf-8'))
        if mode not in ('100644','100755') or kind!='blob':
            raise ValueError('Only regular files may be published: '+str(path))
        if path.parts[0]!='site' or len(path.parts)<2 or any(p.lower()=='.git' or p in ('.','..') for p in path.parts):
            raise ValueError('Unsafe publication path: '+str(path))
        output=target.joinpath(*path.parts[1:])
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_bytes(subprocess.check_output(['git','cat-file','blob',oid],cwd=repo))
        count+=1
    if not count:raise ValueError('Source commit contains no website files')
