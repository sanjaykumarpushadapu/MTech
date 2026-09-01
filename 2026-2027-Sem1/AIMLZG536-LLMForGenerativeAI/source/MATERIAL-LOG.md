# AIML ZG536 · Large Language Models for Generative AI · Material Log

**Last reconciled:** 01 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | Historically checked against S1–S2. `_handouts/AIML ZG536 COURSE HANDOUT.docx` is absent from the current checkout and accessible local paths; restore it before the next scope-changing update. |
| Raw decks, recordings, transcripts, books | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab material in `labs/`, and this material ledger. |

## Session material status

| Session | Handout topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S01 | Foundations of LLMs | ✓ Intro decks; transcript; T1/T2/R1 scope material | ✓ `notes/S01-foundations.md` | none known |
| S02 | LLM Pre-Training | ✓ Training deck; T1/R1; web references | ✓ `notes/S02-pretraining.md` | none known |
| S03 | Advancements in LLM Architecture | ✓ Architecture deck, 29 slides; T2; cited references | ✓ `notes/S03-architecture.md` | Emerging Architectures is marked as filled-in reasoning because the deck only points to it from references |
| S04–S16 | Remaining handout topics | ✗ decks not held | ☐ no notes yet | collect the deck and required references before writing |

## Reference scope

| Reference | Current scope/status |
|---|---|
| T1 Jurafsky & Martin | cited chapters only: ch2, 7, 8, 10, 11 |
| T2 Alammar & Grootendorst | cited chapters only: ch1, 2, 3, 6, 7, 8, 12 |
| R1 Raschka | cited chapters only: ch1, 2, 5, 7 |
| R2 Bahree | ch7; held |
| R3 Kimothi | ch6 for S12; still missing and tracked on `MATERIALS-WATCHLIST.md` |

## Durable decisions

- S01–S03 deck audits were completed against the held decks; temporary inventories are deleted after coverage verification.
- The handout's Relative PE and Emerging Architectures items are explicitly distinguished from direct deck teaching in the S03 note rather than silently treated as slide coverage.
- The subject note is the primary learning artifact; shared notes are optional synthesis and cannot be the only home for core material.

## Storage rule

Recordings, decks, transcripts, raw PDFs, and textbook files stay outside Git or in ignored source folders. The durable record is the note or lab README, not the raw input.
