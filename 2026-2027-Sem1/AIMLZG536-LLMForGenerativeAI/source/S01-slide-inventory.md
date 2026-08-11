# 536 · S01 slide inventory

Derived index of the session-1 deck (`CS-1 Intro to LLM (2).pptx`), captured at intake so coverage can be re-checked without re-uploading the deck. Slide numbers, titles, and the named items on each slide only — no slide prose.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/source/S01-slide-inventory.md \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/notes/S01-foundations.md
```

| Slide | Title | Named items |
|---|---|---|
| 1 | Dr. Monali Mavani | Large, Models |
| 2 | Large Language Models for Generative AI | Large, Models |
| 3 | Handout |  |
| 4 | BITS Pilani, Pilani Campus | Book, Closed, Component, End, Evaluation, Exam, Open, Plan |
| 5 | Agenda | Architectures, Attention, Building, Introduction, Large, LLM, LLMs, Mechanism, Models, Review, Transformer |
| 6 | Introduction to LLMs and Generative AI | Introduction, LLMs |
| 7 | Language AI | Picture |
| 8 | Probabilistic Language Models | Models, Probabilistic, Probability, Simply |
| 9 | What is a Large Language Model? | Large, LLMs, Model, Picture |
| 10 | Conditional generation of text | Almost, Answering, Chan, Conditional, Jackie, NLP, Origin, Picture, Question, Sentiment, Species |
| 11 | Generative AI | Called, Picture |
| 12 | LLMs and Gen AI | Gen, LLMs, Picture |
| 13 | Natural language generation with LLMs | Large, LLMs, Models, Natural, NLG |
| 14 | Attention and Transformers Review | Attention, Review, Transformers |
| 15 | Transformer Decoder | Decoder, Picture, Transformer |
| 16 | Self attention | LLMs, Picture, Self, Self-attention |
| 17 | The three vectors | Dot, Key, Output, Picture, Query, Scale, Value, Weighted |
| 18 | Self attention | Output, Picture, Self |
| 19 | Self-attention: shapes and dimensions | Llama-3-8B, Self-attention, Vaswani |
| 20 | Multihead-Attention | Google, Multihead-Attention, Shape |
| 21 | Multi head attention | Attention, Dimension, Heads, Input, Number, Picture, Shape |
| 22 | Transformer block | Picture, Transformer |
| 23 | Layer Normalization and FFNN | Hidden, Layer, LayerNorm, Normalization, Picture, Standard |
| 24 | Building blocks of LLM | Building, LLM |
| 25 | Transformer LLM | LLM, Picture, Transformer |
| 26 | Transformer LLM | LLM, Picture, Transformer |
| 27 | Vocabulary Building | Building, Picture, Vocabulary |
| 28 | Tokens to token IDs | IDs, Picture, Tokens |
| 29 | Adding special context tokens | Adding, Picture |
| 30 | Token IDs to Token Embeddings | Embeddings, IDs, Picture |
| 31 | Embeddings | Embeddings, Picture |
| 32 | Embedding layer | Embedding, LLM, Picture |
| 33 | Embedding layer | Embedding, Picture |
| 34 | Types of text embeddings | Picture, Types |
| 35 | Positional embeddings | Picture |
| 36 | Positional Encoding | Embeddings, Encoding, Learned, RoPE, Rotary, Sinusoidal |
| 37 | Language Modelling Head | Head, Modelling, Picture |
| 38 | Language Modeling Head | Head, Modeling, Picture, Softmax |
| 39 | Unembedding (LM head): shapes and weight tying | BERT, DeepSeek-V3, Gemma-3, GPT-2, IDs, Input, Introduced, Llama-3, Llama-3-8B, OFF, OLMo, Output, Parameter, Press, Qwen3-0, Qwen3-8B, RoBERTa, Small, SmolLM2, Tied, Unembedding, Untied, Weight, Wolf |
| 40 | Context length | Context, Picture |
| 41 |  |  |
| 42 | LLM Architectures | Architectures, LLM |
| 43 | Encoder-Only Models (e.g., BERT, RoBERTa) | Architecture, BERT, Bidirectional, Context, Encoder-Only, Example, LLMs, MLM, Models, NER, Objective, RoBERTa, Strengths, Training, Transformer, Weaknesses |
| 44 | Decoder-Only Models (e.g., GPT, LLaMA) | Architecture, CLM, Context, Decoder-Only, Example, GPT, LLMs, Meta, Models, Objective, Picture, Strengths, Training, Transformer, Weaknesses |
| 45 | Encoder-Decoder Models (e.g., T5, BART) | Architecture, BART, Dual, Effective, Encoder-Decoder, Example, MLM, Models, Objective, Sequence-to-sequence, Strengths, Training, Weaknesses |
| 46 | Transformer Encoder-Decoder | Encoder-Decoder, Picture, Transformer |
| 47 | Tokenization |  |
| 48 | Common words end up being a part of the subword vocabulary, while rare | Common, Transformer, Transformerify, Variations, Word |
| 49 | Types of tokens | Ability, Apple, ByT5, CANINE, Picture, Subword, Tokenizer-free, Tokens, Types, UTF-8, Word |
| 50 | Subword tokenization | BPE, Byte-Pair, Encoding, Frequent, Kudo, Nakajima, Rare, Schuster, Sennrich, Subword, Unigram, Vocabulary, WordPiece |
| 51 | Byte Pair Encoding | BPE, Construct, Current, Encoding, Iteration, Pair, Pre, Split, Start, Vocab, Words |
| 52 | Find Most Frequent Pair: The algorithm scans the tokenized words and t | Encoding, Frequent, New, Pair, Result |
| 53 | Byte Pair Encoding | Efficient, Encoding, Helps, Limitations, Pair, Reduces |
| 54 | SentencePiece | BPE, English, Example, Gemma-2, Gemma-3, GPT-4o, GPT-5, Input, Language-independent, Llama-2, Llama-3, Llama-4, Mistral-7B, Models, OOV, Pieces, Preserves, SentencePiece, Subword, Supports, Tokenizer, Unicode, Unigram, UTF-8, Viterbi, Vocab, Whitespace-marked |
| 55 | SentencePiece Vs tiktoken | BPE, Hello, Llama-2, Llama-3, OOV, Regex, SentencePiece, Tokens, Whitespace-marked |
| 56 | Language models landscape | Adam, Attention, Bahdanau, Bengio, English, First, Huang, Kingma, Mixture, Model, Pre-neural, Rajbhandari, Sequence-to-sequence, Shannon, Shoeybi, Sutskever, Transformer, Vaswani |
| 57 | Language models landscape | AI2, Alibaba, BERT, BigScience, BLOOM, Chinchilla, DeepMind, DeepSeek, Early, EleutherAI, ELMo, Embracing, Face, Google, GPT-2, GPT-3, GPT-J, Hugging, Kaplan, Llama, LSTMs, Meta, OLMo, Open, OpenAI, OPT, PaLM, Pile, Qwen, Scaling, Transformer |
| 58 | Language models landscape | Alibaba, Anthropic, API, Claude, Closed, DeepSeek, Gemini, Google, GPT-4o, Grok, Hunyuan-T1, Levels, Llama, Max, Meta, OLMo, Open-source, Open-weight, OpenAI, Qwen, Sonnet, Tencent, Today |
| 59 | Recent models | Anthropic, Claude, Deep, DeepSeek, DeepSeek-R1, Family, Gemini, Gemma, Google, GPT-5, Grok, Key, Large, Long-context, Mistral, Model, MoE, Open-weight, OpenAI, Opus, Parallel, Primary, Pro, Reinforcement-learning-driven, Release, Strength, Thinking |
| 60 | References | Alamar, Build, Byte-Level, Ch-1, Dan, Jan, Jurafsky, Large, Machine, Model, Models, RASCHKA, Research, Scratch, SEBASTIAN, Speech, Subwords, Translation |
| 61 | Extra slides (Not for exams) | Extra |
| 62 | Byte tokens Vs BPE | BPE, Bytes, Caf, Characters, Every, Extremely, Failure, First, Frequent, Likely, Merge, Pairs, Second, Space, Tokens, UNK, UTF-8 |
| 63 | Byte-level BPE ( GPT2) | BPE, Byte-level, Bytes, Caf, Emoji, Frequent, GPT-2, GPT2, Merge, Sequences, Space, Tokens, Unicode, Zero |
| 64 | Byte level BPE example | Another, BPE, Bytes, English, Raw, Sentence, Words |
| 65 | Wordpiece | Appear, Base, Begin, Compute, Count, Google, Instead, Machine, Merge, Often, Pairs, Reference, Repeat, Scores, Start, Subword, System, Together, Translation, Units, Vocabulary, Wordpiece, WordPiece, Works |
| 66 | Wordpiece | BPE, Breaks, Efficient, Helps, Limitations, Rare, Reduces, Size, Vocabulary, Wordpiece, WordPiece, Words |
| 67 | WordPiece is the tokenization algorithm Google developed to pretrain B | BERT, BPE, Google, Initial, Starts, WordPiece |
| 68 | Corpus uses these five words: "hug", "pug", "pun", "bun", "hugs" | Assume, Corpus, First, Repeat, Score, Training, Vocabulary |
| 69 | Token segmenter: New inputs are tokenized by applying the following st | Apply, Corpus, Look, New, Pre-tokenize, Repeat, Split, Test, Vocabulary |
