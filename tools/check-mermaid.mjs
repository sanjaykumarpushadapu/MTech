// Validates every ```mermaid block in the given Markdown files.
//   1. parse errors  — a diagram that won't render shows as raw text in the note
//   2. width warning — an LR flowchart with a long chain scrolls off the page
import fs from 'fs';
import { JSDOM } from 'jsdom';

const dom = new JSDOM('<!DOCTYPE html><body></body>', { pretendToBeVisual: true });
global.window = dom.window; global.document = dom.window.document;
global.HTMLElement = dom.window.HTMLElement; global.SVGElement = dom.window.SVGElement;

const mermaid = (await import('mermaid')).default;
mermaid.initialize({ startOnLoad: false, securityLevel: 'loose' });

const MAX_PX = 1100;   // roughly a readable column on a laptop / printed page

let bad = 0, warn = 0, tot = 0;
for (const f of process.argv.slice(2)) {
  const short = f.split('/').slice(-3).join('/');
  const blocks = [...fs.readFileSync(f, 'utf8').matchAll(/```mermaid\n([\s\S]*?)```/g)];
  for (const [i, m] of blocks.entries()) {
    tot++;
    // a fence inside a blockquote carries "> " in the raw text but not by render time
    const src = m[1].replace(/^\s*> ?/gm, '');
    try { await mermaid.parse(src); }
    catch (e) {
      bad++;
      console.log(`\n❌ PARSE  ${short} block ${i + 1}`);
      console.log('   ' + String(e.message || e).split('\n').slice(0, 3).join('\n   '));
      continue;
    }
    const head = src.trim().split('\n')[0];
    if (!/^flowchart\s+LR/.test(head)) continue;
    if (/direction\s+TB/.test(src)) continue;          // subgraph stacks vertically anyway
    const labels = [...src.matchAll(/[\[\("{]{1,2}"?(.*?)"?[\]\)"}]{1,2}/g)]
      .map(x => x[1]).filter(x => x && !x.startsWith('-'));
    const maxLabel = Math.max(0, ...labels.flatMap(l => l.split('<br/>').map(x => x.length)));
    const chain = new Set([...src.matchAll(/([A-Za-z0-9_]+)\s*[-=.]+>/g)].map(x => x[1])).size;
    const est = chain * (maxLabel * 7 + 70);
    if (est > MAX_PX) {
      warn++;
      console.log(`\n⚠️  WIDE   ${short} block ${i + 1} — ~${est}px (chain ${chain}, longest label ${maxLabel})`);
      console.log('   Use `flowchart TD`. LR is for short pipelines; 6+ nodes or long labels scroll off the page.');
    }
  }
}
console.log(`\n${tot - bad}/${tot} diagrams parse OK${warn ? ` · ${warn} too wide for LR` : ''}`);
process.exit(bad || warn ? 1 : 0);
