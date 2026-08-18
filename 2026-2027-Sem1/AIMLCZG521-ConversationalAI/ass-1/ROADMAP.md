# 521 · Group Assignment 1 · Roadmap

**Problem Statement 2 — Study of Embedding Models and Approximate Nearest Neighbor Search: Semantic Quality vs Search Efficiency**
Source: `S1_26_AIMLZG521_Assignment1_PS2_SD.pdf` · **Group 129** · 10 marks · group submission (.ipynb + PDF report, zipped)

**Deadline: 28 Aug 2026 (Fri).** That's 10 days from 18 Aug — noticeably tighter than the course's general "~15 days per assignment" pattern (521-master.md), so the schedule below is compressed accordingly, not the earlier 15-day version.

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

## Timeline — 18 to 28 Aug 2026 (10 days)

The module order (M1→M2→M3→M4) is the right order to *read and understand* the tasks, but it is **not** the tightest order to *execute* them in a 4-person team — T7 only depends on T2, not on T3–T6, so it doesn't need to wait for module 3 to finish, and with only 10 days there's no slack to waste.

**Dependency chain:** T1→T2 gates everything. T3 and T4 both need T2. T5 needs T2, and needs T4's latency number for its "speed relative to exact search" measurement. T6 needs T5. T7 needs only T2 — no dependency on T3–T6. T8 and the report need everything finished.

| Date | Day | Focus | Who |
|---|---|---|---|
| Tue 18 Aug | 0 (today) | Kickoff: confirm remote system access, pick the dataset (SciFact/NFCorpus/FiQA-2018) and both embedding models, lock in the 4-person split | Whole team |
| Wed–Thu 19–20 Aug | 1–2 | T1 (corpus/queries) + T2 (embeddings, both models, logged specs) | P1 |
| Fri–Sat 21–22 Aug | 3–4 | T3 + T4 (similarity metrics, exact kNN baseline) **running in parallel with** T7 (qualitative comparison) — both branches only need P1's Thu embeddings | P2 → T3, T4 · P4 → T7 |
| Fri 21–Mon 24 Aug | 3–6 | T5 (HNSW vs IVF) — starts same day as P2/P4, needs T4's latency number from P2 (~22 Aug) to finish the "speed relative to exact search" measurement | P3 |
| Tue 25 Aug | 7 | T6 (trade-off plots) — needs P3's T5 sweep, finished 24 Aug | P4 |
| Wed 26 Aug | 8 | T8 (final recommendation) — needs T3, T5/T6, T7 all in hand | P1 + P4 |
| Tue–Thu 19–27 Aug | throughout | Draft static report sections (dataset details, tools/libraries, problem statement, methodology) whenever free — don't wait for 27 Aug to start writing | P1 |
| Thu 27 Aug | 9 | Assemble the full PDF report + executive summary, run the 15-point notebook checklist, gather Virtual Lab screenshots | Whole team, P1 leads |
| Fri 28 Aug | 10 (deadline) | Final start-to-end run-through, zip, **submit early in the day** — strictly no makeups, no late buffer | Whole team |

Ten days is tight enough that the parallel T7/T3-T4 split isn't optional — if P2, P3, and P4 all wait for each other in sequence instead of branching after 20 Aug, the team runs out of runway before 28 Aug.

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

## Group contribution split (4 members)

Six contribution areas over four people means two people each own two areas — paired here so each person's load is ~2–3 marks and their active weeks don't all collide:

| Member | Areas | Tasks | Marks | Active when (18–28 Aug) |
|---|---|---|---:|---|
| P1 | Dataset & embedding **+** Visualization & reporting | T1, T2 · T8 + final report/exec-summary assembly | 2.0 + report | 19–20 Aug (setup, blocks everyone else), background report drafting 19–27 Aug, T8 26 Aug, assembly 27–28 Aug |
| P2 | Similarity matrix comparison **+** kNN baseline | T3, T4 | 3.0 | 21–22 Aug, right after P1's 20 Aug embeddings land |
| P3 | HNSW vs IVF | T5 | 2.0 | 21–24 Aug — starts same day as P2 (only needs T2), syncs with P2 ~22 Aug for T4's latency number |
| P4 | Evaluation & analysis | T6, T7 | 3.0 | **T7: 21–22 Aug**, in parallel with P2 (only needs T2, not T3–T6) — don't wait for module order. **T6: 25 Aug**, once P3's T5 sweep lands 24 Aug |

P1 deliberately carries the lightest task-marks load because report assembly (exec summary, consolidated comparative tables, making sure every figure is labelled per the #15 risk flag) is real work that isn't separately marked but is required for every checklist item. P4's two tasks are split across the timeline rather than back-to-back — running T7 early avoids a week of idle time waiting on T5. Every member still documents their own contribution in both the notebook and the report per the contribution guidelines, regardless of this table.

## Resolved clarifications

- ✅ **"Prescribed environment" (#4) and "Virtual Lab" (#10), resolved** — the course has issued remote system access with good specs (confirmed). Run the actual computation there rather than on a personal laptop, and take screenshots of the notebook running on that system for instruction #10's "Virtual Lab screenshots" requirement — a few per module (T2 embedding generation, T5 index building, T6 plots) is a safe amount. This also means model/dataset choice doesn't need to be compute-conservative: `bge-large-en-v1.5` (T2's stronger model recommendation) and the larger `FiQA-2018` corpus are both fine if you'd rather use them than the smaller options.
- ✅ **Two files, not three** — going with the Deliverables section's literal listing: `.ipynb` + one PDF report (max 30 pages), zipped together. That PDF report should do double duty for instruction #2b's "PDF format of the executed notebook," so build it accordingly rather than as pure narrative: include the actual code (or key snippets) alongside its output for every task, not just prose describing what you did — screenshots/exports of executed cells, not just result tables. That gives the single report the best chance of satisfying both #2b and #11/Deliverables at once. If a TA later asks specifically for a raw `nbconvert` export as a third file, that's a five-minute fix, not a redesign.
- ✅ **`SD` suffix, resolved — "Student Details"** (per-group filename tag, not a problem-statement variant code). So the filename itself doesn't raise a "wrong set" risk; it's just this document's per-group naming, not a sign there's a different PS2 variant out there. General Instructions #5's warning about submitting the correct Assignment Set still applies in the general sense (this is Problem Statement 2, not PS1/PS3/etc.) — worth a quick confirmation that Group 129 was assigned PS2 specifically, but not because of the `SD` tag.

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

Submit two files, zipped together: `.ipynb` + the PDF report (built to double as evidence of the executed notebook — see above). Double-check PS2 was Group 129's assigned set, and that you have the Virtual Lab screenshots the course expects.
