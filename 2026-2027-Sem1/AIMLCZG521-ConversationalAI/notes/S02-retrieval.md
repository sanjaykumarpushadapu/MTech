# Conversational AI · Session 02 · Embeddings, Vector Search & Hybrid Retrieval

*Learned 1 Aug 2026*

## Why this matters

Conversational systems need a way to find the right knowledge before the LLM answers. This session teaches that retrieval chain: represent text as embeddings, compare vectors, index them efficiently, and combine dense search with keyword search. After reading it, you should be able to explain why "just use embeddings" is not enough for production RAG.

## Part 1 · Semantic vs Keyword Search

*The core retrieval tradeoff is simple: semantic search retrieves by meaning, keyword search retrieves by exact lexical evidence, and real systems usually need both.*

**Prerequisites recap** — this session assumes basic transformer architecture, self-attention, feedforward layers, and matrix operations.

> - **Transformer architecture**: token IDs become token embeddings, position information is added, transformer layers rewrite the token vectors, and a pooling step can turn many token vectors into one sentence vector.
> - **Self-attention vs cross-attention**: self-attention compares tokens inside the same sequence; cross-attention lets a decoder attend to an encoded source sequence, as in translation. Concretely: in `"The bank was closed because the river overflowed its banks"`, self-attention lets the model reach the first `bank`, look at the rest of the *same* sentence, see `river` and `overflowed`, and realize `bank` means a landform, not a financial institution — query and result both come from one sequence. Translating `"I love Mangoes"` into `"Mujhe Aam pasand hain"` is different: the decoder's query comes from the Hindi word it is generating, but the key/value data it attends to comes from the English input — that is cross-attention, query and data from two different sequences.
>
>   | Mechanism | Where it runs | Query (Q) source | Key/Value (K, V) source |
>   |---|---|---|---|
>   | Self-attention | Encoder and decoder | Current layer's input | Current layer's input (same sequence) |
>   | Cross-attention | Decoder only | Decoder's current state | Encoder's final output (different sequence) |
> - **Multi-headed attention**: several attention heads learn different projections of `Q`, `K`, and `V`, then concatenate their outputs and project through a learned matrix `W^O` back to the model's embedding dimension — so the final representation can carry several relationship patterns (syntax, coreference, topic) at once instead of averaging them into one.
> - **Matrix operations**: dot product scores similarity, softmax turns scores into weights, and weighted sums blend vectors.

### 1. Semantic search vs keyword search

**Intuition** — Keyword search asks, "which documents contain these words?" Semantic search asks, "which documents mean the same thing?" They fail in opposite ways, which is why hybrid retrieval exists.

![Semantic keyword hybrid retrieval](assets/S02-semantic-keyword-hybrid.svg)

**Mechanism** —

| Retrieval type | Representation | Best for | Failure mode |
|---|---|---|---|
| Keyword / sparse | term counts, inverted indexes, BM25-style weighting | names, IDs, exact phrases, rare terms | misses paraphrases |
| Dense / semantic | neural embeddings | synonyms, concepts, natural-language questions | can blur exact facts |
| Hybrid | sparse + dense + fusion | production RAG | more components to tune and monitor |

**Worked example** — Query: `"laptop reimbursement policy"`.

| Document | Keyword behavior | Dense behavior |
|---|---|---|
| `"employee device expense rules"` | may miss: no exact laptop/reimbursement words | likely match |
| `"laptop serial number inventory"` | may match: exact laptop word | likely demote |
| `"reimbursement form LAP-2026"` | likely match exact term/code | likely match if context is enough |

**Tradeoff / when NOT to use** — Dense-only search is risky for compliance, support, and ticketing systems where exact product names, IDs, SKUs, policy clauses, and version numbers matter. Keyword-only search is risky when users describe the same idea with different words from the document.

---

### 2. What an embedding is

**Intuition** — An embedding is a numeric representation of meaning. Texts with similar meanings should land near each other in vector space, even when they use different words.

Imagine a library map arranged by meaning instead of alphabetically: credit cards, accounts, and loans sit near each other; river-bank erosion sits far away even though it shares the word `bank`.

**Mechanism** — An embedding model maps text to a fixed-length vector:

```text
"refund my cancelled flight" -> [0.12, -0.44, 0.87, ..., 0.09]
```

For retrieval, stored chunks and incoming queries are embedded into the same vector space. Search then becomes nearest-neighbor search: find the stored vectors closest to the query vector.

![Embedding retrieval flow](assets/S02-embedding-retrieval.svg)

**Worked example** — Query: `"reset my password"`.

| Candidate text | Match | Why |
|---|---:|---|
| `"change forgotten password"` | high | different words, same intent |
| `"delete account"` | medium | account-related but different action |
| `"weather in Hyderabad"` | low | unrelated |

**Tradeoff / when NOT to use** — Embeddings are weak when the important signal is an exact token. If a user searches `INC-48291`, `v2.3.7`, or `Section 14.2(b)`, keyword search or metadata filtering should lead and semantic search can follow.

---

### 3. What are Encoder Models?

**Intuition** — Encoder models are good embedding machines because they see the whole input at once. That bidirectional view lets them represent meaning in context rather than treating each word as one fixed object.

**Why Encoders for Embeddings?** The important word is **contextual**: the vector for `bank` should change depending on whether the sentence mentions a river or an account.

Older methods such as word2vec and GloVe assign one learned vector to each word. That breaks on polysemy: one `bank` vector has to serve both finance and geography. A contextual encoder computes the vector at inference time, using surrounding words to decide the meaning.

**Mechanism** — Encoder self-attention lets every token attend to every other token in the input. The final token vectors are not just word meanings; they are word-in-this-sentence meanings.

![Contextual embedding disambiguation](assets/S02-contextual-bank.svg)

For token matrix `X`, one attention layer computes:

```text
Q = X W_Q
K = X W_K
V = X W_V
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
```

Plain language: `QK^T` asks which tokens matter to each token, softmax converts those scores into weights, and multiplying by `V` blends the useful information.

**Worked example** — In `"the bank was closed because the river overflowed"`, `bank` attends to `river` and `overflowed`, so its vector moves toward geography. In `"the bank account was closed"`, `bank` attends to `account`, so its vector moves toward finance.

**Tradeoff / when NOT to use** — Encoder embeddings are ideal for understanding and search, but they are not the natural architecture for open-ended generation. If the task is to write an answer token by token, a decoder-only LLM is the standard choice.

---

### 4. Encoder vs Decoder vs Encoder-Decoder

**Intuition** — The architecture decides what kind of task feels natural. Encoders understand, decoders generate, and encoder-decoders transform one sequence into another.

![Encoder decoder architecture choice](assets/S02-architecture-choice.svg)

**Mechanism** —

| Architecture | Context view | Best use cases | Weak fit |
|---|---|---|---|
| Encoder-only | bidirectional: sees the whole input | embeddings, classification, sentiment, NER, semantic search | free-form generation |
| Decoder-only | causal: sees previous tokens only | chat, code, instruction following, text generation | pure embedding quality unless specially trained |
| Encoder-decoder | encoder sees source; decoder generates target | translation, summarization, text-to-text conversion | heavier when one side is enough |

**Per-task decision table** — the same three-way choice, task by task, with the reasoning that drives each verdict:

| Task | Encoder-only | Decoder-only | Encoder-Decoder | Why |
|---|---|---|---|---|
| Sentiment analysis | ✓ Best | ○ Possible | ✗ Overkill | needs bidirectional context, no generation required |
| Text generation | ✗ No | ✓ Best | ○ Possible | requires autoregressive generation capability |
| Machine translation | ✗ No | ○ Suboptimal | ✓ Best | cross-attention optimally aligns source-target pairs |
| Named entity recognition | ✓ Best | ✗ Inefficient | ✗ Overkill | token-level classification needs bidirectional context |
| Conversational AI | ✗ No | ✓ Best | ○ Outdated | decoder-only scales better for dialogue and instruction following |
| Summarization | ✗ No | ✓ Modern | ✓ Traditional | both work; decoder-only now preferred for a unified architecture |
| Semantic search | ✓ Best | ○ Possible | ✗ Overkill | encoder creates optimal dense representations for similarity |
| Code generation | ✗ No | ✓ Best | ○ Rare | sequential generation with context — decoder-only excels |

Read this as a lookup table for "which architecture for this task," not a ranking of architectures in general — semantic search and text generation land on opposite ends on purpose.

**Popular models by architecture (2025 snapshot)** — concrete anchors for each category above: **encoder-only** — BERT, RoBERTa, DeBERTa, ALBERT, DistilBERT; **decoder-only** — GPT-4, GPT-3.5, Claude 3/4, Llama 3, Mistral; **encoder-decoder** — T5, BART, mT5, PEGASUS, mBART, FLAN-T5. Like any specific model list, this dates quickly — the categories and their fit-per-task above are the durable part.

**Worked example** — For sentiment analysis on `"The food was slow but excellent"`, an encoder can inspect both emotional words before deciding. For chatbot response generation, a decoder predicts one token at a time. For translation, an encoder reads the source sentence and a decoder writes the target sentence while attending to the encoded source.

**Tradeoff / when NOT to use** — Do not force one architecture onto every problem. A decoder-only model can perform understanding tasks after suitable fine-tuning, but for embeddings a purpose-built encoder is usually cheaper, faster, and easier to index.

> ***Going deeper*** — Fine-tuned decoders can match encoders on some classification tasks, so "encoders understand, decoders generate" is a practical default, not an absolute law. The production question is cost: if an encoder reaches the same retrieval or classification quality with smaller vectors, faster inference, and simpler indexing, it is still the better tool.
>
> The concrete evidence: Borodach et al., *"Decoders Laugh as Loud as Encoders"* (2025), tested 17 encoders, several encoder-decoders, and several decoders on a six-way humor classification task (five joke types plus "no joke", 1,392 human-authored jokes). Best fine-tuned encoder: RoBERTa-base at F1 0.86 — the prior state of the art. Best fine-tuned decoder: GPT-4o at F1 0.85 — statistically equal. Zero/few-shot decoders, not fine-tuned, only reached F1 ≈ 0.18. The finding that overturns the old assumption isn't "decoders are now better" — it's that **fine-tuning, not architecture, is what closes the gap**; an un-tuned decoder is nowhere close.

> ![Zero/few-shot decoders lag far behind — fine-tuning closes the gap](assets/S02-decoder-vs-encoder-classification.svg)

---

### 5. How Encoder Transformers Create Embeddings

**Intuition** — A sentence embedding is not produced in one magic step. It is built through tokenization, embedding lookup, positional addition, transformer layers, and pooling.

![BERT-style embedding pipeline](assets/S02-bert-embedding-pipeline.svg)

**Mechanism** — BERT Pipeline. For `"Machine learning is fascinating"` in a BERT-like encoder:

| Step | What happens | Output shape idea |
|---|---|---|
| 1. Tokenization | add `[CLS]` at the start and `[SEP]` at the end | 6 tokens |
| 2. Token embeddings | each token ID looks up one row in a learned table | 6 vectors, each 768-dim |
| 3. Positional embeddings | add a learned position vector elementwise | 6 position-aware input vectors |
| 4. Transformer layers | 12 BERT-base layers mix information with self-attention and FFNs | 6 contextual vectors |
| 5. Pooling strategy | compress token vectors into one sentence/chunk vector | 1 vector |

Token embeddings are static at lookup time: the same token ID selects the same row. Context appears only after transformer layers rewrite the vectors.

**Worked example** — Position addition is elementwise:

```text
token embedding      [0.23, -0.15, 0.89]
position embedding   [0.02,  0.03, 0.01]
input embedding      [0.25, -0.12, 0.90]
```

Without position information, `"the dog bit the man"` and `"the man bit the dog"` contain the same token vectors in a different order, and the lookup table alone has no way to tell the difference.

**Tradeoff / when NOT to use** — BERT-style encoders are excellent for medium-length text, but their context window can be short for long documents. If a document exceeds the model's context window, chunk it carefully instead of truncating silently.

---

### 6. Pooling strategies

**Intuition** — The encoder returns one vector per token, but search needs one vector for the whole sentence or chunk. Pooling compresses many contextual token vectors into one vector.

![Pooling strategies](assets/S02-pooling-strategies.svg)

**Mechanism** —

| Pooling | Formula | Best fit |
|---|---|---|
| CLS pooling | `v = h_[CLS]` | classification, sentiment, NLI |
| Mean pooling | `v = (1/n) sum_i h_i` | semantic similarity, search, RAG |
| Max pooling | `v_j = max(h_1j, ..., h_nj)` | some retrieval/classification setups |

Many BERT-family checkpoints expose `[CLS]` conveniently, but sentence-embedding models often prefer mean pooling because it uses signal from every token. **Sentence-BERT** (Reimers & Gurevych, 2019) is the model that established this pattern — a siamese/triplet network fine-tuned specifically to make mean-pooled sentence vectors directly comparable by cosine similarity — and it's why mean pooling is the default for BGE, GTE, and most modern sentence-embedding models, not just an arbitrary alternative to CLS pooling.

**Worked example** — Three 2D token vectors:

```text
h1 = [1, 4]
h2 = [3, 2]
h3 = [5, 0]

mean pooling = [(1+3+5)/3, (4+2+0)/3] = [3, 2]
max pooling  = [max(1,3,5), max(4,2,0)] = [5, 4]
```

**Tradeoff / when NOT to use** — CLS pooling is convenient but not automatically best for retrieval. If a search system returns near-random FAQ matches from a general BERT checkpoint, the issue may be pooling rather than the whole model; mean pooling or a sentence-embedding model may be the simpler fix.

---

### 7. Embedding Models: Key Players

**Intuition** — An embedding model is a production component, not a generic utility. Dimension, context window, training objective, language coverage, latency, deployment type, and cost decide whether retrieval works well.

![Embedding model selection criteria](assets/S02-embedding-model-selection.svg)

**Mechanism** — Read model specifications as a selection checklist, not as a leaderboard.

| Model | Provider | Output dim | Context | Type | Cost | Best fit |
|---|---|---:|---:|---|---|---|
| `bge-large-en-v1.5` | BAAI | 1024 | 512 | open | self-hosted (compute only) | strong general English baseline |
| `gte-large-en-v1.5` | Alibaba | 1024 | 8192 | open | self-hosted (compute only) | longer documents |
| `e5-mistral-7b-instruct` | Microsoft | 4096 | 32768 | open | self-hosted (compute only) | instruction-following, very long context |
| `jina-embeddings-v2` | Jina AI | 768 | 8192 | open | self-hosted (compute only) | multilingual, faster inference |
| `text-embedding-3-large` | OpenAI | 3072 | 8191 | API | **$0.13 / 1M tokens** | highest quality, production |
| `embed-english-v3.0` | Cohere | 1024 | 512 | API | **$0.10 / 1M tokens** | compression support, production |

The cost column is why "just use the best API model" is not automatically the right call: at high query volume, the per-token API charge compounds, while an open model's cost is the (roughly fixed) compute to host it — the crossover point is a real production sizing decision, not a footnote.

**Full spec reference** — architecture, layer count, and training objective for the same six models, for when the summary table above isn't enough to explain a quality difference:

| Model | Provider | Architecture | Layers | Hidden size | Training | Type |
|---|---|---|---:|---:|---|---|
| `text-embedding-3-large` | OpenAI | Transformer | N/A | N/A | Contrastive | API |
| `embed-v3` | Cohere | Transformer | N/A | N/A | Multi-task | API |
| `bge-large-en-v1.5` | BAAI | BERT | 24 | 1,024 | RetroMAE + Contrastive | Open |
| `gte-large-en-v1.5` | Alibaba | BERT | 24 | 1,024 | Contrastive | Open |
| `e5-mistral-7b-instruct` | Microsoft | Mistral 7B | 32 | 4,096 | Contrastive pre-training | Open |
| `jina-embeddings-v2` | Jina AI | BERT | 12 | 768 | Contrastive | Open |

`bge-large-en-v1.5` combining RetroMAE pretraining *and* contrastive fine-tuning (rather than one or the other) is why it's the recommended general-purpose open default in the selection guide above — it gets both the compact-representation benefit of RetroMAE (section 8) and the direct similarity-training benefit of contrastive learning.

**Worked example** — For a small English FAQ, start with a 768- or 1024-dimensional open model. For policy documents where sections exceed 1000 tokens, choose a longer-context model or chunk by headings. For sensitive customer data, local/open deployment may beat a higher-scoring API model because privacy and batch economics dominate.

**Tradeoff / when NOT to use** — Do not chase the largest dimension blindly. A 4096-dimensional vector can improve quality, but if it doubles RAM and slows index traversal without measurable recall gain on your data, a smaller model wins.

---

### 8. Embedding Models: Training Objectives

**Intuition** — Embedding quality comes from the training objective. The model must learn that related texts should be close and unrelated texts should be far.

![Embedding training objectives](assets/S02-embedding-training-objectives.svg)

**Mechanism** —

| Training objective | Core idea | Strength | Main risk |
|---|---|---|---|
| Training Objective - Contrastive Learning | pull positive pairs close; push negatives far | directly trains semantic similarity | needs good negatives and careful batches |
| Training Objective - Masked Language Modeling (MLM) | hide tokens and predict them from context | strong bidirectional understanding | not optimized for retrieval by itself |
| Training Objective - RetroMAE | reconstruct heavily masked input through an encoder-decoder setup | compact retrieval-oriented representations | more complex training and mask-ratio tuning |

Contrastive loss for an anchor `a`, positive `p`, and negatives `n_i`:

```text
loss = -log( exp(sim(a,p)) / sum_i exp(sim(a,n_i)) )
```

Plain language: reward the positive pair for scoring high, and punish it if negatives score nearly as high.

**Worked example** — Anchor: `"The cat sat on the mat"`. Positive: `"A feline rested on the rug"`. Negative: `"How to bake chocolate cookies"`. A good embedding model raises anchor-positive similarity and lowers anchor-negative similarity.

For MLM, `"The [MASK] brown fox [MASK] over the lazy dog"` teaches the encoder to predict `quick` and `jumps` from both sides. For RetroMAE, a more heavily masked sentence forces the encoder to compress the surviving context well enough for the decoder to reconstruct the original.

**Tradeoff / when NOT to use** — Contrastive training is powerful but sensitive to negative sampling. If a "negative" is actually relevant, the model learns the wrong boundary. MLM is a strong pretraining task for understanding, but search quality usually needs retrieval-oriented training or fine-tuning.

## Part 2 · Vector Database Architecture (HNSW, ANN)

*Once vectors exist, the system must search them fast enough for conversational latency.*

### 9. Vector similarity mathematics

**Intuition** — Similarity metrics define what "near" means. Cosine cares about direction, Euclidean distance cares about physical distance, and dot product combines direction with magnitude unless vectors are normalized.

![Vector similarity metrics](assets/S02-vector-similarity-metrics.svg)

**Mechanism** —

| Metric | Formula | How to read it |
|---|---|---|
| Cosine similarity | `cos(A,B) = (A dot B) / (||A|| ||B||)` | high value means similar direction |
| Euclidean / L2 distance | `d(A,B) = sqrt(sum_i (A_i - B_i)^2)` | low value means close points |
| Dot product | `A dot B = sum_i A_i B_i` | high value means alignment and/or larger magnitude |

If vectors are normalized so `||A|| = ||B|| = 1`, dot product equals cosine similarity. This is why many vector systems normalize text embeddings before using inner-product search.

**Worked example** — Let `A = [3,4]`, `B = [4,3]`, and `C = [-4,3]`.

```text
A dot B = 3*4 + 4*3 = 24
||A|| = 5, ||B|| = 5
cos(A,B) = 24 / 25 = 0.96
L2(A,B) = sqrt((3-4)^2 + (4-3)^2) = sqrt(2) = 1.414

A dot C = 3*(-4) + 4*3 = 0
cos(A,C) = 0 / 25 = 0
L2(A,C) = sqrt((3+4)^2 + (4-3)^2) = sqrt(50) = 7.071
```

`B` is close to `A`; `C` is much farther and orthogonal by cosine.

**Tradeoff / when NOT to use** — Cosine is usually safer for text because it ignores vector length. Dot product is fast, but it only behaves like cosine when vectors are normalized or the model was trained for dot-product scoring. L2 can be useful for geometric/image-style spaces but is often too magnitude-sensitive for text.

---

### 10. The Computational Challenge

**Intuition** — Exact nearest-neighbor search is simple: compare the query with every stored vector. It also becomes impossible at production scale.

![Linear scan computational wall](assets/S02-linear-scan-wall.svg)

**Mechanism** — Linear scan cost is:

```text
operations per query = number_of_vectors * vector_dimension
```

For 10 million vectors of dimension 768:

```text
10,000,000 * 768 = 7,680,000,000 multiply-add operations
```

At 1 billion operations per second, that is about 7.68 seconds per query. At 100 queries per second, it implies 768 CPU-core seconds per second of traffic.

**Worked example** — If one query over 10M vectors takes 7.68 seconds on one CPU core, then serving 100 queries per second requires:

```text
7.68 seconds/query * 100 queries/second = 768 cores
```

That is before network overhead, filters, reranking, and the LLM call.

**Tradeoff / when NOT to use** — Linear scan is fine for tiny collections, offline evaluation, and verifying ANN recall. It is not the serving strategy for millions of vectors unless specialized hardware and workload economics justify brute force.

---

### 11. Linear Scan vs ANN Solution

**Intuition** — Approximate Nearest Neighbor search avoids checking every vector. It accepts "close enough" top-k results in exchange for large speedups.

![Approximate nearest neighbor indexing](assets/S02-ann-index.svg)

**Mechanism** — ANN uses index structure to skip most candidates. The contrast is the point:

| Search style | Example latency at 10M vectors | How it works |
|---|---:|---|
| Linear scan | about 7.68 seconds/query | brute-force comparison against all vectors |
| ANN index such as HNSW | about 10 milliseconds/query | navigates an index and avoids unnecessary comparisons |

Scale intuition:

| Documents | Linear scan | HNSW-style ANN |
|---:|---:|---:|
| 10K | ~8 ms | ~2 ms |
| 100K | ~77 ms | ~3 ms |
| 1M | ~770 ms | ~5 ms |
| 10M | ~7.7 s | ~10 ms |

**The cost engineering angle** — latency is only half the production picture; the same scale table, priced monthly, is the other half:

| Documents | Linear scan latency | Linear scan cost/month | HNSW latency | HNSW cost/month |
|---:|---:|---:|---:|---:|
| 10K | 8 ms | $50 | 2 ms | $50 |
| 100K | 77 ms | $50 | 3 ms | $50 |
| 1M | 770 ms | $200 | 5 ms | $120 |
| 10M | 7.7 s | **$5,000** | 10 ms | **$250** |

At small scale, linear scan and HNSW cost about the same — the indexing overhead isn't worth it yet. The gap only opens up at scale: by 10M documents, linear scan is both too slow to serve *and* 20× more expensive to run, because "too slow" in production means throwing more CPU cores at the problem, and CPU cores are what you're paying for. ANN indexing isn't just a speed trick; past a certain scale it's the cheaper option too.

**Worked example** — A support RAG system with 10M chunks does not need the mathematically exact top-10 every time. If ANN returns 9 of the true top-10 in milliseconds, a reranker can often recover the final ordering while keeping end-to-end latency acceptable.

**Tradeoff / when NOT to use** — ANN is a latency-recall tradeoff. If the collection is tiny or the top-1 result must be mathematically exact, brute force may be safer. In RAG, 95-99% approximate recall is usually acceptable because retrieval is followed by reranking, answer generation, and citation checks.

---

### 12. ANN Indexing Strategies

**Intuition** — "ANN" is not one algorithm. It is a family of indexing strategies that trade memory, build cost, query speed, and recall differently.

![Approximate nearest neighbor indexing](assets/S02-ann-index.svg)

**Mechanism** —

| Strategy | Example | How it works | Strength | Weakness |
|---|---|---|---|---|
| Graph-based | HNSW | connect nearby vectors in a navigable graph | high recall, fast search, no training | high memory, slower inserts |
| Partition-based | IVF | cluster vectors; search selected partitions | scalable, works with compression | needs training; sensitive to `nprobe` |
| Compression-based | PQ | compress vectors into compact codes | 8-32x memory reduction, billion-scale search | lower recall, needs training |

PQ — the compression-based strategy in the table above — comes from Jégou et al. (2011).

**Worked example** — For 10M vectors and enough RAM, HNSW is a strong default because it gives high recall and simple tuning. For hundreds of millions of vectors where RAM is the binding constraint, IVF+PQ can be the better engineering choice even if recall is lower.

**Tradeoff / when NOT to use** — Graph indexes are not automatically best. If memory cost dominates, compression can beat HNSW. If insertion rate is very high, a partitioned or disk-backed design may be easier to operate.

---

### 13. HNSW: Hierarchical Navigable Small World

HNSW was introduced by Malkov & Yashunin (2018).

**Intuition** — HNSW is like a multi-level road network for vectors. Top layers are highways with long jumps; the bottom layer is the local street map containing all points.

![HNSW search process](assets/S02-hnsw-search.svg)

**Mechanism** — HNSW stores vectors as graph nodes. Edges connect nearby nodes. Search starts at a sparse high layer, greedily moves closer to the query, then descends layer by layer until the dense base layer. A final beam-style search expands candidates at layer 0.

Key ideas:

| Idea | Meaning |
|---|---|
| hierarchical structure | top layers skip across the dataset quickly |
| small-world property | average path length stays short, often near logarithmic |
| navigable graph | greedy movement usually finds a near-optimal path |
| robustness | multiple possible routes reduce local-minimum risk |

This is the complexity payoff, stated plainly: brute-force search is **O(N)** — every query compares against every stored vector. HNSW's layered structure turns that into **O(log N)** — each layer eliminates most of the remaining candidates before the next layer even starts, which is the same "skip across, then narrow down" shape as the CPU-core math in concept 11.

**Worked example — one concrete run, step by step.** Say the graph has 8 stored vectors, numbered 1-8, and a query vector arrives (drawn as the target point).

1. **Enter at the top layer** at a random entry point, node 1. Node 1 connects to node 2 at this sparse top layer; comparing both to the query, node 2 is closer. Current best: **node 2**.
2. **Drop down** to the middle layer at node 2. This layer has more nodes and edges: 1, 5, 4, 2, 3. A greedy search from node 2 checks its neighbors and finds node 4 is closer to the query than node 2 was. Current best: **node 4**.
3. **Drop down** to the dense bottom layer (layer 0), which holds all 8 vectors and their full connections. A final expanded (beam) search around node 4 checks its neighbors — including node 7 — and finds **node 7 is the closest point to the query**. Search stops here and returns node 7 (plus its nearest neighbors, for top-k).

Three comparisons at the top, a handful at the middle, and one expanded search at the bottom found the true nearest neighbor without ever comparing the query against all 8 points directly — and the saving gets more dramatic as the dataset grows from 8 points to 10 million.

**Tradeoff / when NOT to use** — HNSW is a strong default up to large but memory-manageable datasets. If the dataset reaches hundreds of millions or billions of vectors and RAM is the main constraint, IVF+PQ or another compressed setup may beat HNSW despite lower recall.

---

### 14. HNSW: Memory Layout and Parameter Tuning

**Intuition** — HNSW speed is not free. The graph needs memory for connections, and its tuning parameters decide the latency-recall-memory balance.

![HNSW memory and tuning budget](assets/S02-hnsw-memory-tuning.svg)

**Mechanism** — Per vector, the rough storage components are:

```text
vector bytes      = dimension * 4 bytes for float32
connection bytes  = M * 4 bytes * layer factor
```

For 768-dimensional float32 vectors and `M = 16`:

```text
raw vector bytes        = 768 * 4 = 3,072 bytes
connection bytes approx = 16 * 4 = 64 bytes
rough storage           = about 3,136 bytes before broader graph/metadata overhead
```

Planning table:

| Scale | Raw vector data | Graph overhead | Production memory budget |
|---:|---:|---:|---:|
| 1M vectors | ~3.1 GB | ~0.5-1 GB | ~3.6-4.1 GB |
| 10M vectors | ~31 GB | ~10-20 GB | ~41-51 GB |
| 100M vectors | ~310 GB | ~200-300 GB | ~510-610 GB |

Important knobs:

| Parameter | Typical range | Raising it does |
|---|---:|---|
| `M` | 16-64 | better recall, more memory, slower inserts |
| `ef_construction` | 100-200+ | better index quality, slower build |
| `ef_search` | 50-500 | better query recall, slower query |

**Worked example** — Start with `M=16`, `ef_construction=200`, and `ef_search=100`. If recall is weak but latency has room, raise `ef_search` first because it affects query-time search without rebuilding the index.

**Tradeoff / when NOT to use** — Do not maximize every knob. `M=64` and high `ef_search` may improve recall, but if the product has strict latency or memory limits, a smaller index plus reranking can be better.

---

### 15. Vector database architecture

**Intuition** — A vector database is not just a table with vectors. It is a retrieval system around embeddings, indexes, metadata filters, update pipelines, sparse search, fusion, reranking, and observability.

![Vector database architecture](assets/S02-vector-database-architecture.svg)

**Mechanism** —

| Component | Job |
|---|---|
| chunker | splits documents into retrievable passages |
| embedding service | converts chunks and queries to vectors |
| vector index | serves fast ANN search |
| metadata filters | restrict by tenant, date, access control, document type |
| sparse index | BM25 / keyword retrieval |
| fusion / reranker | combines and improves candidate ordering |
| monitoring | tracks recall, latency, cost, freshness, and failed searches |

Chunking is separate because one vector for a whole document often becomes a blurry average of many topics. Smaller, topically coherent chunks keep each vector specific enough for targeted retrieval.

**Worked example** — In an HR assistant, `"Can I claim a monitor for work from home?"` should search only documents the employee is allowed to see, retrieve semantically related policy chunks, preserve exact policy-code matches, and pass the top few chunks to the LLM with citations or source IDs.

**Tradeoff / when NOT to use** — A vector database does not automatically fix bad retrieval. If chunks are too large, metadata is missing, embeddings are mismatched, or access filters are bolted on after search, the system can return plausible but unsafe context. For a small stable FAQ, a curated keyword index plus approved answers may be easier to audit.

## Part 3 · BM25 + Dense Retrieval + RRF

*Dense and keyword retrieval become useful when they are combined into one production retrieval layer.*

### 16. BM25

**Intuition** — BM25 is the strong classical baseline for keyword search. It rewards documents that contain query terms, especially rare terms, while avoiding unlimited reward for repeated words.

![BM25 scoring components](assets/S02-bm25-scoring.svg)

**Mechanism** — BM25 combines:

| Component | Plain meaning |
|---|---|
| term frequency | a query term appearing more often helps, but the gain saturates |
| inverse document frequency | rare terms matter more than common terms |
| length normalization | long documents should not win only because they contain more words |

**Worked example** — Query: `"HNSW ef_search"`. BM25 strongly rewards a document containing the exact rare term `ef_search`. A dense retriever may understand the general HNSW tuning topic, but exact-match evidence is important because `ef_search` is a parameter name.

**Tradeoff / when NOT to use** — BM25 struggles with vocabulary mismatch. A user asking `"how do I make vector lookup faster?"` may need a document titled `"ANN indexing and HNSW tuning"`; semantic retrieval is more likely to bridge that wording gap.

---

### 17. Dense Passage Retrieval

Dense Passage Retrieval was introduced by Karpukhin et al. (2020) and is the foundation modern dense retrieval builds on.

**Intuition** — Dense Passage Retrieval uses a dual encoder: one encoder embeds the question, another embeds passages. Retrieval is maximum similarity between the query vector and passage vectors.

![Dense Passage Retrieval dual encoder](assets/S02-dpr-dual-encoder.svg)

**Mechanism** —

```text
q = Encoder_question(question)
p = Encoder_passage(passage)
score(question, passage) = q dot p
```

Passage vectors can be precomputed and indexed. At query time, only the question is embedded, then the vector index retrieves high-scoring passages.

Why not use one model that reads the question and passage together? A cross-encoder is usually more accurate, but it must rerun the full model for every candidate passage. That is too slow over millions of passages. The dual encoder trades away cross-attention accuracy so passage vectors can be embedded once and searched quickly.

**Worked example** — Question: `"Who wrote Pride and Prejudice?"`. The positive passage says `"Pride and Prejudice is a novel by Jane Austen..."`; a hard negative might discuss the 2005 film. Training pushes the question vector closer to the answer-bearing passage and farther from negatives.

**Tradeoff / when NOT to use** — DPR-style dense retrieval is excellent for semantic question answering, but it can underperform on exact lexical constraints and fresh domain terminology unless adapted for the domain. Hybrid retrieval is the safer production default.

---

### 18. Reciprocal Rank Fusion

**Intuition** — RRF combines rankings, not raw scores. That matters because BM25 scores and dense similarity scores live on different scales.

![Reciprocal Rank Fusion](assets/S02-rrf-fusion.svg)

**Mechanism** —

```text
RRF(doc) = sum_over_rankers 1 / (k + rank(doc))
```

`k` is often around 60. A document appearing reasonably high in both lists can beat a document that appears high in only one.

**Worked example** — Use `k = 60`.

| Document | BM25 rank | Dense rank | RRF score |
|---|---:|---:|---:|
| A | 1 | 10 | `1/61 + 1/70 = 0.0307` |
| B | 5 | 3 | `1/65 + 1/63 = 0.0313` |
| C | 2 | not in top list | `1/62 = 0.0161` |

Document B wins because it is strong in both systems.

**Tradeoff / when NOT to use** — RRF is robust and simple, but it ignores score margins. If dense retrieval is overwhelmingly confident and BM25 is only weakly matching, rank-only fusion can over-promote the keyword result. Production systems often follow hybrid retrieval with reranking.

---

### 19. Hybrid retrieval end-to-end

**Intuition** — Hybrid retrieval is the practical answer to the whole session: use semantic search for meaning, keyword search for exact evidence, ANN for speed, and fusion/reranking for final quality.

![Vector database architecture](assets/S02-vector-database-architecture.svg)

**Mechanism** — A typical flow:

```text
user query
  -> dense embedding -> ANN vector search
  -> keyword terms   -> BM25 sparse search
  -> RRF fusion
  -> optional reranker
  -> top passages to the LLM
```

**Worked example** — Query: `"policy for monitor reimbursement LAP-2026"`. Dense search can find `"work-from-home equipment expenses"` even without the exact wording. BM25 preserves `LAP-2026`. RRF promotes documents that satisfy both meaning and exact evidence.

**Tradeoff / when NOT to use** — Hybrid retrieval is overkill for tiny, stable, curated FAQ sets where exact approved answers already exist. For live document corpora with paraphrases, product codes, policy clauses, and changing terminology, hybrid is usually worth the extra moving parts.

## Self-study / Lab / build

**521 Lab 2 material now held:** `labs/S02-embeddings-vector-search/Embedding-distilbert.ipynb`.

Run the DistilBERT notebook before building the retriever. It makes sections 3, 6, and 9 concrete: the same token `bank` receives different final vectors depending on context, mean pooling turns those token vectors into sentence vectors, and cosine similarity gives a quick way to compare all of it.

⚠️ **One spec detail worth noticing.** Section 5's pipeline walkthrough uses BERT-base numbers (12 layers) because that is the canonical teaching example. The notebook actually loads `distilbert-base-uncased` — a **6-layer, ~66M-parameter distilled version of BERT**, same 768 hidden size and 12 attention heads, trained so a small "student" model imitates the larger BERT "teacher" (knowledge distillation). Fewer layers means faster, cheaper inference at a small quality cost — a real production tradeoff, not a mismatch to worry about. The pipeline mechanics (tokenize → embed → position → transformer layers → pool) are identical; only the layer count differs.

**Note → code map** — reading a concept and want to see it run? Jump to the exact cell:

| This note's concept | Notebook cell | What you run / see |
|---|---|---|
| §5 — BERT pipeline, but on DistilBERT's 6 layers instead of BERT-base's 12 | cell 3 | a spec table: 6 layers, 768 hidden, 12 heads, ~66M params, 512 max tokens |
| Setup — loading an encoder model | cell 5 | `AutoModel.from_pretrained("distilbert-base-uncased")` |
| §3 — contextual embeddings, the mechanism itself | cell 6 | `get_token_embedding()` — runs the model, finds the target word's token(s), averages sub-word pieces into one vector |
| §3 — worked example: `bank` in a river sentence vs a finance sentence | cell 7 | the two `bank` embeddings computed side by side, with their token positions printed |
| §3 + §9 — contextual embeddings compared with cosine similarity | cell 8 | `cosine_similarity(bank_river_vec, bank_finance_vec)` — a number well below 1.0, proving the two vectors genuinely differ |
| §9 — reading a cosine similarity number | cell 9 (markdown) | the scale this note's Mechanism table describes: ~1.0 identical, 0.8-0.95 very similar, 0.5-0.75 related, ~0.0 unrelated |
| §3 — same-context vs cross-context comparisons (does `bank` move *toward* the right neighbor?) | cell 10 | `bank` (river) scored against `river`, and `bank` (finance) scored against `money`/`account` — same-context scores come out higher than cross-context ones |
| §6 — mean pooling, applied to whole sentences | cell 11 | `mean_pool_sentence_embedding()` over 4 sentences, then a full pairwise similarity matrix — the two river sentences and the two finance sentences cluster together |

*(Cell 12 is the notebook's own one-line takeaway: `bank` has no single fixed vector — self-attention keeps rewriting it based on whatever words happen to be nearby.)*

Build a tiny hybrid retriever on 10-20 short documents:

1. Create document chunks and metadata.
2. Compute simple embeddings with any local/API embedding model.
3. Implement cosine similarity in Python.
4. Implement a minimal BM25 search or use a small library.
5. Combine dense and BM25 rankings with RRF.
6. Print the top-5 results for queries that test paraphrase, exact ID, and mixed cases.

The lab lesson is not the library call; it is seeing which query fails under dense-only or keyword-only retrieval.

⚠️ The held S02 notebook covers embeddings, contextual vectors, and cosine similarity. The rest of the expected Lab 2 package also includes text-to-speech, rule-based systems, and sentiment analysis; keep those open until their files arrive or the instructor confirms they are not part of this offering's Lab 2.

---

*Exam: this session is in scope for the **closed-book mid-sem** (L1-L8). Full evaluation, weights, dates and course logistics live once in [`521-master.md`](../521-master.md) — not repeated per session.*
