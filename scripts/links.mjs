import {readdir,readFile} from 'node:fs/promises';
const urls=new Set();
for(const f of ['site/index.html','site/guide/index.html','site/privacy/index.html']){
 for(const [,u]of(await readFile(f,'utf8')).matchAll(/href="(https:[^"]+)"/g))if(!u.startsWith('https://hotplug.dev'))urls.add(u);
}
let failed=false;
for(const url of urls){
 try{const r=await fetch(url,{method:'GET',redirect:'follow',signal:AbortSignal.timeout(25000),headers:{'user-agent':'Hotplug-website-link-check'}});await r.body?.cancel();
 // Private security reporting intentionally requires GitHub sign-in.
 const expectedPrivate=url.endsWith('/security/advisories/new')&&r.status===404;
 console.log(`${r.status} ${url}${expectedPrivate?' (sign-in required)':''}`);
 if(!r.ok&&!expectedPrivate)failed=true;
 }catch(e){console.error(url,e.message);failed=true;}
}
if(failed)process.exitCode=1;
