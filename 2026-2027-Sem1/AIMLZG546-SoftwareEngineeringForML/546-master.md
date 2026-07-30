# AIML ZG546 · Software Engineering for Machine Learning — Master Index

4 credits · 3-0-1 · Author: Prof. Shreyas Rao · Instructors: Shreyas Suresh Rao (Lead), Komal Soni, Prashant Vaish
**Mid-sem: sessions 1–8, closed book · Comprehensive: all 16, open book**

> Revision homepage during the semester; **open-book front index** in December.

**Primary path (within this subject):** open this master first, then the session note. `_shared/` is optional background only. *(Semester-level entry is `2026-2027-Sem1/README.md` → `PROGRESS.md`.)*

## Evaluation

| EC | Component | Marks | Type | When — ✅ **confirmed in the S1 recording** |
|---|---|---|---|---|
| **EC-1** | Quiz + Situated Learning + Assignment I + Assignment II | **30** | Online | see below |
| EC-1 · Quiz | **15–20 questions, ~15 minutes** | 5 | Online | 🔴 **"just before the mid sem"** — *not* 10–20 Aug as the handout says. Covers concepts up to session 8 |
| EC-1 · Situated Learning | ⚠️ *"we are still working on the situated learning part… I'll explain later once it's finalised"* | 5 | Online | **undecided** |
| EC-1 · **Assignment I** | 🔴 **BEFORE the mid-sem** | 10 | Online | **2 weeks** to complete |
| EC-1 · Assignment II | After the mid-sem | 10 | Online | 2 weeks |
| **EC-2** | Mid-semester test | **30** | **Closed book**, 2h | **19 Sep 2026 (EN)** — *"the mid sem happens after session 7 or session 8"* |
| **EC-3** | Comprehensive exam | **40** | Open book, 2–2½h | **5 Dec 2026 (EN)** |

✅ **EC-1 RESOLVED from the session-1 recording.** *"Assignment one and assignment two — one will happen before the mid sem, another one will happen after the mid sem."* **The slide was right and the handout was wrong.** Marks confirmed: EC-1 30, EC-2 30, EC-3 40.

🔴 **Two changes to the study plan:**

1. **Assignment I (10%) lands before 19 Sep** — inside the mid-sem run-up the plan treated as clear.
2. **The quiz is NOT in the 10–20 Aug window.** It's *"15 minutes just before the mid sem"*, covering sessions up to 8. So 546 has nothing due in the August quiz window.

⚠️ **Still undecided:** whether assignments are **individual or team**. *"It may be individual perspective, or it may be a team perspective… still not decided."* He's leaning team, because *"many people are not from an industry background, so it's our job to make sure they upgrade themselves."*

**Open-book exam rules — stated precisely, and they matter for the December binding plan:**

> You may take **watermarked PPT printouts**, plus the **T1 and T2 books** — printouts allowed. Attend at the exam centre or online.

*So printed, watermarked slide decks are explicitly permitted. Confirm whether your own typed notes count before relying on them.*

**Lab environment:**

- **Virtual lab** — enabled *"after the second session"*, roughly sessions 2–3 onward. All demos, Python coding and practice labs run there.
- **AWS Console Lab** — from around **sessions 13–14**, for production deployment.
- 💰 **Both free of cost.** *"Whatever runs inside that virtual lab or AWS site will be charged — not chargeable."* Do the work inside the labs; nothing is billed to you.
- **FastAPI** was chosen for the labs — *"looking at the limitations of the virtual lab or virtual machines, FastAPI looks best for us as of now."*

**Everything is on Taxila** — course materials, announcements, assignments. PPTs and handout also on MS Teams.

## Session index

| S | Topic | Sub-topics | Source | Exam | Note file |
|---|---|---|---|---|---|
| 1 | Foundations of ML Systems Engineering | Introduction; SE process models & roles; data science pipeline & roles; ML terminology, ML pipeline, foundation models, ML domains | T1 ch1,3 · R1 | mid | `notes/S01-foundations.md` |
| 2 | Foundations (cont.) | ML in production: scope & challenges; **from models to systems**; ML and non-ML components; AI paradigms (predictive, generative, agentic); cloud-native ML systems; case studies | T1 ch1,2 · R2–R5 | mid | `notes/S02-models-to-systems.md` |
| 3 | Requirements Engineering for ML | Requirements engineering; when to use ML (ML as predictions); setting & measuring goals; goals → requirements; **GR4ML notation**. **Lab 1** | T1 ch4–7 · R6 | mid | `notes/S03-requirements.md` |
| 4 | Requirements / Architecture | Defining, composing & evaluating measures; **quality attributes of ML components**; thinking like a software architect. **Lab 2** | T1 ch8,9 | mid | `notes/S04-measures-quality.md` |
| 5 | Architecture & Design | Architectural design challenges for ML-enabled systems; common system architectures; architectural patterns for ML; **microservices pattern**; heartbeat tactic | T1 ch8 | mid | `notes/S05-architecture.md` |
| 6 | Architecture & Design | Design patterns for ML systems; **feature store pattern**; **RAG model for LLMs**. **Lab 3** | T1 ch8 | mid | `notes/S06-patterns.md` |
| 7 | Implementation & Code Sharing | Coding practices; what is good code; analysing code performance; using data structures effectively | T2 ch1–3 | mid | `notes/S07-coding.md` |
| 8 | Implementation & Code Sharing | OOP & functional programming; errors, logging & debugging; formatting & linting; **research code vs production code** | T2 ch4–6 | mid | `notes/S08-production-code.md` |
| 9 | Implementation & Code Sharing | Design & refactoring; **designing APIs for ML services**; version control, dependencies, packaging. **Lab 4** | T2 ch8,10,11 | comp | `notes/S09-apis-packaging.md` |
| 10 | Quality Assurance | Types of tests; testing for ML; testing model training; testing model inference; **model quality**; **data quality** | T1 ch14–16 | comp | `notes/S10-testing.md` |
| 11 | Quality Assurance | Pipeline quality; system quality; testing & experimentation in production; **security for ML**. **Lab 5** | T1 ch17–19 | comp | `notes/S11-production-qa.md` |
| 12 | Deployment | Docker & Kubernetes basics; deployment strategies (batch, real-time, edge); deploying a model; inference function; feature encoding & feature stores; serving infrastructure | T1 ch10 | comp | `notes/S12-deployment.md` |
| 13 | Deployment | Types of deployment models; **model cards**; stages of the ML pipeline; automating the pipeline; automation & infrastructure design; code quality & observability. **Lab 6** | T1 ch11 | comp | `notes/S13-automation.md` |
| 14 | Responsible ML Engineering | Responsible engineering; versioning, provenance & reproducibility; **explainability**; **fairness**; safety; security & privacy | T1 ch23–29 | comp | `notes/S14-responsible-ml.md` |
| 15 | SE Principles for Agentic AI | Phases of the AI-Driven Software Development Life Cycle (**ADLC**); applying SE principles to agentic AI | Lecture notes | comp | `notes/S15-agentic-se.md` |
| 16 | Agentic AI & Course Review | Important agentic AI patterns; wrap-up and review | Lecture notes | comp | `notes/S16-review.md` |

## Labs (6)

| Lab | Objective | Session ref | Done |
|---|---|---|---|
| 1 | End-to-end ML system blueprint for a real-world use case (e.g. **fraud detection** or recommendation) | 3 | ☐ |
| 2 | Requirement specifications and measurable goals using GR4ML | 4 | ☐ |
| 3 | Scalable ML architecture using microservices and feature store patterns | 6 | ☐ |
| 4 | Modular ML pipeline with versioning, packaging, experiment tracking | 9 | ☐ |
| 5 | Testing & validation framework covering data, model and system quality | 11 | ☐ |
| 6 | Automated ML pipeline with containerised deployment and orchestration | 13 | ☐ |

Plus **2 case studies**.
Tools: Prefect / Prefect Cloud, MLflow, DVC, Amazon SageMaker, Docker, Kubernetes (Minikube), FastAPI, PyTest, Evidently AI.

## Books

| | |
|---|---|
| T1 | Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, Apr 2025) |
| T2 | Nelson, *Software Engineering for Data Scientists* (O'Reilly, Apr 2024) |
| R1 | Tech Mahindra white paper — SDLC → ADLC |
| R2 | Apollo autonomous-driving ML integration case study (2020) |
| R3 | Microsoft, *Software Engineering for Machine Learning: A Case Study* (2019) |
| R4 | Schneider, *Generative to Agentic AI* (arXiv:2504.18875, 2025) |
| R5 | CNCF AI Working Group, *Cloud Native Artificial Intelligence* (2024) |
| R6 | GR4ML — https://www.cs.toronto.edu/~soroosh/gr4ml_introduction.html |

## How to study this subject

Design and judgment, least mathematical of the four. **Pick one running example on day one** and apply every single module to that same system: requirements for it, architecture for it, tests for it, deployment for it, fairness analysis for it. Lab 1 (session 3) forces this choice anyway — make it early and never change it.

**Trap:** memorising definitions in the abstract. A definition you can only recite is worth nothing in an exam that asks you to apply it.

> **Reference profile.** T1 (Kästner) and T2 (Nelson) chapters cover sessions 1–14 — the best textbook coverage of the four subjects, so a missed session is largely recoverable. **S15–S16 (agentic AI, ADLC) are lecture notes only** — deck and recording are the whole source there.
> T1 is free online: https://mlip-cmu.github.io/book/ (CC BY-NC-ND). Chapter→page map in `source/MATERIAL-LOG.md`.

**Weekday slot:** Thursday. First subject to drop if you fall behind — least cumulative, most recoverable.

## Running example

**System:** **Fraud detection** — named in the handout as the Lab 1 example. Locked in at session 1; every module applies to this same system.

## Overlap

- **549** S4–S7 (ML lifecycle, pipelines, MLOps) ≈ 546 S1–2, S13
- **549** S3/S12 (Docker, K8s, deployment) ≈ 546 S12
- **521** L10 / **536** S14 (evaluation, metrics) ≈ 546 S10–11
- **521** L15–16 / **536** S15 (ethics, bias, safety) ≈ 546 S14
- 546 S6 teaches **RAG as an architectural pattern** — the same RAG you build elsewhere, seen from the systems side. Use the overlap as revision, not as a reason to split your first-pass learning.
