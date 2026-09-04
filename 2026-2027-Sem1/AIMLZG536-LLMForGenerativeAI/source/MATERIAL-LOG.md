# AIML ZG536 · Large Language Models for Generative AI · Material Log

**Last reconciled:** 04 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | ✓ External handout Learning Plan extracted and checked; checkout copy remains absent. |
| Raw decks, recordings, transcripts, books | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab material in `labs/`, and this material ledger. |

## Session material status

| Session | Handout topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S01 | Foundations of LLMs | ✓ Intro decks; transcript; T1/T2/R1 scope material | ✓ `notes/S01-foundations.md` | none known |
| S02 | LLM Pre-Training | ✓ Training deck; T1/R1; web references | ✓ `notes/S02-pretraining.md` | none known |
| S03 | Advancements in LLM Architecture | ✓ Architecture deck, 29 slides; T2; cited references; fresh render/media audit complete | ✓ `notes/S03-architecture.md` | Emerging Architectures is marked as filled-in reasoning because the deck only points to it from references |
| S04 | LLM Finetuning | ✓ `CS-4 LLM Fine tuning.pptx`, 25 slides; fresh render/media audit complete; native source figures retained | ✓ `notes/S04-fine-tuning.md` | Distillation is handout scope with filled-in reasoning because the supplied deck has no dedicated distillation slide |
| S05–S07 | LLM Optimization & Serving; Training and Attention Efficiency | ✗ decks not held | ☐ no notes yet | collect the decks and required references before writing |
| S08–S16 | Remaining handout topics | ✗ decks not held | ☐ no notes yet | collect the deck and required references before writing |

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
- The supplied `CS-4 LLM Fine tuning.pptx` matches the updated handout S04 row, **LLM Finetuning**. The former lecture-only exception is retired; the handout's Training and Attention Efficiency topic is now S07 and remains a genuine deck gap.
- The S04 deck's reference slides are routed to the master/ledger rather than copied into the learner note; the note keeps native embedded source figures without conversion.
- The subject note is the primary learning artifact; shared notes are optional synthesis and cannot be the only home for core material.

## Storage rule

Recordings, decks, transcripts, raw PDFs, and textbook files stay outside Git or in ignored source folders. The durable record is the note or lab README, not the raw input.
