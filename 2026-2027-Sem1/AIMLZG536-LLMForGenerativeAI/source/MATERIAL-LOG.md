# AIML ZG536 · Large Language Models for Generative AI · Material Log

**Last reconciled:** 04 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | ✓ External handout Learning Plan rows checked for Sessions 3–4; checkout copy remains absent. |
| Raw decks, recordings, transcripts, books | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab material in `labs/`, and this material ledger. |

## Session material status

| Session | Handout topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S01 | Foundations of LLMs | ✓ Intro decks; transcript; T1/T2/R1 scope material | ✓ `notes/S01-foundations.md` | none known |
| S02 | LLM Pre-Training | ✓ Training deck; T1/R1; web references | ✓ `notes/S02-pretraining.md` | none known |
| S03 | Advancements in LLM Architecture | ✓ Architecture deck, 29 slides; T2; cited references; fresh render/media audit complete | ✓ `notes/S03-architecture.md` | Emerging Architectures is marked as filled-in reasoning because the deck only points to it from references |
| S04 (lecture exception) | Handout row: Training and Attention Efficiency; Class 4 lecture: LLM Fine-tuning | ✓ Fine-tuning lecture deck, 25 slides; cited references; fresh render/media audit complete | ✓ `notes/S04-fine-tuning.md` | Lecture content is intentionally recorded as a special case and is not treated as the standard handout S04 topic |
| S05–S16 | Remaining handout topics | ✗ decks not held | ☐ no notes yet | collect the deck and required references before writing |

## Reference scope

| Reference | Current scope/status |
|---|---|
| T1 Jurafsky & Martin | cited chapters only: ch2, 7, 8, 10, 11 |
| T2 Alammar & Grootendorst | cited chapters only: ch1, 2, 3, 6, 7, 8, 12 |
| R1 Raschka | cited chapters only: ch1, 2, 5, 7 |
| R2 Bahree | ch7; held |
| R3 Kimothi | ch6 for S12; still missing and tracked on `MATERIALS-WATCHLIST.md` |

## Durable decisions

- S01–S04 deck audits were completed against the held decks; temporary inventories are deleted after coverage verification.
- The handout's Relative PE and Emerging Architectures items are explicitly distinguished from direct deck teaching in the S03 note rather than silently treated as slide coverage.
- S03's four numbered Part headings use the handout sub-topic wording; the note preserves the deck's source order and native instructional figures as PNG derivatives. Supplementary emerging-architecture context is kept outside the numbered Parts because the deck provides no dedicated worked slide for it.
- Class 4 is an explicit lecture-scope exception: the supplied deck teaches LLM Fine-tuning instead of the handout's standard S04 Training and Attention Efficiency row. `notes/S04-fine-tuning.md` follows the lecture deck and records the mismatch at the top of the note.
- The subject note is the primary learning artifact; shared notes are optional synthesis and cannot be the only home for core material.

## Storage rule

Recordings, decks, transcripts, raw PDFs, and textbook files stay outside Git or in ignored source folders. The durable record is the note or lab README, not the raw input.
