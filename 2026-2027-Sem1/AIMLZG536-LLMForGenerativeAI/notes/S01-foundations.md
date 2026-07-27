# 536 · Session 01 · Foundations of Large Language Models

*Learned ____ · Instructor Dr. Monali Mavani · built from `CS-1 Intro to LLM.pptx` (69 sl, 47 images) + T1 Jurafsky & Martin ch2/7/8 + T2 Alammar & Grootendorst ch1–3 + R1 Raschka ch1–2 + HF LLM course 6.5 + 2h05 recording. Exam scope & logistics folded into the **Exam layer** at the end.*

## Why this matters

This is the session that makes you fluent in how modern AI actually works under the hood. **Every LLM you'll use, fine-tune, or deploy in your career is a transformer doing next-token prediction** — and this is where *attention*, *embeddings*, *context window*, *tokenization* and *decoder-only* stop being buzzwords and become things you can compute and reason about. Get this and you can read any model card, debug a tokenizer surprise, size a context window against its cost, or answer the interview question about how attention scales. It's the vocabulary and machinery the whole field is written in.

**Running example throughout:** **Llama-3 8B** (d = 4096, 32 heads, d_k = 128). Anchor every new number to it.

## How to use this note

| Goal | Where to go |
|---|---|
| **Learn it end to end** | Top to bottom. Each concept runs **Intuition → Mechanism → Worked example → Tradeoff**, with ***In practice*** / ***Going deeper*** blocks where the real-world detail earns its place |
| **Actually understand attention** | Sections 4–5 — and **reproduce the shape tables from a blank page.** Reading them is not the same as being able to write them |
| **Look something up later** | The topic list below is the index; each concept is self-contained |
| **Revise for the exam** | Fold out the **Closed-book recall card** under each concept; scope and dates are in the collapsed *Exam layer* at the end |

> **This is the one subject where reading is not enough** — for your career as much as the exam. The mechanism topics (sections 4, 5, 6, 9, 10) have worked examples with real numbers. If you can't reproduce the multi-head shape table from a blank page, you don't have section 5 yet. The course framing (*"before mid-sem: mechanism; after: application engineering"*) maps onto sections 1–7 vs 9–16, and onto closed-book vs open-book.

## Topics

**Part 1 — What a language model is** *(the conceptual base; ~20 min of her class time, the longest stretch)*
1. **What a language model is** — P(W) and P(next word); why word order emerges from counting
2. **What makes it "large"** — three different things, each with its own cost
3. **Generation as prediction** — the idea the whole field rests on; why any NLP task can be next-word prediction

**Part 2 — How the machinery works** *(mechanism; ~17 min on attention alone, worked by hand)*
4. **Self-attention** — Q/K/V, the three-step computation, and the shape table
5. **Multi-head attention** — why h heads cost the same as one; the worked N=4, d=512 example
6. **The transformer block** — the equations, two residuals, pre-norm
7. **Positional encoding** — attention has no sense of order; learned vs sinusoidal vs RoPE

**Part 3 — Text in, text out** *(the pipeline around the model)*
8. **Text → tokens → embeddings** — special tokens, the embedding lookup with real numbers, positional addition
9. **The LM head and weight tying** — three shapes, and a 13%-of-model parameter decision
10. **Context length** — why it's capped by O(n²) and KV-cache, not ambition

**Part 4 — The landscape** *(comparison tables only — do not over-invest)*
11. **Architectures** — encoder-only vs decoder-only vs encoder-decoder, and why decoder-only won
12. **Tokenization** — → mostly lives in `_shared/tokenization.md`; **Lab 1 is here**
13. **The LLM landscape** — the causal chain, and the three levels of openness

---

## 1. What a language model is

*Reference: T1 Jurafsky & Martin, *Speech and Language Processing* ch3 (N-gram language models) — the P(W) framing.*

**Intuition** — A language model answers one question: *given what came before, what comes next?* Everything else in this course is built on that.

**Mechanism** — formally, a model that computes either:

- the probability of a sentence, **P(W)**, or
- the probability of an upcoming word, **P(wₙ | w₁, w₂, …, wₙ₋₁)**

Equivalently: it assigns a probability to each possible next word — **a probability distribution over the vocabulary**.

**Worked example — the deck's own:**

```
P(all of a sudden I notice three guys standing on the sidewalk)
    >
P(on guys all I of notice sidewalk three a sudden standing the)
```

Same words, different order. A language model that has learned English assigns far more probability to the first. That's the entire signal — no grammar rules were written down; word order emerged from counting.

**Tradeoff / what this framing costs** — Defining a model purely by next-word probability means there is **no notion of truth in the objective**. A fluent falsehood scores well; that's not a bug in the training, it's what the objective asked for. Hallucination is downstream of this definition, which is why S14 needs separate faithfulness metrics.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> Language model = computes **P(W)** (probability of a sentence) or **P(wₙ|w₁…wₙ₋₁)** (probability of the next word). Equivalently: a **probability distribution over the next token**. Learns word order from data, not rules — *P(fluent sentence) > P(scrambled sentence)*. Note: the objective contains **no notion of truth**, only fluency.

</details>

---

## 2. What makes a language model "large"

*Reference: R1 Raschka, *Build a Large Language Model (From Scratch)* ch1.*

**Intuition** — "Large" is not one thing. The deck names three, and the exam can ask for all three:

1. **Model size** — number of parameters
2. **Dataset size** — trained on massive text, "large portions of the entire publicly available text on the internet"
3. **Context** — a larger context of words

LLMs are **deep neural networks** trained on that data.

**Tradeoff** — all three scale cost. Parameters cost memory and inference compute; data costs collection, cleaning and training time; context costs attention compute that grows **quadratically** with sequence length (section 4). Each of the three has its own optimisation topic later: quantization for parameters (S6), scaling laws for data (S2), and efficient attention for context (S4).

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> LLM = deep neural network trained on massive text. **"Large" means three things: parameter count · training dataset size · context length.** Each scales cost differently → quantization (S6), scaling laws (S2), attention efficiency (S4).

</details>

---

## 3. Generation as prediction

*Reference: T2 Alammar & Grootendorst, *Hands-On Large Language Models* ch1.*

**Intuition** — This is the session's key idea, and the deck calls it *the fundamental intuition of language models*: **a model that can predict text can also generate text, by sampling from the distribution it predicts.** Prediction and generation are the same machine used in two directions.

A model used this way is an **autoregressive language model** — each generated token is fed back in to predict the next.

```mermaid
flowchart LR
    P[Prompt] --> M[LLM]
    M -->|distribution over vocab| S[Sample a token]
    S --> O[Output token]
    O -.->|append, feed back| M
```

**The consequence that makes LLMs general** — *almost any NLP task can be modelled as word prediction.* The deck's two examples:

**Sentiment classification** becomes a comparison of two probabilities:

```
P("positive" | "The sentiment of the sentence 'I like Jackie Chan' is:")
P("negative" | "The sentiment of the sentence 'I like Jackie Chan' is:")
```

**Question answering** becomes next-word prediction:

```
P(w | Q: Who wrote the book "The Origin of Species"? A:)
```

**Generative AI** is the broader area: using computational models to generate text, code, speech, images, video and audio. LLMs are the text branch. And LLMs are **(mostly) natural language generation (NLG) systems** — the process of generating text with them is called **decoding** (the whole of S5).

**Tradeoff / when NOT to reframe a task as generation** — You *can* express classification as generation, and it's often worse: a fine-tuned classifier is smaller, faster, cheaper and gives calibrated probabilities, where an LLM gives you a token that happens to read "positive". Reframing buys generality and zero-shot capability; it costs efficiency and calibration. This is the same tradeoff 546 draws in its foundation-models section — the expensive general answer versus the cheap specific one.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Fundamental intuition: a model that can predict text can generate it, by sampling from the predicted distribution.** Feeding output back in = **autoregressive**. Generating text with an LLM = **decoding**. Because prediction is general, **almost any NLP task can be cast as word prediction** — sentiment = compare P("positive"|prompt) vs P("negative"|prompt); QA = P(w|"Q:…A:"). **Generative AI** = using models to generate text, code, speech, images, video, audio. Cost of the reframing: a fine-tuned classifier is smaller, faster and better calibrated.

</details>

---

## 4. Self-attention

*Reference: T2 ch3; the original ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) (Vaswani et al. 2017); [Alammar, "The Illustrated Transformer"](https://jalammar.github.io/illustrated-transformer/).*

**Intuition** — Self-attention lets every token look at every earlier token and decide how much each one matters to it. The deck's framing: it gives **an uncompressed view of the entire sequence with fast training**. "Uncompressed" is the key word — unlike an RNN, nothing is squeezed through a fixed-size hidden state; every position stays individually addressable.

It builds a matrix comparing each token with every token before it, weighted by **how relevant the token pairs are to one another**. During training the whole matrix is computed **in one go**, which is what enables **parallelisation** — and that, not accuracy alone, is why transformers won.

**Mechanism — the three vectors.** Every token produces three projections, and the deck's phrasing for each is worth memorising verbatim:

| | Name | The question it asks |
|---|---|---|
| **Q** | Query | *"What am I looking for?"* — the current token asking a question of every previous token |
| **K** | Key | *"What do I contain?"* — each past token advertising its relevance to the query |
| **V** | Value | *"What do I contribute?"* — the actual content pulled in once relevance is decided |

**The computation, in three steps:**

```mermaid
flowchart LR
    X[Token embeddings X] --> Q[Q = X·WQ]
    X --> K[K = X·WK]
    X --> V[V = X·WV]
    Q --> S["1 · Q·Kᵀ / √dk<br/>attention scores"]
    K --> S
    S --> A["2 · softmax<br/>attention weights"]
    A --> Z["3 · A·V<br/>weighted sum"]
    V --> Z
    Z --> OUT[Context-aware representation]
```

1. **Q · Kᵀ** — dot product: how similar is the query to each key? Higher = more relevant.
2. **÷ √d_k** — scaling: keeps scores from blowing up and destabilising the softmax. *Why √d_k specifically (my clarity — the deck states the effect, not the reason): each score is a dot product of two d_k-dimensional vectors, so its size grows with the dimension — variance ≈ d_k, typical magnitude ≈ √d_k. Dividing by √d_k renormalises scores back to unit scale. Skip it and, at d_k = 128, scores run into the tens; softmax of widely-spread inputs saturates to almost one-hot, its gradient collapses toward 0, and the layer stops learning. √d_k is exactly the factor that cancels the dimension's inflation.*
3. **softmax → × V** — blend the values by how much attention each token deserves.

As the original paper's block, which is the form to reproduce in an exam:

```
MatMul(Q, Kᵀ) → Scale (÷√d_k) → Mask (optional) → SoftMax → MatMul(·, V)
```

The **Mask** step is optional in the general figure and **mandatory in a decoder** — it's what enforces causality (section 11).

Then an **output projection** maps the result from (n × d_v) back to (n × d), the model dimension, so layers can stack.

**Worked example — the shapes, which you must be able to write from memory.** Notation: **n** sequence length · **d** model/embedding dim · **d_k** key/query dim · **d_v** value dim · **h** heads.

| Tensor | Shape |
|---|---|
| X | n × d |
| W_Q, W_K | d × d_k |
| W_V | d × d_v |
| Q, K | n × d_k |
| V | n × d_v |
| QKᵀ ÷ √d_k | **n × n** |
| A = softmax(...) | **n × n** |
| Z = A · V | n × d_v |

| Model | d | h | d_k = d_v |
|---|---|---|---|
| Vaswani et al. 2017 (original) | 512 | 8 | 64 |
| Llama-3-8B | 4096 | 32 | 128 |

**Tradeoff / the cost that defines the field** — the attention matrix is **n × n**. Double the context and you quadruple the attention compute and memory. Every efficiency topic in S4 — FlashAttention, Ring Attention, sliding-window, sparse and linear attention — exists to attack that single quadratic term. Self-attention buys an uncompressed view and parallel training; it charges O(n²).

> ***In practice*** *(beyond the deck — what this O(n²) means when you actually use LLMs):*
> - You **never implement attention yourself** in a real job — you call an optimised kernel (**FlashAttention**) inside a serving stack (**vLLM**, **TGI**, TensorRT-LLM). Knowing the maths is what lets you reason about *why* a 100K-token prompt is slow and expensive, not code the softmax.
> - At **inference** the trick that makes generation fast is the **KV-cache**: keys and values for past tokens are cached so each new token is O(n) not O(n²). This is why the *first* token of a long prompt is slow ("prefill") and later tokens are fast ("decode") — a distinction you'll meet the moment you look at latency metrics.
> - Practical consequence: **long prompts cost real money and time.** "Just paste the whole document in" runs straight into this quadratic. It's the reason retrieval (RAG) exists — fetch the relevant 4K tokens instead of paying for 100K.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Self-attention** = uncompressed view of the whole sequence + parallel training (matrix built in one go). **Q** "what am I looking for" · **K** "what do I contain" · **V** "what do I contribute".
> Steps: **① Q·Kᵀ** (dot product = similarity) **② ÷√d_k** (stops softmax destabilising) **③ softmax → ×V** (weighted blend). Then output projection (n×d_v) → (n×d) so layers stack.
> Shapes: X n×d · W_Q,W_K d×d_k · W_V d×d_v · Q,K n×d_k · V n×d_v · **scores and weights n×n** · Z n×d_v.
> Vaswani 2017: d=512, h=8, d_k=d_v=64. Llama-3-8B: d=4096, h=32, d_k=128.
> **Cost: O(n²) in sequence length** — the reason S4 exists.

</details>

---

## 5. Multi-head attention

*Reference: "Attention Is All You Need" sec. 3.2.2; Alammar's *Illustrated Transformer*.*

**Intuition** — One attention head learns one notion of relevance. Run several in parallel with **their own K, Q, V weight matrices** and each can specialise — syntax, coreference, topic. Concatenate, project back down, and the output is the same size as the input, **so layers can be stacked**.

**The key economy** — because each head works in a *reduced* dimension d_k = d_v = d/h, **the total computational cost is similar to single-head attention at full dimensionality.** You get multiple views for roughly the price of one. That sentence is a likely exam question.

**Worked example — reproduce this by hand.** Input length N = 4, d = 512, heads A = 8, so d_k = d_v = 512/8 = **64**.

| Tensor | Shape | Why |
|---|---|---|
| Input X | **4 × 512** | 4 tokens, 512-dim embeddings |
| Projection matrices W | **512 × 64** | project d down to d_k per head |
| Q | **4 × 64** | per head |
| K | **4 × 64** | per head |
| V | **4 × 64** | per head |
| One head's output | **4 × 64** | |
| Concatenated 8 heads | **4 × (8×64) = 4 × 512** | back to model width |
| W_O | **(8×64) × 512 = 512 × 512** | output projection |
| **Final MHA output** | **4 × 512** | same shape as input → stackable |

Weight-matrix notation from the slide: W_Qi ∈ ℝ^(d×d_k), W_Ki ∈ ℝ^(d×d_k), W_Vi ∈ ℝ^(d×d_v), W_O ∈ ℝ^(h·d_v × d).

**Tradeoff** — More heads means more specialised views but a smaller dimension each, so beyond some point each head is too narrow to represent anything useful. And note what multi-head does *not* fix: the n × n matrix exists **per head**, so KV-cache memory scales with head count — which is precisely the problem MQA, GQA and MLA solve in S5.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Multi-head attention** — h parallel heads, **each with its own W_Q, W_K, W_V**; outputs **concatenated then projected by W_O** back to d, so output size = input size → **layers stack**. Each head uses **d_k = d_v = d/h**, so **total cost ≈ single-head at full dimensionality**.
> Worked: N=4, d=512, h=8 → d_k=d_v=64. X [4×512] · W [512×64] · Q,K,V [4×64] · head out [4×64] · concat [4×512] · W_O [512×512] · final [4×512].
> Doesn't fix the n² per head — hence MQA/GQA/MLA in S5.

</details>

---

## 6. The transformer block

*Reference: T2 ch3; "Attention Is All You Need" sec. 3. On pre-norm specifically, Xiong et al. 2020, "On Layer Normalization in the Transformer Architecture".*

**Intuition** — Attention alone only *mixes* information between tokens. The block adds the parts that *process* it: a feed-forward network to do computation, layer normalisation to keep training stable, and residual connections so gradients survive depth.

**Mechanism — the block, as equations.** The deck gives these twice, and they were images not text, so they are easy to miss. **Learn the two-line form; be able to expand it to the six-line form.**

Compact (pre-norm, which is what modern LLMs use):

```
O = X + MultiHeadAttention(LayerNorm(X))
H = O + FFN(LayerNorm(O))
```

Expanded step by step, with **T** marking each intermediate ([N × d]):

```
T¹ = LayerNorm(X)
T² = MultiHeadAttention(T¹)
T³ = T² + X            ← residual 1
T⁴ = LayerNorm(T³)
T⁵ = FFN(T⁴)
H  = T⁵ + T³           ← residual 2
```

```mermaid
flowchart LR
    X[X input] --> LN1["T¹ = LayerNorm(X)"]
    LN1 --> MHA["T² = MultiHeadAttention(T¹)"]
    MHA --> R1(("+"))
    X --> R1
    R1 --> T3["T³ residual 1"]
    T3 --> LN2["T⁴ = LayerNorm(T³)"]
    LN2 --> FFN["T⁵ = FFN(T⁴)"]
    FFN --> R2(("+"))
    T3 --> R2
    R2 --> H["H output, same shape as X"]
```

Three things to read off it, all examinable:

1. **Two residual connections**, one around attention and one around the FFN. `X` and `T³` both reappear as addends — that's what lets gradients reach the bottom of a deep stack.
2. **LayerNorm comes *before* each sublayer, not after** — `LayerNorm(X)` feeds attention, and the residual adds the *un*-normalised `X`. This is **pre-norm**, and it's why deep transformers train stably.
3. **H has the same shape as X**, which is what makes blocks stackable.

**The components:**

**Layer normalisation** — applied **independently to each token's hidden vector**, normalising **across the feature dimension** (not across the batch or the sequence — that's the distinction that gets examined). Has **two learnable parameters, γ and β**.

**Feed-forward network (FFNN)** — uses the contextual information created by the attention layer to capture complex relationships. A fully-connected **2-layer** network: one hidden layer, one output layer, **two weight matrices**. The hidden dimension **d_ff is larger than the model dimension d** — in the original transformer, **d = 512 and d_ff = 2048** (4×).

Notation from the slides: **X** is the input to the layer; **T** (shape [N × d]) marks the transformer computation, with superscripts demarcating each step inside the block.

**The critical architectural line** — *we use transformers to create generative models by using only decoders.* That's the bridge to section 11.

**Tradeoff** — the FFNN's 4× expansion is where most of a transformer's parameters live, not in attention. That's why quantization and pruning (S6) target it, and why Mixture-of-Experts (S3) replaces the dense FFNN with sparsely-activated ones: it's the biggest block of weights to attack.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> Transformer block = **multi-head attention + FFNN + LayerNorm + residuals**.
> **LayerNorm**: applied per token, normalising **across the feature dimension**; **two learnable params γ and β**.
> **FFNN**: fully-connected **2-layer** (one hidden, one output = two weight matrices); **d_ff > d** — original: **d=512, d_ff=2048** (4×). Uses attention's context to capture complex relationships.
> Generative models use **decoders only**. Most parameters live in the FFNN → target of quantization (S6) and MoE (S3).

</details>

---

## 7. Positional encoding

*Reference: T2 ch3; RoPE — Su et al. 2021, ["RoFormer"](https://arxiv.org/abs/2104.09864).*

**Intuition** — **Attention has no inherent sense of order.** Shuffle the tokens and the attention maths gives the same answer, because a dot product doesn't know which token came first. Position has to be *added* to the embeddings so the model can infer sequence structure.

**Three approaches:**

| Approach | How it works | Property |
|---|---|---|
| **Learned positional embeddings** | Position is a **trainable lookup** — the network discovers optimal encodings for the dataset | Fits the data; doesn't extrapolate past trained length |
| **Sinusoidal encodings** | **Fixed sine/cosine functions at multiple frequencies** | Preserves **relative distance**; no parameters |
| **RoPE** (Rotary Positional Embeddings) | Encodes position by **rotating Q and K in ℂ space** | Embeds **relative phase relationships**; **scales better for long and sliding-window contexts** |

**Tradeoff** — learned embeddings are simplest and fail hardest outside the trained length; sinusoidal costs nothing and generalises modestly; RoPE is the current default precisely because long context is the pressure point, and it's the only one of the three that rotates rather than adds. RoPE gets full treatment in S3 — this is the preview.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Attention has no inherent sense of order** → positional encoding is added to embeddings. Three kinds: **learned** (trainable lookup, dataset-optimal, poor extrapolation) · **sinusoidal** (fixed sin/cos at multiple frequencies, preserves **relative distance**, no params) · **RoPE** (rotates **Q and K in ℂ space**, encodes **relative phase**, **scales best for long / sliding-window context**). Detail in S3.

</details>

---

## 8. From text to tokens to embeddings

*Reference: R1 Raschka ch2 (working with text data) — the embedding lookup and special tokens.*

**Intuition** — A model can only do arithmetic, so text has to become numbers. Four steps, each with its own name, and the exam can ask for the order:

```mermaid
flowchart LR
    T[Raw text] --> V[Vocabulary building]
    V --> TK[Tokens]
    TK --> ID[Token IDs<br/>integers]
    ID --> EMB[Token embeddings<br/>dense vectors]
    EMB --> PLUS[+ positional embeddings]
    PLUS --> IN[Model input]
```

**Special context tokens** are added at this stage — end-of-text, unknown, padding and similar markers the model needs but the raw text doesn't contain.

**The embedding layer**, precisely as the deck describes it:

- The weight matrix starts as **small random values**.
- Those values are **optimised during LLM training as part of the LLM optimisation itself** — embeddings are *learned*, not looked up from somewhere else.
- Shape: **rows = vocabulary size, columns = embedding dimension**.

So the embedding matrix is **E ∈ ℝ^(|V| × d)** — remember this shape; section 9 reuses it.

**Special context tokens — the concrete case.** Raschka's example extends a vocabulary of `brown→0, dog→1, fox→2, …` with two extras at the end:

| Token | ID | Purpose |
|---|---|---|
| `<|unk|>` | 783 | New/unknown words not in the training data, so absent from the vocabulary |
| `<|endoftext|>` | 784 | Separates two **unrelated** text sources |

**Worked example — the embedding lookup, with numbers.** Input `fox jumps over dog` → token IDs `[2, 3, 5, 1]`. The embedding matrix is `|V| × d`; each ID selects a **row**:

```
Embedding weight matrix (|V| × 3 shown)
row 0:   0.3374  -0.1778  -0.1690
row 1:   0.9178   1.5810   1.3010
row 2:   1.2753  -0.2010  -0.1606   ← token ID 2 ("fox")
row 3:  -0.4015   0.9666  -1.1481
row 4:  -1.1589   0.3255  -0.6315
row 5:  -2.8400  -0.7849  -1.4096   ← token ID 5 ("over")
```

⚠️ **The trap Raschka calls out explicitly:** the embedding for token ID 5 is the **sixth** row, not the fifth — Python counts from 0. Easy marks lost if you index by one.

**Then positional embeddings are added elementwise**, and they have **the same dimension** as the token embeddings:

```
token embedding      [1.0, 1.0, 1.0]     (shown as 1s for simplicity)
positional embedding [1.1, 1.2, 1.3]   ← position 1
                   + ─────────────────
input embedding      [2.1, 2.2, 2.3]

position 2:  + [2.1, 2.2, 2.3]  →  [3.1, 3.2, 3.3]
position 3:  + [3.1, 3.2, 3.3]  →  [4.1, 4.2, 4.3]
```

Note it is **addition, not concatenation** — the vector doesn't grow. That's why positional information has to share capacity with semantic information, and it's the reason RoPE's rotation approach (section 7) is considered cleaner.

**Tradeoff** — vocabulary size is a direct dial on the embedding matrix's size. A bigger vocabulary means shorter sequences (good — attention is O(n²)) but a much larger embedding matrix (bad — parameters and memory). That tension is exactly what section 12's tokenizer choices are negotiating.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> Pipeline: **text → vocabulary building → tokens → token IDs → token embeddings → + positional embeddings → model input.** Special context tokens (end-of-text, unknown, padding) added here.
> **Embedding layer**: weight matrix starts as **small random values**, **optimised during LLM training itself**; **rows = vocab size, columns = embedding dim**, i.e. **E ∈ ℝ^(|V|×d)**.
> Tension: bigger vocab → shorter sequences (helps O(n²)) but bigger embedding matrix.

</details>

---

## 9. The language modelling head, and weight tying

*Reference: weight tying — Press & Wolf 2017, ["Using the Output Embedding to Tie Word Vectors"](https://arxiv.org/abs/1608.05859).*

**Intuition** — After the last transformer block you have a hidden vector per position. The **LM head** turns that vector back into a guess over the vocabulary. It's the mirror image of the embedding layer: embeddings map IDs → vectors, the LM head maps vectors → IDs.

**Mechanism**

```mermaid
flowchart LR
    W["w₁ … w_N tokens"] --> TB["Layer L<br/>transformer block"]
    TB --> H["h^L_N &nbsp; [1 × d]"]
    H --> UE["Unembedding layer<br/>U = Eᵀ &nbsp; [d × |V|]"]
    UE --> U["logits u &nbsp; [1 × |V|]"]
    U --> SM["Softmax over vocabulary V"]
    SM --> Y["word probabilities y &nbsp; [1 × |V|]"]
```

- **h_LN** = output token embedding at position N from the final block L, shape **[1 × d]**
- **Unembedding layer U = Eᵀ**, shape **[d × |V|]**
- Product → **u**, the **logit vector**, shape **[1 × |V|]** — one score per vocabulary item
- **Softmax** turns logits u into probabilities **y**, shape **[1 × |V|]**

Carry the three shapes — `[1 × d] → [d × |V|] → [1 × |V|]`. The whole head is one matrix multiply plus a softmax.

Softmax probabilities y can then be used to **assign a probability to a given text**, or to **generate text by sampling a word from them** — the two directions of section 3, now concrete.

Training vs inference differ in *which position* is used: during training **every position predicts its next token** (that's the parallelism paying off); during inference **only the last position** is used to generate. At training the logits go to cross-entropy against the next token; at inference they're sampled with **temperature, top-k or top-p** — all of S5.

**Weight tying** — the same matrix **E [|V| × d]** maps token IDs ↔ hidden vectors in both directions. Weight tying means the LM head **reuses Eᵀ** instead of learning a fresh output projection. Introduced by **Press & Wolf (2017)**; standard through GPT-2, BERT and RoBERTa.

An implementation detail worth knowing: on the input side **no matrix multiplication actually happens** — the one-hot picks out row *t* of E, an **O(1) row lookup (gather)** per token.

**Worked example — the parameter arithmetic, Llama-3-8B:**

```
|V| = 128,256    d = 4,096
E = 128,256 × 4,096 ≈ 525 M parameters

Tied:    one E                    ≈ 525 M
Untied:  E + separate lm_head     ≈ 1.05 B
         1.05 B / 8 B ≈ 13% of an 8B model
```

**Who ties in 2026** — a **size-dependent design choice**:

| | Models |
|---|---|
| **Tied** (small models) | Gemma-3 · Llama-3.2-1B/3B · Qwen3-0.6B/4B · SmolLM2 |
| **Untied** (frontier scale) | Llama-3/4 · DeepSeek-V3 · OLMo 2 · Qwen3-8B+ |

**Tradeoff / when NOT to tie** — the deck states it cleanly: untying costs ~13% of an 8B model's parameters, and **large models happily pay it for the perplexity gain**. For a 1B model that same matrix is a much larger fraction of the budget, so small models tie. The decision is *ratio of vocabulary matrix to total parameters*, not a universal best practice — which makes it a good tradeoff question.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **LM head (unembedding)**: final hidden state **h_LN [1×d]** → **logits u** → **softmax → probabilities y** over vocab. y used to score text *or* sample to generate. Training: **every position** predicts next token, cross-entropy. Inference: **last position only**, sampled with temperature / top-k / top-p.
> **Weight tying** = LM head reuses **Eᵀ** rather than a fresh projection. **Press & Wolf 2017**; standard through GPT-2, BERT, RoBERTa. Input side is an **O(1) row lookup**, not a matmul.
> Llama-3-8B: |V|=128,256, d=4,096 → E ≈ **525M**. Tied ≈525M, untied ≈**1.05B ≈ 13% of an 8B model**. **Small models tie** (Gemma-3, Llama-3.2-1B/3B, Qwen3-0.6B/4B, SmolLM2); **frontier models untie** (Llama-3/4, DeepSeek-V3, OLMo 2, Qwen3-8B+) and pay for the perplexity gain.

</details>

---

## 10. Context length

*Reference: follows from section 4's O(n²) attention cost and KV-cache growth — no single canonical text; the framing is the deck's.*

**Intuition** — The maximum number of tokens the model can process. And because generation is autoregressive, **the current context length grows as new tokens are generated** — your prompt plus everything produced so far both count against the limit.

**Tradeoff** — context length is capped not by ambition but by the O(n²) attention cost from section 4 and by KV-cache memory, which grows linearly with context and is the actual constraint in production serving (S5–S6). "Why not just use a million tokens?" is answered by memory and money, not by capability.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Context length** = maximum tokens the model can process. **Autoregressive ⇒ current context grows as tokens are generated** (prompt + generated so far). Capped by **O(n²) attention** and **KV-cache memory**, not by architecture.

</details>

---

## 11. LLM architectures

*Reference: the source papers — BERT (Devlin et al. 2018), GPT, T5 (Raffel et al. 2020); "Attention Is All You Need" for the original encoder–decoder figure.*

**Intuition** — Three shapes, distinguished by **what each token is allowed to see**. That one question determines the training objective, the strengths and the weaknesses — so learn the table by the *context* column and derive the rest.

| | **Encoder-only** (BERT, RoBERTa) | **Decoder-only** (GPT, Llama) | **Encoder-decoder** (T5, BART) |
|---|---|---|---|
| **Architecture** | Transformer encoder stacks, **bidirectional self-attention** | Transformer decoder stacks, **causal masking** blocking future tokens | Encoder → contextual representations; decoder generates via **cross-attention** |
| **Objective** | **MLM** — mask random tokens, predict from left *and* right context | **CLM** — minimise cross-entropy over next-token predictions | **Seq2seq** — translation/summarisation; T5 uses a **span-corruption** variant of MLM |
| **Context** | **Bidirectional** | **Unidirectional (left-to-right)**, preserving causal structure | Both |
| **Strengths** | Comprehension — classification, **NER**, sentiment — builds dense semantic representations | Open-ended generation, dialogue, code completion, story synthesis | Translation, summarisation, **multimodal pipelines where input and output domains differ** |
| **Weaknesses** | **Not naturally generative** — needs adapter heads or fine-tuning for sequence output | Less efficient for classification or bidirectional reasoning | **Dual stacks increase training complexity and inference latency** |

**The original Vaswani figure, which all three descend from** — worth being able to sketch:

```mermaid
flowchart BT
    IN[Inputs] --> IE[Input embedding]
    IE --> PE1((+ positional encoding))
    PE1 --> ENC["ENCODER ×N<br/>Multi-Head Attention → Add & Norm<br/>Feed Forward → Add & Norm"]
    OUT["Outputs<br/>shifted right"] --> OE[Output embedding]
    OE --> PE2((+ positional encoding))
    PE2 --> DEC["DECODER ×N<br/>MASKED Multi-Head Attention → Add & Norm<br/>Multi-Head Attention (cross) → Add & Norm<br/>Feed Forward → Add & Norm"]
    ENC -->|K, V| DEC
    DEC --> LIN[Linear]
    LIN --> SM[Softmax]
    SM --> P[Output probabilities]
```

Three details the figure encodes that the prose doesn't:

- The decoder's **first** attention is **masked** (no peeking ahead); its **second** is cross-attention taking **K and V from the encoder** and Q from the decoder. That's the only place the two stacks touch.
- Outputs are **shifted right** so position *i* predicts token *i*, never seeing it.
- **Add & Norm** appears after every sublayer — the residual-plus-normalisation pattern from section 6, repeated six times in this diagram.

And the zoom-ins, which are section 4 and section 5 in picture form: **scaled dot-product attention** = `MatMul(Q,K) → Scale → Mask (opt.) → SoftMax → MatMul(·,V)`; **multi-head attention** = `Linear ×3 (V,K,Q) → h parallel scaled-dot-product heads → Concat → Linear`.

**Worked example** — sentiment classification. BERT: one forward pass, a classification head, done — efficient because it never needed to generate. GPT: prompt it and sample a token, hoping for "positive" — general, but you burned a generation step to get a label.

**Tradeoff / why decoder-only won anyway** — encoder-only is strictly better at classification, and encoder-decoder is cleaner for translation. Decoder-only won because **section 3 holds**: if every task can be cast as next-word prediction, one architecture covers all of them, and generality beat per-task efficiency once models got large enough. Note the deck's own line from section 6 — *we use transformers to create generative models by using only decoders*. Multimodal systems (speech-text, vision-language) still extend the encoder-decoder blueprint.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> **Encoder-only** (BERT, RoBERTa): bidirectional self-attention, **MLM** objective, bidirectional context. Strong at classification/NER/sentiment; **not naturally generative**.
> **Decoder-only** (GPT, Llama): **causal masking**, **CLM** objective, unidirectional L→R. Strong at generation/dialogue/code; weak at classification.
> **Encoder-decoder** (T5, BART): encoder makes representations, decoder generates via **cross-attention**; seq2seq / **span corruption** (T5). Strong at translation, summarisation, multimodal; **dual stacks cost training complexity + inference latency**.
> Decoder-only dominates because any task can be cast as next-word prediction.

</details>

---

## 12. Tokenization

*Reference: [HuggingFace NLP course ch6](https://huggingface.co/learn/nlp-course/chapter6) (tokenizers); BPE — Sennrich et al. 2016.*

### 12.1 Why subwords

**Intuition** — the deck's framing: **common words end up in the subword vocabulary; rarer words are split into components** (sometimes intuitive, sometimes not). Worst case, a word is split into as many subwords as it has characters.

```
hat, learn          →  common words, one token each
taa##aaa##sty       →  variations
la##ern##           →  misspellings
Transformer##ify    →  novel items
```

### 12.2 Three types of token

| Type | How | Problem it solves / creates |
|---|---|---|
| **Word tokens** (e.g. word2vec) | One token per word | **Cannot handle new words** entering after the tokenizer was trained; and **many tokens with minimal differences** — apology, apologize, apologetic, apologist |
| **Subword tokens** | Break unknown words into smaller pieces already in the vocabulary | **Can represent new words**; the standard choice |
| **Byte tokens** | Vocabulary of **UTF-8 bytes (256)**; **one token = one byte** | No OOV ever; very long sequences. "Apple" → `[65][112][112][108][101]` = 5 tokens. Used by **tokenizer-free models — ByT5, CANINE** |

### 12.3 Subword algorithms

Three, all sharing the same two-part structure:

| Algorithm | Origin |
|---|---|
| **Byte-Pair Encoding (BPE)** | Sennrich et al., 2016 |
| **Unigram language modelling** | Kudo, 2018 |
| **WordPiece** | Schuster and Nakajima, 2012 |

Every one has **two parts** — this is the definitional split, and it's examinable:

1. A **token learner** — takes a raw training corpus and induces a vocabulary
2. A **token segmenter** — takes a raw test sentence and tokenizes it according to that vocabulary

The vocabulary is built **dynamically**: frequent words get their own tokens, rare words get split.

### 12.4 BPE — worked example, reproduce this by hand

The algorithm: **pre-tokenize** into words (rule-based), build a **word dictionary with frequency counts**, start from a **uni-character vocabulary**, then **merge the most frequent adjacent pair** repeatedly until the target vocabulary size is reached.

Corpus: `("hug", 10), ("pug", 5), ("pun", 12), ("bun", 4), ("hugs", 5)`

**Finding the first merge — count each adjacent pair across the whole corpus:**

| Pair | Where it appears | Total |
|---|---|---|
| **("u","g")** | hug (10) + pug (5) + hugs (5) | **20** ✅ most frequent |
| ("u","n") | pun (12) + bun (4) | 16 |
| ("h","u") | hug (10) + hugs (5) | 15 |

So `"u"` and `"g"` merge into the new token **`"ug"`**, which is added to the vocabulary.

**The iterations:**

| Iter | Vocabulary | Tokenization |
|---|---|---|
| 1 | `b, g, h, n, p, s, u` | `("h","u","g",10) ("p","u","g",5) ("p","u","n",12) ("b","u","n",4) ("h","u","g","s",5)` |
| 2 | `+ ug` | `("h","ug",10) ("p","ug",5) ("p","u","n",12) ("b","u","n",4) ("h","ug","s",5)` |
| 3 | `+ un` | `("h","ug",10) ("p","ug",5) ("p","un",12) ("b","un",4) ("h","ug","s",5)` |
| 4 | `+ hug` | `("hug",10) ("p","ug",5) ("p","un",12) ("b","un",4) ("hug","s",5)` |

⚠️ **The trap, at merge 2 (my clarity — 521 teaches this same corpus and flags it; this deck doesn't):** once `ug` exists, the pair `("h","ug")` = 15 is sitting right there and *looks* like the obvious next merge. But `("u","n")` = pun(12) + bun(4) = **16** still beats it, so **`un` merges second, not `hug`.** Re-count every adjacent pair each round — never assume the pair you just created wins the next one.

**Advantages** — efficient handling of rare words and subword units; reduces vocabulary size, making the model more efficient; better generalisation by breaking words into subword units.

**Limitations** — can produce **fragmented tokens for languages with complex morphology**; **may not capture semantic meaning** as effectively as other methods.

### 12.5 SentencePiece

**Language-independent** subword tokenizer that learns **directly from raw Unicode text** with a fixed vocabulary size — **no whitespace pre-tokenizer required**, which is what makes it language-independent.

- **Supports multiple algorithms** — BPE and unigram LM are the two used in practice
- **Preserves whitespace with `▁`** — detokenization is **lossless**: join the pieces, replace `▁` with a space
- **Byte fallback** — anything outside the vocabulary is emitted as raw UTF-8 bytes, so **no true OOV**; arbitrary Unicode works (emoji, rare scripts)

`Tokenization matters` → `▁Tokenization▁matters` → pieces.

**Unigram picks the best split** — it enumerates candidate segmentations and runs **Viterbi** to pick the most probable one under its learned piece probabilities:

```
"lowering"   chosen:    [lower, ing]
             alternate: [low, er, ing]
```

The first wins if its learned piece probabilities score higher.

### 12.6 SentencePiece vs tiktoken

The distinction, stated precisely: they differ in **what unit they merge over (characters vs bytes)** and **whether they pre-split the text (no vs regex-yes)**.

```
SentencePiece BPE (Llama-2):
  Whitespace-marked:  ▁Hello,▁world!
  Tokens:             [▁Hello, ,, ▁world, !]

tiktoken BPE (Llama-3):
  Regex chunks:       [Hello, ,,  world, !]
  Tokens:             [Hello, ,, ' world', !]    ← space is inside " world"
```

**tiktoken's byte-level + regex-pretokenized design gives better compression, no OOV, and byte-exact reversibility — which is why every frontier model released after Llama-2 uses it or something like it.**

**Who uses what in 2026:**

| Tokenizer | Vocab | Models |
|---|---|---|
| SentencePiece unigram | 32K–250K | T5, mT5 |
| SentencePiece BPE | 32K | Llama-2, Mistral-7B |
| SentencePiece BPE | 256K | Gemma-2, Gemma-3 |
| **tiktoken BPE** | 128K | Llama-3, Llama-4 |
| tiktoken (o200k) | ~200K | GPT-4o, GPT-5 |

⚠️ **Llama-3 switched from SentencePiece → tiktoken** for a better compression ratio — fewer tokens per byte of English and code.

**Tradeoff / the whole tokenizer decision in one line** — bigger vocabulary means fewer tokens per document, which means shorter sequences and cheaper O(n²) attention — but a bigger embedding matrix and more rarely-seen tokens. That's why vocabulary sizes cluster between 32K and 256K rather than at either extreme, and why compression ratio (tokens per byte) is the metric people actually optimise.

> ***In practice*** *(beyond the deck — tokenization is where your API bill comes from):*
> - **You pay per token**, in and out. Tokenization is the invisible layer that decides how many tokens a document costs. `tiktoken.encoding_for_model("gpt-4o").encode(text)` counts them before you send — do this to estimate cost and to stay under the context window.
> - **Non-English text costs more.** The same sentence in Hindi, Arabic or code can take 2–3× the tokens of English, because the tokenizer's merges were learned mostly on English. A multilingual product's cost and latency are silently worse for exactly the users who aren't in the training-data majority — a real fairness-and-cost issue you'll meet on the job.
> - **Prompt engineering is partly token engineering:** the "model selection + prompt optimisation cuts cost 10–20×" figure you'll see in 521 is mostly about tokens — fewer, cheaper tokens per call at the same quality.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> Common words → own token; rare words split into subwords; worst case one token per character.
> **Token types**: **word** (can't handle new words; apology/apologize/apologetic near-duplicates) · **subword** (represents new words; standard) · **byte** (256 UTF-8 bytes, 1 token = 1 byte, "Apple"→5 tokens, ByT5/CANINE).
> **Three subword algorithms**: **BPE** (Sennrich 2016) · **Unigram LM** (Kudo 2018) · **WordPiece** (Schuster & Nakajima 2012). All have **a token learner** (corpus → vocabulary) and **a token segmenter** (sentence → tokens).
> **BPE**: pre-tokenize → word freq dict → uni-character vocab → **merge most frequent adjacent pair** until target size. Worked: hug10/pug5/pun12/bun4/hugs5 → ("u","g")=20 beats ("u","n")=16 and ("h","u")=15 → merge **"ug"**, then "un", then "hug". **+** rare words, smaller vocab, generalisation. **−** fragments morphologically complex languages; weak on semantics.
> **SentencePiece**: language-independent, raw Unicode, **no whitespace pre-tokenizer**, `▁` marks space, **lossless** detokenization, **byte fallback = no OOV**. Unigram uses **Viterbi** over candidate segmentations.
> **tiktoken vs SentencePiece**: merges over **bytes not characters**, **regex pre-split** — better compression, no OOV, byte-exact reversibility. **Llama-3 switched SP→tiktoken.**

</details>

---

## 13. The LLM landscape

*Reference: T2 ch1 for the history; scaling laws — Kaplan et al. 2020 and Hoffmann et al. 2022 (Chinchilla).*

**Intuition** — Worth learning as a *causal chain*, not a list of names: each item made the next possible.

**Pre-neural (before 2010s)** — Shannon 1950 uses a language model to measure the **entropy of English**; then decades of **n-gram** language models for machine translation and speech recognition.

**Neural ingredients (2010s)** — each a component the transformer needed:

| Year | Contribution |
|---|---|
| 2003 | First **neural language model** — Bengio+ |
| 2014 | **Sequence-to-sequence** modelling (for MT) — Sutskever+ |
| 2014 | **Adam** optimizer — Kingma+ |
| 2014 | **Attention** mechanism (for MT) — Bahdanau+ |
| **2017** | **Transformer** architecture (for MT) — Vaswani+ |
| 2017 | **Mixture of experts** — Shazeer+ |
| 2018–19 | **Model parallelism** — Huang+, Rajbhandari+, Shoeybi+ |

Note that attention, seq2seq and the transformer all arrived **for machine translation**. None of them were built to make chatbots.

**Early foundation models (late 2010s)** — **ELMo** (pretraining with LSTMs, fine-tuning helps tasks) → **BERT** (pretraining with a Transformer) → **T5, 11B** (cast everything as text-to-text).

**Embracing scaling, becoming more closed:**

| Model | Size | Significance |
|---|---|---|
| GPT-2 | 1.5B | Fluent text, **first signs of zero-shot**, staged release |
| — | — | **Scaling laws** — hope/predictability for scaling (**Kaplan** law) |
| GPT-3 | 175B | **In-context learning**; closed |
| PaLM | 540B | Massive scale, **undertrained** |
| **Chinchilla** | 70B | **Compute-optimal scaling laws** — smaller and better, correcting PaLM |

PaLM "undertrained" followed by Chinchilla "compute-optimal" is the story of S2 in two rows: bigger stopped being automatically better.

**Open models** — EleutherAI (The Pile dataset, GPT-J) · Meta's OPT 175B (GPT-3 replication, lots of hardware issues) · HuggingFace/BigScience BLOOM (focused on data sourcing) · Meta Llama · Alibaba Qwen · DeepSeek · AI2 OLMo 2.

**Three levels of openness** — a favourite exam question because the middle case is counter-intuitive:

| Level | Example | What you get |
|---|---|---|
| **Closed** | GPT-4o | **API access only** |
| **Open-weight** | DeepSeek | **Weights available**, paper with architecture and some training details, **no data details** |
| **Open-source** | OLMo | **Weights and data available**, paper with most details — though not necessarily rationale or failed experiments |

"Open-weight ≠ open-source" is the point: you can run the model but cannot reproduce it, because the data isn't there.

**Frontier models named in the deck** — OpenAI o3 · Anthropic Claude Sonnet 3.7 · xAI Grok 3, with a more recent table listing GPT-5.4 Thinking (deep reasoning, tool use, long-horizon research), Gemini 3.1 Pro (complex problem-solving, multimodal, tool workflows), Gemma 4 (open-weight reasoning, agentic), Claude Opus 4.6 (long-context reasoning, coding, sustained agentic work), Mistral Large 3 (open-weight multimodal, **sparse MoE**), Grok 4.20 (parallel multi-agent research), DeepSeek-R1 (**RL-driven** math, logic, reasoning).

**Tradeoff / how to study this section** — this is *landscape*, not *mechanism*. Per the subject's study rule: build the comparison table, learn the causal chain and the three openness levels, and do **not** try to memorise every model and parameter count. Specific frontier model names date within months; the openness taxonomy and the Kaplan → Chinchilla correction don't.

<details>
<summary>📄 <b>Closed-book recall card</b> — fold out for exam revision</summary>

> **Closed-book card**
> Chain: **Shannon 1950 entropy → n-grams → Bengio 2003 neural LM → seq2seq / Adam / attention (all 2014, all for MT) → Transformer 2017 → MoE 2017 → model parallelism 2018–19.**
> Foundation era: **ELMo** (LSTM pretraining) → **BERT** (Transformer pretraining) → **T5 11B** (everything as text-to-text).
> Scaling: **GPT-2 1.5B** (first zero-shot signs) → **Kaplan scaling laws** → **GPT-3 175B** (in-context learning, closed) → **PaLM 540B** (massive, **undertrained**) → **Chinchilla 70B** (**compute-optimal** — smaller, better).
> Open: The Pile/GPT-J · OPT · BLOOM · Llama · Qwen · DeepSeek · OLMo 2.
> **Openness: closed = API only (GPT-4o) · open-weight = weights + architecture, no data (DeepSeek) · open-source = weights AND data (OLMo).**

</details>

---

## Extra material — ⚠️ explicitly NOT for exams

*Reference: the deck's "Extra slides (Not for exams)"; WordPiece — Schuster & Nakajima 2012; byte-level BPE — GPT-2 paper (Radford et al. 2019). Kept as Lab-1 reference.*

Kept because **Lab 1 is tokenization** and this is the reference for it. **Skip during closed-book revision.**

**Byte tokens vs BPE** — byte tokens never merge anything, so they're extremely inefficient (long sequences) but can read **any file or character**. BPE is efficient for what it knows and **"blind" to what it doesn't**. On `"Café 🚀"`: byte tokens give 10 tokens (`[67][97][102][195][169][32][240][159][154][128]` — note `é` takes two bytes and the rocket takes four); BPE gives 3, **one of which is `[UNK]` — the failure**.

**Byte-level BPE (GPT-2)** — UTF-8 encodes each Unicode character into 1–4 bytes, so a sentence is modelled as a **sequence of bytes rather than characters**. Starts with 256 bytes and learns to "glue" them into useful words. **Zero unknown words**, because it can always fall back to individual bytes. GPT-2's vocabulary is **50,257 = 256 byte tokens + 50,000 merges + 1 special end-of-text token** — worth knowing where that odd number comes from. `"Café 🚀"` → 2 tokens.

Example, `The sun is ☀️`:

| Word | Raw bytes | Token ID | Why |
|---|---|---|---|
| `The` | 54 68 65 | 464 | Very common English word, merged into one token |
| ` sun` | 20 73 75 6e | 6035 | **The space is "glued" to the word** |
| ` is` | 20 69 73 | 374 | Another space+word merge |
| ` ` | 20 | 220 | A single space before the emoji |
| `☀️` | E2 98 80 … | 99321 | **One token** — common emoji, all bytes merged into one entry |

**WordPiece** — Google's tokenizer, developed to pretrain **BERT**. Very similar to BPE in training; **the actual tokenization is done differently**.

*Token learner:* start from a small vocabulary (special tokens + initial alphabet), split words with a **`##` prefix** for non-initial pieces — `word` → `w ##o ##r ##d`. Instead of merging the most frequent pair, WordPiece **computes a score** and merges by score, **prioritising pairs whose individual parts are less frequent**:

```
score(a,b) = freq(a,b) / (freq(a) × freq(b))
```

Same corpus as BPE — `hug 10, pug 5, pun 12, bun 4, hugs 5`, split as `("h","##u","##g",10)` etc. Initial vocabulary `[b, h, p, ##g, ##n, ##s, ##u]`:

| Pair | Score | Value |
|---|---|---|
| `("##u","##g")` | 20 / (36 × 20) | **1/36** |
| `("##g","##s")` | 5 / (20 × 5) | **1/20** ✅ higher |

So the **first merge is `##gs`**, not `##ug` — the opposite of BPE's answer on the same corpus, which is exactly the point of the example.

*Token segmenter:* pre-tokenize, split, then for each word **find the biggest subword starting at the beginning**, split it off, and repeat on the remainder. With final vocabulary `[b, h, p, ##g, ##n, ##s, ##u, ##gs, hu, hug]`, the test word `hugs` tokenizes as **`["hug", "##s"]`**.

*Advantages* — efficient handling of rare words, reduced vocabulary size, better generalisation. *Limitations* — the scoring mechanism **adds complexity** over BPE; still fragments morphologically complex languages. WordPiece's **likelihood-based scoring** distinguishes it from BPE's **frequency-based** approach, often producing a vocabulary that better captures linguistic structure.

---

## Lab / build

**536 Lab 1 is at session 1 (module M1): construct and analyse tokenization techniques.** Everything you need is in section 12 plus the extra material.

Minimum useful version, ~15 lines:

```python
from transformers import AutoTokenizer

for name in ["gpt2", "meta-llama/Llama-2-7b-hf", "meta-llama/Meta-Llama-3-8B"]:
    tok = AutoTokenizer.from_pretrained(name)
    for text in ["Tokenization matters", "Café 🚀", "Transformerify", "The sun is ☀️"]:
        ids = tok.encode(text)
        print(f"{name:35} {text:20} {len(ids):3} tokens  {tok.convert_ids_to_tokens(ids)}")
```

That single script makes concrete: SentencePiece vs tiktoken (section 12.6), why Llama-3 switched, byte fallback on the emoji, and subword splitting on the novel word. **Run it before session 2** — the compression-ratio argument only lands once you've seen the token counts differ.

---

## 🎓 Exam layer & course logistics

*For passing the course, not for building knowledge — folded here so the note reads as a knowledge base first. Open it when the exam is close.*

<details>
<summary><b>Exam scope, weights, evaluation & confusions</b> — fold out</summary>

**The handout is superseded.** The instructor confirmed in class, repeatedly:

> *"I'm repeating — there are **no quizzes** for this course."*
> *"EC2 will be closed book 30 marks and EC3 will be 35 marks."*

So **EC-1 = 35%, two group assignments** (plan shared ~week 2); **EC-2 mid-sem = 30%, closed book**, scope sessions **1–8** (S8 is revision, so ~7 sessions of new content); **EC-3 comprehensive = 35%, open book**, all sessions. The handout's "Quiz 5% + Assignment 30%" split never applied.

**Assignment design (from the recording):**
- **Group work** — you form your own groups; Ops creates a placeholder.
- **Assignments 1 and 2 combine into one end-to-end project** — plan them together.
- Each has **two problem statements** + **5–6 enterprise case-study options**; you choose.
- Everything assigned **is taught first**. Lab sheets are notebooks with **80–90% of the code already written**.

🔴 **The remote lab is mandatory for assignments** — *"in laptop, no."* Manual to be shared; expect slowdowns near deadlines. Colab handles only very small models. *Study-plan consequence:* two group assignments, not one solo 30% piece — lighter per person, but with coordination overhead.

**References (slide 60):** T1 Jurafsky & Martin (3rd ed. draft, Jan 2026) ch2/7/8 · T2 Alammar ch1/2/3 · R1 Raschka ch1/2 · HuggingFace LLM course ch6.5 · paper *Neural Machine Translation with Byte-Level Subwords*.

### Confusions to resolve

- [x] ~~Is the quiz replaced by assignments?~~ ✅ no quizzes; 35% two group assignments; remote lab mandatory.
- [ ] Which two problem statements, and which enterprise case studies? (~week 2)
- [ ] Remote lab access — manual not yet shared.
- [ ] Does the deck's `MultiplyResponse`-style sloppiness appear elsewhere — check slide 21's arithmetic.
- [ ] Slide 41 is blank in the export — check whether something was on it.

</details>
