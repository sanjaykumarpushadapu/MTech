# 521 · S02 slide inventory

Derived index of the session-2 deck (`Session_02_Embeddings_Vector_Search.pdf`), captured at intake so coverage can be re-checked without re-uploading the deck. Slide numbers, titles, and the named items on each slide only — no slide prose.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/source/S02-slide-inventory.md \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/notes/S02-retrieval.md
```

| Slide | Title | Named items |
|---|---|---|
| 1 | Conversational AI | ANN, Conversational, Embeddings, Search, Vector |
| 2 | BITS Pilani | AIMLCZG521, Conversational, Lecture, Module |
| 3 | Disclaimer & Acknowledgement |  |
| 4 | Outline | ANN, Basic, Cost, Database, Embedding, Embeddings, Encoder, HNSW, Index, IVF, Part, Prerequisites, Transformer, Vector |
| 5 | Learning Objectives | ANN, Explain, HNSW, IVF, Learning, Objectives |
| 6 | Transformer Architecture | Add, Architecture, Block, Decoder, Embeddings, Encoder, Encoding, Feed-Forward, FFN, IDs, LayerNorm, Layers, Linear, Multi-Head, Network, Parallel, Project, ReLU, Residual, Softmax, Transformer |
| 7 | Self-Attention vs Cross-Attention- Revisit | Aam, Attention, Cross-Attention, Current, Decoder, Encoder, English, Financial, Hindi, Input, Institution, Job, Key, Layer, Mangoes, Mechanism, Mujhe, Output, Point, Query, Result, Sentence, Source, Value |
| 8 | Multi-headed Attention | Attention, Concept, Instead, Multi-Head, Multi-headed, Outputs |
| 9 | What are Encoder Models? | Autoregressive, BERT, Bidirectional, Capability, Causal, Classification, Encoder, GPT, Key, MASK, Masked, Missing, MLM, Modeling, Models, Predict, Random, Tokens, Training, Transformers |
| 10 | Why Encoders for Embeddings? | Bidirectional, BOTH, Contextual, Embedding, Embeddings, Encoder, Encoders, Looks, Master, Mechanism, Models, Sentence, View, Word |
| 11 | Encoder vs Decoder | Attends, Causal, Context, Cross-attention, Decoder, Encoder, Encoders, Generation, Input, Masked, Output, Parallel, Position-aware, Self-attention, Sequential |
| 12 | Decoders Laugh as Loud as Encoders | ALBERT, BART-large-mnli, BERT, Borodach, Categories, COMPARED, Dataset, DeBERTa, Decoders, DECODERS, Eli, Encoder, ENCODER-DECODERS, Encoders, ENCODERS, Fine-tuned, Flan-T5, Flan-T5-base, Gemma, GPT-4, GPT-4o, Human-authored, Humor, Laugh, Llama, Loud, Mistral, MODEL, ModernBERT, NeoBERT, Prior, Qwen2, Result, RoBERTa, RoBERTa-base, Statistically, TYPES, XLNet |
| 13 | Encoder vs Decoder vs Encoder-Decoder | ALBERT, Analysis, Answering, BART, BERT, Bidirectional, Cases, Causal, ChatGPT, Classification, Claude, Code, Conversational, Copilot, DeBERTa, Decoder, Decoder-Only, DistilBERT, Document, Embeddings, Encoder, Encoder-Decoder, Encoder-Only, English, Entity, FLAN-T5, Following, French, Generation, GitHub, GPT-3, GPT-4, Instruction, Learning, Machine, Mistral, Models, Named, NER, PEGASUS, Popular, Predicts, Question, Recognition, RoBERTa, Search, Sees, Semantic, Sentiment, Separate, Strength, Summarization, Synthesis, Tasks, Text-to-Text, Translation, Use |
| 14 | Comparison | Analysis, Code, Comparison, Conversational, Cross-attention, Decoder, Decoder-only, Decoder-Only, Encoder, Encoder-, Encoder-Only, Entity, Generation, Inefficient, Machine, Modern, Named, Needs, Outdated, Overkill, Possible, Rare, Reasoning, Recognition, Requires, Search, Semantic, Sentiment, Sequential, Suboptimal, Summarization, Task, Token-level, Traditional, Translation |
| 15 | How Encoder Transformers Create Embeddings | BERT, BERT-base, BGE, CLS, Create, Default, DistilBERT, Embeddings, Encoder, FFN, GTE, IDs, Input, LayerNorm, Layers, Machine, Max, Mean, Pooling, Position, RoBERTa, Sentence-BERT, SEP, Step, Strategy, Sum, Transformer, Transformers |
| 16 | BERT Pipeline | BERT, Classification, CLS, IDs, Machine, Pipeline, Required, SEP, Single, Step |
| 17 | 2 / 5 | BERT, CLS, Embedding, Embeddings, Key, Lookup, Machine, Pipeline, Same, SEP, Single, STATIC, Step |
| 18 | BERT Pipeline | Added, BERT, CLS, Embeddings, Machine, Pipeline, Result, SEP, Single, Step |
| 19 | BERT Pipeline | ALL, BERT, Every, Feed-Forward, Inside, Layer, LayerNorm, Layers, Machine, Network, Output, Pipeline, POS, Single, Step, Transformer |
| 20 | BERT Pipeline | Average, BERT, BGE, CLS, Default, DistilBERT, GTE, Machine, Max, Mean, NLI, ONE, Pipeline, Pooling, RAG, RoBERTa, Sentence-BERT, Single, Step, Strategy, Take |
| 21 | How Encoder Transformers Create Embeddings | Attention, CLS, Create, Embeddings, Encoder, GloVe, Key, Mathematics, Max, Mean, Pooling, Query, Strategies, Transformers, Value |
| 22 | Embedding Models: Key Players | Alibaba, BAAI, Context, Embedding, General, Instruction-following, Jina, Key, Long, Microsoft, Model, Models, Multilingual, Open, Players, Production, Provider, Recommended, Source |
| 23 | Embedding Models: Key Players | API, Compression, Context, Cost, Embedding, Guide, Highest, Key, Model, Models, Players, Quality, Start, Use |
| 24 | Embedding Models: Complete Reference | Alibaba, API, Arch, BAAI, BERT, Cohere, Complete, Con, Context, Contrastive, Embedding, Hidde, Jina, Layer, Microsof, Mistral, Model, Models, Multi-task, Open, OpenAI, Output, Provider, Reference, RetroMAE, See, Slide, Training, Transfor |
| 25 | Embedding Moels: Training Objectives | Contrastive, Embedding, Learning, Masked, MLM, Modeling, Objectives, RetroMAE, Training |
| 26 | Training Objective – Contrastive Learning | Contrastive, Creates, DPR, GTE, Hard, Learning, Loss, Models, Negative, NV-Embed, Objective, Pair, Positive, Requires, SBERT, Sensitive, SimCSE, Train, Training, Works |
| 27 | Training Objective – Masked Language | Assumes, BERT, BERTa, Example, Foundation, Learns, Loss, MASK, Masked, Maximize, MLM, Model, Modeling, Models, Objective, Original, Predict, RoBERTa, Slower, SpanBERT, Training, Using, Works |
| 28 | Training Objective – RetroMAE | Creates, Decoder, Efficient, Encoder, Example, Loss, Masked, MLM, Models, Objective, Original, Process, Reconstruct, Requires, RetroMAE, RetroMAE-BEIR, Step, Task, Training, Works |
| 29 | From Embeddings to Search | Different, Embeddings, Learn, Learned, Next, Search, Self-attention, Transformer, Vector |
| 30 | Vector Similarity: Mathematical Foundations | Cosine, Distance, Dot, Euclidean, Inner, Key, Larger, Mathematical, Product, Range, Sensitive, Similarity, Vector |
| 31 | Vector Similarity: Visual Intuition | Angle, Cosine, Distance, Euclidean, High, Image, Intuition, Product, Range, Similarity, Value, Vector |
| 32 | Vector Similarity | Code, Similarity, Vector |
| 33 | The Computational Challenge | Challenge, Computational, CPU, Operations, Problem, Task, Time |
| 34 | Linear Scan vs ANN Solution | ANN, Approximate, Brute-force, Challenge, Computational, CPU, Failure, HNSW, Linear, Nearest, Neighbor, Requires, Scan, Solution |
| 35 | What Is Vector Indexing? | ANN, Approximate, Indexing, Instead, Nearest, Neighbor, Search, Vector |
| 36 | ANN: Approximate Nearest Neighbor Search | ANN, Approximate, Instead, Nearest, Neighbor, RAG, Search |
| 37 | Approximate Nearest Neighbor (ANN) | Analysis, ANN, Approximate, Cost, Documents, EXACT, HNSW, Index, Key, Linear, Nearest, Neighbor, Scale, Scan, Solution |
| 38 | ANN Indexing Strategies | ANN, Billions, Build, Cluster, Compress, Compression-Based, Cons, Example, Excellent, Fast, Graph-Based, High, HNSW, Indexing, IVF, Lower, Needs, Partition-Based, Scalable, Sensitive, Slow, Strategies, Works |
| 39 | HNSW: Hierarchical Navigable Small World | Average, Concept, Enter, Entry, Expand, Greedy, Hierarchical, HNSW, Layer, List, Malkov, Medium, Multi-Layer, Multiple, Navigable, Process, Repeat, Robust, Search, Skip, Small, Source, Sparse, Top, Vectors, World, Yashunin |
| 40 | HNSW (Hierarchical Navigable Small World) | Concept, Hierarchical, HNSW, List, Multi-Layer, Navigable, Skip, Small, Vectors, World |
| 41 | HNSW (Hierarchical Navigable Small World) | Hierarchical, HNSW, Navigable, Small, World |
| 42 | HNSW (Hierarchical Navigable Small World) | Concept, Hierarchical, HNSW, List, Malkov, Multi-Layer, Navigable, Skip, Small, Source, Vectors, World, Yashunin |
| 43 | HNSW: Memory Layout | Components, Connections, Example, HNSW, Layer, Layout, Memory, Original, Search, Storage, Vector |
| 44 | HNSW: Memory Calculation by Scale | Budget, Graph, HNSW, Memory, Overhead, Planning, Practical, Production, Scale, Vector |
| 45 | Parameter Tuning: HNSW | Default, Fast, Faster, Higher, HNSW, Layer, Lower, Parameter, Pro, Slow, Slower, Start, Time, Tip, Tuning, Typical |
| 46 | Resources & Further Reading | Dense, Efficient, Foundation, Gurevych, HNSW, Karpukhin, Malkov, Passage, Product, Reading, Reimers, Retrieval, Sentence-BERT, Siamese, Vector, Yashunin |
| 47 | References | CUy1DZZspM, Embedding |
| 48 | Thank you | Thank |
