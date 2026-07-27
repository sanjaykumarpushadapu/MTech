# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

> 🔴 **Slides are mandatory.** No deck → **no note is written** for that session. The handout is too coarse to define scope and the textbook is too broad; only the deck shows what this instructor taught and what they emphasised. Collect the deck for every session the same weekend, without exception.

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `Session-1-Foundations-of-ConvAI.pdf` (56 sl) | ✓ T1 *Building Effective Agents* · *Landscape of AI Agents* | ✗ | ✗ | ✅ `notes/S01-foundations.md` |
| 2 |  |  |  |  | ☐ |
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


## T1 — Official documentation (primary textbooks, all public)

| Source | URL | Status | Sessions |
|---|---|---|---|
| Anthropic, **Building Effective Agents** (Dec 2024) | anthropic.com/engineering/building-effective-agents | ✅ fetched | **S1** (workflows vs agents, when not to) · **S9** (the five patterns) · **S4** (tool/ACI design) |
| OpenAI **function calling** docs | platform.openai.com | ☐ | S4 |
| **MCP** specification | modelcontextprotocol.io | ☐ | S13 |
| **A2A** specification | official spec | ☐ | S14 |

**R2 — core research papers** (all public, fetch when the session arrives)

| Paper | Session |
|---|---|
| *The Landscape of AI Agents* (Masterman et al., arXiv:2404.11584) | ✅ S1 |
| Dense Passage Retrieval (Karpukhin et al., 2020) | S2 |
| ReAct (Yao et al., 2023) | S4 |
| Direct Preference Optimization (Rafailov et al., 2023) | S5 |
| MemGPT (2023) | S6 |
| Anthropic Contextual Retrieval (2024) | S7–8 |
| MetaGPT (2024) | S9 |
| Judging LLM-as-a-Judge / MT-Bench (2023), GAIA | S10 |
| Anthropic prompt caching docs | S11 |
| Anthropic Responsible Scaling Policy | S15–16 |

**Nothing here needs uploading.** Give the session number and these get fetched.


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


## Scope rule

521 cites **no textbook chapters** — every reference is a specific public paper or spec, listed per session in `521-master.md`. **The named paper is the scope.** Related work it cites, or later papers by the same authors, are out of the syllabus unless the handout names them.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts (`.txt`, `.srt`, `.vtt`) are small and plain text, so they **may** be committed if useful:
put them in `source/transcripts/`. They are not blocked by `.gitignore`.
