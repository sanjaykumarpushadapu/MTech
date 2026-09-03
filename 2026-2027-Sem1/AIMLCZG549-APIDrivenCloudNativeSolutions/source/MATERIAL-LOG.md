# AIMLC ZG549 · API-driven Cloud Native Solutions · Material Log

**Last reconciled:** 03 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | Checked against S1–S3 and labs, and now also against S4–S7's Learning Plan rows (used to scope S04 and S05, and to confirm S06 is a genuine gap). `_handouts/AIML ZG549 COURSE HANDOUT.docx` is still absent from the current checkout; restore it before the next scope-changing update so this doesn't have to be re-sourced from an uploaded copy again. |
| Raw decks, recordings, transcripts, books | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab material in `labs/`, and this material ledger. |

## Session material status

| Session | Handout topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S00 | Python self-study | ✓ Severance source is listed in the course plan | — | self-study note not yet created |
| S01 | API Basics | ✓ Lecture 1 deck(s); transcript; R2 ch1 | ✓ `notes/S01-api-basics.md` | none known |
| S02 | Cloud Native Application | ✓ Mixed Lecture 2/3 deck, slides 4–17; R2/R3 ch1 | ✓ `notes/S02-cloud-native.md` | none known |
| S03 | Cloud Native ecosystem | ✓ Mixed Lecture 2/3 deck, slides 18–71; R3 ch1 | ✓ `notes/S03-ecosystem.md` | none known |
| S04 | Big Data & Characteristics, Data Science and ML intro, Data Science Process | ✓ Lecture 4 deck, 37 slides | ✓ `notes/S04-big-data-and-data-science.md` | none known |
| S05 | API-driven Cloud-native Data Pipeline (ingestion, processing, storage, integration, monitoring & alerting, scalability & reliability, demo) | ✓ "Lecture 5 & 6" deck, 90 slides — covers S05's sub-topics in full | ✓ `notes/S05-dataops-pipeline.md` | none known |
| S06 | API-driven ML Pipelines (model development & training, deployment, monitoring, scalability, MLOps practices) | ✗ deck not held — the "Lecture 5 & 6" deck received is DataOps/Prefect/CI-CD content only, not S6's model-development/deployment/MLOps topics | ☐ no note yet | collect S6's own deck before writing |
| S07–S16 | Tools review, AI services, LLMs/RAG, deployment, IoT, review | ✗ decks not held | ☐ no notes yet | collect each deck before writing |

## Reference scope

| Reference | Current scope/status |
|---|---|
| R1 Severance | S00 self-study; cited chapters only |
| R2 Gough/Bryant/Auburn | ch1 for S1–S2 |
| R3 Davis | ch1 for S2–S3 |
| R4 Treveil | held for S6; chapter map when S6 arrives |
| R5 public web resources | fetch when the corresponding session arrives |

## Durable decisions

- The mixed Lecture 2/3 deck is split by handout scope: **slides 4–17 → S02** and **slides 18–71 → S03**.
- The "Lecture 5 & 6" deck (90 slides, DataOps/Prefect/CI-CD/pipeline-reliability content) maps entirely to S05's handout sub-topics (ingestion, processing, storage, integration, monitoring & alerting, scalability & reliability, demo); it contains nothing on S06's core sub-topics (model development/training, model deployment, MLOps practices). The whole deck became **S05 only** — S06 remains logged as a genuine gap pending its own deck, following the same content-driven split precedent as S02/S03.
- S01–S05 notes are the current durable outputs. Sessions S06 onward require their deck before note creation.
- The subject note is the primary learning artifact; shared notes are optional synthesis and cannot be the only home for core material.

## Storage rule

`source/decks/` and `source/transcripts/` are ignored source-input locations. Do not stage or commit raw course material; keep the durable record in notes and lab READMEs.
