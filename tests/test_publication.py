import importlib.util,subprocess,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('publication',Path(__file__).resolve().parents[1]/'scripts/publication.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class PublicationTests(unittest.TestCase):
 def fixture(self,repo):
  def git(*args):return subprocess.check_output(['git',*args],cwd=repo,text=True,stderr=subprocess.DEVNULL).strip()
  git('init');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
  (repo/'site').mkdir();(repo/'site/index.html').write_text('validated original');(repo/'.gitignore').write_text('site/ignored.txt\n');git('add','.');git('commit','-m','fixture');return git
 def test_snapshot_ignores_later_edits_and_untracked_ignored_files(self):
  with tempfile.TemporaryDirectory() as temp:
   repo=Path(temp)/'repo';repo.mkdir();git=self.fixture(repo);sha=git('rev-parse','HEAD')
   (repo/'site/index.html').write_text('different working copy');(repo/'site/ignored.txt').write_text('never public');(repo/'site/untracked.txt').write_text('never public')
   out=Path(temp)/'output';out.mkdir();module.copy_commit_site(repo,sha,out)
   self.assertEqual((out/'index.html').read_text(),'validated original');self.assertEqual(sorted(p.name for p in out.iterdir()),['index.html'])
 def test_rejects_committed_symlink(self):
  with tempfile.TemporaryDirectory() as temp:
   repo=Path(temp)/'repo';repo.mkdir();git=self.fixture(repo);(repo/'site/link').symlink_to('../private');git('add','.');git('commit','-m','symlink fixture')
   out=Path(temp)/'output';out.mkdir()
   with self.assertRaises(ValueError):module.copy_commit_site(repo,git('rev-parse','HEAD'),out)
if __name__=='__main__':unittest.main()
