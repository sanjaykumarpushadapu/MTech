# 521 · Group Assignment 1 · Roadmap

**Problem Statement 2 — Study of Embedding Models and Approximate Nearest Neighbor Search: Semantic Quality vs Search Efficiency**
Source: `S1_26_AIMLZG521_Assignment1_PS2_SD.pdf` · 10 marks · group submission (.ipynb + PDF report, zipped)

Window: handout says ~15 days per assignment (521-master.md flags the slide's "~3 weeks" as optimistic — plan for 15 days from whenever it's assigned).

## Scoring map

| Module | Task | Marks | Proves |
|---|---|---:|---|
| M1 — Dataset & Embedding Prep | T1 Corpus/query dataset | 0.5 | You can assemble a valid retrieval eval set |
| M1 | T2 Embedding generation & pooling | 0.5 | You understand encoder models, not just an API call |
| M2 — Similarity & Exact Retrieval | T3 Similarity metric comparison | 1.5 | Cosine vs dot vs L2 — you know when they diverge |
| M2 | T4 Exact kNN baseline | 1.5 | You have ground truth to judge ANN against |
| M3 — ANN Search | T5 HNSW vs IVF | 2.0 | You can run and tune real ANN indexes |
| M3 | T6 Trade-off analysis | 1.0 | You can read recall/latency curves and justify a pick |
| M4 — Embedding Quality | T7 Qualitative retrieval analysis | 2.0 | You can explain *why* two models disagree |
| M4 | T8 Final recommendation | 1.0 | You can turn evidence into a production decision |

Everything here is already covered conceptually in `notes/S02-retrieval.md` — this assignment is that note's Part 2 (and half of Part 1) turned into code. Section numbers below point at the exact place to re-read before implementing each task.

## Suggested timeline (15 days)

| Days | Focus |
|---|---|
| 1–2 | Pick dataset + both embedding models; confirm relevance-label format; assign contribution areas |
| 3–4 | M1 — generate embeddings for both models, log dims/pooling/time (Task 1–2) |
| 5–7 | M2 — similarity metric comparison + exact kNN baseline with Recall@5/latency (Task 3–4) |
| 8–11 | M3 — build HNSW and IVF indexes, sweep parameters, produce the two trade-off plots (Task 5–6) |
| 12–13 | M4 — qualitative comparison across 10 queries, write the final recommendation (Task 7–8) |
| 14 | Assemble PDF report (exec summary + all sections), cross-check against the 15-point notebook checklist below |
| 15 | Final run-through top to bottom, zip, submit |

## Task-by-task plan

**T1 — Corpus & query dataset.** Use a BEIR-format dataset — it already ships `corpus`, `queries`, and `qrels` (relevance labels) in the exact shape the task asks for, so you're not hand-building relevance judgments. Good size fits (≥1,000 passages, ≥50 queries out of the box): `SciFact`, `NFCorpus`, or `FiQA-2018`. Subsample if you want a smaller working set; don't undersample below the stated minimums.

**T2 — Embedding generation & pooling.** Pick two models with genuinely different profiles so the later "semantic quality vs efficiency" comparisons have something real to show:
- `distilbert-base-uncased` (mean pooling) — you already have working code for this from Lab 2's `Embedding-distilbert.ipynb`. Small, fast, weaker semantic quality.
- One contrastively-trained sentence-embedding model — `bge-large-en-v1.5` or a smaller `bge-small-en-v1.5`/`all-MiniLM-L6-v2` if compute is tight. Named and profiled in S02 note §8 (dimension, context length, training objective per model).
- Log per model: name, embedding dim, max input length, pooling strategy (§7), wall-clock time to embed the corpus.
- **"Why encoder models are appropriate" is a separate sub-requirement from the model comparison** — answer it from §3 (What are Encoder Models?) and §4 (Encoder vs Decoder vs Encoder-Decoder): encoders produce a fixed bidirectional representation of the whole input in one pass, which is exactly what a similarity search needs; a decoder is built to generate the *next* token, not a stable whole-input vector. §9's training-objective contrast (contrastive vs MLM) is the separate explanation for why your *two chosen models* differ, not for why encoders in general are the right family.

**T3 — Similarity metric comparison.** Pick **one** of your two Task 2 models (the task is explicit: "for one selected embedding model") — don't redo this for both, that's wasted effort the rubric isn't asking for. Cosine, dot product, L2 — math definitions and when they diverge are in §10. Practical note: dot product and cosine only rank identically when vectors are normalized; that's the concrete thing to demonstrate on your 20 query-document pairs, not just assert.

**T4 — Exact kNN baseline.** Brute-force search against every document embedding, Top-5, Recall@5, per-query latency, **and "number of vectors examined per query"** — for exact search this is simply the full corpus size N every time, but the PDF asks you to report it explicitly so it's the number T5's ANN configs get compared against. This is your ground truth — §12 ("Linear Scan vs ANN Solution") explains why this baseline exists and what it costs at scale (O(N) per query, §11's computational-challenge math).

**T5 — HNSW vs IVF.** Use FAISS for both (`IndexHNSWFlat`, `IndexIVFFlat`) — it's the standard tool and matches the index behavior described in §13–16. Vary `ef_search` for HNSW (§16 gives typical ranges: `M=16`, `ef_construction=200`, sweep `ef_search` 50→500) and `nprobe` for IVF across at least three values (§13's IVF row: "sensitive to nprobe"). ⚠️ FAISS's actual attribute names are camelCase, not the snake_case used in the literature/notes: `index.hnsw.efSearch`, `index.hnsw.efConstruction`, `index.nprobe` — a common bug is setting the wrong-cased attribute silently (FAISS won't error, it'll just ignore it). For each configuration measure Recall@5, average query latency, speed relative to the T4 exact baseline, **and** number/fraction of candidate vectors examined (FAISS doesn't expose this directly for HNSW; approximate it via `ef_search` for HNSW and `nprobe/nlist × N` for IVF, and say so explicitly — "where measurable" in the PDF is permission to do exactly this).

**T6 — Trade-off analysis.** Plot Recall@5 vs latency and Recall@5 vs search efficiency across all HNSW/IVF configurations from T5. Call out the fastest config, the highest-recall config, and the best-balanced one — this is the same "brute-force O(N) vs HNSW O(log N)" trade-off argued qualitatively in §14, now backed by your own numbers.

**T7 — Qualitative retrieval analysis.** Take 10 queries, compare Top-5 from both embedding models side by side. The task requires **at least three** of the six named difference types (semantic similarity, keyword overlap, domain-specific terminology, ambiguous queries, short queries, long queries) — pick three you can actually show with a real example pair, don't just assert all six. §9's training-objective distinction predicts the pattern to look for: the contrastive model should win on paraphrase and domain terminology; DistilBERT (MLM-only, no retrieval fine-tuning) should lean more on lexical overlap. Naming *why* — pooling strategy, training objective — is what separates this from just eyeballing two lists.

**T8 — Final recommendation.** Answer all six sub-questions with a number or config from T3–T7, not a general statement — the PDF explicitly says recommendations must be evidence-based. "Resource-constrained deployment" should point at a specific T5/T6 configuration (smaller `M`/lower `ef_search`, or IVF with fewer `nprobe`), not a new idea introduced here. For "how would you deploy in production," §17 (vector database architecture) gives the components to reference (embedding service, index, metadata filters, monitoring) rather than answering in the abstract.

## Group contribution split

The assignment's 6 contribution areas map directly to the 8 tasks — a natural 6-person (or fewer, doubled-up) split:

| Area | Tasks | Marks |
|---|---|---:|
| Dataset & embedding | T1, T2 | 1.0 |
| Similarity matrix comparison | T3 | 1.5 |
| kNN baseline | T4 | 1.5 |
| HNSW vs IVF | T5 | 2.0 |
| Evaluation & analysis | T6, T7 | 3.0 |
| Visualization & reporting | T8 + final PDF/report assembly | 1.0 + report |

## Grading risk flags (easy to lose marks even with correct code)

- **Explain the internals, not just the API call** (General Instructions #9) — calling `SentenceTransformer.encode()` or `faiss.IndexHNSWFlat()` and reporting numbers is not enough. For every method used, state what it's doing underneath (pooling math, HNSW's layered graph search, IVF's cluster-then-search) — the note sections cited above are exactly this explanation, adapt them in your own words.
- **Wrong assignment set = not evaluated at all** (General Instructions #5) — confirm PS2 is actually the set assigned to your group before starting.
- **Every executed cell must show its output** (#3) and **the notebook must run start-to-end without errors** (#12) — a broken cell or a missing dataset link at submission time is explicitly called out as penalizable.
- **AI-assisted content without demonstrated understanding is penalized** (#13) — if you use an LLM to help write explanation text, make sure you can defend every claim; the inference/justification sections are graded on understanding, not prose quality.
- **Every claim needs a citable reference** (#14) — dataset source, model names/cards, FAISS docs, and Malkov & Yashunin (2018) for HNSW if you explain its mechanism, all belong in the references section.

## Deliverables checklist

Notebook must include all of (PDF instruction §7 a–o — every letter is graded individually, missing any one risks a deduction per §10):

- [ ] (a) Assignment title
- [ ] (b) Student details
- [ ] (c) Per-member contribution, including which section each student did
- [ ] (d) Problem statement
- [ ] (e) Dataset details and source
- [ ] (f) Tools and libraries used
- [ ] (g) Code implementation
- [ ] (h) Output screenshots/results
- [ ] (i) Explanation of the logic used
- [ ] (j) Justification for the chosen method/model/approach
- [ ] (k) Inference drawn from the results
- [ ] (l) Limitations observed
- [ ] (m) Possible improvements
- [ ] (n) Final conclusion
- [ ] (o) References

PDF report (max 30 pages): experimental methodology, comparative tables, graphs, retrieval examples, analysis/recommendations, **one-page executive summary**.

Submit: `.ipynb` + PDF report, zipped as one file per group. Double-check the **correct assignment set** was used — an incorrect set is not evaluated at all.
