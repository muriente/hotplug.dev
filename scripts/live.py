import urllib.request,json
base='https://hotplug.dev'
for path,marker in [('/',b'Your phone.'),('/guide/',b'first-time setup'),('/privacy/',b'no analytics scripts')]:
 with urllib.request.urlopen(base+path,timeout=25) as r:
  assert r.status==200 and marker.lower() in r.read().lower(),path
with urllib.request.urlopen(base+'/version.json',timeout=25) as r:
 version=json.load(r);assert len(version['sha'])==40;print('Deployed source:',version)
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args):return None
try:urllib.request.build_opener(NoRedirect).open('https://www.hotplug.dev/guide/?check=canonical',timeout=25)
except urllib.error.HTTPError as r:
 assert r.code in (301,308),r.code
 assert r.headers['Location']=='https://hotplug.dev/guide/?check=canonical',r.headers
else:raise AssertionError('www did not redirect')
print('Live content and canonical redirect passed.')
