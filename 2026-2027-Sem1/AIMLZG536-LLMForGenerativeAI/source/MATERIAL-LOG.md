# AIML ZG536 · Large Language Models for Generative AI · Material Log

Rebuilt: 10 Aug 2026.

This file records held teaching material, direct handout scope, processed outputs, and unresolved gaps. Raw decks, recordings, transcripts, and downloaded books are source inputs only; they must not be committed.

Legend: `✓` held/complete · `partial` held but incomplete · `✗` missing · `—` not applicable.

## Handout

| Item | Status |
|---|---|
| Direct handout file | ✓ `_handouts/AIML ZG536 COURSE HANDOUT.docx` |
| Direct row verification | ✓ S1 and S2 checked directly on 10 Aug 2026 |

## Session Material Status

| Session | Handout topic and required sub-topics | Material held | Processed output | Open gap |
|---|---|---|---|---|
| S1 | Foundations of Large Language Models (LLMs): Introduction to LLMs and Generative AI; Attention Mechanism & Transformer review; Building blocks of LLM; LLM Architectures; Tokenization; LLM landscape | ✓ `CS-1 Intro to LLM.pptx` / `CS-1 Intro to LLM (2).pptx`; S01 transcript; T1 ch2,7,8; T2 ch1,2,3; R1 ch1,2 | ✓ `notes/S01-foundations.md` | none known |
| S2 | LLM Pre-Training: LLM Pre-training; Pre-training Objectives; Pre-training Data; Continuous Pre training (CPT) and Domain Adaptation; Scaling Laws; Pretraining of popular frontier models | ✓ `CS-2 LLM Training.pptx`; T1 ch7,8; R1 ch2,5; web references | ✓ `notes/S02-pretraining.md` | none known |
| S3 | Architecture advances | ✗ | ☐ | deck required |
| S4 | Attention/architecture continuation | ✗ | ☐ | deck required |
| S5 | LLM training/evaluation continuation | ✗ | ☐ | deck required |
| S6 | Paper/web-only session | ✗ | ☐ | deck and cited paper required |
| S7 | Fine-tuning / instruction tuning | ✗ | ☐ | deck required |
| S8 | Revision | ✗ | ☐ | verify whether a revision deck is issued |
| S9 | Preference Alignment: alignment motivation; preference data; RLHF reward modeling and PPO; DPO/GRPO; Constitutional AI and RLAIF | ✗ | ☐ | deck and cited references required |
| S10 | Prompt Engineering and Reasoning: prompt components; zero/few-shot; self-consistency; in-context learning; prompt engineering as system design; APE, prompt chaining, function calling | ✗ | ☐ | deck and references required |
| S11 | Prompt Engineering and Reasoning: structured output control; constrained decoding; CoT, ToT, Step-Back, PAL; ReAct; self-reflection; test-time compute | ✗ | ☐ | deck and references required |
| S12 | Retrieval-Augmented and Retrieval-Enhanced Language Models: retriever-generator; dense/sparse retrieval; similarity search; chunking; reranking; tabular/semi-structured RAG | ✗; R2 ch7 held; R3 missing | ☐ | deck required; Kimothi R3 ch6 still missing |
| S13 | LLMs for Agentic AI: reasoning-action gap; memory, tools, planning, perception; multi-agent orchestration; text-to-SQL/data-frame agents; agentic RAG | ✗ | ☐ | deck and references required |
| S14 | Evaluation: automatic metrics; benchmarks; faithfulness/hallucination; FActScore/RAGAS; LLM-as-a-judge; human evaluation | ✗ | ☐ | deck and references required |
| S15 | LLM Safety, Security and Ethics: jailbreaks, prompt injection, guardrails, red teaming, memorization, bias and toxicity | ✗ | ☐ | deck and references required |
| S16 | Advanced topics: multimodal and frontier-model case studies | ✗ | ☐ | deck and references required |

## Reference Scope

| Reference | In-scope chapters/status |
|---|---|
| T1 Jurafsky & Martin, *Speech and Language Processing* | ch2, ch7, ch8, ch10, ch11 only |
| T2 Alammar & Grootendorst, *Hands-On Large Language Models* | ch1, ch2, ch3, ch6, ch7, ch8, ch12 only |
| R1 Raschka, *Build a Large Language Model From Scratch* | ch1, ch2, ch5, ch7 only |
| R2 Bahree, *Generative AI in Action* | ch7 only; held |
| R3 Kimothi, *A Simple Guide to Retrieval Augmented Generation* | ch6; missing, first needed around S12 |

## Recheck Notes — 10 Aug 2026

- S01 and S02 were rechecked against the direct 536 handout rows now held in `_handouts/`.
- S02 previously had five Mermaid diagrams; they were replaced with SVGs on 10 Aug 2026 to satisfy the SVG-first rule.
- No raw textbook, paper, or deck images were copied into the repo; authored SVGs under `notes/assets/` carry the visual teaching value.
- Source-framing scan passes for current notes via `npm run check`.

## Storage Rule

Recordings, decks, transcripts, and raw PDFs stay outside git or in ignored source folders only. The durable record is the note/lab README, not the raw course material.
