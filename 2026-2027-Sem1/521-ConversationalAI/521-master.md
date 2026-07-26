# AIMLCZG521 · Conversational AI — Master Index

4 credits · 3-1-0 · Instructors: Bharathi R (Lead), S Bhagath, Anupam Purwar, Vijay Singh
**Mid-sem: L1–L8, closed book · Comprehensive: L1–L16, open book**

> This file is the revision homepage during the semester, and the **open-book front index** in December. Keep the "Note file" column accurate — in the exam it is how you find things.

## Evaluation

| EC | Component | Type | Weight | Timing |
|---|---|---|---|---|
| EC-1 | Quiz ×3 (best 2) | Open book | 10% | ⚠️ announced in class / Canvas |
| EC-1 | Assignment 1 & 2 | Open book | 20% | ⚠️ ~15 days each, announced |
| EC-2 | Mid-term | **Closed book** | 30% | ~19–20 Sep 2026 |
| EC-3 | End semester | Open book | 40% | ~early Dec 2026 |

⚠️ **No dates are published in the handout.** Strictly no makeups for quizzes and assignments. Check Canvas every Wednesday.

## Session index

| S | Topic | Sub-topics | Source | Exam | Note file | Shared |
|---|---|---|---|---|---|---|
| L1 | Foundations of Conversational AI | Chatbots → agentic systems; system lifecycle & architecture | *The Landscape of AI Agents* (2024), arXiv:2404.11584 | mid | `notes/S01-foundations.md` | → `agents.md` |
| L2 | Embeddings, Vector Search & Hybrid Retrieval | Semantic vs keyword; vector DB architecture (HNSW, ANN); BM25 + dense + RRF | Dense Passage Retrieval (Karpukhin 2020) | mid | `notes/S02-retrieval.md` | → `retrieval.md` |
| L3 | Model Landscape & Cost Engineering | LLM/MoE/SLM/SSM comparison; quantization; KV-cache; prompt caching; model routing | QLoRA (Dettmers 2023) | mid | `notes/S03-model-landscape.md` | → `quantization.md` · **536** |
| L4 | Structured Outputs & Function Calling | Native function-calling APIs (OpenAI, Anthropic); ReAct (thought-action-observation); error handling & validation | ReAct (Yao 2023) | mid | `notes/S04-function-calling.md` | → `function-calling.md` |
| L5 | Fine-Tuning & Preference Optimization | Fine-tune vs prompt engineering; QLoRA / PEFT; DPO, GRPO | DPO (Rafailov 2023) | mid | `notes/S05-finetuning.md` | → `finetuning.md` · **536** |
| L6 | Agent Memory Systems | Short-term vs long-term; hybrid architecture (SQL + vector) | MemGPT (2023) + LangGraph memory docs | mid | `notes/S06-memory.md` | → `agents.md` |
| L7–L8 | RAG: Foundations to Advanced | Processing & chunking; re-ranking & contextual retrieval; agentic RAG (routing, iteration). *Mid-term revision* | Anthropic *Contextual Retrieval* (2024) | mid | `notes/S07-08-rag.md` | → `rag.md` · **549 S10–11** |
| L9 | Agent Planning & Multi-Agent Systems | State management & planning; hierarchical & collaborative architectures; error recovery & iteration limits | MetaGPT (2024) | comp | `notes/S09-multi-agent.md` | → `agents.md` |
| L10 | Evaluation: RAG to Agents | RAG & agent metrics; LLM-as-judge pattern & limits; benchmarks | MT-Bench (2023), GAIA | comp | `notes/S10-evaluation.md` | → `evaluation.md` · **546** |
| L11 | Cost Optimization & Prompt Caching | Token economics & hidden costs; prompt caching; cache warming & invalidation; model routing | Anthropic prompt-caching docs | comp | `notes/S11-cost.md` | → `quantization.md` · **536** |
| L12 | Security & Adversarial Robustness | Prompt injection (direct & indirect) defence; PII detection & redaction; red-teaming | ⚠️ handout cites OpenAI caching docs — likely a typo; expect a security reading in class | comp | `notes/S12-security.md` | → **546 governance** |
| L13 | MCP (Model Context Protocol) Deep Dive | Client-server architecture; primitives (resources, tools, prompts); building MCP servers | MCP specification | comp | `notes/S13-mcp.md` | → `agents.md` |
| L14 | A2A & Interoperability | Agent cards; task lifecycle; protocol comparison (A2A, Agent Protocol); orchestration patterns | A2A protocol spec | comp | `notes/S14-a2a.md` | → `agents.md` |
| L15–L16 | Ethics, Governance & Bias Mitigation | Bias types & manifestations; mitigation & debiasing; self-improving agents & risks. *Final revision* | Anthropic Responsible Scaling Policy | comp | `notes/S15-16-ethics.md` | → **546** |

## Labs (10 · tentative, from handout)

| Lab | Objective | Session ref | Done |
|---|---|---|---|
| 1 | Tokenization and AI bot with tool calling | L1 | ☐ |
| 2 | Similarity metrics, text-to-speech, rule-based systems, sentiment analysis | L2 | ☐ |
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
**Weekday slot:** Wednesday. Lab weeks will overflow into Friday flex — expect this more often than for the other three subjects.

## Prerequisites (assumed by the handout)

Python · ML basics (training, inference, evaluation) · neural nets & transformers · API/JSON · precision/recall/probability.
