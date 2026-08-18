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

Each task below is a literal step list — do them in order, check them off as you go. S02 note section numbers (§) tell you where to re-read the concept before implementing it.

### T1 — Corpus & query dataset · 0.5 marks

1. Choose one BEIR-format dataset: `SciFact` (~5K docs / 300 queries), `NFCorpus` (~3.6K / 323), or `FiQA-2018` (~57K / 648) — all clear the 1,000-passage / 50-query minimums out of the box.
2. Download its `corpus`, `queries`, and `qrels` (relevance labels) — BEIR ships all three already in the right shape, so you don't hand-build relevance judgments.
3. Optional: subsample down to a lighter working set — never below 1,000 passages or 50 queries.
4. Record the dataset name, size, and source now — you'll need it verbatim for checklist item (e).

### T2 — Embedding generation & pooling · 0.5 marks

1. Pick two encoder models with clearly different profiles:
   - `distilbert-base-uncased` with mean pooling — reuse Lab 2's `Embedding-distilbert.ipynb` code.
   - One contrastively-trained model: `bge-large-en-v1.5` (or `bge-small-en-v1.5` / `all-MiniLM-L6-v2` if compute is tight). Profiled in S02 §8.
2. Generate embeddings for the **same** corpus with both models.
3. For each model, log: name, embedding dimension, max/typical input length, pooling strategy used (§7), approximate embedding time.
4. Answer **"why are encoder models appropriate"** — this is a separate sub-requirement from step 5. Source it from §3–§4: encoders build one fixed, bidirectional representation of the whole input in a single pass, which is exactly what similarity search needs; a decoder is built to predict the *next* token, not a stable whole-input vector.
5. Explain **why your two specific models differ** — source it from §9 (contrastive training vs MLM). This is the model-comparison half; keep it separate from step 4.

### T3 — Similarity metric comparison · 1.5 marks

1. Pick **one** of your two Task 2 models — the task says "for one selected embedding model," so don't repeat this for both.
2. Select at least 20 query-document pairs.
3. Compute cosine similarity, dot product, and L2/Euclidean distance for every pair (definitions in §10).
4. Check whether the Top-k ranking changes depending on which metric you use.
5. Check whether normalizing the vectors changes the result — cosine and dot product only rank identically once vectors are normalized; show this, don't just assert it.
6. State which metric is most suitable for your embeddings, referencing the math (not the library default).

### T4 — Exact kNN baseline · 1.5 marks

1. Implement brute-force search: for each query, compare its embedding against every document embedding.
2. Retrieve Top-5 per query.
3. Measure, per query: search latency, Recall@5, and number of vectors examined (this equals the full corpus size N for exact search every time — report it anyway, since it's the number T5's ANN configs get compared against).
4. Report the average latency across the whole query set.
5. Ground the "why this baseline matters" explanation in §12/§11 (exact search costs O(N) per query).

### T5 — HNSW vs IVF · 2 marks

1. Build an HNSW index (`faiss.IndexHNSWFlat`) and an IVF index (`faiss.IndexIVFFlat`) over the same embedding vectors.
2. For HNSW, sweep `ef_search` across at least two values, e.g. start `M=16`, `ef_construction=200`, then vary `efSearch` 50 → 500 (§16). ⚠️ FAISS's real attribute name is camelCase: `index.hnsw.efSearch` / `index.hnsw.efConstruction` — using the snake_case from the literature silently does nothing, no error.
3. For IVF, vary `nprobe` (attribute: `index.nprobe`) across at least three values.
4. Run the identical query set through every configuration.
5. For each configuration measure: Recall@5, average query latency, speed relative to the T4 exact baseline, and candidate vectors examined — approximate this via `ef_search` for HNSW and `nprobe/nlist × N` for IVF, and say explicitly that it's an approximation ("where measurable" in the PDF is permission to do exactly this).

### T6 — Trade-off analysis · 1 mark

1. Plot Recall@5 vs query latency across every HNSW/IVF configuration from T5.
2. Plot Recall@5 vs search efficiency (vectors examined, or speedup vs the exact baseline).
3. From the two plots, name: the fastest config, the highest-recall config, the best-balanced config.
4. Answer: for a large query volume, which configuration would you deploy and why — cite the actual numbers from steps 1–3, not a general statement.

### T7 — Qualitative retrieval analysis · 2 marks

1. Select 10 representative queries.
2. Retrieve Top-5 from each of your two Task 2 models for every query.
3. Compare the two result lists side by side.
4. Pick **at least 3 of the 6** named difference types (semantic similarity, keyword overlap, domain-specific terminology, ambiguous queries, short queries, long queries) and give a real example pair for each — don't just assert all six.
5. Explain *why* the models differ for each example, tying back to §9: the contrastive model should win on paraphrase/domain terms; the MLM-only model (DistilBERT) should lean more on lexical overlap.

### T8 — Final recommendation · 1 mark

Answer all six, each with a specific number or config pulled from T3–T7 — not a general statement:

1. Which embedding model performed better?
2. Which similarity metric was most appropriate?
3. Which ANN method had the best trade-off?
4. What configuration for a resource-constrained deployment — point at a specific T5/T6 config (smaller `M`/lower `ef_search`, or IVF with fewer `nprobe`), not a new idea introduced here.
5. What's the main limitation of your chosen approach?
6. How would you deploy this in production — reference §17's components (embedding service, index, metadata filters, monitoring).

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

## Two things to verify before you start — genuinely ambiguous from this PDF alone

- ⚠️ **"Virtual Lab screenshots"** — General Instruction #10 lists these as a required, penalizable-if-missing item ("missing Virtual Lab screenshots ... may lead to a reduction of marks"), and #4 requires the "prescribed environment" specifically. Neither is defined in this PDF — that's almost certainly set up in the course handout / Canvas (the "prescribed environment" is very likely BITS's Virtual Lab). **Confirm what this environment is and what screenshots are expected before you build anything** — code correctly run in Colab or a local notebook may not count if the prescribed environment is something else.
- ⚠️ **One PDF or two?** Instruction #2 asks for "the completed assignment notebook in both formats: (a) `.ipynb`, (b) PDF format of the executed notebook" — that reads as a straight PDF export of the notebook itself (all cells + outputs, via `nbconvert`/print). Separately, Instruction #11 and the Deliverables section ask for a "final report in PDF format," capped at 30 pages, with its own structure (methodology, tables, graphs, exec summary) — that reads as a distinct written report, not a notebook export. The Deliverables section only lists two items (`.ipynb` + "PDF report"), which could mean they're treated as the same PDF, or that #2b was folded into #11. **Safest interpretation**: submit all three — `.ipynb`, the notebook exported to PDF, and the separate structured report PDF — zipped together. Confirm with the instructor/TA if possible; Instruction #10 explicitly penalizes "absence of either the .ipynb file or the final PDF report."
- ⚠️ **Confirm "PS2" is actually your group's assigned set** (General Instructions #5: "submission of an incorrect Assignment Set will not be evaluated" — zero, not a deduction). The filename also contains `SD`, which isn't explained anywhere in the extracted text — check the handout/Canvas for what that suffix denotes before assuming this is definitely your group's variant.

## Grading risk flags (easy to lose marks even with correct code)

- **Explain the internals, not just the API call** (General Instructions #9) — calling `SentenceTransformer.encode()` or `faiss.IndexHNSWFlat()` and reporting numbers is not enough. For every method used, state what it's doing underneath (pooling math, HNSW's layered graph search, IVF's cluster-then-search) — the note sections cited above are exactly this explanation, adapt them in your own words.
- **Explanation/justification/inference is required per task, not once for the whole notebook** (#6) — "merely providing code and output will not be sufficient." Each of the 8 tasks needs its own explanation block, not one generic write-up at the end.
- **Every executed cell must show its output** (#3) and **the notebook must run start-to-end without errors** (#12) — a broken cell or a missing dataset link at submission time is explicitly called out as penalizable.
- **Figures, tables, and diagrams must be labelled and explained** (#15) — this note-check-heavy assignment produces a lot of plots (T6's two required charts, comparison tables in T3/T7); an unlabelled axis or an unexplained table is a direct instruction violation, not just a style nitpick.
- **The final conclusion has a specific required shape** (#16) — it must cover key observations, strengths of your approach, limitations, and possible future improvements. A generic wrap-up paragraph doesn't satisfy this; treat it as four sub-points, not one.
- **AI-assisted content without demonstrated understanding is penalized** (#13) — if you use an LLM to help write explanation text, make sure you can defend every claim; the inference/justification sections are graded on understanding, not prose quality.
- **Every claim needs a citable reference** (#14) — dataset source, model names/cards, FAISS docs, and Malkov & Yashunin (2018) for HNSW if you explain its mechanism, all belong in the references section.
- **Each group member contributes to at least one area** and it must be stated in both the notebook and the report (contribution guidelines) — not just the notebook.

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
- [ ] (n) Final conclusion — key observations, strengths, limitations, **and** future improvements (all four, per #16)
- [ ] (o) References

Report PDF (max 30 pages): experimental methodology, comparative tables, graphs, retrieval examples, analysis/recommendations, **one-page executive summary**.

Submit (see the "one PDF or two?" flag above): `.ipynb` + notebook-exported PDF + report PDF, zipped as one file per group. Double-check the **correct assignment set** was used — an incorrect set is not evaluated at all — and that you have whatever Virtual Lab screenshots the course expects.
