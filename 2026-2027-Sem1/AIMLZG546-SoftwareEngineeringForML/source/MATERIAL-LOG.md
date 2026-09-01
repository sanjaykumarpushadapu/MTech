# AIML ZG546 · Software Engineering for Machine Learning · Material Log

**Last reconciled:** 01 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | Historically checked against S1. `_handouts/AIML ZG546 COURSE HANDOUT-9335246709.docx` is absent from the current checkout and accessible local paths; restore it before the next scope-changing update. |
| Raw decks, recordings, transcripts, books | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab material in `labs/`, and this material ledger. |

## Session material status

| Session | Handout topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S01 | Foundations of ML Systems Engineering | ✓ Intro deck; transcript; T1 ch1/ch3; R1 | ✓ `notes/S01-foundations.md` | none known |
| S02 | Foundations continued: models to systems and cloud-native ML | ✗ deck not held | ☐ no note | collect deck before writing |
| S03–S16 | Requirements, architecture, implementation, QA, deployment, responsible and agentic ML | ✗ decks not held | ☐ no notes yet | collect each deck and cited references before writing |

## Reference scope

| Reference | Current scope/status |
|---|---|
| T1 Kästner | ch1/ch3 for S1; ch1/ch2 for S2; later chapters only when the handout cites them |
| T2 Nelson | implementation/code-sharing sessions only |
| R1 Tech Mahindra SDLC → ADLC | S1 and later S15 support; read in full |
| R2–R6 public references | fetch when the corresponding session arrives; do not request them unless blocked |

## Durable decisions

- S01 is the only currently processed 546 session. The no-deck/no-note rule remains active for S02 onward.
- Public references can supplement a held deck, but they do not create a new session scope or replace the missing deck.
- The subject note is the primary learning artifact; shared notes are optional synthesis and cannot be the only home for core material.

## Storage rule

Recordings, decks, transcripts, raw PDFs, and textbook files stay outside Git or in ignored source folders. The durable record is the note or lab README, not the raw input.
