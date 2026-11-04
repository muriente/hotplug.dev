import { readdir, readFile, stat } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import assert from 'node:assert/strict';
import { HtmlValidate } from 'html-validate';
const root=resolve('site');
const walk=async p=>(await Promise.all((await readdir(p)).map(async n=>(await stat(join(p,n))).isDirectory()?walk(join(p,n)):join(p,n)))).flat();
const files=await walk(root);
const validator=new HtmlValidate({extends:['html-validate:recommended'],rules:{'void-style':'off','long-title':'off','svg-focusable':'off','prefer-native-element':'off','no-inline-style':'error','no-redundant-role':'off'}});
for(const file of files.filter(f=>f.endsWith('.html'))){
 const source=await readFile(file,'utf8');
 const report=await validator.validateString(source,file);
 assert(report.valid,JSON.stringify(report.results.map(r=>({file:r.filePath,messages:r.messages})),null,2));
 assert.equal((source.match(/<h1\b/g)||[]).length,1,file+' must have one h1');
 assert(!/<script\b/i.test(source),'No runtime script needed');
 assert(source.includes('rel="canonical"')&&source.includes('property="og:image"'),'Metadata missing');
 for(const [,url] of source.matchAll(/(?:href|src)="([^"]+)"/g)){
  if(!url.startsWith('/'))continue;
  const [pathname,fragment]=url.split('#');
  let target=join(root,pathname);
  if((await stat(target)).isDirectory())target=join(target,'index.html');
  assert((await stat(target)).isFile(),url);
  if(fragment)assert((await readFile(target,'utf8')).includes(`id="${fragment}"`),url);
 }
 for(const [,anchor] of source.matchAll(/href="#([^"]+)"/g))assert(source.includes(`id="${anchor}"`),anchor);
 assert((await stat(file)).size<40000,'HTML budget exceeded');
}
assert((await stat('site/assets/style.css')).size<22000,'CSS budget exceeded');
assert((await stat('site/assets/social.png')).size<200000,'Social image budget exceeded');
console.log('Validated HTML, local links/fragments, metadata, script-free pages and size budgets.');
