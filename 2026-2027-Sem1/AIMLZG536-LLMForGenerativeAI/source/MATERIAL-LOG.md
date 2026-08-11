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
| S3 | Advancements in LLM Architecture: Normalization (LayerNorm, RMSNorm, norm placement); Positional Encoding Advances (Relative PE, RoPE, NoPE); Advanced activations (GELU, Swish, GLU, SwiGLU); MoE sparse activation and routing; Emerging Architectures | ✓ `CS-3 Advancements in LLM Architecture.pptx`; T2 ch3; Shaw et al. 2018 (verified via web search); Mamba/SSM reference (filled-in, no direct slide coverage) | ✓ `notes/S03-architecture.md` | none known — Emerging Architectures sub-topic marked as filled-in reasoning since the deck only cites it via a references-slide link, not direct teaching content |
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

## Recheck Notes — 11 Aug 2026

- `CS-1 Intro to LLM (2).pptx` and `CS-2 LLM Training.pptx` arrived as a re-upload alongside the new `CS-3 Advancements in LLM Architecture.pptx`. Both were cross-checked against `notes/S01-foundations.md` and `notes/S02-pretraining.md` via targeted extraction of distinctive facts and numbers; both notes already covered their decks comprehensively. One addition was made to S01 (a current-frontier-models snapshot table); S02 needed no changes.
- `CS-3 Advancements in LLM Architecture.pptx` (29 slides) unblocked S3, previously listed as deck-required. Full text extraction plus rendered slide images (for diagram/equation-heavy slides) were used to write `notes/S03-architecture.md`.
- The handout's "Relative PE" sub-topic is cited by the deck via reference to Shaw et al. 2018 but not taught directly; the mechanism (clipped relative-distance embeddings, BLEU gains) was verified via a targeted web search of the cited paper before writing that section, per the Cited Sources Must Be Read rule.
- The handout's "Emerging Architectures" sub-topic has no deck coverage at all beyond a references-slide link to a Mamba/state-space-models article. That section of the note is marked with a `*filled-in reasoning for this syllabus item*` aside.
- Six new SVG diagrams were authored for S3 under `notes/assets/`, matching the 536 house style (white background, Georgia serif, black-stroke pastel boxes).

## Recheck Notes — 11 Aug 2026 (second pass, exhaustive)

Re-uploaded copies of all three decks (`CS-1 (2)`, `CS-2`, `CS-3` — confirmed byte-identical to the first upload) prompted a second, exhaustive line-by-line re-extraction (including tables, speaker notes, and rendered slide images for image-only slides) and comparison against all three affected notes, rather than trusting the first pass's "comprehensive" verdict. Six real content gaps were found and fixed:

- **S03 concept 2 (norm placement):** the deck names a fourth architecture, **Gemma 3**, which normalizes both before and after each sublayer (a "sandwich" pattern distinct from the three already covered). Added.
- **S03 concept 4 (RoPE):** missing the paper attribution — RoPE was introduced by **Su et al., RoFormer (2021)**. Added.
- **S03 concept 10 (MoE):** the deck draws a **Sparse MoE vs Dense MoE** distinction (hard top-k routing vs running every expert with different weighting) that the note hadn't covered at all — a genuine naming trap since "dense" already means something different in concept 8. Added as a callout.
- **S03 concepts 6-7 (activations):** the References slide names the source papers for GELU (Hendrycks & Gimpel), Swish/SiLU (Elfwing et al.), and GLU/SwiGLU (Shazeer 2020, "GLU Variants Improve Transformer") — none were cited by name. Added.
- **S01 weight-tying table:** the "Untied" row was generalized to "many frontier-scale decoder LLMs" instead of the deck's exact named examples (**DeepSeek-V3, OLMo 2**, alongside Llama-3/4 and Qwen3-8B+). Fixed to name them.
- **S02 data preprocessing:** the deck's dedicated "Model-as-a-Judge for data curation (Llama 3)" slide — a chained fastText → RoBERTa-family (Llama-2-supervised) → DistilRoBERTa quality-filtering pipeline — was entirely absent from the note's general quality-filtering paragraph. Added as a worked example.

Everything else checked (RoPE rotation math on S03 slide 13, the GEGLU/SwiGLU equations on S03 slide 16, the GPT-1/T5 case-study numbers in S02, the BloombergGPT/FinLLaMA figures, the three-eras-of-scaling table, weight-tying arithmetic in S01) matched the notes exactly, including several numeric worked examples reproduced close to verbatim. `npm run check` re-run clean after fixes (36/36 diagrams, 0 source-framing violations).

## Recheck Notes — 11 Aug 2026 (third pass, bullet-by-bullet reconciliation)

Applied the new Draft-to-Source Reconciliation rule (`AGENTS.md`) to the same three decks: went through the full extraction bullet by bullet against the current drafts, rather than a synthesis-based re-read. Four more gaps surfaced, all in S01 (the file least recently touched before this pass):

- **"Neural ingredients" timeline table:** had year + contribution but no author attribution. The deck's slide 56 names each paper (Bengio et al. 2003, Sutskever et al. 2014, Kingma et al. 2014, Bahdanau et al. 2014, Vaswani et al. 2017, Shazeer et al. 2017, Huang/Rajbhandari/Shoeybi 2018-19). Added a Source column.
- **Pre-neural line:** the 1950 entropy-of-English claim wasn't attributed to Shannon by name. Fixed.
- **"Three levels of openness" table:** used generic descriptions instead of the deck's exact named examples (Closed = GPT-4o, Open-weight = DeepSeek, Open-source = OLMo). Fixed.
- **"Today's frontier models" list (deck slide 58):** entirely absent — superseded in spirit by the note's own fresher current-as-of-2026 snapshot table, but per the exhaustive-cross-check rule a distinctly-labeled source list still needs its own visible home even when a fresher equivalent exists elsewhere. Added as a clearly-dated "frontier models at time of authoring" note.
- **S02 data-mixture example:** Llama 3's downsampling example named "arts and entertainment" specifically in the deck; the note had genericized it away. Restored the named example.

S02 and S03 held up well under the same bullet-by-bullet check — only the one S02 fix above. `npm run check` clean after fixes (36/36 diagrams, 0 source-framing violations).

## Slide Inventories Backfilled — 11 Aug 2026

`source/S01-slide-inventory.md` existed only for 521 S01, never generated for any 536 session despite the "Capture a Slide Inventory at Intake" rule in `AGENTS.md` requiring one per deck. Backfilled `S01-slide-inventory.md`, `S02-slide-inventory.md`, and `S03-slide-inventory.md` from the already-held decks and ran `tools/check-slide-coverage.mjs` against each note. After pruning extraction noise (OCR corruption, logistics slides, generic words) from the inventories, all three came back clean, but the first raw run before pruning surfaced several genuine gaps that the manual reconciliation passes had missed:

- **S01:** author attributions for BPE (Sennrich et al., 2016), Unigram (Kudo, 2018), and WordPiece (Schuster & Nakajima, 2012); Press & Wolf (2017) for weight tying; DeepMind attribution for Chinchilla plus the models it beat (GPT-3, Gopher, MT-NLG); the SentencePiece/tiktoken table had been genericized away from the deck's exact named models (restored Llama-2/Mistral-7B, Gemma-2/Gemma-3, Llama-3/Llama-4, GPT-4o/GPT-5).
- **S02:** Raffel et al. (2020) citation and GLUE/SuperGLUE/SQuAD/WMT downstream-task names for T5; "Model-as-a-Judge" as the deck's own label for the Llama 3 data-curation pipeline; Gopher/MT-NLG named again in this note's own Chinchilla section (S01 and S02 cover it independently); GELU spelled out as Gaussian Error Linear Unit.
- **S03:** held up clean on the automated pass — validates the earlier manual reconciliation.

All three inventories are now committed and will catch drift automatically on future runs without needing the decks re-uploaded.

## Storage Rule

Recordings, decks, transcripts, and raw PDFs stay outside git or in ignored source folders only. The durable record is the note/lab README, not the raw course material.
