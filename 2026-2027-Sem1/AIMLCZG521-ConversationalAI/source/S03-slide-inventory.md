# 521 · S03 slide inventory (ANN & Hybrid deck)

Index of the instructor's **Lecture No. 3 — ANN Search algorithm and Hybrid Retrieval** deck (`Session3-ANN-HybridSearch-Ranking.pdf`, 62 slides). Under the handout-first rule this is contact session S03, still handout L2 scope. Every slide is listed; logistics and recap slides have no note-only named items because they belong to the master index or add no new examinable content. The deck's substantive depth is recorded in `notes/S03-ann-hybrid-retrieval.md`.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/source/S03-slide-inventory.md \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/notes/S03-ann-hybrid-retrieval.md
```

Slide numbers, titles and named items only — no slide prose.

| Slide | Title | Named items |
|---|---|---|
| 1 | Conversational AI | |
| 2 | AIMLCZG521, Conversational AI | |
| 3 | Disclaimer & Acknowledgement | |
| 4 | Outline | |
| 5 | ANN Indexing Strategies-Revisit | HNSW, IVF, PQ |
| 6 | IVF: Inverted File Index | k-means, nlist, centroids, inverted list, nprobe |
| 7 | STEP 1 — PARTITION THE DATASET | k-means, centroids, inverted lists |
| 8 | THE INVERTED LISTS — DATA STRUCTURE | inverted lists, vector IDs, clusters |
| 9 | Step 2-SEARCH PROCESS | query vector, nlist, nprobe, top-k |
| 10 | NUMERICAL EXAMPLE | nlist, nprobe, C1, C2, C3, Euclidean, v3, v4 |
| 11 | TIME COMPLEXITY — IVF vs kNN | O(N·D), O(K·D), O(ND/K) |
| 12 | THE ACCURACY TRADEOFF — WHY APPROXIMATE? | nprobe, recall |
| 13 | PROS & CONS | advantages, limitations |
| 14 | USE CASES & IMPLEMENTATIONS | Visual Search, Semantic Search, Recommendations, FAISS IVF-PQ |
| 15 | IVF: Inverted File Index + PQ (Product Quantization) | IVF, PQ, k-means, centroids, inverted lists, compression |
| 16 | Parameter Tuning: IVF | nlist, nprobe, PQ Subquantizers |
| 17 | Product Quantization | compression, ADC, approximate distance |
| 18 | Product Quantization (PQ) | subvector, codebook, compression |
| 19 | Product Quantization (PQ) – Step 1: Train Codebooks | codebook, k-means, centroids |
| 20 | Product Quantization (PQ) – Step 2: Encode Vectors → Compact IDs | centroid, IDs, compression |
| 21 | Product Quantization: Step 3 – Fast Distance Computation (ADC) | ADC, distance tables, lookups |
| 22 | PQ Numerical Example – Step 1: The Dataset | vectors, dimensions |
| 23 | PQ Numerical Example – Step 2: Split into Subvectors | subvectors, dimensions |
| 24 | PQ Numerical Example – Step 2: Collect Codebook Training Data | codebooks, k-means |
| 25 | PQ Numerical Example – Step 3: Create Codebooks with K-Means | codebooks, centroids, k-means |
| 26 | PQ Numerical Example – Step 4: Encode Vectors Using the Codebooks | PQ codes, centroids |
| 27 | PQ Numerical Example – Step 5: Memory Savings | codebooks, compression |
| 28 | PQ Numerical Example – Step 6: Similarity Search | query vector, ADC, compressed codes |
| 29 | PQ Numerical Example – Step 6a: Compute Distance Tables | codebooks, distance tables |
| 30 | PQ Numerical Example – Step 6b: Compute Approximate Distances | table lookups, approximate distances |
| 31 | PQ Key Parameters | M, k, compression |
| 32 | Product Quantization (PQ) – Why It Is Powerful | compression, fast search, scalability, IVF |
| 33 | Complexity Comparison – ANN Algorithms | Linear Scan, HNSW, IVF, PQ, IVF+PQ, HNSW+PQ, FAISS, ScaNN, ANNOY |
| 34 | II. Sparse Retrieval | dense, sparse, BM25 |
| 35 | Dense Vector Search Has Limitations | exact keyword, rare terms, OOV, BM25 |
| 36 | Limitation 1: Struggles with Exact Keyword Matching | ERROR code 500, BM25 |
| 37 | Limitation 2: Misses Rare / Unique Terms | XR55-QW7, BM25 |
| 38 | Limitation 3: Can't Handle Out-of-Vocabulary (OOV) Words Perfectly | VijayawadaExpress123, sub-tokens, BM25 |
| 39 | Summary: Why We Need Sparse + Dense Together | Dense Models, BM25, Hybrid Search |
| 40 | TF-IDF: Foundation of Sparse Retrieval | TF, IDF, TF-IDF |
| 41 | TF-IDF: Foundation of Sparse Retrieval – Worked Example | corpus, machine, learning, IDF |
| 42 | TF-IDF: Foundation of Sparse Retrieval – Limitations | Linear TF, length normalization, bag of words, saturation, BM25 |
| 43 | BM25: Best Matching 25 (Improved TF-IDF) | BM25, k1, b, saturation, length normalization |
| 44 | BM25: IDF and TF Components | IDF, TF, saturation |
| 45 | BM25: Including Saturation – Intuition | saturation curve, term frequency |
| 46 | BM25: Step-by-Step Example | machine, learning, IDF |
| 47 | BM25: Step-by-Step Example (Steps 2 & 3) | TF, BM25 score |
| 48 | BM25 vs TF-IDF – Understanding the Difference | TF-IDF, BM25, length normalization, saturation |
| 49 | BM25 vs TF-IDF – Understanding the Difference (Detail) | length normalization, saturation, probabilistic foundation |
| 50 | Why Hybrid Search? Dense + Sparse | dense, sparse, BM25, exact keywords |
| 51 | Why Hybrid Search? Dense + Sparse – Example 2: Unique IDs | AIMLCZG521, BM25, dense |
| 52 | Dense + Sparse – Complementary Strengths | dense, sparse, semantic, BM25 |
| 53 | The Challenge: Combining Different Score Ranges | cosine, BM25, min-max, z-score, RRF |
| 54 | Reciprocal Rank Fusion (RRF): The Math | RRF, rank, k |
| 55 | Properties of RRF | score-agnostic, bounded, symmetric, robust, no training |
| 56 | RRF: Example – Scenario: Query machine learning tutorial | Dense Retrieval, BM25, ranked lists |
| 57 | RRF: Example – Score Calculation (k=60) | RRF, consensus, final ranking |
| 58 | Performance Characteristics (Typical) | BM25, Vector, Hybrid, recall, precision |
| 59 | Hybrid Search Implementation-Demo | dense retrieval, BM25, RRF, lambda |
| 60 | Key Takeaways | |
| 61 | Resources & Further Reading | |
| 62 | References | |
