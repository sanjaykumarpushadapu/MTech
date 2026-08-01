# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

> 🔴 **Slides are mandatory.** No deck → **no note is written** for that session. The handout is too coarse to define scope and the textbook is too broad; only the deck shows what this instructor taught and what they emphasised. Collect the deck for every session the same weekend, without exception.

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `CS-1 Intro to LLM.pptx` (69 sl, 47 images read; **mixed/overlap deck**) | ✅ **all three held**: T1 ch2,7,8 · T2 ch1,2,3 · R1 ch1,2 | ✓ Teams 2h05 | ✅ received & extracted into note (not stored) | ✅ `notes/S01-foundations.md` (S1 scope only: intro, attention/transformer review, building blocks, architectures, tokenization, LLM landscape) |
| 2 | ◐ **partial overlap** in `CS-1 Intro to LLM.pptx` slides 57–59 only: scaling laws / frontier-model landscape. **Not a complete S2 deck**: missing dedicated pre-training objectives, pre-training data, CPT/domain adaptation | ✅ readings held: T1 ch7,8 · R1 ch2,5 |  |  | ☐ |
| 3 |  |  |  |  | ☐ |
| 4 |  |  |  |  | ☐ |
| 5 |  |  |  |  | ☐ |
| 6 |  |  |  |  | ☐ |
| 7 |  |  |  |  | ☐ |
| 8 |  |  |  |  | ☐ |
| 9 |  |  |  |  | ☐ |
| 10 |  |  |  |  | ☐ |
| 11 |  |  |  |  | ☐ |
| 12 |  |  |  |  | ☐ |
| 13 |  |  |  |  | ☐ |
| 14 |  |  |  |  | ☐ |
| 15 |  |  |  |  | ☐ |
| 16 |  |  |  |  | ☐ |


## T1 · Jurafsky & Martin, *Speech and Language Processing* 3rd ed. draft (Jan 2026, 626 pp)

**536's T1 and 521's R1.** Free: https://web.stanford.edu/~jurafsky/slp3/

| Ch | Title | PDF page | Cited for |
|---|---|---|---|
| 1 | Introduction | 11 | ✗ **OUT OF SCOPE** |
| **2** | **Words and Tokens** | **12** | **536 S1** ✅ |
| 3 | N-gram Language Models | 46 | ✗ **OUT OF SCOPE** |
| 4 | Logistic Regression | 70 | ✗ **OUT OF SCOPE** |
| 5 | Embeddings | 104 | ✗ **OUT OF SCOPE** |
| 6 | Neural Networks | 128 | ✗ **OUT OF SCOPE** |
| **7** | **Large Language Models** | **154** | **536 S1, S2, S5, S14** ✅ |
| **8** | **Transformers** | **181** | **536 S1, S2, S5** ✅ |
| 9 | Masked Language Models | 207 | ✗ **OUT OF SCOPE** |
| **10** | **Post-training: Instruction Tuning, Alignment, Test-Time Compute** | **226** | **536 S7, S9** |
| **11** | **Retrieval-based Models** | **243** | **536 S12** |
| 12 | Machine Translation | 266 | ✗ **OUT OF SCOPE** |
| 13 | RNNs and LSTMs | 292 | ✗ **OUT OF SCOPE** |
| 14–16 | Phonetics · ASR · Text-to-Speech | 318 · 347 · 373 | ✗ **OUT OF SCOPE** |
| Part II (17–26) | Annotating Linguistic Structure — POS/NER, parsing, SRL, coreference, discourse, conversation | 387–581 | ✗ **OUT OF SCOPE** |

**Scope: only ch2, 7, 8, 10, 11 are cited across all of 536.** That's five chapters of twenty-six. Part II is entirely outside the syllabus despite chapter 26 being "Conversation and its Structure" — 521 cites J&M only as general R1 background, never a chapter.

**Section maps for the S1 chapters:**

*Ch2 Words and Tokens* — Words (13) · Morphemes (16) · Unicode: code points, UTF-8 (18) · **Subword Tokenization: BPE (21)** — BPE training (22), BPE encoder (24), BPE in practice (24) · Corpora (25) · Regular Expressions (27) · Rule-based tokenization (36) · Minimum Edit Distance (38)

*Ch7 Large Language Models* — Three architectures for language models (157) · **Conditional Generation of Text: The Intuition (158)** · Prompting (159) · **Generation and Sampling (162)** · Training LLMs (166) · Evaluating LLMs (171) · Ethical and Safety Issues (175)

*Ch8 Transformers* — **Attention (182)** · **Transformer Blocks (188)** · Parallelizing computation using a single matrix X (191) · **The input: embeddings for token and position (195)** · **The Language Modeling Head (197)** — *this is the source of the deck's fig 8.15* · More on Sampling (198) · Training (200) · Dealing with Scale (201) · Interpreting the Transformer (203)



## T2 · Alammar & Grootendorst, *Hands-On Large Language Models* (O'Reilly, 428 pp)

**The most-cited book in 536** — sessions 1, 3, 4, 5, 10, 11, 12, 13.

| Part | Ch | Title | PDF page | Cited for |
|---|---|---|---|---|
| **I · Understanding language models** | **1** | An Introduction to Large Language Models | **25** | **S1** ✅ |
| | **2** | **Tokens and Embeddings** | **59** | **S1** ✅ |
| | **3** | **Looking Inside Large Language Models** | **95** | **S1, S3, S4, S5** ✅ |
| II · Using pretrained models | 4 | Text Classification | 133 | ✗ **OUT OF SCOPE** |
| | 5 | Text Clustering and Topic Modeling | 159 | ✗ **OUT OF SCOPE** |
| | **6** | Prompt Engineering | 189 | **S10, S11** |
| | **7** | Advanced Text Generation | 221 | **S10, S11, S13** |
| | **8** | Semantic Search and RAG | 247 | **S12** |
| | 9 | Multimodal Large Language Models | 281 | ✗ **OUT OF SCOPE** |
| III · Training and fine-tuning | 10 | Creating Text Embedding Models | 311 | ✗ **OUT OF SCOPE** |
| | 11 | Fine-Tuning Representation Models | 345 | ✗ **OUT OF SCOPE** |
| | **12** | Fine-Tuning Generation Models | 377 | **S7, S9** |

**Scope: ch1, 2, 3, 6, 7, 8, 12 only.** Chapters 4, 5, 9, 10, 11 are outside the syllabus.

**Section maps for the S1 chapters:**

*Ch2 Tokens and Embeddings* (p59) — LLM Tokenization (60) · How tokenizers prepare inputs (60) · How does the tokenizer break down text (65) · **Word vs subword vs character vs byte tokens (66)** · **Comparing trained LLM tokenizers (68)** · **Tokenizer Properties (77)** · Token Embeddings (79) · Contextualized word embeddings (80) · Text embeddings for sentences/documents (83) · Word embeddings beyond LLMs, word2vec (85) · Embeddings for recommendation (89)

*Ch3 Looking Inside LLMs* (p95) — Overview of transformer models (96) · Inputs and outputs of a trained transformer LLM (96) · **The components of the forward pass (98)** · **Choosing a single token from the probability distribution (101)** · **Parallel token processing and context size (103)** · **Speeding up generation by caching keys and values (105)** ← *KV-cache, previews S5* · **Inside the transformer block (107)** · Recent improvements (117) · **More efficient attention (118)** ← *previews S4* · The transformer block (123) · **Positional embeddings (RoPE) (124)** ← *previews S3* · Other architectural experiments (127)

⚠️ **Ch3 spans four sessions.** Read p96–116 for S1; p117–127 belongs to S3 and S4. Don't read the whole chapter in week 1.


## R1 · Raschka, *Build a Large Language Model (From Scratch)* (157 pp, markdown export)

Cited for **536 S1 (ch1–2), S2 (ch2, 5), S5 (ch5), S7 (ch7)**.

| Ch | Title | PDF page | Cited for |
|---|---|---|---|
| **1** | **Understanding LLM** | **3** | **S1** ✅ |
| **2** | **Working with Text Data** | **7** | **S1, S2** ✅ |
| 3 | Coding Attention Mechanisms | ~20 | ✗ **OUT OF SCOPE** |
| 4 | Implementing a GPT Model from Scratch | 48 | ✗ **OUT OF SCOPE** |
| **5** | **Pretraining on Unlabeled Data** | **72** | **S2, S5** |
| 6 | Fine-tuning for Classification | 90 | ✗ **OUT OF SCOPE** |
| **7** | **Fine-tuning to Follow Instructions** | **108** | **S7** |

**Scope: ch1, 2, 5, 7 only.** Chapters 3, 4 and 6 are outside the syllabus — note that ch3 (Coding Attention Mechanisms) and ch4 (Implementing a GPT Model) are *not* cited even though 536 S1 covers attention and the transformer block; that material comes from **T1 ch8** and **T2 ch3** instead.

**Ch2 section map (the S1 chapter):**

| § | Title | p | In S1 note? |
|---|---|---|---|
| 2.1 | Understanding word embeddings | 7 | ✅ §8 |
| 2.2 | Tokenizing text | ~9 | ✅ §8 |
| 2.3 | Converting tokens into token IDs | ~10 | ✅ §8 |
| 2.4 | **Adding special context tokens** | ~11 | ✅ §8 — source of the `<\|unk\|>` 783 / `<\|endoftext\|>` 784 figure |
| 2.5 | **Byte pair encoding** | **12** | ✅ `_shared/tokenization.md` |
| 2.6 | Data sampling with a sliding window | ~14 | ⚠️ *not in the deck* — belongs to S2 (pre-training data) |
| 2.7 | **Creating token embeddings** | **16** | ✅ §8 — source of the fig 2.16 embedding-lookup figure |
| 2.8 | **Encoding word positions** | **17** | ✅ §8 — source of the fig 2.18 positional-addition figure |

**The deck's figures came from here.** Slides 29, 32 and 35 of `CS-1 Intro to LLM.pptx` reproduce Raschka figs 2.9, 2.16 and 2.18 — special tokens, the embedding-matrix row lookup, and token + positional embedding addition. All three are already extracted into `notes/S01-foundations.md` §8 with their numbers.

**S1 visual consolidation (1 Aug).** Rechecked cited S1 textbook figures from T1 ch2/7/8, T2 ch1/2/3 and R1 ch1/2, plus public paper anchors for the original Transformer and BPE. Useful figure value was folded into authored SVGs under `notes/assets/S01-*.svg`; no original textbook, slide or paper images were copied into the repo. The original Transformer encoder-decoder blueprint was recreated as `S01-original-transformer-blueprint.svg`; BPE paper figures did not add a better visual than the tokenizer explanations already in §12.

## Scope rule

**Only the chapters named in the handout's Reference column are in the syllabus.** For 536 these are: T1 (Jurafsky & Martin) ch2, 7, 8, 10, 11 · T2 (Alammar) ch1, 2, 3, 6, 7, 8, 12 · R1 (Raschka) ch1, 2, 5, 7 · R2 ch7 · R3 ch6. **Every other chapter in those books is out of scope** — not background, not optional extra reading.

Session 1's own slides make the same point internally: slides 61–69 are marked *"Extra slides (Not for exams)"*.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts are **raw source, not committed** — `source/transcripts/` is gitignored. Read a transcript to build or update the note, fold the important content (instructor quotes, emphasis, off-slide clarifications) into it, then it's done. The note is the record.

## R2 Bahree received — 27 Jul 2026

**536 R2 = Amit Bahree, *Generative AI in Action*** (Manning, 698 pp) → `_library/536-R2-Bahree-GenerativeAIinAction.pdf`.
Verified against the citation: Manning imprint, full TOC, and **ch7 is "Retrieval-augmented generation"** — exactly what the handout cites for S12.

⚠️ **Not to be confused with** the 9-page vendor whitepaper of the same title uploaded the same day (*"Adoption Trends, Emerging Use Cases, and Tips for IT Leaders"*). That one was rejected and never filed.

### Chapter → page map

| Ch | Title | PDF page | Scope |
|---|---|---|---|
| 1 | Introduction to generative AI | 35 | ❌ OUT OF SCOPE |
| 2 | Introduction to large language models | 71 | ❌ OUT OF SCOPE |
| 3 | Working through an API: generating text | 116 | ❌ OUT OF SCOPE |
| 4 | From pixels to pictures: generating images | 168 | ❌ OUT OF SCOPE |
| 5 | What else can AI generate? | 221 | ❌ OUT OF SCOPE |
| 6 | Guide to prompt engineering | 260 | ❌ OUT OF SCOPE |
| **7** | **Retrieval-augmented generation: the secret weapon** | **308–351** | ✅ **S12 — the only cited chapter** |
| 8 | Chatting with your data | 352 | ❌ OUT OF SCOPE |
| 9 | Tailoring models with model adaptation and fine-tuning | 393 | ❌ OUT OF SCOPE |
| 10 | Application architecture for generative AI apps | 454 | ❌ OUT OF SCOPE |
| 11 | Scaling up: best practices for production deployment | 508 | ❌ OUT OF SCOPE |
| 12 | Evaluations and benchmarks | 560 | ❌ OUT OF SCOPE |

**Only ch7 (pp 308–351) is cited by the handout.** Eleven of twelve chapters are outside this semester — several cover material 536 teaches from other sources (ch6 prompt engineering → S10 from T1/T2; ch9 fine-tuning → S7/S9 from R1). Do not pull from them, and do not recommend reading them.
