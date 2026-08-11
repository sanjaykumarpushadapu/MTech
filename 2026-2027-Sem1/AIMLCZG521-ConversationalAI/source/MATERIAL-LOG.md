# AIMLC ZG521 · Conversational AI · Material Log

Rebuilt: 10 Aug 2026.

This file records what material is held, what has been processed into durable notes/labs, and what still blocks completion. Raw decks, recordings, transcripts, and downloaded PDFs are source inputs only; they must not be committed. Session scope comes from the handout first, then decks/notebooks explain how the instructor taught it.

Legend: `✓` held/complete · `partial` held but incomplete · `✗` missing · `—` not applicable.

## Handout

| Item | Status |
|---|---|
| Direct handout file | ✓ `_handouts/Conversational_AI_Course_Handout (S2-25_AIMLCZG521) - April 2026.pdf` |
| Direct row verification | ✓ L1, L2, lab 1, and lab 2 checked on 10 Aug 2026 |
| Cohort caveat | Handout is April 2026 / S2-25; recordings are S1-26. Evaluation scheme was confirmed from recording as unchanged |

## Session Material Status

| Session | Handout topic and required sub-topics | Material held | Processed output | Open gap |
|---|---|---|---|---|
| L1 | Foundations of Conversational AI: Chatbots to Agentic Systems; System Lifecycle & Architecture | ✓ `Session-1-Foundations-of-ConvAI.pdf`; S01 transcript; `byte_pair_encoding.ipynb`; public paper *The Landscape of AI Agents* | ✓ `notes/S01-foundations.md`; `labs/S01-tokenization-and-tool-calling/README.md` | none known |
| L2 | Embeddings, Vector Search & Hybrid Retrieval: Semantic vs Keyword Search; Vector Database Architecture (HNSW, ANN); BM25 + Dense Retrieval + RRF | ✓ `Session_02_Embeddings_Vector_Search.pdf`; `Embedding-distilbert.ipynb`; public paper *Dense Passage Retrieval* | ✓ `notes/S02-retrieval.md`; `labs/S02-embeddings-vector-search/README.md` | Lab 2 remains partial: text-to-speech, rule-based systems, and sentiment-analysis files/confirmation still missing |
| L3 | Model Landscape & Cost Engineering | partial `Session3-ANN-HybridSearch-Ranking.pdf` is extra hybrid-search / ANN / lab material, not the official L3 deck | ✓ `labs/S03-hybrid-search/README.md` only | official L3 deck still needed before writing `notes/S03-model-landscape.md` |
| L4 | Structured Outputs & Function Calling | ✗ | ☐ | deck required |
| L5 | Fine-Tuning & Preference Optimization | ✗ | ☐ | deck required |
| L6 | Agent Memory Systems | ✗ | ☐ | deck required |
| L7-L8 | RAG: Foundations to Advanced; Mid-Term Revision | ✗ | ☐ | deck required |
| L9 | Agent Planning & Multi-Agent Systems | ✗ | ☐ | deck required |
| L10 | Evaluation: RAG to Agents | ✗ | ☐ | deck required |
| L11 | Cost Optimization & Prompt Caching | ✗ | ☐ | deck required |
| L12 | Security & Adversarial Robustness | ✗ | ☐ | deck required |
| L13 | MCP Deep Dive | ✗ | ☐ | deck required |
| L14 | A2A & Interoperability | ✗ | ☐ | deck required |
| L15-L16 | Ethics, Governance & Bias Mitigation; final revision | ✗ | ☐ | deck required |

## Lab Material Status

| Lab | Handout objective | Material held | Status |
|---|---|---|---|
| 1 | Tokenization and AI Bot with Tool Calling | ✓ `byte_pair_encoding.ipynb`; `LocalGPT.ipynb`; `tavily_weather_agent.ipynb` | Notebook map added to S01 note and Lab 1 README |
| 2 | Similarity metrics, Text to speech, Rule based systems, Sentiment analysis | partial `Embedding-distilbert.ipynb` | Embeddings/similarity covered; remaining lab items open |
| 3 | Hybrid Search Implementation | partial extension material reviewed | Lab README exists; official L3 session note still waits for correct deck |
| 4-10 | Later labs | ✗ | collect when sessions arrive |

## Public References

521 references are public papers/specs, not commercial textbooks. Fetch public sources directly when each session arrives; do not ask the user to upload them unless access is blocked.

| Reference | Session | Status |
|---|---|---|
| *The Landscape of AI Agents* (Masterman et al., 2024) | L1 | ✓ processed into S01 |
| *Dense Passage Retrieval* (Karpukhin et al., 2020) | L2 | ✓ processed into S02 |
| ReAct (Yao et al., 2023) | L4 | later |
| DPO (Rafailov et al., 2023) | L5 | later |
| MemGPT (2023) + LangGraph memory docs | L6 | later |
| Anthropic Contextual Retrieval (2024) | L7-L8 | later |
| MetaGPT (2024) | L9 | later |
| MT-Bench / LLM-as-judge and GAIA | L10 | later |
| Anthropic prompt-caching docs | L11 | later |
| MCP specification | L13 | later |
| A2A specification | L14 | later |
| Anthropic Responsible Scaling Policy | L15-L16 | later |

## Recheck Notes — 10 Aug 2026

- S01 note title and taught scope match the L1 handout row. BPE is treated as Lab 1 support, not as a new session title.
- S02 note title and taught scope match the L2 handout row. Deep audit repeated on 10 Aug 2026 against all 48 slides of `Session_02_Embeddings_Vector_Search.pdf`, the direct handout row, the DistilBERT notebook, and the DPR paper metadata. Reorganized the note so the main parts visibly match the three handout sub-topics: Semantic vs Keyword Search; Vector Database Architecture (HNSW, ANN); BM25 + Dense Retrieval + RRF. Added missing deck-level teaching details for model key players, training objectives, ANN scale/cost, and HNSW memory/tuning. The DistilBERT notebook remains lab support and does not change the session scope.
- `Session3-ANN-HybridSearch-Ranking.pdf` is deliberately logged as extra L2/Lab 3 material and must not be used as the official L3 model-landscape deck.
- Source-framing scan passes for current notes via `npm run check`.

## Recheck Notes — 11 Aug 2026

- Second-pass line-by-line re-audit of `Session_02_Embeddings_Vector_Search.pdf` and `Embedding-distilbert.ipynb` against `notes/S02-retrieval.md`. Files are unchanged (byte-identical to the 10 Aug upload) but the earlier pass had summarized several of the deck's own concrete numbers into abstract prose instead of keeping the numbers. Folded in: the Borodach et al. 2025 humor-classification F1 stats and dataset size (§4); the deck's own per-task encoder/decoder/encoder-decoder decision table from its "Comparison" slide (§4); the self-attention-vs-cross-attention English/Hindi worked example and Q/K,V source table (prerequisites recap); commercial embedding API pricing and the fuller architecture/layer/training spec table (§7); the deck's $/month cost-at-scale table for linear scan vs HNSW (§11); and the deck's own concrete numbered HNSW walkthrough (entry 1 → 2 → 4 → final 7), added to both the prose worked example and the `S02-hnsw-search.svg` diagram caption. Also rebuilt the Self-study section's note-to-notebook-cell map (previously just a one-line summary) now that the notebook's 13 cells have been read in full, and flagged that the notebook's DistilBERT model is a 6-layer distilled variant while §5's pipeline walkthrough uses BERT-base's 12-layer numbers as the generic teaching example.

## Recheck Notes — 11 Aug 2026 (bullet-by-bullet reconciliation)

- Third pass on `Session_02_Embeddings_Vector_Search.pdf` (unchanged, byte-identical re-upload), this time applying the new Draft-to-Source Reconciliation rule from `AGENTS.md`: extracted text checked bullet by bullet against `notes/S02-retrieval.md` rather than a synthesis-based re-read. All four concepts the deck cites via named papers were taught correctly in the note but the paper attributions themselves were missing. Fixed: **Sentence-BERT** (Reimers & Gurevych, 2019) added to the pooling section — the note taught mean pooling without naming the model that established the pattern; **HNSW** (Malkov & Yashunin, 2018) added to §13; **Product Quantization** (Jégou et al., 2011) added next to the IVF/PQ comparison table; **Dense Passage Retrieval**'s Karpukhin et al. (2020) citation — already logged in this file's Public References table — was missing from the note body itself, now added inline in §17.
- Also added the deck's own "Popular models by architecture (2025 snapshot)" list (encoder-only / decoder-only / encoder-decoder named examples) to §4, which the note's per-task decision table didn't carry even though the underlying architecture comparison was already thorough.
- `npm run check` clean after fixes (36/36 diagrams, 0 source-framing violations).

## Storage Rule

Recordings, decks, transcripts, and raw PDFs stay outside git or in ignored source folders only. The durable record is the note/lab README, not the raw course material.
