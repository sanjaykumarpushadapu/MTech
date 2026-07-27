# Shared · Tokenization & BPE

**Status:** ☐ not started
**Written from:** 521 S1 + 536 S1 — **both taught it in session 1**
**Reused by:** 521 L11 (cost), 536 S6 (serving economics)
**Target date:** 2 Aug 2026

> ⚠️ **Closed-book scope in BOTH subjects** (521 mid-sem L1–L8, 536 mid-sem S1–8). You must be able to reproduce BPE by hand for two different exams. Highest-value shared note of the semester after `rag.md`.

## Concepts

- Why subwords · token types (word / subword / byte) · BPE · SentencePiece · tiktoken · WordPiece · token economics

## Course-specific angles

| Course | Session | Emphasis | Extra detail it adds |
|---|---|---|---|
| **521** | S1 | **Economics and conversation cost** — tokens price the conversation; context window limits dialogue length | `[UNK]` behaviour when a character is absent from base vocab (`mug` → `[UNK], ug`); the `unhug` exercise → `[un, hug]`; per-conversation cost model (~800–1,200 tokens, $0.01–0.03 on GPT-4o) |
| **536** | S1 | **Mechanism and model design** — vocabulary size vs sequence length; tokenizer choice per model | Byte tokens vs BPE; byte-level BPE (GPT-2 vocab = 256 + 50,000 merges + 1 = **50,257**); SentencePiece vs tiktoken (characters vs bytes, regex pre-split); who uses what in 2026 |

**Both decks use the identical corpus** — `hug 10, pug 5, pun 12, bun 4, hugs 5` — and reach the same three merges (`ug`, `un`, `hug`). Learn it once.

⚠️ **536 marks byte-level BPE and WordPiece as "Extra slides (Not for exams)"**; 521 does not teach them at all. So those are **out of exam scope for both** — keep them here for Lab 1 only.

## Exam scope

| Course | Mid-sem (closed) | Comprehensive (open) |
|---|---|---|
| 521 | ✅ L1 | ✅ |
| 536 | ✅ S1 | ✅ |
