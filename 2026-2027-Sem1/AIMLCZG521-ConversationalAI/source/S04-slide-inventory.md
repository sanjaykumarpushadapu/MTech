# 521 · S04 slide inventory

Derived index of the session-4 deck (`Session4-Model-Landscape-Cost-Engineering.pdf`, instructor label "Lecture No. 4 | Module 1"), captured at intake so coverage can be re-checked without re-uploading the deck. Slide numbers, titles, and the named items on each slide only — no slide prose.

This deck teaches the handout **L3** row (Model Landscape & Cost Engineering); the instructor's "Lecture 4" label reflects retrieval having taken two contact sessions (L2 embeddings + a hybrid-search session). Session identity resolved to handout L3 — see `source/MATERIAL-LOG.md`.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/source/S04-slide-inventory.md \
  ../2026-2027-Sem1/AIMLCZG521-ConversationalAI/notes/S04-model-landscape.md
```

| Slide | Title | Named items |
|---|---|---|
| 1 | Conversational AI | Model, Landscape, Cost, Engineering |
| 2 | BITS Pilani | AIMLCZG521, Conversational, Lecture, Module |
| 3 | Disclaimer & Acknowledgement | |
| 4 | Learning Objectives | Dense, MoE, SLM, SSM, MMLU, GPTQ, AWQ, QLoRA, M_total, M_weights, M_KV, M_activation, vLLM |
| 5 | Agenda | Dense, GPT-4o, Claude, Llama, Gemini, Mixtral, DeepSeek-V3, Phi-4, Gemma, Qwen2.5, Mamba-2, Jamba, FP32, NF4, GPTQ, AWQ, FP8, LoRA, QLoRA, KV-Cache, Activations |
| 6 | The 2025 LLM Landscape | Dense Transformer, Mixture-of-Experts, Small LMs, State Space Models, GPT-4o, Claude 3.7 Sonnet, Llama 3.3, Gemini 2.0, DeepSeek-V3, Mixtral, Qwen2, Jamba-1.5, Phi-4, Gemma 3, Mamba-2, RWKV, MMLU, Context Window |
| 7 | The 2026 LLM Landscape | GPT-5, Claude 4, Llama 4, Gemini 3, DeepSeek-V4, Qwen3-MoE, Grok-2, Phi-5, Gemma 4, Mamba-3, RWKV-7, Jamba 2, Liquid-2, MMLU |
| 8 | Dense Transformer Models | GPT-4o, Claude 3.7 Sonnet, Llama 3.3 70B, Gemini 2.0 Flash, Extended Thinking, vLLM, BF16, H100, MMLU |
| 9 | Mixture of Experts | Transformer, Router, Experts, Decoder block, Multi-Head Attention |
| 10 | Mixture of Experts: Router Mechanism | Router, TopK, softmax, Expert, Expert Collapse, Auxiliary Load-Balance Loss, DeepSeek-V3, Shazeer, W_router |
| 11 | Mixture of Experts Models | DeepSeek-V3, Qwen2-57B-A14B, Jamba-1.5 Large, Active, Total, Saving, H100 |
| 12 | Small Language Models (SLMs) | Phi-4, Gemma 3, Qwen2.5, Llama 3.2, SmolLM2, MMLU, router, NER, slot-filling |
| 13 | Attention Mechanism Fundamentals | Query, Key, Value, Scaled Dot-Product Attention, softmax, d_k, Vaswani |
| 14 | Transformer's Quadratic Complexity Problem | QK, FlashAttention-3, Sparse Attention, sequence length |
| 15 | State Space Models: Linear Complexity Solution | Mamba-2, S4, hidden state, d_state, Selective SSM |
| 16 | State Space Models (SSMs) | Mamba-2, Jamba-1.5, O(n), In-Context Learning, hybrid, vLLM, TRT-LLM, MMLU |
| 17 | Intelligent Model Routing | SLM, MoE, Dense, Phi-4-mini, Qwen2.5, Mixtral, DeepSeek-V3, Claude 3.7, GPT-4o, RouteLLM, CSAT, P50 latency |
| 18 | Transition — quantify cost | Architecture, VRAM, Quantization, Token pricing |
| 19 | Quantization: Making Models Efficient | FP32, BF16, FP8, E4M3, E5M2, INT8, LLM.int8, NF4, GPTQ, AWQ, INT4, bits |
| 20 | Floating Point Formats | FP32, BF16, FP16, FP8, E4M3, E5M2, Sign, Exponent, Mantissa, Transformer Engine |
| 21 | Post-Training Quantization (PTQ) | GPTQ, AWQ, FP8 Native, Hessian, calibration, salient weights, exllama, AutoAWQ, Transformer Engine, vLLM, TRT-LLM, SGLang, Ollama |
| 22 | Low-Rank Adaptation (LoRA) | W_frozen, B A, low-rank, adapter, Hu |
| 23 | LoRA Architecture Visualization | rank |
| 24 | QLoRA: Quantization + Fine-Tuning | NF4, double quantization, LoRA, BF16, A6000, A40, A100, MMLU, MT-Bench, Adam, Dettmers |
| 25 | Quantization Decision Guide | FP32, BF16, QLoRA, NF4, FP8, INT8, AWQ, TTFT, A10G |
| 26 | GPU Memory Estimation | M_total, M_weights, M_KV-cache, M_activation, layers, heads, d_head, seq, batch |
| 27 | Why Do We Need KV-Cache | KV-Cache, autoregressive, O(n), Query, Key, Value, cache |
| 28 | KV-Cache: Technical Implementation | Prefill, Generation, d_head, W_Q, W_K, W_V, concat, softmax |
| 29 | KV-Cache: The Hidden Memory Consumer | M_KV, layers, heads, d_head, seq_len, batch_size, PagedAttention, GQA, Grouped-Query Attention |
| 30 | Hands-On: Memory Calculation | 175B, BF16, KV-Cache, Activations, H100, A100, FP8, tensor parallelism |
| 31 | Memory-Efficient Inference at Scale | FlashAttention-3, PagedAttention, vLLM, FlexGen, Tensor Parallelism, Pipeline Parallelism, Megatron-LM, continuous batching |
| 32 | Token Economics: Understanding API Costs | GPT-4o, GPT-4 Turbo, Claude 3.7 Sonnet, Claude 3.5 Haiku, Gemini 2.0 Flash, DeepSeek-V3, Mixtral, vLLM, Input, Output, Cached Input |
| 33 | Prompt Caching: 90% Cost Reduction | prompt caching, TTL, system prompt, few-shot, cache invalidation, breakpoint, Anthropic, OpenAI |
| 34 | Production Cost Optimization Playbook | prompt caching, model routing, RouteLLM, self-host, vLLM, AWQ, speculative decoding, Batch API, max_tokens |
| 35 | Emerging Trends in LLM Optimization | 1-BIT LLMs, BitNet, FlashAttention-4, Hardware-Aware Quantization, ternary, GQA, ring attention |
| 36 | Self-Hosting vs API: Break-Even Analysis | Managed API, Self-Hosted, vLLM, H100, break-even, DevOps, tokens/month, latency, data privacy |
| 37 | Key Takeaways | Dense, MoE, SLM, SSM, Mamba-2, Jamba-1.5, KV-Cache, GQA, PagedAttention, FlashAttention-3, prompt caching, self-host |
| 38 | References | |
| 39 | References & Further Reading | |
