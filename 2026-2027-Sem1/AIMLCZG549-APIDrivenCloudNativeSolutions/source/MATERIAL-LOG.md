# AIMLC ZG549 · API-driven Cloud Native Solutions · Material Log

Rebuilt: 10 Aug 2026.

This file records held teaching material, direct handout scope, processed outputs, and unresolved gaps. Raw decks, recordings, transcripts, and downloaded books are source inputs only; they must not be committed.

Legend: `✓` held/complete · `partial` held but incomplete · `✗` missing · `—` not applicable.

## Handout

| Item | Status |
|---|---|
| Direct handout file | ✓ `_handouts/AIML ZG549 COURSE HANDOUT.docx` |
| Direct row verification | ✓ S1, S2, S3 and labs checked on 10 Aug 2026 |

## Session Material Status

| Session | Handout topic and required sub-topics | Material held | Processed output | Open gap |
|---|---|---|---|---|
| S1 | API Basics: API introduction; design/specify/build; REST standards and structure; OpenAPI specification; mocking; semantic versioning; tools; OpenAPI generators; REST/GraphQL/gRPC; API versioning; examples | ✓ `API driven_Lecture 1_25Jul.pptx`; duplicate `Lecture 1 (1).ppt`; S01 transcript; R2 ch1 | ✓ `notes/S01-api-basics.md` | none known |
| S2 | Cloud Native Application: modern application requirements; cloud-native evolution; cloud-native software; cloud-enabled vs cloud-based vs cloud-native; examples | ✓ `Lecture 2 and 3.pptx` slides 4-17; R2 ch1; R3 ch1 | ✓ `notes/S02-cloud-native.md` | none known |
| S3 | Cloud Native Application: CNCF landscape; cloud-native ecosystem; DevOps and GitOps; microservices and service mesh; containers and Kubernetes; serverless; architecture case study | ✓ `Lecture 2 and 3.pptx` slides 18-71; R3 ch1 | ✓ `notes/S03-ecosystem.md` | none known |
| S4 | Data Science and Machine Learning | ✗ | ☐ | deck required |
| S5 | Data Science and Machine Learning: API-driven data pipeline | ✗ | ☐ | deck required |
| S6 | Data Science and Machine Learning: API-driven ML pipelines and MLOps practices | ✗; R4 book held | ☐ | deck required |
| S7 | Tools review and API-driven ML model deployment case study | ✗ | ☐ | deck required |
| S8 | AI and Cognitive Services Part-A: Basic APIs for AI applications | ✗ | ☐ | deck required |
| S9 | Not listed as new handout session content | — | ☐ | verify class plan when reached |
| S10-S11 | AI and Cognitive Services Part-B: Language Models / RAG | ✗ | ☐ | deck required |
| S12 | Cloud Native Application Deployment: Docker, containers, Kubernetes, deployment strategies | ✗ | ☐ | deck required |
| S13 | IoT and Data Analytics | ✗ | ☐ | deck required |
| S14-S15 | IoT and Data Analytics: APIs, ingestion, processing, analytics, monitoring, serverless functions, case study | ✗ | ☐ | deck required |
| S16 | Course Review and Discussion | ✗ | ☐ | deck required |

## Reference Scope

| Reference | Scope |
|---|---|
| R1 Severance, *Python for Everybody* | Module 0 self-study: ch1-10 and ch14-16 only; ch11-13 out of scope unless a lab requires them |
| R2 Gough/Bryant/Auburn, *Mastering API Architecture* | ch1 only for S1-S2 |
| R3 Davis, *Cloud Native Patterns* | ch1 only for S2-S3 |
| R4 Treveil, *Introducing MLOps* | held for S6; chapter map to build when S6 arrives |

## Recheck Notes — 10 Aug 2026

- S01, S02 and S03 note titles match the handout session titles.
- S02 and S03 use one mixed deck split by handout scope: slides 4-17 for S2 and slides 18-71 for S3.
- S01 includes the handout's `mocking` item even though it was not taught by a dedicated slide; it is filled from the OpenAPI toolchain because the handout names it explicitly.
- S03 includes a concise service-mesh subsection because the handout names it, even though the agenda/deck treatment is thin.
- Source-framing scan passes for current notes via `npm run check`.

## Storage Rule

`source/decks/` and `source/transcripts/` are ignored source-input locations. Do not stage or commit raw course material.
