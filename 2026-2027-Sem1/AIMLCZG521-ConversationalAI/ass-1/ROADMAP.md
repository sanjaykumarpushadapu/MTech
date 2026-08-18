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

## Day-by-day execution plan

One linear path, in date order — each step is a concrete action, not a description. S02 note section numbers (§) tell you where to re-read the concept before implementing it. **Why this order:** T1→T2 gates everything; T3 and T4 both need T2; T5 needs T2 plus T4's latency number; T6 needs T5; T7 needs only T2, so it runs in parallel with T3/T4 instead of waiting; T8 and the report need everything finished. With only 10 days, skipping the parallel branch (T7 running alongside T3/T4) means running out of runway before 28 Aug.

### Day 0 — Tue 18 Aug (today): kickoff — whole team

1. Confirm everyone can log into the provided remote system.
2. Pick the dataset: `SciFact`, `NFCorpus`, or `FiQA-2018` (all three clear the 1,000-passage/50-query minimums — compute isn't a constraint on the remote system, so pick by topic interest, not size).
3. Pick the two embedding models: `distilbert-base-uncased` (mean pooling) and `bge-large-en-v1.5`.
4. Lock in roles: P1, P2, P3, P4 per the split below.
5. Set up one shared notebook/folder the whole team commits results into.

### Days 1–2 — Wed–Thu 19–20 Aug: T1 + T2 · owner P1 · 1.0 mark

1. Download the chosen dataset's `corpus`, `queries`, and `qrels` (BEIR ships all three pre-labelled).
2. Optional: subsample — never below 1,000 passages / 50 queries.
3. Record the dataset name, size, and source (needed verbatim for checklist item e).
4. Generate embeddings for the full corpus with **both** models.
5. Log per model: name, embedding dimension, max/typical input length, pooling strategy used (§7), approximate embedding time.
6. Write "why encoder models are appropriate" — source from §3–§4 (fixed bidirectional whole-input representation vs a decoder's next-token focus). Keep this separate from step 7.
7. Write "why these two specific models differ" — source from §9 (contrastive training vs MLM).
8. **Share the embeddings + specs with P2, P3, and P4 by end of day** — everything downstream is blocked on this.

### Days 3–4 — Fri–Sat 21–22 Aug: T3 + T4 (owner P2, 3.0 marks) run in parallel with T7 (owner P4, 2.0 marks)

**P2 — T3 (similarity metrics, 1.5 marks):**
1. Pick **one** of the two Day-2 models — the task says "for one selected embedding model," don't repeat for both.
2. Select at least 20 query-document pairs.
3. Compute cosine similarity, dot product, and L2/Euclidean distance for every pair (§10).
4. Check whether the ranking changes across the three metrics.
5. Check whether normalizing the vectors changes the result — cosine and dot product only rank identically once normalized; show it, don't assert it.
6. State which metric is most suitable, referencing the math.

**P2 — T4 (exact kNN baseline, 1.5 marks), right after T3:**
7. Implement brute-force search: compare every query embedding against every document embedding.
8. Retrieve Top-5 per query.
9. Measure per query: latency, Recall@5, and vectors examined (= corpus size N — report it anyway, T5 needs it as the comparison point).
10. Report the average latency across the query set — **send this number to P3 as soon as it's ready**, T5 depends on it.
11. Ground the "why this baseline matters" write-up in §12/§11 (O(N) cost).

**P4 — T7 (qualitative analysis, 2.0 marks), same two days, independently:**
1. Select 10 representative queries.
2. Retrieve Top-5 from each of the two embedding models for every query.
3. Compare the two result lists side by side.
4. Pick **at least 3 of 6** named difference types (semantic similarity, keyword overlap, domain-specific terminology, ambiguous/short/long queries) with a real example pair for each.
5. Explain *why* the models differ per example, tying back to §9 (contrastive model should win on paraphrase/domain terms; DistilBERT should lean on lexical overlap).

### Days 3–6 — Fri 21–Mon 24 Aug: T5 · owner P3 · 2.0 marks (starts same day as P2/P4)

1. Build an HNSW index (`faiss.IndexHNSWFlat`) and an IVF index (`faiss.IndexIVFFlat`) over the same embeddings.
2. Sweep `ef_search` for HNSW across at least two values — start `M=16`, `ef_construction=200`, vary `efSearch` 50→500 (§16). ⚠️ FAISS's real attribute names are camelCase — `index.hnsw.efSearch` / `index.hnsw.efConstruction` — the snake_case version silently does nothing.
3. Vary `nprobe` for IVF (`index.nprobe`) across at least three values.
4. Once P2's Day-4 latency number arrives (~22 Aug), run the identical query set through every configuration.
5. For each configuration, measure Recall@5, average query latency, speed relative to P2's exact baseline, and candidate vectors examined — approximate via `ef_search` for HNSW and `nprobe/nlist × N` for IVF, and say explicitly that it's an approximation.

### Day 7 — Tue 25 Aug: T6 · owner P4 (now free after finishing T7) · 1.0 mark

1. Plot Recall@5 vs query latency across every HNSW/IVF configuration from T5.
2. Plot Recall@5 vs search efficiency (vectors examined, or speedup vs the exact baseline).
3. Name the fastest config, the highest-recall config, and the best-balanced config.
4. Answer: for a large query volume, which configuration would you deploy and why — cite the actual T5/T6 numbers.

### Day 8 — Wed 26 Aug: T8 · owners P1 + P4 · 1.0 mark

Answer all six with a specific number or config from T3–T7, not a general statement:
1. Which embedding model performed better?
2. Which similarity metric was most appropriate?
3. Which ANN method had the best trade-off?
4. Resource-constrained deployment config — point at a specific T5/T6 result (smaller `M`/lower `ef_search`, or IVF with fewer `nprobe`).
5. Main limitation of the chosen approach?
6. How would you deploy this in production — reference §17 (embedding service, index, metadata filters, monitoring).

### Throughout Days 1–9 (19–27 Aug, background): report drafting · owner P1

1. Draft the static sections that don't depend on anyone else's results as soon as there's spare time: dataset details, tools/libraries, problem statement, methodology write-up.
2. Fold in each teammate's results as they land (P2's Day 4, P3's Day 6, P4's Day 7/8) rather than waiting until Day 9 to start assembling.

### Day 9 — Thu 27 Aug: assemble everything · whole team, P1 leads

1. Merge all task write-ups into the notebook, in task order, each with its own explanation/justification/inference (not one generic block — see grading risk flags).
2. Build the PDF report: experimental methodology, comparative tables, graphs, retrieval examples, analysis/recommendations, one-page executive summary.
3. Write the final conclusion as four explicit sub-points: key observations, strengths, limitations, future improvements (#16).
4. Check every figure and table is labelled and explained (#15).
5. Gather Virtual Lab screenshots from the remote system.
6. Run the full 15-point notebook checklist (a–o, below).

### Day 10 — Fri 28 Aug: submit · whole team · DEADLINE

1. Run the notebook start-to-end on a clean kernel — zero errors, every cell shows output.
2. Confirm the report PDF also carries code + outputs per task (it's doing double duty as the "executed notebook" evidence — see below).
3. Zip `.ipynb` + report PDF together.
4. **Submit early in the day** — strictly no makeups, no late buffer.

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
