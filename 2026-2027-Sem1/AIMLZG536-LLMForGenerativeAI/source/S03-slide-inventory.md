# 536 · S03 slide inventory

Derived index of the session-3 deck (`CS-3 Advancements in LLM Architecture.pptx`), captured at intake so coverage can be re-checked without re-uploading the deck. Slide numbers, titles, and the named items on each slide only — no slide prose.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/source/S03-slide-inventory.md \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/notes/S03-architecture.md
```

| Slide | Title | Named items |
|---|---|---|
| 1 | Dr. Monali Mavani | Large, Models |
| 2 | Large Language Models for Generative AI | Large, Models |
| 3 | Agenda | Advanced, Advances, Encoding, Gated, GELU, GLU, LayerNorm, Linear, MoE, NoPE, Norm, Normalization, RMSNorm, RoPE, Swish, Units |
| 4 | Transformer architecture | Attention, Encoding, Feed, Forward, Layer, Norm, Places, Transformer |
| 5 | RMSNorm is simplified version of LayerNorm with fewer trainable parame | LayerNorm, Picture, RMS, RMSNorm |
| 6 | LayerNorm Vs RMSNorm | LayerNorm, RMSNorm |
| 7 | In Post-Norm (original "Attention is All You Need" design), LayerNorm | Attention, Gemma, Gradient, LayerNorm, Norm, OLMo, Post, Post-Norm, PostNorm, Pre-Norm, PreNorm, RMSNorm, Sublayer, Tolerates, Trains |
| 8 |  |  |
| 9 | You are designing a very deep decoder-only LLM with more than 100 laye | Answer, DeepSeek, LayerNorm, Llama, LLM, LLMs, Mistral, Norm, Pre-Norm, Question, Qwen, RMSNorm, Sample |
| 10 | Position Embedding | Embedding, Position |
| 11 | Key intuition: instead of each token saying “I am at position k”, pair | Attention, Embeddings, Example, Key, RoPE, Rotary, Rotation |
| 12 | RoPE | Introduced, RoFormer, RoPE |
| 13 | RoPE | Picture, RoPE |
| 14 | Why did many models move away from learned absolute positional embeddi | Cleaner, DeepSeek, GLM-4, GPT-OSS, Llama, NoPE, Position, Qwen, RoPE, RoPE-based, Sarvam, SmolLM3, Typical |
| 15 | Activation Functions in Modern LLMs | Activation, LLMs, Modern, Picture |
| 16 | Where It Sits: FFN → Gated FFN (GLU) | FFN, Gated, GLU, Linear, Picture, Regular, Same, Sits |
| 17 | Mixture of Experts (MoE) | Experts, Mixture, MoE |
| 18 | Mixture of Experts (MoE) | Decoder, Dense, Experts, FLOPs, Layers, LLMs, Mixture, MoE, Sparse, Transformer |
| 19 | Architecture of Experts | Architecture, Experts, Picture |
| 20 | Mixture of Experts (MoE) | Different, Experts, LLMs, Mixture, Model, MoE, Picture |
| 21 | Router (or gate network) is also an FFNN and is used to choose the exp | Expert, Experts, Mixture, MoE, Picture, Router |
| 22 | allows for a given token to be sent to one expert (top-1 routing) or t | Balancing, Choice, Experts, Load, Picture |
| 23 | It is not just about which experts are used but how much they are used | Balancing, Capacity, Expert, Load, Picture |
| 24 | Sparse MoE | Dense, Learning-driven, Llama, Maverick, Mode, MoE, Newer, Qwen3-Next, Reinforcement, Scout, Sparse, Sparsity, Thinking, Uses |
| 25 | Shared experts always active → capture common knowledge, reduce redund | DeepSeek-V3, GLM-4, Kimi, Modern, MoE, Picture, Routed, Same, Shared |
| 26 | Llama 4 Maverick (400B total / 17B active) — Fewer, bigger experts | Alternating, Bet, DeepSeek, DGX, Fewer, FFN, H100, Llama, Maverick, Modern, MoE, Picture |
| 27 | Benefits | Active, Different, Expert, GPU, Mixtral, MoE, Routing, Scaling, Training |
| 28 | Question: In an MoE architecture, explain the concept of "Expert Capac | Answer, Capacity, Expert, GPU, Inference, MoE, Overflow, Question, Sample, Training |
| 29 | Hands-On Large Language Models by Jay Alammar and Maarten Grootendorst | Approximation, EMBEDDING, ERROR, Function, GAUSSIAN, GLU, Improve, Large, Learning, LINEAR, Linear, Models, Network, Position, POSITION, Reinforcement, Relative, Representations, Research, ROFORMER, ROTARY, Sigmoid-Weighted, TRANSFORMER, Transformer, Units, UNITS, Variants, Vector, WITH |
