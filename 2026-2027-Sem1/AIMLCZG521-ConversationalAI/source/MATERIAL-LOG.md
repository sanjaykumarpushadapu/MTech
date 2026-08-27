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
| L3 | Model Landscape & Cost Engineering | ✓ Session-4 deck (instructor label "Lecture No. 4 | Module 1"), title "Model Landscape & Cost Engineering"; QLoRA (Dettmers 2023, public) | ✓ `notes/S03-model-landscape.md`; `source/S03-slide-inventory.md`; 11 authored SVGs; `labs/S03-hybrid-search/README.md` | none known |
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
| 3 | Hybrid Search Implementation | ✓ ANN/hybrid deck ("Lecture 3", 62 slides) processed | Deck depth folded into `notes/S02-retrieval.md` (IVF, PQ, TF-IDF, BM25 math, RRF); `source/S02-ann-hybrid-slide-inventory.md` added, coverage 52/52; hybrid-search lab code still ☐ |
| 4-10 | Later labs | ✗ | collect when sessions arrive |

## Public References

521 references are public papers/specs, not commercial textbooks. Fetch public sources directly when each session arrives; do not ask the user to upload them unless access is blocked.

| Reference | Session | Status |
|---|---|---|
| *The Landscape of AI Agents* (Masterman et al., 2024) | L1 | ✓ processed into S01 |
| *Dense Passage Retrieval* (Karpukhin et al., 2020) | L2 | ✓ processed into S02 |
| *QLoRA: Efficient Finetuning of Quantized LLMs* (Dettmers et al., 2023) | L3 | ✓ taught in S03 (NF4, double quantization, paged optimizers, 31× on 70B) from established paper knowledge + deck; full arXiv text fetch deferred |
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

- Second-pass line-by-line re-audit of `Session_02_Embeddings_Vector_Search.pdf` and `Embedding-distilbert.ipynb` against `notes/S02-retrieval.md`. Files are unchanged (byte-identical to the 10 Aug upload) but the earlier pass had summarized several of the deck's own concrete numbers into abstract prose instead of keeping the numbers. Folded in: the Borodach et al. 2025 humor-classification F1 stats and dataset size under **Encoder vs Decoder vs Encoder-Decoder**; the deck's own per-task encoder/decoder/encoder-decoder decision table from its "Comparison" slide under **Encoder vs Decoder vs Encoder-Decoder**; the self-attention-vs-cross-attention English/Hindi worked example and Q/K,V source table (prerequisites recap); commercial embedding API pricing and the fuller architecture/layer/training spec table under **Embedding Models: Key Players**; the deck's $/month cost-at-scale table for linear scan vs HNSW under **Linear Scan vs ANN Solution**; and the deck's own concrete numbered HNSW walkthrough (entry 1 → 2 → 4 → final 7), added to both the prose worked example and the `S02-hnsw-search.svg` diagram caption. Also rebuilt the Self-study section's note-to-notebook-cell map (previously just a one-line summary) now that the notebook's 13 cells have been read in full, and flagged that the notebook's DistilBERT model is a 6-layer distilled variant while **How Encoder Transformers Create Embeddings** uses BERT-base's 12-layer numbers as the generic teaching example.

## Recheck Notes — 11 Aug 2026 (bullet-by-bullet reconciliation)

- Third pass on `Session_02_Embeddings_Vector_Search.pdf` (unchanged, byte-identical re-upload), this time applying the new Draft-to-Source Reconciliation rule from `AGENTS.md`: extracted text checked bullet by bullet against `notes/S02-retrieval.md` rather than a synthesis-based re-read. All four concepts the deck cites via named papers were taught correctly in the note but the paper attributions themselves were missing. Fixed: **Sentence-BERT** (Reimers & Gurevych, 2019) added to the pooling section — the note taught mean pooling without naming the model that established the pattern; **HNSW** (Malkov & Yashunin, 2018) added to **HNSW: Hierarchical Navigable Small World**; **Product Quantization** (Jégou et al., 2011) added next to the IVF/PQ comparison table; **Dense Passage Retrieval**'s Karpukhin et al. (2020) citation — already logged in this file's Public References table — was missing from the note body itself, now added inline in **Dense Passage Retrieval**.
- Also added the deck's own "Popular models by architecture (2025 snapshot)" list (encoder-only / decoder-only / encoder-decoder named examples) to **Encoder vs Decoder vs Encoder-Decoder**, which the note's per-task decision table didn't carry even though the underlying architecture comparison was already thorough.
- `npm run check` clean after fixes (36/36 diagrams, 0 source-framing violations).

## Recheck Notes — 11 Aug 2026 (fourth pass, image slides)

- Explicitly re-rendered and visually inspected the HNSW walkthrough slides (pp. 40-42) and the computational-challenge slide (p. 33), since these carry mostly diagram content that plain text extraction under-represents. The step-by-step walkthrough (entry 1→2, greedy to 4, final closest 7) and the 10M/768-dim/7.68s/768-core numbers all matched **Linear Scan vs ANN Solution** and **HNSW: Hierarchical Navigable Small World** exactly — no gap there. One thing the diagram carried that the note's prose didn't state explicitly: the deck's own **Brute-Force O(N) vs HNSW O(log N)** complexity labels, shown visually on p. 42 rather than as a bullet. The note only said "near logarithmic" in prose; added the explicit Big-O comparison to **HNSW: Hierarchical Navigable Small World**.
- `npm run check` clean (36/36 diagrams, 0 source-framing violations).

## Recheck Notes — 11 Aug 2026 (fifth pass, automated slide-coverage check)

- Generated `source/S02-slide-inventory.md` (previously only S01 had one, despite `AGENTS.md`'s intake rule requiring one per deck) and ran `tools/check-slide-coverage.mjs` against `notes/S02-retrieval.md`. The first raw run, before pruning extraction noise, surfaced several genuine gaps the four prior manual passes had missed: the full transformer-block breakdown (Embeddings+PosEnc, Multi-Head Self-Attention, LayerNorm+Residual, FFN with ReLU, Nx layers, Linear+Softmax) in the prerequisites recap; the Borodach paper's actual tested model list (XLNet, ModernBERT, NeoBERT, BART-large-mnli, Flan-T5-base, Qwen2); named models for each embedding training objective (SimCSE, NV-Embed, SpanBERT, RetroMAE v2/RetroMAE-BEIR); "skip list" as HNSW's formal underlying data structure; concrete product examples (ChatGPT, Claude, GitHub Copilot) behind the architecture-choice table.
- After fixes, pruned the inventory of extraction noise (OCR corruption from the source PDF's font-kerning bug, logistics slides, generic capitalized words) and re-ran: 43/43 slides fully covered.
- `npm run check` clean (36/36 diagrams, 0 source-framing violations).

## Recheck Notes — 27 Aug 2026 (L3 identity resolved; L3/L4 numbering reconciled)

- The official **Model Landscape & Cost Engineering** deck arrived, self-labelled by the instructor as **"Lecture No. 4 | Module 1"**. Under the repo's Handout-First rule its *topic* maps cleanly to the handout **L3** row (LLMs/MoE/SLMs/SSMs comparison; Quantization & KV-Cache; Prompt Caching & Model Routing; ref QLoRA/Dettmers 2023), so it was written as `notes/S03-model-landscape.md`. Uploads do not renumber sessions — the deck's "Lecture 4" label reflects delivery order, not handout scope.
- This resolves the open L3 gap and **validates the earlier call** (10–11 Aug) that `Session3-ANN-HybridSearch-Ranking.pdf` is extra **L2** material, not the L3 model-landscape deck. Both facts now line up: the instructor's live lecture count runs one ahead of the handout because retrieval took two contact sessions — instructor Lecture 2 = handout L2 (embeddings/vector search), instructor Lecture 3 = still handout L2 scope (ANN algorithms + hybrid: HNSW/IVF/PQ, TF-IDF/BM25, RRF), instructor Lecture 4 = handout L3 (model landscape). Handout session numbers (and exam scope) are unchanged.
- Full 39-slide audit performed against the rendered deck: title slide, agenda, 2025/2026 landscape tables, Dense/MoE/SLM/SSM sections, attention + quadratic-complexity bridge, quantization ladder + FP formats + PTQ (GPTQ/AWQ/FP8), LoRA/QLoRA, GPU-memory formula, KV-cache (3 slides), inference-at-scale, token economics, prompt caching, routing, cost playbook, self-host break-even, emerging trends. Slide 9's image-only "Transformer vs. MoE" architecture diagram (text extraction dropped it to a bare title) was caught on the visual pass and captured. Logistics slides (disclaimer, objectives, references) kept out of the note per the master-index rule.
- Worked-example arithmetic executed and reconciled against the deck: MoE savings (94.5/72.3/75.4/86.9%), LoRA 256× / QLoRA 31× (1,120→36 GB), KV-cache Llama-8B ≈1 GB @2K, routing effective $0.06/1K, caching 89%. Two deck rounding inconsistencies flagged in-note with ⚠️: the routing case-study headline (deck 95% vs table-computed 92%) and the 128K KV-cache figure (deck ~137 GB; the point that survives is KV ≫ weights at long context).
- `Session3-ANN-HybridSearch-Ranking.pdf` (instructor Lecture 3) is being folded into `notes/S02-retrieval.md` as additional L2 depth in the same session; a further recheck note will record what was added.

## Recheck Notes — 27 Aug 2026 (ANN/Hybrid deck folded into S02)

- The instructor "Lecture 3" deck (`Session3-ANN-HybridSearch-Ranking.pdf`, 62 slides) was audited slide-by-slide against `notes/S02-retrieval.md`. Its topics are all handout **L2** scope, so — per the Handout-First / no-renumber rule — its genuinely-new depth was layered into the existing S02 note rather than made a new session.
- Added to S02: a full **IVF** section (k-means partition, inverted lists, nprobe search, the nlist=3/nprobe=1 numerical example, O(KD+ND/K) complexity, nlist/nprobe tuning), a full **Product Quantization** section (subvector split, codebook training, ADC table-lookup distance, the 5×8 memory example 160 B→74 B, M/k parameters, IVF+PQ), the **ANN-algorithm complexity-comparison** table (Linear/HNSW/IVF/PQ/IVF+PQ/HNSW+PQ + FAISS/ScaNN/ANNOY), a new **TF-IDF** section (TF·IDF, the dense-retrieval limitations that motivate sparse: exact-keyword/rare-term/OOV, TF-IDF's four gaps), and expanded **BM25** (full formula with k₁/b, saturation curve, worked example BM25=4.159, BM25-vs-TF-IDF), **RRF** (score-range problem, why k≈60, five properties), and **hybrid** (BM25/vector/hybrid performance table). Four new diagrams: `S02-ivf-search.svg`, `S02-pq-encode.svg`, `S02-tfidf-idf.svg`, `S02-bm25-saturation.svg`.
- Section renumber: IVF/PQ inserted as 14/15 (HNSW block shifted to 16–19), TF-IDF inserted as 20 (BM25→21, DPR→22, RRF→23, Hybrid→24). Existing numeric cross-references all point to sections ≤11 and were unaffected. Worked-example arithmetic re-executed (TF-IDF 0.530, BM25 4.159, IVF ~100×, PQ 160→74 B, RRF Doc A 0.03252). `npm run check` clean (0 framing violations); all 22 S02 diagram links resolve, no unused SVGs; slide-coverage 52/52 against the new ANN inventory.

## Storage Rule

Recordings, decks, transcripts, and raw PDFs stay outside git or in ignored source folders only. The durable record is the note/lab README, not the raw course material.
