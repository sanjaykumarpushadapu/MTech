# AIML ZG536 · Large Language Models for Generative AI — Master Index

4 credits · 3-1-0 · Author: Prof. Monali Mavani · Instructors: Monali Tushar Mavani (Lead), Akash Goel, S. Prabakeran, Rahil N Modi
**Mid-sem: sessions 1–8, closed book · Comprehensive: all 16, open book**

> Revision homepage during the semester; **open-book front index** in December.

**Primary path (within this subject):** open this master first, then the session note. `_shared/` is optional background only. *(Semester-level entry is `2026-2027-Sem1/README.md` → `PROGRESS.md`.)*

## Evaluation

| EC | Component | Type | Weight | Date |
|---|---|---|---|---|
| EC-1 | ~~Quiz~~ | — | — | ❌ **NO QUIZZES.** Instructor, S1 recording: *"I'm repeating there are no quizzes for this course."* |
| EC-1 | **Assignment 1 & 2** — **group**, together forming one end-to-end project | Online | **35%** | Plan shared ~week 2 |
| EC-2 | Mid-semester test | **Closed book** | **30 marks** | **20 Sep 2026 (EN)**, 2h |
| EC-3 | Comprehensive exam | Open book | **35 marks** | **6 Dec 2026 (EN)**, 2½h |

✅ **EC-1 RESOLVED from the session-1 recording** (25 Jul 2026). The handout's "Quiz 5% + Assignment 30%" is superseded — the instructor stated the quiz split three times. Weights confirmed: EC-2 30, EC-3 35.

**How the assignments work** — stated in class, in no written source:

- **Group assignments**, not individual. *"You have to create your own groups"* — Ops creates a placeholder.
- **Assignments 1 and 2 are designed to combine into one complete end-to-end project.** Don't treat them as separate.
- For each assignment she gives **two problem statements on two different topics**, plus **five or six enterprise case-study options**. **You choose.**
- Everything assigned **is covered in webinars or classes** first.
- She supplies lab sheets as Jupyter notebooks with **"80, 90% of the code readily available."**

🔴 **Assignments must run on the BITS remote lab, not your laptop.** *"In laptop, no — you have to use the remote lab for the assignments."* A manual will be shared. No time limit on the lab, but expect contention near deadlines. Colab works only for very small models.

## Session index

| S | Topic | Sub-topics | Source | Exam | Note file |
|---|---|---|---|---|---|
| 1 | Foundations of Large Language Models (LLMs) | Introduction to LLMs and Generative AI; attention mechanism & transformer (review); building blocks of LLM; LLM architectures; **tokenization**; LLM landscape | T1 ch2,7,8 · T2 ch1,2,3 · R1 ch1,2 | mid | `notes/S01-foundations.md` |
| 2 | LLM Pre-Training | Pre-training objectives; pre-training data; continuous pre-training (CPT) & domain adaptation; **scaling laws**; frontier model pretraining | T1 ch7,8 · R1 ch2,5 | mid | `notes/S02-pretraining.md` |
| 3 | Advancements in LLM Architecture | Normalization (LayerNorm, RMSNorm, placement); positional encoding (relative PE, **RoPE**, NoPE); activations (GELU, Swish, GLU, SwiGLU); **MoE** sparse activation & routing; emerging architectures | T2 ch3 · papers | mid | `notes/S03-architecture.md` |
| 4 | Training & Attention Efficiency | Memory bottlenecks; mixed-precision training; IO-aware attention (**FlashAttention**); long context (Ring Attention); efficiency variants (sliding window, sparse, linear) | T2 ch3 · papers | mid | `notes/S04-efficiency.md` |
| 5 | LLM Optimization & Serving I | Two-phase inference; **decoding strategies** (greedy, beam, top-k, top-p, temperature); inference bottlenecks; **KV-caching** & memory optimization (MQA, GQA, MLA) | T1 ch7,8 · T2 ch3 · R1 ch5 | mid | `notes/S05-inference.md` |
| 6 | LLM Optimization & Serving II | Model compression (**quantization**, pruning, pipeline); speculative decoding; production serving (continuous/in-flight batching, chunked prefill, paged attention); production metrics & economics | Papers, web | mid | `notes/S06-serving.md` |
| 7 | LLM Finetuning | Full FT; **SFT**; instruction FT; prompt & prefix tuning; **PEFT (LoRA, QLoRA, adapters)**; model merging; distillation | T1 ch7,10 · T2 ch12 · R1 ch7 | mid | `notes/S07-finetuning.md` |
| 8 | **Revision** | Consolidation of sessions 1–7 | — | mid | `notes/S08-revision.md` |
| 9 | Preference Alignment | Why alignment; preference data collection; **RLHF** (reward modelling, PPO); RL-free (**DPO** & variants, **GRPO**); Constitutional AI & RLAIF | T1 ch10 · T2 ch12 · papers | comp | `notes/S09-alignment.md` |
| 10 | Prompt Engineering & Reasoning I | Prompt components (role, instruction, context, examples, output format, tabular serialization); paradigms (zero-shot, few-shot, instruction, self-consistency); **in-context learning**; prompt engineering as system design (APE, chaining, **function calling**) | T2 ch6,7 | comp | `notes/S10-prompting.md` |
| 11 | Prompt Engineering & Reasoning II | Structured output control (verification, structured generation, constrained decoding); structured reasoning (**CoT**, ToT, step-back, PAL); iterative reasoning (**ReAct**, self-reflection); test-time compute scaling | T2 ch6,7 | comp | `notes/S11-reasoning.md` |
| 12 | Retrieval-Augmented & Retrieval-Enhanced LMs | Retriever-generator framework; semantic retrieval (dense embeddings, **BM25**, similarity search); chunking (fixed, semantic, sliding window); **reranking**; tabular & semi-structured RAG | T1 ch11 · T2 ch8 · R2 ch7 · R3 ch6 | comp | `notes/S12-rag.md` |
| 13 | LLMs for Agentic AI | Reasoning-action gap; single-agent architecture (memory, tools, planning, perception); multi-agent orchestration & communication; text-to-SQL & dataframe agents; **agentic RAG** | T2 ch7 · papers | comp | `notes/S13-agents.md` |
| 14 | Evaluation | Automatic metrics (perplexity, BLEU, ROUGE, METEOR, BERTScore); benchmarks (static, live, human arenas, model-based); faithfulness & hallucination (FActScore, **RAGAS**); **LLM-as-a-judge**; human evaluation | T1 ch7 · papers | comp | `notes/S14-evaluation.md` |
| 15 | LLM Safety, Security & Ethics | Adversarial attacks (jailbreaking, **prompt injection**, indirect injection); guardrails & safety layers; red-teaming; training-data extraction & memorization; bias & toxicity | Papers, web | comp | `notes/S15-safety.md` |
| 16 | Advanced Topics | Multimodal & frontier model case studies | Papers, web | comp | `notes/S16-advanced.md` |

## Labs (8)

| Lab | Objective | Module ref | Done |
|---|---|---|---|
| 1 | Construct and analyse tokenization techniques | M1 | ☐ |
| 2 | Build end-to-end training and fine-tuning pipelines | M2–M5 | ☐ |
| 3 | Parameter-efficient fine-tuning and alignment | M6, M7 | ☐ |
| 4 | Implement prompt engineering techniques | M8 | ☐ |
| 5 | Retrieval system handling unstructured text and structured tables | M9 | ☐ |
| 6 | Build a ReAct-style agent | M10 | ☐ |
| 7 | Evaluate an LLM using a benchmark dataset and LLM-as-judge | M11 | ☐ |
| 8 | Implement LLM safety guardrails | M12 | ☐ |

Plus **4 webinars** + case studies on advanced topics.
Tools: Python, Jupyter, scikit-learn, OpenAI, Hugging Face, PyTorch, LangChain. Infra: Colab / open source.

## Books

| | |
|---|---|
| T1 | Jurafsky & Martin, *Speech and Language Processing* (McGraw Hill, Jan 2026) |
| T2 | Alammar & Grootendorst, *Hands-On Large Language Models* (O'Reilly) |
| R1 | Raschka, *Build a Large Language Model (From Scratch)* (Manning) |
| R2 | *Generative AI in Action* (Manning) |
| R3 | Kimothi, *A Simple Guide to Retrieval Augmented Generation* (Manning) |

## How to study this subject

Theory-heavy — give it your sharpest hour. Split every topic into one of two kinds:

- **Mechanism** — attention, RoPE, MoE routing, FlashAttention, KV-cache/MQA-GQA-MLA, quantization, LoRA/QLoRA, DPO vs RLHF, speculative decoding → intuition, then **one worked example reproduced by hand**. Not read. Reproduced.
- **Landscape** — decoding strategies, serving patterns, benchmarks, emerging architectures → a comparison table, nothing more.

**Trap:** reading a slide and feeling you got it. You didn't, until you reproduced the example without looking.

> **Reference profile.** T1 (Jurafsky & Martin), T2 (Alammar & Grootendorst) and R1 (Raschka) chapters cover most sessions, always supplemented by research papers. **S6 (compression & serving), S15 (safety) and S16 (advanced topics) are research papers and web references only** — no chapter behind them.

**Weekday slot:** Monday.

## Notes on scope

- **Session 8 is a revision session**, so the closed-book mid-sem really covers sessions 1–7 of new material. That's foundations → pretraining → architecture → efficiency → inference/serving → finetuning. Densest mechanism block of the semester.
- Sessions 9–15 (alignment, prompting, RAG, agents, evaluation, safety) overlap heavily with 521. Use that overlap for revision after your 536 note is clear, not as a reason to split core learning across folders.
