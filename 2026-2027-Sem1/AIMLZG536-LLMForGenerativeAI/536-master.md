# AIML ZG536 · Large Language Models for Generative AI — Master Index

4 credits · 3-1-0 · Author: Prof. Monali Mavani · Instructors: Monali Tushar Mavani (Lead), Akash Goel, S. Prabakeran, Rahil N Modi
**Mid-sem: sessions 1–8, closed book · Comprehensive: all 16, open book**

> Revision homepage during the semester; **open-book front index** in December.

**Primary path (within this subject):** open this master first, then the session note. `_shared/` is optional background only. _(Semester-level entry is `2026-2027-Sem1/README.md` → `PROGRESS.md`.)_

## Evaluation

| EC   | Component                                                                 | Type            | Weight       | Date                                                                                                 |
| ---- | ------------------------------------------------------------------------- | --------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| EC-1 | ~~Quiz~~                                                                  | —               | —            | ❌ **NO QUIZZES.** Instructor, S1 recording: _"I'm repeating there are no quizzes for this course."_ |
| EC-1 | **Assignment 1 & 2** — **group**, together forming one end-to-end project | Online          | **35%**      | Plan shared ~week 2                                                                                  |
| EC-2 | Mid-semester test                                                         | **Closed book** | **30 marks** | **20 Sep 2026 (EN)**, 2h                                                                             |
| EC-3 | Comprehensive exam                                                        | Open book       | **35 marks** | **6 Dec 2026 (EN)**, 2½h                                                                             |

✅ **EC-1 RESOLVED from the session-1 recording** (25 Jul 2026). The handout's "Quiz 5% + Assignment 30%" is superseded — the instructor stated the quiz split three times. Weights confirmed: EC-2 30, EC-3 35.

**How the assignments work** — stated in class, in no written source:

- **Group assignments**, not individual. _"You have to create your own groups"_ — Ops creates a placeholder.
- **Assignments 1 and 2 are designed to combine into one complete end-to-end project.** Don't treat them as separate.
- For each assignment she gives **two problem statements on two different topics**, plus **five or six enterprise case-study options**. **You choose.**
- Everything assigned **is covered in webinars or classes** first.
- She supplies lab sheets as Jupyter notebooks with **"80, 90% of the code readily available."**

🔴 **Assignments must run on the BITS remote lab, not your laptop.** _"In laptop, no — you have to use the remote lab for the assignments."_ A manual will be shared. No time limit on the lab, but expect contention near deadlines. Colab works only for very small models.

## Modules at a glance

536's handout names each module with an hour count, almost 1:1 with sessions — except two modules that run **4 hours across 2 sessions**, which is a signal of relative weight worth carrying forward (more contact time, likely more exam weight).

| Module | Sessions | Hours |
|---|---|---|
| Foundations of LLMs | S1 | 2 |
| LLM Pre-Training | S2 | 2 |
| Advancements in LLM Architecture | S3 | 2 |
| Training and Attention Efficiency | S4 | 2 |
| LLM Optimization & Serving | **S5–S6** | **4** |
| LLM Finetuning | S7 | 2 |
| *(Revision)* | S8 | — |
| Preference Alignment | S9 | 2 |
| Prompt Engineering and Reasoning | **S10–S11** | **4** |
| Retrieval-Augmented / Retrieval-Enhanced LMs | S12 | 2 |
| LLMs for Agentic AI | S13 | 2 |
| Evaluation | S14 | 2 |
| LLM Safety, Security and Ethics | S15 | 2 |
| Advanced Topics | S16 | 2 |

## Session index

Titles below follow the handout learning-plan wording as closely as possible so the subject notes and the master index stay aligned.

| S   | Topic                                                      | Sub-topics                                                                                                                                                                                                                                                                                                                                                             | Source                             | Exam | Note file                   |
| --- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---- | --------------------------- |
| 1   | Foundations of Large Language Models (LLMs)                | Introduction to LLMs and Generative AI; Attention Mechanism & Transformer (Review); Building blocks of LLM; LLM Architectures; Tokenization; LLM landscape                                                                                                                                                                                                             | T1 ch2,7,8 · T2 ch1,2,3 · R1 ch1,2 | mid  | `notes/S01-foundations.md`  |
| 2   | LLM Pre-Training                                           | LLM Pre-training; Pre-training Objectives; Pre-training Data; Continuous Pre training (CPT) and Domain Adaptation; Scaling Laws; Pretraining of popular frontier models                                                                                                                                                                                                | T1 ch7,8 · R1 ch2,5                | mid  | `notes/S02-pretraining.md`  |
| 3   | Advancements in LLM Architecture                           | Normalization: LayerNorm, RMSNorm, Norm placement; Positional Encoding Advances: Relative PE, RoPE, NoPE; Advanced activations: GELU, Swish, Gated Linear Units (GLU), SwiGLU; MoE: Sparse activation and routing; Emerging Architectures                                                                                                                              | T2 ch3 · papers                    | mid  | `notes/S03-architecture.md` |
| 4   | Training and Attention Efficiency                          | Memory Bottlenecks; Mixed Precision Training; IO-Aware Attention: Flash Attention; Long Context Training: Ring Attention; Attention Efficiency Variants: sliding window, Sparse, Linear                                                                                                                                                                                | Class 4 lecture exception: LLM Fine-tuning deck | mid  | `notes/S04-fine-tuning.md` (lecture exception) |
| 5   | LLM Optimization & Serving                                 | Two-phase inference process; Inference bottlenecks; Decoding strategies and Sampling: Greedy, Beam Search, Top-K, Top P, temperature; KV-Caching and Memory optimization: MQA, GQA, and MLA                                                                                                                                                                            | T1 ch7,8 · T2 ch3 · R1 ch5         | mid  | *deck awaited*              |
| 6   | LLM Optimization & Serving                                 | Model Compression: Quantization, Pruning, Compression pipeline; Generation Acceleration: Speculative Decoding; Production Serving Patterns: Continuous/In-flight batching, Chunked prefill, Paged attention; Production Metrics and Economics                                                                                                                          | Papers, web                        | mid  | *deck awaited*              |
| 7   | LLM Finetuning                                             | Full Fine-tuning; Supervised Fine Tuning (SFT); Instruction fine tuning(IFT); Prompt and Prefix tuning; Parameter Efficient Fine tuning (PEFT): LoRA and QLoRA, Adapters; Model Merging; Distillation                                                                                                                                                                  | T1 ch7,10 · T2 ch12 · R1 ch7       | mid  | *deck awaited*              |
| 8   | Revision                                                   | Consolidation of sessions 1–7                                                                                                                                                                                                                                                                                                                                          | —                                  | mid  | *deck awaited*              |
| 9   | Preference Alignment                                       | Why Alignment?; Preference Data collection; Reinforcement Learning from Human Feedback (RLHF): Reward Modelling, PPO; RL free techniques: Direct Preference Optimization (DPO) and variants, Group Relative Policy Optimization (GRPO); Constitutional AI and RLAIF                                                                                                    | T1 ch10 · T2 ch12 · papers         | comp | *deck awaited*              |
| 10  | Prompt Engineering and Reasoning                           | Prompt Components & Design: Role, Instruction, Context, Examples, Output Format, Tabular Serialization; Prompting Paradigms: Zero-shot, Few-shot, Instruction Prompting, Self-Consistency; In-context Learning; Prompt Engineering as System Design: APE, Prompt Chaining & Control Flow, Function-Calling                                                             | T2 ch6,7                           | comp | *deck awaited*              |
| 11  | Prompt Engineering and Reasoning                           | Structured Output Control: Output Verification, Structured Generation, Constrained Decoding; Structured Reasoning via Prompting: Chain-of-Thought (CoT), Tree of Thought (ToT), Step-Back Prompting, PAL (Program-Aided Reasoning); Iterative Reasoning via Prompting: ReACT, Self-Reflection; Test-Time Compute Scaling: Thinking Tokens and Inference-Time Reasoning | T2 ch6,7                           | comp | *deck awaited*              |
| 12  | Retrieval-Augmented and Retrieval-Enhanced Language Models | Retriever-Generator framework; Semantic Retrieval: Dense Embeddings, Sparse Retrieval (BM25), and Similarity Search; Chunking strategies: Fixed, Semantic, Sliding Window; Reranking; Tabular and Semi-Structured RAG                                                                                                                                                  | T1 ch11 · T2 ch8 · R2 ch7 · R3 ch6 | comp | *deck awaited*              |
| 13  | LLMs for Agentic AI                                        | From LLMs to Agents: Reasoning-Action Gap; Single Agent Architecture: Memory, Tools, Planning, and Perception; Multi-Agent Systems: Orchestration Patterns and Communication; Structured Data Interaction; Agentic RAG                                                                                                                                                 | T2 ch7 · papers                    | comp | *deck awaited*              |
| 14  | Evaluation                                                 | Automatic Evaluation Metrics: Perplexity, BLEU, ROUGE, METEOR, and BERTScore; Benchmarks: Static, Live, Human-in-the-Loop Arenas, and Model-Based Benchmarks; Faithfulness and Hallucination Evaluation: FActScore and RAGAS; LLM-as-a-Judge: Evaluation Prompts, Scoring Patterns; Human Evaluation                                                                   | T1 ch7 · papers                    | comp | *deck awaited*              |
| 15  | LLM Safety, Security and Ethics                            | Adversarial Attacks: Jailbreaking, Prompt Injection, and Indirect Prompt Injection; Guardrails and Safety Layers: Input/Output Filtering and Constitutional Rules; Red Teaming LLMs: Structured Adversarial Testing and Automation; Training Data Extraction and Memorization; Bias and Toxicity: Sources, Measurement, and Mitigation                                 | Papers, web                        | comp | *deck awaited*              |
| 16  | Advanced Topics                                            | Multimodal & Frontier Model Case Studies                                                                                                                                                                                                                                                                                                                               | Papers, web                        | comp | *deck awaited*              |

## Labs (8)

| Lab | Objective                                                         | Module ref | Done |
| --- | ----------------------------------------------------------------- | ---------- | ---- |
| 1   | Construct and analyse tokenization techniques                     | M1         | ☐    |
| 2   | Build end-to-end training and fine-tuning pipelines               | M2–M5      | ☐    |
| 3   | Parameter-efficient fine-tuning and alignment                     | M6, M7     | ☐    |
| 4   | Implement prompt engineering techniques                           | M8         | ☐    |
| 5   | Retrieval system handling unstructured text and structured tables | M9         | ☐    |
| 6   | Build a ReAct-style agent                                         | M10        | ☐    |
| 7   | Evaluate an LLM using a benchmark dataset and LLM-as-judge        | M11        | ☐    |
| 8   | Implement LLM safety guardrails                                   | M12        | ☐    |

Plus **4 webinars** + case studies on advanced topics.
Tools: Python, Jupyter, scikit-learn, OpenAI, Hugging Face, PyTorch, LangChain. Infra: Colab / open source.

## Books

|     |                                                                             |
| --- | --------------------------------------------------------------------------- |
| T1  | Jurafsky & Martin, _Speech and Language Processing_ (McGraw Hill, Jan 2026) |
| T2  | Alammar & Grootendorst, _Hands-On Large Language Models_ (O'Reilly)         |
| R1  | Raschka, _Build a Large Language Model (From Scratch)_ (Manning)            |
| R2  | _Generative AI in Action_ (Manning)                                         |
| R3  | Kimothi, _A Simple Guide to Retrieval Augmented Generation_ (Manning)       |

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
