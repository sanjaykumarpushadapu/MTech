#!/usr/bin/env node
// Check a session note against its slide inventory.
//
//   node check-slide-coverage.mjs <inventory.md> <note.md> [--all]
//
// Reads the inventory's "| slide | title | named items |" table and reports any
// named item that does not appear in the note. Logistics slides (course
// architecture, evaluation, references, ...) are skipped by default because that
// content belongs in the subject master index, not the session note.
//
// Why this exists: coverage was repeatedly checked by *reading* the deck and
// judging "looks covered". That judgement kept passing notes that had dropped
// named items and flattened the deck's structure. Matching is not a judgement
// call, and it works from the committed inventory, so the deck does not need to
// be re-uploaded to re-run the check.

import { readFileSync } from "node:fs";

const [invPath, notePath, ...flags] = process.argv.slice(2);
if (!invPath || !notePath) {
  console.error("usage: node check-slide-coverage.mjs <inventory.md> <note.md> [--all]");
  process.exit(2);
}
const includeLogistics = flags.includes("--all");

// Titles are matched loosely because PDF text extraction corrupts characters
// (e.g. "Evaluation" can come through as "EvaluaDon"), so match on the least
// corruptible distinctive word in each logistics title.
const LOGISTICS = /disclaimer|acknowledge|course architecture|learning outcome|scheme|pre-?requisite|textbook|reference|next session|discussion|thank you|lecture overview|^bits pilani$|module-1/i;

const note = readFileSync(notePath, "utf8").toLowerCase();
const rows = readFileSync(invPath, "utf8")
  .split("\n")
  .map((l) => l.match(/^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|\s*$/))
  .filter(Boolean)
  .map((m) => ({
    slide: +m[1],
    title: m[2].trim(),
    items: m[3].split(",").map((s) => s.trim()).filter(Boolean),
  }));

if (!rows.length) {
  console.error(`no inventory rows parsed from ${invPath}`);
  process.exit(2);
}

let checked = 0;
const gaps = [];
for (const r of rows) {
  if (!includeLogistics && LOGISTICS.test(r.title)) continue;
  checked++;
  const missing = r.items.filter((i) => !note.includes(i.toLowerCase()));
  if (missing.length) gaps.push({ ...r, missing });
}

console.log(`slides checked: ${checked}  ·  fully covered: ${checked - gaps.length}`);
if (gaps.length) {
  console.log("\nnamed items not found in the note:");
  for (const g of gaps) {
    console.log(`  slide ${String(g.slide).padStart(2)} (${g.title}): ${g.missing.join(", ")}`);
  }
  console.log(
    "\nReview each: a genuine omission must be added to the note; a false positive is" +
      "\nusually PDF text corruption, a spelling variant, or a word the note phrases" +
      "\ndifferently. Prune confirmed false positives from the inventory so the signal stays clean."
  );
}
process.exit(0);
