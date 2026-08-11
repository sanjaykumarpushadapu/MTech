# AIML ZG546 · Software Engineering for Machine Learning · Material Log

Rebuilt: 10 Aug 2026.

This file records held teaching material, direct handout scope, processed outputs, and unresolved gaps. Raw decks, recordings, transcripts, and downloaded books are source inputs only; they must not be committed.

Legend: `✓` held/complete · `partial` held but incomplete · `✗` missing · `—` not applicable.

## Handout

| Item | Status |
|---|---|
| Direct handout file | ✓ `_handouts/AIML ZG546 COURSE HANDOUT-9335246709.docx` |
| Direct row verification | ✓ S1 checked directly on 10 Aug 2026 |

## Session Material Status

| Session | Handout topic and required sub-topics | Material held | Processed output | Open gap |
|---|---|---|---|---|
| S1 | Foundations of ML Systems Engineering: Introduction; Software Engineering process models and roles; Data Science pipeline and roles; Machine Learning basic terminology, ML pipeline, foundation models, and types of ML domains | ✓ `Session 1- Intro.pptx`; S01 transcript; T1 ch1,ch3; R1 | ✓ `notes/S01-foundations.md` | none known |
| S2 | Foundations of ML Systems Engineering: ML in production; models to systems; ML/non-ML components; predictive/generative/agentic AI; cloud-native ML systems; case studies | ✗ deck; T1 ch1,ch2 held; public references fetchable | ☐ | S2 deck required before writing note |
| S3 | Requirements Engineering for ML Systems | ✗ | ☐ | deck and public references required |
| S4 | Requirements Engineering for ML Systems Architecture & Design | ✗ | ☐ | deck required |
| S5 | Architecture & Design: common architecture challenges; system architectures; architectural patterns; microservices for ML; heartbeat tactic | ✗ | ☐ | deck required |
| S6 | Architecture & Design: ML design patterns; feature-store pattern; RAG model for LLMs | ✗ | ☐ | deck required |
| S7 | Implementation and Code sharing: coding practices; good code; performance analysis; data structures | ✗ | ☐ | deck required |
| S8 | Implementation and Code sharing: OOP/functional programming; errors/logging/debugging; formatting/linting; research vs production code | ✗ | ☐ | deck required |
| S9 | Implementation and Code sharing: design/refactoring; APIs for ML services; version control, dependencies, packaging | ✗ | ☐ | deck required |
| S10 | Quality Assurance: test types; ML tests; training tests; inference tests; model quality; data quality | ✗ | ☐ | deck required |
| S11 | Quality Assurance: pipeline quality; system quality; production experimentation; ML security | ✗ | ☐ | deck required |
| S12 | Deployment: Docker/Kubernetes; batch/real-time/edge deployment; model inference functions; feature stores; serving infrastructure | ✗ | ☐ | deck required |
| S13 | Deployment: deployment models; model cards; ML pipeline stages; automation; infrastructure design; code quality; observability | ✗ | ☐ | deck required |
| S14 | Responsible ML Engineering: responsible engineering; versioning, provenance, reproducibility; explainability; fairness; safety; security/privacy | ✗ | ☐ | deck required |
| S15 | Application of SE Principles for Agentic AI: ADLC phases; SE principles for agentic AI | ✗ | ☐ | lecture notes/deck required |
| S16 | Application of SE Principles for Agentic AI & Course Review: agentic AI patterns; course wrap-up and review | ✗ | ☐ | lecture notes/deck required |

## Reference Scope

| Reference | Scope/status |
|---|---|
| T1 Kästner, *Machine Learning in Production* | ch1,ch3 for S1; ch1,ch2 for S2; later chapters by handout row only |
| T2 Nelson, *Software Engineering for Data Scientists* | S7-S9 implementation/code-sharing block only: ch1-3, ch4-6, ch8,ch10,ch11 |
| R1 Tech Mahindra, *Moving from SDLC to ADLC* | S1 and later S15 support; read in full |
| R2-R6 public references | fetch when the corresponding session arrives; do not ask user unless blocked |

## Recheck Notes — 10 Aug 2026

- S01 note title matches the direct handout row.
- S01 covers the deck agenda gap: the deck did not fully teach ML terminology, ML pipeline, foundation models, or types of ML domains, so those syllabus items were filled from T1/handout scope inside the note.
- S2 remains blocked because the handout row is known but the deck is not held, and the repo rule says no deck means no note.
- Source-framing scan passes for current notes via `npm run check`.

## Storage Rule

Recordings, decks, transcripts, and raw PDFs stay outside git or in ignored source folders only. The durable record is the note/lab README, not the raw course material.
