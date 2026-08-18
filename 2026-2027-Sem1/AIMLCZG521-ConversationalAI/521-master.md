# AIMLCZG521 · Conversational AI — Master Index

4 credits · 3-1-0 · Instructors: Bharathi R (Lead), S Bhagath, Anupam Purwar, Vijay Singh
**Mid-sem: L1–L8, closed book · Comprehensive: L1–L16, open book**

> This file is the revision homepage during the semester, and the **open-book front index** in December.

**Primary path (within this subject):** open this master first, then the session note. `_shared/` is optional background only. *(Semester-level entry is `2026-2027-Sem1/README.md` → `PROGRESS.md`.)*

🔴 **Session 8 is a REVISION session, not new material.** Instructor, S1 recording: *"In the pre-mid sem we will complete 7 sessions, and session 8 is dedicated for revising the contents from session 1 to session 7."* So the closed-book mid-sem covers **seven sessions of new content**, not eight. **536 is the same** — its deck marks S8 as revision too. Keep the "Note file" column accurate — in the exam it is how you find things.

## Evaluation

| EC | Component | Type | Weight | Timing |
|---|---|---|---|---|
| EC-1 | **Quiz ×3 — best 2 of 3** ✅ | Open book | 10% | Announced in class / **Canvas** |
| EC-1 | Assignment 1 & 2 | Open book | 20% | ~15 days each *(slide 26 says ~3 weeks — take the longer figure as optimistic)* |
| EC-2 | Mid-term | **Closed book** | 30% | ~19–20 Sep 2026 · scope **L1–L8** |
| EC-3 | End semester | Open book | 40% | ~early Dec 2026 · scope **L1–L16** |

✅ **Quizzes: three, best two count — confirmed 27 Jul.** The handout is right; **slide 26's "×2" is wrong.**

**Why that matters, in your favour:** one bad quiz costs nothing. Sit all three; the worst is dropped. Don't skip any on the assumption it's the droppable one — you can't know which until you've taken all three.

⚠️ **Where slide 26 and the handout still disagree: assignment duration** — handout ~15 days, slide ~3 weeks. Since the slide was wrong on quizzes, **plan for 15 days.** Being early costs nothing; being late is uncorrectable — *strictly no makeups*.

**Assignment 1 (PS2 — embedding models & ANN search), Group 129, due 28 Aug 2026 — roadmap:** `ass-1/ROADMAP.md`.

> ### 📌 Note on the handout's cohort
>
> The handout held is `(S2-25_AIMLCZG521) - April 2026.pdf`, Version 2.0, dated 25/02/2025 — labelled for the **April–May** cohort, while your recordings are labelled **S1-26**. The evaluation scheme evidently carried over unchanged, so this is not a live problem.
>
> It does mean the **session plan below is inherited from that document**. It matches the current deck's course-architecture slide, so it's very likely still accurate — but if an S1-26 handout appears on Canvas, worth a two-minute diff.

Strictly **no makeups** for quizzes and assignments. All assignments are plagiarism-checked.

## Modules at a glance

The handout groups all 16 sessions into 4 themes before it lists them one by one — worth holding in your head as the shape of the course, not just a flat list of 16 topics.

| Module | Theme | Sessions |
|---|---|---|
| 1 | Foundations — embeddings, retrieval, model landscape, cost engineering | L1–L3 |
| 2 | Core Building Blocks — function calling, memory systems, RAG pipelines | L4–L8 |
| 3 | Autonomous Agents — planning, multi-agent systems, evaluation, optimization | L9–L11 |
| 4 | Production Ecosystem — security, protocols (MCP, A2A), ethics, governance | L12–L16 |

## Session index

| S | Topic | Sub-topics | Source | Exam | Note file |
|---|---|---|---|---|---|
| L1 | Foundations of Conversational AI | Chatbots → agentic systems; **7-stage lifecycle**; architecture; **tokenization/BPE**; context windows; protocols; production concerns | *The Landscape of AI Agents* (2024), arXiv:2404.11584 | mid | `notes/S01-foundations.md` |
| L2 | Embeddings, Vector Search & Hybrid Retrieval | Semantic vs keyword; vector DB architecture (HNSW, ANN); BM25 + dense + RRF | Dense Passage Retrieval (Karpukhin 2020) | mid | `notes/S02-retrieval.md` |
| L3 | Model Landscape & Cost Engineering | LLM/MoE/SLM/SSM comparison; quantization; KV-cache; prompt caching; model routing | QLoRA (Dettmers 2023) | mid | `notes/S03-model-landscape.md` |
| L4 | Structured Outputs & Function Calling | Native function-calling APIs (OpenAI, Anthropic); ReAct (thought-action-observation); error handling & validation | ReAct (Yao 2023) | mid | `notes/S04-function-calling.md` |
| L5 | Fine-Tuning & Preference Optimization | Fine-tune vs prompt engineering; QLoRA / PEFT; DPO, GRPO | DPO (Rafailov 2023) | mid | `notes/S05-finetuning.md` |
| L6 | Agent Memory Systems | Short-term vs long-term; hybrid architecture (SQL + vector) | MemGPT (2023) + LangGraph memory docs | mid | `notes/S06-memory.md` |
| L7 | RAG: Foundations to Advanced | Processing & chunking; re-ranking & contextual retrieval; agentic RAG (routing, iteration). *Mid-term revision* | Anthropic *Contextual Retrieval* (2024) | mid | `notes/S07-08-rag.md` |
| L9 | Agent Planning & Multi-Agent Systems | State management & planning; hierarchical & collaborative architectures; error recovery & iteration limits | MetaGPT (2024) | comp | `notes/S09-multi-agent.md` |
| L10 | Evaluation: RAG to Agents | RAG & agent metrics; LLM-as-judge pattern & limits; benchmarks | MT-Bench (2023), GAIA | comp | `notes/S10-evaluation.md` |
| L11 | Cost Optimization & Prompt Caching | Token economics & hidden costs; prompt caching; cache warming & invalidation; model routing | Anthropic prompt-caching docs | comp | `notes/S11-cost.md` |
| L12 | Security & Adversarial Robustness | Prompt injection (direct & indirect) defence; PII detection & redaction; red-teaming | ⚠️ handout cites OpenAI caching docs — likely a typo; expect a security reading in class | comp | `notes/S12-security.md` |
| L13 | MCP (Model Context Protocol) Deep Dive | Client-server architecture; primitives (resources, tools, prompts); building MCP servers | MCP specification | comp | `notes/S13-mcp.md` |
| L14 | A2A & Interoperability | Agent cards; task lifecycle; protocol comparison (A2A, Agent Protocol); orchestration patterns | A2A protocol spec | comp | `notes/S14-a2a.md` |
| L15–L16 | Ethics, Governance & Bias Mitigation | Bias types & manifestations; mitigation & debiasing; self-improving agents & risks. *Final revision* | Anthropic Responsible Scaling Policy | comp | `notes/S15-16-ethics.md` |

## Labs (10 · tentative, from handout)

| Lab | Objective | Session ref | Done |
|---|---|---|---|
| 1 | Tokenization and AI bot with tool calling — **notebooks in `labs/S01-…`**: BPE from scratch, Ollama `llama3` + LangChain + Tavily, ReAct agent | L1 | ☐ |
| 2 | Similarity metrics, text-to-speech, rule-based systems, sentiment analysis — **current notebook in `labs/S02-…` covers DistilBERT contextual embeddings + cosine; remaining items open** | L2 | ☐ |
| 3 | Hybrid search implementation | L3 | ☐ |
| 4 | Function calling, prompting techniques, multimodal AI | L5 & L6 | ☐ |
| 5a | LLM fine-tuning | L6 & L7 | ☐ |
| 5b | Naïve RAG | L9 | ☐ |
| 6 | Advanced RAG | L10 | ☐ |
| 7 | Guardrail implementation | L11 | ☐ |
| 8 | LLM and RAG evaluation | L12 | ☐ |
| 9 | Building agents using standard frameworks and protocols | L13 & L15 | ☐ |
| 10 | LLM orchestration | L14 | ☐ |

*(Handout numbers two different labs "5" — recorded here as 5a/5b.)*

Plus **4 webinars** (case studies).
Tools: Python, NLTK, spaCy, Jupyter, scikit-learn, OpenAI. Infra: Colab / VS Code / open source.

## How to study this subject

Build-it, not read-it. Every session is effectively a lab. Skip trying to understand from notes — write the minimal version (ReAct loop, tiny RAG, memory store, MCP server) and it clicks when the code runs.
**Trap:** reading about agents instead of coding one.

> **Reference profile.** No textbook chapters — every reference is a **public paper or spec** (ReAct, DPO, Dense Passage Retrieval, MemGPT, MetaGPT, MCP spec, A2A spec, Anthropic contextual retrieval). These can be fetched directly, so you never need to upload a 521 reference. Just give the session number.

**Weekday slot:** Wednesday. Lab weeks will overflow into Friday flex — expect this more often than for the other three subjects.

## Prerequisites (assumed by the handout)

Python · ML basics (training, inference, evaluation) · neural nets & transformers · API/JSON · precision/recall/probability.
