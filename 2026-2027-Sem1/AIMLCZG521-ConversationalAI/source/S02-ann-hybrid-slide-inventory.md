# 521 · S02 (ANN & Hybrid deck) slide inventory

Derived index of the **second** deck taught under handout L2, instructor label "Lecture No. 3 — ANN Search algorithm and Hybrid Retrieval" (62 slides). Its topics — deeper ANN algorithms (IVF, PQ), TF-IDF, BM25 mathematics, and RRF — are all handout-L2 scope, so its genuinely-new depth was folded into `notes/S02-retrieval.md` rather than made a new session (see `source/MATERIAL-LOG.md`, 27 Aug 2026). Slide numbers, titles and named items only.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/source/S02-ann-hybrid-slide-inventory.md \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/notes/S02-retrieval.md
```

| Slide | Title | Named items |
|---|---|---|
| 4 | Outline | ANN, HNSW, IVF, PQ, TF-IDF, BM25, Hybrid, RRF |
| 5 | ANN Indexing Strategies Revisit | HNSW, IVF, PQ |
| 6 | IVF: Inverted File Index | k-means, nlist, centroids, inverted list, nprobe |
| 7 | Partition the Dataset | k-means, Voronoi, centroid, Euclidean |
| 8 | The Inverted Lists | inverted list, cluster |
| 9 | Search Process | nlist, nprobe, top-k |
| 10 | Numerical Example | nprobe, centroid, Euclidean |
| 11 | Time Complexity IVF vs kNN | brute-force, centroids |
| 12 | The Accuracy Tradeoff | nprobe, recall |
| 13 | Pros and Cons | nlist, nprobe, training |
| 14 | Use Cases and Implementations | FAISS |
| 16 | Parameter Tuning: IVF | nlist, nprobe, subvectors |
| 17 | Product Quantization | ADC, codes, IVF |
| 18 | Product Quantization | subvector, codebook, compression |
| 19 | PQ Step 1: Train Codebooks | codebook, k-means, centroids |
| 20 | PQ Step 2: Encode | centroid, compression |
| 21 | PQ Step 3: Fast Distance | ADC, distance table |
| 22 | PQ Numerical: Dataset | subvector |
| 23 | PQ Numerical: Split | subvector |
| 24 | PQ Numerical: Codebook data | codebook, k-means |
| 26 | PQ Numerical: Encode | centroid |
| 27 | PQ Numerical: Memory Savings | codebook, compression |
| 28 | PQ Numerical: Similarity Search | ADC |
| 29 | PQ Numerical: Distance Tables | codebook, centroid |
| 30 | PQ Numerical: Approximate Distances | table lookups |
| 31 | PQ Key Parameters | compression |
| 32 | PQ Why It Is Powerful | compression, IVF |
| 33 | Complexity Comparison ANN Algorithms | Linear scan, HNSW, IVF, PQ, IVF+PQ, HNSW+PQ, FAISS, ScaNN, ANNOY |
| 35 | Dense Vector Search Has Limitations | exact keyword, rare, out-of-vocabulary, BM25 |
| 36 | Limitation 1: Exact Keyword Matching | BM25, IDF |
| 37 | Limitation 2: Rare Terms | BM25, inverse document |
| 38 | Limitation 3: OOV | out-of-vocabulary, BM25 |
| 39 | Summary: Sparse + Dense | BM25, hybrid |
| 40 | TF-IDF: Foundation | term frequency, inverse document frequency, TF-IDF |
| 41 | TF-IDF: Worked Example | IDF |
| 42 | TF-IDF: Limitations | saturation, length normalization, bag-of-words, BM25 |
| 43 | BM25: Improved TF-IDF | saturation, length normalization, probabilistic |
| 44 | BM25: IDF and TF Components | saturation, length |
| 45 | BM25: Saturation Intuition | saturation, term frequency |
| 46 | BM25: Step-by-Step Example | IDF |
| 47 | BM25: Step-by-Step (Steps 2 and 3) | norm |
| 48 | BM25 vs TF-IDF | length normalization, saturation, probabilistic |
| 49 | BM25 vs TF-IDF Detail | length normalization, saturation |
| 50 | Why Hybrid: Exact Keywords | BM25, dense |
| 51 | Why Hybrid: Unique IDs | BM25, dense |
| 52 | Dense + Sparse Complementary | dense, sparse, semantic |
| 53 | Combining Different Score Ranges | min-max, z-score, RRF |
| 54 | Reciprocal Rank Fusion: The Math | RRF, rank |
| 55 | Properties of RRF | score-agnostic, bounded, symmetric, robust |
| 56 | RRF Example: Scenario | RRF |
| 57 | RRF Example: Score Calculation | RRF, consensus |
| 58 | Performance Characteristics | BM25, hybrid, recall, precision |
