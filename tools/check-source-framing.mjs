// Greps every session note for source-framing phrases AGENTS.md bans under "Source Style":
// notes must state knowledge directly, never narrate where it came from or how it's organized.
// This exists because that rule has been violated and caught by hand more than once —
// this makes the check automatic instead of relying on someone noticing.
import fs from 'fs';

const PATTERNS = [
  [/\bthe deck says\b/i, '"the deck says"'],
  [/\bthe source says\b/i, '"the source says"'],
  [/\bin the instructor'?s own words\b/i, '"in the instructor\'s own words"'],
  [/\bspoken version first\b/i, '"spoken version first"'],
  [/\bworth memou?rising verbatim\b/i, '"worth memorising verbatim"'],
  [/\bquotable\b/i, '"quotable"'],
  [/\bthe deck copied\b/i, '"the deck copied"'],
  [/\bthe deck'?s own\b/i, '"the deck\'s own"'],
  [/\bthe deck marks\b/i, '"the deck marks"'],
  [/\bthe deck'?s structure\b/i, '"the deck\'s structure"'],
  [/\bthe slides? (says?|shows?|marks?)\b/i, '"the slide(s) says/shows/marks"'],
  [/\bthe handout (says?|shows?)\b/i, '"the handout says/shows"'],
  [/\bper the (deck|handout|slides?)\b/i, '"per the deck/handout/slide"'],
  [/^\s*Reference:/im, '"Reference:" label'],
];

let hits = 0, files = 0;
for (const f of process.argv.slice(2)) {
  const short = f.split('/').slice(-3).join('/');
  const text = fs.readFileSync(f, 'utf8');
  const lines = text.split('\n');
  let fileHit = false;
  lines.forEach((line, i) => {
    for (const [re, label] of PATTERNS) {
      if (re.test(line)) {
        if (!fileHit) { console.log(`\n${short}`); fileHit = true; files++; }
        console.log(`  L${i + 1}: ${label} — "${line.trim().slice(0, 100)}"`);
        hits++;
      }
    }
  });
}
console.log(`\n${hits === 0 ? '✅' : '❌'} ${hits} source-framing violation${hits === 1 ? '' : 's'} in ${files} file${files === 1 ? '' : 's'}`);
process.exit(hits ? 1 : 0);
