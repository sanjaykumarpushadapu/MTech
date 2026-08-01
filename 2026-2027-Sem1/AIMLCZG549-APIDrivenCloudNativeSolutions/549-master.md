# AIMLC ZG549 · API-driven Cloud Native Solutions — Master Index

5 credits (heaviest) · 3-1-1 · Author: Prof. Shreyas Rao · Instructors: Ankita Karmakar (Lead), Nithya Ramachandran
**Mid-sem: S1–S8, closed book · Comprehensive: all topics, open book**

> Revision homepage during the semester; **open-book front index** in December.

**Primary path (within this subject):** open this master first, then the session note. `_shared/` is optional background only. *(Semester-level entry is `2026-2027-Sem1/README.md` → `PROGRESS.md`.)*

## Evaluation

| EC | Component | Weight | Type | Date |
|---|---|---|---|---|
| EC-1 · Quiz ×1 | | **5%** | Online | ⚠️ *"duration, date, session — will let you know before itself"* — **not yet announced** |
| EC-1 · **Assignment/Mini-Project I** | | **15%** | Online | not yet announced |
| EC-1 · **Assignment/Mini-Project II** | | **15%** | Online | not yet announced |
| **EC-1 total** | | **35%** | | |
| **EC-2** | Mid-semester test | **30%** | **Closed book**, 2h | **20 Sep 2026 (FN)** · scope **contact sessions 1–8** |
| **EC-3** | Comprehensive exam | **35%** | Open book, 2½h | **6 Dec 2026 (FN)** · scope **all topics, 1–16** |

✅ **EC-1 RESOLVED from the session-1 recording.** *"You will have one quiz and two assignments… one is 15, other is also 15… so this will basically cover 35."* **The slide was right** — the handout's single "Project/Assignment 30%" is actually **two 15% assignments plus a 5% quiz**.

**Her own framing, worth noting:** *"It's a bit different from other courses, where your EC-1 will cover most — a big portion — compared to EC-2 and EC-3. EC-2 is 30 and EC-3 open book is 35%, **instead of 40**."* So 549 weights continuous assessment more heavily and its comprehensive less, relative to 546 and 521.

⚠️ **No dates announced yet for any EC-1 component.** Watch Teams.

**Everything lives in MS Teams** — *"I upload everything in MS Teams. I'll create a folder, and in the course materials everything will be uploaded — the handout, the deck for that particular session, and whatever code will be used for that session."* **Including the code.** Check the shared folder after every session.

## Session index

| S | Topic | Sub-topics | Source | Exam | Note file |
|---|---|---|---|---|---|
| 0 | **Python Programming — SELF STUDY** | Structure, variables, conditionals, functions, iteration, strings, files, lists, dicts, tuples, OOP, databases & SQL, visualising data | R1 Severance (free PDF) | prereq | `notes/S00-python-selfstudy.md` |
| 1 | API Basics | Intro to APIs; design/specify/build; RESTful standards & structure; OpenAPI spec, mocking, semantic versioning, tools; OpenAPI generators; REST vs GraphQL vs gRPC; API versioning; Google Maps / Rapid API | R2 ch1 + web | mid | `notes/S01-api-basics.md` |
| 2 | Cloud Native Application | Modern application requirements; cloud-native evolution; introducing cloud-native software; cloud-enabled vs cloud-based vs cloud-native; examples | R2 ch1, R3 ch1 | mid | `notes/S02-cloud-native.md` |
| 3 | Cloud Native Application | CNCF landscape; ecosystem overview; DevOps & GitOps; microservices & service mesh; containers & Kubernetes; serverless computing & stack; case study | R3 ch1 + web | mid | `notes/S03-ecosystem.md` |
| 4 | Data Science & Machine Learning | Big data & characteristics; DS and ML intro; data science process; ML lifecycle | Web + notes | mid | `notes/S04-ds-ml.md` |
| 5 | API-driven Cloud-native Data Pipeline | Ingestion; (pre)processing; storage; integration; monitoring & alerting; scalability & reliability. **Lab 1** | Web + notes | mid | `notes/S05-data-pipeline.md` |
| 6 | API-driven ML Pipelines | Model development & training; deployment; monitoring; scalability; MLOps practices | R4 Treveil | mid | `notes/S06-ml-pipeline.md` |
| 7 | Tools Review & ML Deployment | Tools review; case study: API-driven ML model deployment. **Lab 2** | Web + notes | mid | `notes/S07-mlops-tools.md` |
| 8 | AI & Cognitive Services — Part A | Hugging Face APIs; computer vision APIs; NLP APIs; speech recognition APIs; case study. **Lab 3** | Web + notes | mid | `notes/S08-ai-apis.md` |
| 9 | AI & Cognitive Services — Part B | What are language models; LLM / SLM; MMLU; LLMOps; LangChain | Web + notes | comp | `notes/S09-language-models.md` |
| 10–11 | Language Models — RAG | Document loading; splitting; vectorstores & embedding; retrieval mechanisms; question answering; chatbot design; RAG metrics (deflection rate, context precision, context relevance); tools/APIs; case study. **Lab 4** | Ragas docs, LangChain | comp | `notes/S10-11-rag.md` |
| 12 | Cloud Native Deployment — Part C | Docker; containers; Kubernetes; deployment strategies | Web + notes | comp | `notes/S12-deployment.md` |
| 13 | IoT & Data Analytics | Internet of Things; API integration for device communication; data analytics overview; types of analytics | Web + notes | comp | `notes/S13-iot.md` |
| 14–15 | IoT & Data Analytics (cont.) | APIs for ingestion, preprocessing, analytics, monitoring; serverless functions in IoT; tools overview; case study. **Lab 5** | Web + notes | comp | `notes/S14-15-iot-analytics.md` |
| 16 | Course Review | Review of contact sessions 1–16 | — | comp | — |

## Labs (5)

| Lab | Objective | Session ref | Done |
|---|---|---|---|
| 1 | API-based data pipeline: ingestion, pre-processing, analysis, monitoring | 5 | ☐ |
| 2 | ML pipeline: model development, training, deployment, monitoring | 7 | ☐ |
| 3 | NLP tasks (speech, translation, summarisation, generation) via cloud APIs | 8 | ☐ |
| 4 | Generative AI assistant using RAG — chatbot answering queries about an application | 11 | ☐ |
| 5 | IoT and data analytics application | 14 | ☐ |

Tools: Prefect / Prefect Cloud, MLflow, AWS SageMaker, Hugging Face APIs, OpenAI APIs, LangChain, Amazon Bedrock. Infra: Colab / open source / virtual lab.

## References

| | |
|---|---|
| R1 | Severance, *Python for Everybody* (2020) — free: https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf |
| R2 | Gough, Bryant & Auburn, *Mastering API Architecture* (O'Reilly 2023) |
| R3 | Cornelia Davis, *Cloud Native Patterns* (Manning 2019) |
| R4 | Mark Treveil, *Introducing MLOps* (O'Reilly 2021) |
| R5 | huggingface.co · langchain.com · docs.ragas.io · kubernetes.io · docker.com · landscape.cncf.io · flowiseai.com |

## How to study this subject

Breadth, not depth. Build **one layer-map** — containers → orchestration → serverless → observability — and hang each new tool on its layer with a single line of what it does. Never study internals. The labs are where the actual learning happens.
**Trap:** drowning in tools. The CNCF landscape has hundreds of logos; you need the layers, not the logos.

> ⚠️ **Reference profile — read this once.** Only sessions 1–3 cite a book (R2, R3). **Sessions 4–16 list "Web Resources, Lecture Notes" only** — there is no textbook behind those slides. A missed 549 session cannot be reconstructed from a chapter the way a 546 one can.
> **Therefore: collect the deck and the recording for every 549 session the same weekend, without exception** — including during the 27 Aug – 7 Sep crunch when notes drop to bare concept lists. These are the highest-value artifacts in the semester.

**Weekday slot:** Tuesday. Highest credit count, so this is the last subject to drop if you fall behind.

## Overlap note

Sessions 9–11 (language models, LangChain, RAG, RAG metrics) overlap with 521, and S3 previews S12. Use that overlap for faster revision after your 549 session notes exist; do not make overlap the main navigation route.
