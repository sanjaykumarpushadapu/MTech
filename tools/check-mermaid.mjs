import fs from 'fs';
import { JSDOM } from 'jsdom';
const dom = new JSDOM('<!DOCTYPE html><body></body>', {pretendToBeVisual:true});
global.window = dom.window; global.document = dom.window.document;
global.HTMLElement = dom.window.HTMLElement;
global.SVGElement = dom.window.SVGElement; global.DOMPurify = null;
const mermaid = (await import('mermaid')).default;
mermaid.initialize({startOnLoad:false, securityLevel:'loose'});
const files = process.argv.slice(2);
let bad=0, tot=0;
for (const f of files){
  const txt = fs.readFileSync(f,'utf8');
  const blocks = [...txt.matchAll(/```mermaid\n([\s\S]*?)```/g)];
  for (const [i,m] of blocks.entries()){
    tot++;
    try { await mermaid.parse(m[1].replace(/^\s*> ?/gm,"")); }
    catch(e){ bad++; console.log(`\n❌ ${f.split('/').slice(-3)[0]} block ${i+1}\n   ${String(e.message||e).split('\n').slice(0,4).join('\n   ')}\n   --- source ---\n${m[1].split('\n').slice(0,4).map(l=>'   '+l).join('\n')}`); }
  }
}
console.log(`\n${tot-bad}/${tot} diagrams parse OK`);
process.exit(bad?1:0);
