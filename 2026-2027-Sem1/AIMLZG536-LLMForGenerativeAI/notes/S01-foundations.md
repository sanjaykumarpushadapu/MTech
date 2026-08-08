# Large Language Models for Generative AI · Session 01 · Foundations of Large Language Models (LLMs)

_Learned 26 Jul 2026_

## Why this matters

This session is the foundation for everything that follows in 536. Modern LLMs can look mysterious from the outside, but under the hood they are doing a small number of very specific things: turning text into tokens, turning tokens into vectors, mixing those vectors with attention, and predicting one next token at a time. Once that picture is clear, terms like _attention_, _embeddings_, _context window_, _tokenization_, and _decoder-only_ stop sounding like jargon and start feeling like engineering choices you can reason about.

By the end of this note, you should be able to explain six things comfortably in your own words: what LLMs and generative AI are, how attention and the transformer block work, what the building blocks of an LLM are, how the main architecture families differ, how tokenization works, and how today's LLM landscape is organized.

**Running example throughout:** **Llama-3 8B** (d = 4096, 32 heads, d_k = 128). Anchor every new number to it.

## Session map — one forward pass

Use this picture as the backbone of the whole session. Every decoder-only LLM runs some version of this loop:

![Decoder-only LLM forward pass loop](assets/S01-forward-pass-loop.svg)

One pass over the prompt produces **one** probability distribution over the next token. Then the chosen token is appended, the model runs again, and the cycle repeats. That repeated loop is what "autoregressive generation" means. Keep this picture in mind while reading: every section below explains one part of this loop. The **context length** (section 11) is the size limit on the `token IDs` list, and the **O(n²)** cost comes from attention inside the transformer block.

The clean storyline is:

| Stage                   | Plain-English job                                                     | Main failure if weak                                             |
| ----------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Text → tokens           | Decide what pieces of text the model can see                          | Bad tokenization wastes context, money, and multilingual quality |
| Tokens → vectors        | Give each token a learned numeric representation plus position        | The model cannot compute over raw text or word order             |
| Transformer blocks      | Repeatedly mix contextual information and transform each token vector | The model sees words but cannot use surrounding context well     |
| LM head → probabilities | Score every vocabulary item as the next token                         | The model has hidden states but no way to choose output text     |
| Decode → append         | Pick one token, add it to the context, and repeat                     | No long answer can be generated from a single prediction         |

---

## Part 1 · Introduction to LLMs and Generative AI

_Start here: what "language model" and "large" mean, and the one idea the rest of the note builds on. A model trained to predict the next word can generate a whole passage simply by repeating that prediction and feeding each new word back in as input._

### 1. Introduction to LLMs and Generative AI

**Intuition** — **Language AI** is the broad umbrella: systems that take unstructured text and do something useful with it. A **language model** is the generative branch of that umbrella. At its core, it answers one question: _given what came before, what should come next?_ Almost everything else in this course is built on that one idea.

_One input type, three different output types — this course mostly follows the generative branch, but the same text backbone can support the other two:_

![Language AI input and output tasks](assets/S01-language-ai.svg)

So language AI does not automatically mean "chatbot". The input is text, but the output may be **new text** (`write the answer`), an **embedding vector** (`represent this paragraph for retrieval`), or a **class label** (`is this review positive or negative?`). The same transformer backbone can support all three. What changes is the task-specific head on top. That is why section 10 matters: change the head, and the same model body can behave like a generator, an embedder, or a classifier.

Three vocabulary words keep the taxonomy clean:

| Term    | Meaning in this session                                                         |
| ------- | ------------------------------------------------------------------------------- |
| **NLP** | The broad field: computational systems that process human language              |
| **NLU** | Understanding-oriented tasks: classification, extraction, retrieval, entailment |
| **NLG** | Generation-oriented tasks: writing text, code, summaries, answers, dialogue     |

An LLM is usually a **foundation model**: a broadly pre-trained model that can be adapted to many downstream tasks through prompting, retrieval, fine-tuning, or tool use. "Foundation" does not mean "always correct"; it means many task-specific systems can be built on the same base model.

**Mechanism** — formally, a language model computes either:

- the probability of a sentence, **P(W)**, or
- the probability of an upcoming word, **P(wₙ | w₁, w₂, …, wₙ₋₁)**

Equivalently: it assigns a probability to each possible next word — **a probability distribution over the vocabulary**.

That is the core definition in three moves: **score whole sequences, score next tokens, and turn those scores into a probability distribution over the vocabulary.**

**Worked example — word order is the whole signal:**

```
P(all of a sudden I notice three guys standing on the sidewalk)
    >
P(on guys all I of notice sidewalk three a sudden standing the)
```

Same words, different order. A language model that has learned English assigns far more probability to the first. That's the entire signal — no grammar rules were written down; word order emerged from counting.

**Use case — one backbone, three products.** A bank could use the same text backbone three ways: generate a reply to a complaint, embed policy paragraphs for search, and classify whether a message is a fraud report. The body of the model learns language patterns; the output head and surrounding product design decide which task it performs.

**Tradeoff / what this framing costs** — Defining a model purely by next-word probability means there is **no notion of truth in the objective**. A fluent falsehood scores well; that's not a bug in the training, it's what the objective asked for. Hallucination is downstream of this definition, which is why S14 needs separate faithfulness metrics.

---

### 2. What makes a language model "large"

**Intuition** — "Large" does not mean just one thing. In practice it usually points to three different kinds of scale:

1. **Model size** — number of parameters
2. **Dataset size** — trained on massive text, "large portions of the entire publicly available text on the internet"
3. **Context** — a larger context of words

An LLM is therefore "large" not just because it has many weights, but because it was trained on a lot of data and is often used with a long context.

**Mechanism — the three axes work together.** Parameters decide how much the model can store and how much computation happens inside each layer. Training data provides the statistical signal the model learns from. Compute is the budget that turns that data into learned parameters. Context length is the runtime side of the same story: the model can condition on more tokens, but every extra token makes attention more expensive and increases the memory needed to store past tokens' key/value vectors, called the **KV-cache**. Later sessions treat that as a real serving constraint rather than a theory detail.

_The three axes, and what each actually charges you:_

![Three axes that make a language model large](assets/S01-large-model-axes.svg)

**The useful way to read this table is from the cost side.** Training data and training compute are mostly one-time costs. Parameters keep costing you every time the model runs. That asymmetry is why later serving and compression work focuses so heavily on parameter count.

**Worked example** — A 7B model and a 70B model may be trained once, but the 70B model costs roughly ten times as many parameter values to load for every request. If both serve 1M prompts per day, the larger model keeps charging memory and latency on every prompt. A larger training set does not charge per request in the same way; it was paid for during training.

**Use case — choosing a model for a support assistant.** A bank may prefer a 7B open-weight model for routine support tickets because it fits on cheaper GPUs and responds faster under peak load. A 70B model may answer harder questions better, but if most requests are password-reset or card-status queries, the larger model spends money on capacity the product does not need. "Large" is therefore a deployment decision, not just a leaderboard number.

**Tradeoff** — all three scale cost. Parameters cost memory and inference compute; data costs collection, cleaning and training time; context costs attention compute that grows **quadratically** with sequence length (section 4). Each of the three has its own optimisation topic later: quantization for parameters (S6), scaling laws for data (S2), and efficient attention for context (S4).

---

### 3. Generation as prediction

**Intuition** — This is the key idea of the whole session: **a model that can predict text can also generate text, simply by sampling from the distribution it predicts.** Predicting the next word and generating a whole paragraph are the same computation repeated many times. Each new output token is fed back in as part of the next input.

A model used this way is an **autoregressive language model** — each generated token is fed back in to predict the next.

![Autoregressive generation loop](assets/S01-autoregressive-generation.svg)

**Mechanism — first the probability rule, then the generation loop.** A language model scores a whole sequence by breaking it into next-token predictions:

```
P(w₁ … w_n) = ∏  P(w_i | w₁ … w_{i−1})
              i=1..n
```

Generation simply runs that same idea forward. Four steps repeat until the model reaches a stop condition:

| Step | What happens                                                                            | Shape              |
| ---- | --------------------------------------------------------------------------------------- | ------------------ |
| 1    | Feed the context through the model → **logits**, one raw score per vocabulary entry     | `[1 × \|V\|]`      |
| 2    | **softmax** turns logits into a probability distribution: `p_i = e^{z_i} / Σ_j e^{z_j}` | `[1 × \|V\|]`      |
| 3    | **Select** a token — `argmax` (greedy) or sample from `p`                               | one ID             |
| 4    | **Append** it to the context and return to step 1                                       | context grows by 1 |

_What softmax actually does, in plain language:_ it takes raw scores, which can be positive or negative and do not yet mean anything probabilistic, and turns them into positive numbers that add up to 1. In other words, it converts "preferences" into probabilities. Higher scores become much more likely, lower scores shrink, and the whole vector becomes something you can sample from.

The loop stops when the model emits an end-of-sequence token or hits a length cap. Step 3 is the only place randomness enters. That is why the _same_ model can give different answers on different runs, and why `temperature=0` makes decoding deterministic.

**Worked example — generate two tokens by hand.** Vocabulary of five: `the, cat, sat, mat, <eos>`. Prompt: `"The"`.

_Step 1 — the model emits logits, softmax converts them:_

| Token   | logit z | e^z        | p = e^z / 13.345 |
| ------- | ------- | ---------- | ---------------- |
| the     | 2.0     | 7.389      | **0.554**        |
| cat     | 1.0     | 2.718      | **0.204**        |
| sat     | 0.5     | 1.649      | 0.124            |
| mat     | 0.2     | 1.221      | 0.092            |
| `<eos>` | −1.0    | 0.368      | 0.028            |
|         |         | Σ = 13.345 | Σ = 1.000        |

Greedy decoding would pick `the` (0.554) and loop forever. **Sampling** picks `cat` often enough that the sentence goes somewhere — the first concrete reason decoding strategy matters, which is the whole of S5.

Say we sample **`cat`**. Context is now `"The cat"`.

_Step 2 — feed the longer context back in:_

| Token   | p         |
| ------- | --------- |
| the     | 0.064     |
| cat     | 0.078     |
| **sat** | **0.702** |
| mat     | 0.086     |
| `<eos>` | 0.070     |

The distribution **sharpened**: `cat` was sampled off a fairly flat first distribution (its own probability was only 0.204, well behind `the`'s 0.554), but once `"The cat"` is the context, the new top prediction `sat` is a clear front-runner at 0.702. More context means less uncertainty. That is the entire mechanism behind "prompting works": you are not instructing the model, you are conditioning the distribution.

⚠️ **The important reframe:** nothing in these two steps explicitly knows what a sentence _is_. There is no hidden grammar module and no separate planning engine here. Fluency appears because the next-token probabilities become good enough that locally sensible choices add up to globally fluent text.

**The consequence that makes LLMs general** — _almost any NLP task can be modelled as word prediction._ Two examples:

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

**Tradeoff / when NOT to reframe a task as generation** — You _can_ express classification as generation, and it's often worse: a fine-tuned classifier is smaller, faster, cheaper and gives calibrated probabilities, where an LLM gives you a token that happens to read "positive". Reframing buys generality and zero-shot capability; it costs efficiency and calibration.

**Checkpoint — what Part 1 established.** An LLM is not magic conversation software. It is a large neural language model that turns context into a next-token probability distribution. Generative AI appears because the model repeats that one operation: predict, choose, append, predict again.

---

## Part 2 · Attention Mechanism & Transformer (Review)

_This part opens the black box. Up to now the note has treated the LLM as "something that predicts the next token." Here we look inside that something: attention, multi-head attention, the transformer block, and positional encoding. The goal is not to memorize equations first. The goal is to understand what problem each piece is solving, then use the equations to make that picture precise._

The problem Part 2 solves: after tokenization, the model has a row of vectors, one per token. Those vectors still need three things:

| Need                                                      | Mechanism                                           |
| --------------------------------------------------------- | --------------------------------------------------- |
| Each token must use surrounding tokens                    | self-attention                                      |
| The model must learn several relationship types at once   | multi-head attention                                |
| The network must become deep without becoming untrainable | transformer blocks with residuals and normalisation |
| Word order must be represented                            | positional encoding                                 |

### 4. Self-attention

**Intuition** — Self-attention lets each token look back at the other tokens and decide which ones matter right now. That is the real shift from older sequence models: the model does not have to squeeze the whole past into one hidden state and hope nothing important is lost. Every earlier position stays available, and the current token can decide whom to listen to.

In practice, self-attention builds a table of relevance scores between tokens. During training, that whole table is computed in one shot, which is why transformers train in parallel much more easily than RNN-style models.

![Self-attention matrix](assets/S01-self-attention-matrix.svg)

**Mechanism — the three vectors.** Every token produces three projections, and each one plays a distinct role:

|       | Name  | The question it asks                                                                     |
| ----- | ----- | ---------------------------------------------------------------------------------------- |
| **Q** | Query | _"What am I looking for?"_ — the current token asking a question of every previous token |
| **K** | Key   | _"What do I contain?"_ — each past token advertising its relevance to the query          |
| **V** | Value | _"What do I contribute?"_ — the actual content pulled in once relevance is decided       |

If you remember only one sentence before the arithmetic starts, remember this one: **Q asks, K advertises, V supplies the content.**

_An everyday analogy for Q, K, V — hold this and the maths below is just the analogy with numbers:_ imagine you post a question in a group chat. Your **query** is what you're looking for. Every earlier message carries a **key** — a little label advertising what that message is about — and a **value** — its actual content. You mentally compare your query against each key to judge relevance, then you pull in the values of the relevant messages, paying most attention to the most relevant. Self-attention does exactly this, except "compare" is a dot product and "pay attention in proportion" is a softmax.

![Q, K, V attention worked step](assets/S01-qkv-attention.svg)

**The computation, in three steps:**

1. **Q · Kᵀ** — dot product: how similar is the query to each key? Higher = more relevant.
2. **÷ √d_k** — scaling: keeps scores from blowing up and destabilising the softmax. _Plain-language first:_ longer vectors naturally produce larger dot products, simply because you are summing more little products. If you feed those oversized scores straight into softmax, it becomes too peaky too early: one token gets almost all the probability, the rest get almost none, and learning becomes unstable. Dividing by `√d_k` shrinks the scores back to a sensible size so softmax stays responsive. The reason the divisor is `√d_k` rather than `d_k` is that a dot product's **variance** grows roughly like `d_k`, so its typical size grows like `√d_k`; dividing by `√d_k` cancels exactly that inflation.
3. **softmax → × V** — blend the values by how much attention each token deserves.

The same computation, written as a pipeline:

```
MatMul(Q, Kᵀ) → Scale (÷√d_k) → Mask (optional) → SoftMax → MatMul(·, V)
```

The **Mask** step is optional in the general figure and **mandatory in a decoder** — it's what enforces causality (section 12).

Then an **output projection** maps the result from (n × d_v) back to (n × d), the model dimension, so layers can stack.

**Worked example — the shapes, which you must be able to write from memory.** Notation: **n** sequence length · **d** model/embedding dim · **d_k** key/query dim · **d_v** value dim · **h** heads.

| Tensor           | Shape     |
| ---------------- | --------- |
| X                | n × d     |
| W_Q, W_K         | d × d_k   |
| W_V              | d × d_v   |
| Q, K             | n × d_k   |
| V                | n × d_v   |
| QKᵀ ÷ √d_k       | **n × n** |
| A = softmax(...) | **n × n** |
| Z = A · V        | n × d_v   |

| Model                | d    | h   | d_k = d_v |
| -------------------- | ---- | --- | --------- |
| Original transformer | 512  | 8   | 64        |
| Llama-3-8B           | 4096 | 32  | 128       |

> **First pass? Skim the arithmetic and keep one sentence.** Each token's new vector is a weighted average of other tokens' value vectors, and the model learned the weights. The rest of the worked example just makes that sentence concrete.

**Worked example — attention by hand, with actual numbers** _(you don't_ have _attention until you've pushed real numbers through it)._ Two tokens, `d = d_k = d_v = 2`, and take `W_Q = W_K = W_V = I` so `Q = K = V = X` (keeps the arithmetic visible). Tokens: `x₁ = [1, 0]`, `x₂ = [1, 1]`.

**① Scores `QKᵀ`** — every query dotted with every key:

|           | K(x₁)           | K(x₂)           |
| --------- | --------------- | --------------- |
| **Q(x₁)** | 1·1+0·0 = **1** | 1·1+0·1 = **1** |
| **Q(x₂)** | 1·1+1·0 = **1** | 1·1+1·1 = **2** |

**② Scale `÷√d_k = ÷√2`** → x₂'s row becomes `[0.71, 1.41]`.

**③ Causal mask** (decoder — a token cannot see the future): x₁'s score against x₂ is set to `−∞`, so x₁ may attend only to itself.

**④ Softmax each row → attention weights** (a probability distribution over the allowed tokens):

|        | on x₁    | on x₂      |
| ------ | -------- | ---------- |
| **x₁** | **1.00** | — (masked) |
| **x₂** | **0.33** | **0.67**   |

_(x₂'s row: `e^0.71 / (e^0.71 + e^1.41) = 2.03 / 6.14 = 0.33`; the rest is 0.67.)_

**⑤ Weighted sum `Z = A·V`:**

- `z₁ = 1.00·[1,0] = ` **`[1, 0]`** — with the mask, token 1's new vector is just itself.
- `z₂ = 0.33·[1,0] + 0.67·[1,1] = ` **`[1, 0.67]`** — a blend, leaning 67% on itself and 33% on token 1.

That last line is the heart of attention: each token's output becomes a weighted average of other tokens' value vectors, and the weights come from learned relevance. Notice that the weight table is `2 × 2` here. In a real sequence it becomes `n × n`, which is exactly where the cost problem comes from.

**Tradeoff / the cost that defines the field** — the attention matrix is **n × n**. Double the context and you quadruple the attention compute and memory. Every efficiency topic in S4 — FlashAttention, Ring Attention, sliding-window, sparse and linear attention — exists to attack that single quadratic term. Self-attention buys an uncompressed view and parallel training; it charges O(n²).

> **_In practice_** _— what this O(n²) means when you actually use LLMs:_
>
> - You **never implement attention yourself** in a real job — you call an optimised kernel (**FlashAttention**) inside a serving stack (**vLLM**, **TGI**, TensorRT-LLM). Knowing the maths is what lets you reason about _why_ a 100K-token prompt is slow and expensive, not code the softmax.
> - At **inference** the trick that makes generation fast is the **KV-cache**: keys and values for past tokens are cached so each new token is O(n) not O(n²). This is why the _first_ token of a long prompt is slow ("prefill") and later tokens are fast ("decode") — a distinction you'll meet the moment you look at latency metrics.
> - Practical consequence: **long prompts cost real money and time.** "Just paste the whole document in" runs straight into this quadratic. It's the reason retrieval (RAG) exists — fetch the relevant 4K tokens instead of paying for 100K.

**Tools to try — watch this section run instead of just reading it:**

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (Georgia Tech Polo Club) — type any sentence and watch a real GPT-2 run on it live: tokenization → embeddings → each attention head lighting up → softmax into next-token probabilities.
- [Transformer & Attention Visualizer](https://ai.williamtheisen.com/transformer.html) — toggle BERT / GPT-2 / the original encoder-decoder, expand a layer, and see the actual Q, K, V projections and the attention heatmap for the worked example above. Also makes the encoder-vs-decoder masking difference (section 12) visible side by side.

---

### 5. Multi-head attention

**Intuition** — One attention head gives one view of the sequence. Multi-head attention says: do not trust one view to capture everything. Let several heads look at the same tokens in parallel, each with its own learned projections, so different heads can specialize in different patterns such as syntax, reference, or local phrase structure.

**Mechanism — four steps.** For h heads on an input `X [N × d]`:

| Step                | Operation                                                                                             | Result                   |
| ------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------ |
| 1 · **Project**     | For each head i, compute `Q_i = X·W_Qi`, `K_i = X·W_Ki`, `V_i = X·W_Vi`, where each `W ∈ ℝ^{d × d_k}` | h sets of `[N × d_k]`    |
| 2 · **Attend**      | Run the section-4 computation independently in each head: `softmax(Q_iK_iᵀ / √d_k)·V_i`               | h outputs of `[N × d_k]` |
| 3 · **Concatenate** | Stack the h head outputs side by side along the feature axis                                          | `[N × h·d_k] = [N × d]`  |
| 4 · **Project out** | One final multiply by `W_O ∈ ℝ^{h·d_v × d}` to mix what the heads found                               | `[N × d]`                |

Step 4 is the part people often skip mentally. Without `W_O`, the heads would simply sit side by side without being combined. `W_O` is what mixes their findings back into one shared representation.

**The key economy** — each head works in a reduced dimension, usually `d_k = d_v = d/h`, so the total cost stays in the same ballpark as one full-width head. In plain terms: you get multiple perspectives without paying for multiple full-sized attention layers.

![Multi-head attention layer](assets/S01-multihead-attention.svg)

**Worked example — reproduce this by hand.** Input length N = 4, d = 512, heads h = 8, so d_k = d_v = 512/8 = **64**.

| Tensor                | Shape                        | Why                             |
| --------------------- | ---------------------------- | ------------------------------- |
| Input X               | **4 × 512**                  | 4 tokens, 512-dim embeddings    |
| Projection matrices W | **512 × 64**                 | project d down to d_k per head  |
| Q                     | **4 × 64**                   | per head                        |
| K                     | **4 × 64**                   | per head                        |
| V                     | **4 × 64**                   | per head                        |
| One head's output     | **4 × 64**                   |                                 |
| Concatenated 8 heads  | **4 × (8×64) = 4 × 512**     | back to model width             |
| W_O                   | **(8×64) × 512 = 512 × 512** | output projection               |
| **Final MHA output**  | **4 × 512**                  | same shape as input → stackable |

Weight-matrix notation: W_Qi ∈ ℝ^(d×d_k), W_Ki ∈ ℝ^(d×d_k), W_Vi ∈ ℝ^(d×d_v), W_O ∈ ℝ^(h·d_v × d).

Each head runs the exact same computation from section 4, just in 64 dimensions instead of 512 — that's why h heads cost about the same as one full-width head.

**Use case — why one head isn't enough.** Take "The trophy didn't fit in the suitcase because it was too big." Resolving "it" needs a head that attends back to "trophy" (coreference); scoring how plausible the sentence is needs a head that attends to "because" and tracks clause structure (syntax). A single attention head has to average both signals into one weighted sum, blurring each. Llama-3-8B gives every layer 32 heads precisely so different heads can specialise — one tracking coreference, another local syntax — instead of one head doing a mediocre job of both.

**Tradeoff** — More heads means more specialised views but a smaller dimension each, so beyond some point each head is too narrow to represent anything useful. And note what multi-head does _not_ fix: the n × n matrix exists **per head**, so KV-cache memory scales with head count — which is precisely the problem MQA, GQA and MLA solve in S5.

---

### 6. The transformer block

**Intuition** — Attention is only one part of the job. It tells each token where to look, but it does not by itself give the model enough depth or stability to learn rich transformations. The transformer block adds the supporting machinery: a feed-forward network to process each token, layer normalization to keep values well-behaved, and residual connections to keep deep stacks trainable.

> **What "gradients survive depth" means** — training a network works by measuring how much each weight contributed to the error, then nudging it slightly (this signal is the _gradient_). That signal has to flow backward through every layer it passed through. Each extra layer it crosses shrinks it a bit more (repeated multiplication by small numbers), so in a very deep stack the earliest layers can end up receiving a gradient close to zero — they effectively stop learning. This is the **vanishing gradient problem**, and it's the actual failure residual connections are fixing, not just a vague "training gets harder."

_Two everyday analogies for the two supporting parts:_

- **Residual connection** = a **highway with exits**. The `X +` keeps a straight through-lane running past each sublayer; a token can _take the exit_ to be processed by attention or the FFN, but the through-lane always continues. So even in a 100-layer stack the original signal (and, during training, the gradient) never has to squeeze through every single exit — it always has a clear road home. That's why very deep transformers train at all.
- **Layer normalisation** = **grading on a curve, per token**. Before each sublayer, it rescales one token's vector so its numbers sit in a consistent range (mean 0, unit spread), stopping values from drifting to extremes as they pass through many layers. `γ` and `β` then let the model stretch and shift that curve if it wants.

**Mechanism — the block, as equations.** These are the lines worth learning because they show the whole block compactly:

![Transformer decoder block](assets/S01-transformer-block.svg)

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

Three practical things to notice from the equations and the diagram:

1. **Two residual connections**, one around attention and one around the FFN. `X` and `T³` both reappear as addends — that's what lets gradients reach the bottom of a deep stack.
2. **LayerNorm comes _before_ each sublayer, not after** — `LayerNorm(X)` feeds attention, and the residual adds the _un_-normalised `X`. This is **pre-norm**, and it's why deep transformers train stably.
3. **H has the same shape as X**, which is what makes blocks stackable.

**Worked example — one token through the block.** Take `d = 4`, `d_ff = 16`, and follow a single token's vector. The point is not the numbers themselves. The point is to see how the same vector is repeatedly normalized, transformed, and reconnected to its original path.

Suppose the token's incoming vector is `X = [2, 4, 4, 6]`.

_T¹ = LayerNorm(X)_ — normalise **across the 4 features of this one token**:

```
mean μ = (2+4+4+6)/4                = 4.0
var  σ² = ((−2)²+0²+0²+2²)/4        = 2.0
std  σ  = √2                        ≈ 1.414

T¹ = (X − μ)/σ = [−1.414, 0, 0, +1.414]
```

(then scaled by the learnable `γ` and shifted by `β`, both `[1 × 4]`, initialised to 1 and 0)

_The rest of the block, by shape:_

| Step | Operation                                             | Shape     | Note                                                    |
| ---- | ----------------------------------------------------- | --------- | ------------------------------------------------------- |
| T¹   | LayerNorm(X)                                          | `[1 × 4]` | computed above                                          |
| T²   | MultiHeadAttention(T¹)                                | `[1 × 4]` | mixes across tokens — the only step that looks sideways |
| T³   | T² **+ X**                                            | `[1 × 4]` | residual adds the **un-normalised** input               |
| T⁴   | LayerNorm(T³)                                         | `[1 × 4]` |                                                         |
| T⁵   | FFN(T⁴): `[1×4]·[4×16] → [1×16]` then `[1×16]·[16×4]` | `[1 × 4]` | **expand 4× then contract**                             |
| H    | T⁵ **+ T³**                                           | `[1 × 4]` | residual 2 — same shape as X ✅                         |

**Two things to notice, both examinable:**

1. **The residual adds `X`, not `T¹`.** If it added the normalised version, the block would have no clean gradient path back to the original input — that's the whole point of pre-norm.
2. **Only step T² looks at other tokens.** LayerNorm is per-token, the FFN is per-token. A transformer block is _one_ mixing operation wrapped in a lot of per-token processing — which is why the FFN can be sharded across devices trivially and attention cannot.

**Use case — training a deep decoder.** A 32-layer Llama-style model cannot just stack attention operations and hope depth will work automatically. Without residual paths and normalization, early layers become hard to train and the extra depth mostly buys instability. The transformer block is the pattern that turns "many layers" into something trainable and useful.

**Parameter count for this toy block:** attention `4 × (4×4) = 64` (W_Q, W_K, W_V, W_O) · FFN `4×16 + 16×4 = 128` · LayerNorm `2 × 2 × 4 = 16`. **The FFN is 2× the attention** — at real scale it stays roughly 2:1, which is the arithmetic behind the tradeoff below.

**The components:**

**Layer normalisation** — applied **independently to each token's hidden vector**, normalising **across the feature dimension** (not across the batch or the sequence — that's the distinction that gets examined). Has **two learnable parameters, γ and β**.

**Feed-forward network (FFN)** — uses the contextual information created by the attention layer to capture complex relationships. A fully-connected **2-layer** network: one hidden layer, one output layer, **two weight matrices**. The hidden dimension **d_ff is larger than the model dimension d** — in the original transformer, **d = 512 and d_ff = 2048** (4×).

**The critical architectural line** — _we use transformers to create generative models by using only decoders._ That's the bridge to section 12.

**Tradeoff** — the FFN's 4× expansion is where most of a transformer's parameters live, not in attention. That's why quantization and pruning (S6) target it, and why Mixture-of-Experts (S3) replaces the dense FFN with sparsely-activated ones: it's the biggest block of weights to attack.

---

### 7. Positional encoding

**Intuition** — Attention, by itself, has no built-in notion of before and after. If we gave it token vectors without position information, it could compare tokens but not know their order. Positional encoding fixes that by injecting sequence order into the vectors before attention starts working on them.

**Use case — what breaks without it.** "Alice called Bob" and "Bob called Alice" are the same three tokens in a different order. Section 4's attention scores relevance with dot products between token vectors, and a dot product between the same set of vectors doesn't change just because you feed them in a different order — so without positional information, both sentences would produce identical attention outputs, and the model could not tell who called whom. Adding a position-dependent vector to each token embedding is what breaks that symmetry.

**Three approaches:**

| Approach                                | How it works                                                                                 | Property                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Learned positional embeddings**       | Position is a **trainable lookup** — the network discovers optimal encodings for the dataset | Fits the data; doesn't extrapolate past trained length                                          |
| **Sinusoidal encodings**                | **Fixed sine/cosine functions at multiple frequencies**                                      | Preserves **relative distance**; no parameters                                                  |
| **RoPE** (Rotary Positional Embeddings) | Encodes position by **rotating Q and K in ℂ space**                                          | Embeds **relative phase relationships**; **scales better for long and sliding-window contexts** |

**Mechanism — the sinusoidal formula.** For position `pos` and dimension index `i`:

```
PE(pos, 2i)   = sin( pos / 10000^(2i/d) )     ← even dimensions
PE(pos, 2i+1) = cos( pos / 10000^(2i/d) )     ← odd dimensions
```

Read the denominator as a **wavelength dial**. At `i = 0` it is `10000⁰ = 1`, so the sine completes a cycle every ~6 positions. As `i` climbs toward `d/2` the denominator grows to 10000, so the wave stretches until it barely moves across the whole sequence. The vector at each position is therefore a stack of clock hands turning at geometrically-spaced speeds.

The result is **added elementwise** to the token embedding — position is not concatenated, it is summed into the same `d` dimensions the meaning lives in.

**Worked example — compute it by hand.** With `d = 4` there are two frequency bands:

```
i = 0  →  10000^(0/4)  = 1        → fast:  sin(pos/1),   cos(pos/1)
i = 1  →  10000^(2/4)  = 100      → slow:  sin(pos/100), cos(pos/100)
```

`PE(pos, 0..3)`:

| pos | dim0 = sin(pos·1) | dim1 = cos(pos·1) | dim2 = sin(pos·0.01) | dim3 = cos(pos·0.01) |
| --- | ----------------- | ----------------- | -------------------- | -------------------- |
| 0   | 0.00              | 1.00              | 0.00                 | 1.00                 |
| 1   | 0.84              | 0.54              | 0.01                 | 1.00                 |
| 2   | 0.91              | −0.42             | 0.02                 | 1.00                 |

**Read the table column-wise** — the **low dimensions swing fast** (dim0: 0 → 0.84 → 0.91) while the **high dimensions barely move** (dim2 crawls 0 → 0.01 → 0.02). Picture a bank of clock hands turning at different speeds: the seconds hand (dim0) races round while the hour hand (dim2) barely stirs, so no two moments ever show the same _combination_ of hand positions. That combination is each position's unique multi-frequency "fingerprint." And because it's the _same fixed function at every position_, the model can even fingerprint a position it never saw during training — something learned embeddings simply cannot do.

_The other key point: position is added on by an **elementwise sum**, not a concatenation — position and meaning share the same d dimensions:_

![Token embeddings plus positional embeddings](assets/S01-positional-addition.svg)

Both tokens carry the **identical** token embedding `[1,1,1]` — the same word — yet leave with different input embeddings. Position is the only thing that separated them. That is this whole section in one picture.

**Tradeoff** — the three approaches trade off cleanly. **Learned embeddings** are simplest and fail hardest outside the trained length. **Sinusoidal** costs nothing and generalises modestly, but it preserves only _relative_ distance and the model has to infer even that from a sum — nothing enforces it — while packing position into the same dimensions as meaning makes the two compete for space. **RoPE** is the current default precisely because long context is the pressure point, and it's the only one of the three that **rotates** Q and K rather than **adding** to the embedding: position then acts on the _angle_ between vectors, which is exactly what the dot product measures, so relative distance falls out of the maths instead of being learned from it. RoPE keeps sinusoidal's multi-frequency idea but applies it by rotation; it gets full treatment in S3 — this is the preview.

**Checkpoint — what Part 2 established.** A transformer block does not "understand" text directly. It repeatedly updates token vectors: attention mixes information across positions, the FFN transforms each position, residuals keep the stack trainable, and positional encoding prevents the model from treating word order as irrelevant.

## Part 3 · Building blocks of LLM

_Now reassemble the machine. The previous part opened the transformer block; this part shows how raw text reaches that block, how the block stack returns vocabulary scores, and why tokenization/context decisions change both quality and cost._

This part is the bridge between the abstract transformer and the concrete LLM you call from an API. Section 9 explains where tokenization sits in the **input pipeline**; section 13 later explains how tokenizer algorithms are designed and why their choices affect cost.

### 8. Building blocks of an LLM

**Intuition** — Up to now, the pieces have been introduced one at a time. This section puts them back together so the whole machine is visible again. If someone asks, "What are the building blocks of a decoder-only LLM?", this is the compact answer you should be able to give.

![Transformer LLM components](assets/S01-transformer-llm.svg)

**Mechanism — what each block contributes:**

| Block                           | Job                                                                 |
| ------------------------------- | ------------------------------------------------------------------- |
| **Tokenizer**                   | Break raw text into IDs the model can process                       |
| **Embeddings**                  | Turn token IDs into dense vectors                                   |
| **Positional encoding**         | Inject word order, because attention alone has no sense of position |
| **Self-attention**              | Let each token pull information from other relevant tokens          |
| **Feed-forward network**        | Apply a learned non-linear transformation at each position          |
| **Residuals + normalization**   | Keep very deep stacks trainable and numerically stable              |
| **Repeated transformer blocks** | Build depth; one block is not enough capacity                       |
| **LM head**                     | Turn the final hidden vector into logits over the vocabulary        |

**Worked example — the shortest possible forward pass.** Prompt `"The cat"`:

1. Tokenizer maps it to token IDs.
2. Embeddings turn each ID into a length-`d` vector.
3. Positional encoding marks which vector is first and which is second.
4. Attention lets `"cat"` look back at `"The"` when forming its hidden vector.
5. The FFN reshapes that hidden vector into a more useful feature vector.
6. After many repeated blocks, the LM head produces scores like `{sat, sleeps, is, ...}` over the vocabulary.

That is the whole machine in miniature: text becomes token IDs, IDs become vectors, vectors are repeatedly updated by the transformer stack, and the final vector is turned into vocabulary scores.

**Tradeoff / what this checklist hides** — The list makes the model look like eight equal boxes, which is useful for revision and slightly misleading in implementation. The expensive parts are not equal: parameters concentrate in embeddings, FFNs and the LM head, while run-time cost under long contexts concentrates in attention. Later sessions are mostly optimisations of one of those hotspots, not new building blocks.

---

### 9. From text to tokens to embeddings

**Intuition** — A model cannot read text directly. It can only operate on numbers. So the input pipeline has to turn text into numerical representations in a fixed sequence of steps.

![Token IDs to token embeddings](assets/S01-token-embeddings.svg)

**Special context tokens** are added at this stage — end-of-text, unknown, padding and similar markers the model needs but the raw text doesn't contain.

Keep two things separate:

| Thing                    | Created when?         | Changes during model training? | Example                                  |
| ------------------------ | --------------------- | ------------------------------ | ---------------------------------------- |
| **Tokenizer vocabulary** | Before model training | No, normally fixed             | token string `"cat"` gets ID `9246`      |
| **Embedding table**      | During model training | Yes, learned weights update    | ID `9246` selects one learned vector row |

That distinction matters because students often blend the two together. The tokenizer decides **which integer** a piece of text becomes. The model learns **what that integer means as a vector**.

**Mechanism — the five stages, in order.** The exam can ask for this sequence:

| #   | Stage                   | In → out                                                               |
| --- | ----------------------- | ---------------------------------------------------------------------- |
| 1   | **Vocabulary building** | corpus → a fixed set of tokens (done once, before training)            |
| 2   | **Tokenization**        | raw text → token strings, plus any special tokens                      |
| 3   | **ID lookup**           | token strings → integers, via the vocabulary dictionary                |
| 4   | **Embedding lookup**    | integers → dense vectors, by selecting **rows** of `E ∈ ℝ^{\|V\| × d}` |
| 5   | **Positional addition** | token embedding **+** positional embedding, elementwise, same `d`      |

![From raw text to input embeddings](assets/S01-text-to-embedding-pipeline.svg)

Stage 4 is a _lookup, not a matrix multiply_ — mathematically it's one-hot × E, but no implementation does that; it's an indexing operation, which is why it costs nothing at inference.

**The embedding layer**:

- The weight matrix starts as **small random values**.
- Those values are **optimised during LLM training as part of the LLM optimisation itself** — embeddings are _learned_, not looked up from somewhere else.
- Shape: **rows = vocabulary size, columns = embedding dimension**.

So the embedding matrix is **E ∈ ℝ^(|V| × d)** — remember this shape; section 10 reuses it.

**Special context tokens — the concrete case.** A worked example extends a vocabulary of `brown→0, dog→1, fox→2, …` with two extras at the end:

| Token | ID        | Purpose |
| ----- | --------- | ------- | --- | ------------------------------------------------------------------------- |
| `<    | unk       | >`      | 783 | New/unknown words not in the training data, so absent from the vocabulary |
| `<    | endoftext | >`      | 784 | Separates two **unrelated** text sources                                  |

**Use case — what breaks without a separator token.** Say you're fine-tuning on a folder of old support tickets, and two unrelated tickets get concatenated into one training example with no marker between them: `...issue resolved by replacing the battery. Customer B's laptop won't turn on...`. Without a boundary, the model can learn spurious continuations — it starts finishing ticket B's problem with ticket A's unrelated resolution, because nothing told it these are two separate documents. Inserting `<|endoftext|>` between them fixes it: a hard signal that nothing before this token is relevant to what comes after.

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

⚠️ **The trap:** the embedding for token ID 5 is the **sixth** row, not the fifth — Python counts from 0. Easy marks lost if you index by one.

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

**Tradeoff** — vocabulary size is a direct dial on the embedding matrix's size. A bigger vocabulary means shorter sequences (good — attention is O(n²)) but a much larger embedding matrix (bad — parameters and memory). That tension is exactly what the tokenizer choices in this part are negotiating.

---

### 10. The language modelling head and weight tying

**Intuition** — After the last transformer block, the model still does not have words. It has a hidden vector. The job of the LM head is to turn that hidden vector back into scores over the vocabulary, so the model can decide which token should come next. In that sense, it mirrors the embedding layer: embeddings map token IDs into vectors, while the LM head maps vectors back into likely token IDs.

Think of the embedding table as a dictionary shelf. On the way in, token ID `5` pulls one book from the shelf. On the way out, the final hidden vector is compared against every book on the shelf and asks: _which token vector am I closest to?_

![Language modelling head and weight tying](assets/S01-lm-head.svg)

**Mechanism**

- **h_LN** = final hidden vector at position N after the last block and final normalisation, shape **[1 × d]**
- **Embedding table E** = the input lookup matrix, shape **[|V| × d]**
- **LM-head / unembedding matrix U**, shape **[d × |V|]**
- If weights are **tied**, **U = Eᵀ**. If weights are **untied**, **U = W_out**, a separately learned matrix with the same shape.
- Product → **u**, the **logit vector**, shape **[1 × |V|]** — one score per vocabulary item
- **Softmax** turns logits u into probabilities **y**, shape **[1 × |V|]**

Carry the three shapes — `[1 × d] → [d × |V|] → [1 × |V|]`. The whole head is one matrix multiply plus a softmax. For a tied model, the logit for token `j` is a dot product: `u_j = h_LN · E_j`, where `E_j` is token `j`'s row in the embedding table.

Softmax probabilities y can then be used to **assign a probability to a given text**, or to **generate text by sampling a word from them** — the two directions of section 3, now concrete.

Training vs inference differ in _which position_ is used: during training **every position predicts its next token** (that's the parallelism paying off); during inference **only the last position** is used to generate. At training the logits go to cross-entropy against the next token; at inference they're sampled with **temperature, top-k or top-p** — all of S5.

**Use case — why weight tying shows up in small models.** Suppose you want a local code assistant that fits on a single consumer GPU. If the vocabulary matrices take up a big fraction of the model, tying the LM head to the embedding table can save hundreds of millions of parameters without touching the transformer stack. On a much larger model, that saving is a smaller fraction of the total, so paying for a separate output matrix may be worth it.

**Weight tying** — the same learned matrix **E [|V| × d]** is used on both sides. Input uses it as a lookup table; output reuses its transpose as the classifier over vocabulary. Tying only works when the hidden size `d` matches the embedding width, which is true for standard decoder-only LLMs.

An implementation detail worth knowing: on the input side **no matrix multiplication actually happens** — the one-hot picks out row _t_ of E, an **O(1) row lookup (gather)** per token.

**Worked example — the parameter arithmetic, Llama-3-8B:**

```
|V| = 128,256    d = 4,096
E = 128,256 × 4,096 ≈ 525 M parameters

Tied:    one E                    ≈ 525 M
Untied:  E + separate lm_head     ≈ 1.05 B
         extra untied head        ≈ 525 M ≈ 6.6% of an 8B model
         E + head together        ≈ 13.1% of an 8B model
```

**Who ties** — a **size-dependent design choice**, not a law:

|                                    | Models                                                         |
| ---------------------------------- | -------------------------------------------------------------- |
| **Tied** (small models)            | Gemma-3 · Llama-3.2-1B/3B · Qwen3-0.6B/4B · SmolLM2            |
| **Untied** (larger/general models) | Llama-3/3.1-8B+ · Qwen3-8B+ · many frontier-scale decoder LLMs |

**Tradeoff / when NOT to tie** — tying saves one full `|V| × d` matrix and is attractive when the vocabulary matrix is a large fraction of the model budget. Untying costs extra parameters, but it lets the output classifier learn a geometry that is not forced to match the input embedding geometry, which can improve modelling quality. For very small models, tie; for larger models with enough budget, untying is often worth paying for. The decision is _ratio of vocabulary matrix to total parameters_, not a universal best practice — which makes it a good tradeoff question.

---

#### Zoom out — where an LLM's parameters actually live

We just counted the LM head. Now step back and count the whole model. This is the picture behind names like 7B, 70B, or 400B, and it is much easier to reason about once you know where those parameters actually live.

**What a parameter is** — a **parameter** (or **weight**) is just **one number learned during training**. So "8B parameters" literally means 8 billion learned numbers. After training, those numbers are frozen and loaded into memory whenever the model runs. Training changes them; inference only reads them.

**Where they live** — a decoder-only LLM is just: **one embedding matrix** at the bottom → **a stack of N identical transformer blocks** → **one final norm** → **the LM head** at the top. Only a few components actually hold weights. Writing **d** = hidden size, **|V|** = vocabulary size, **N** = number of layers, classic FFN width = 4·d:

| Where                        | Matrices                          | Parameter count                 |
| ---------------------------- | --------------------------------- | ------------------------------- |
| **Token embedding**          | E                                 | `\|V\| × d`                     |
| **Attention** (per layer)    | W_Q, W_K, W_V, W_O — each `d × d` | `4 d²`                          |
| **Feed-forward** (per layer) | W_up `d × 4d` + W_down `4d × d`   | `8 d²`                          |
| **LayerNorms** (per layer)   | 2 × (γ, β)                        | `4 d` (negligible)              |
| **Final LayerNorm**          | γ, β                              | `2 d` (negligible)              |
| **LM head**                  | Eᵀ                                | **0 if tied**, else `\|V\| × d` |

Drop the tiny norm terms and one layer costs `4d² + 8d² = ` **`12 d²`**. That gives the single most useful rule of thumb in the subject:

> **Total ≈ 12 · N · d² + vocabulary terms.**
> The stack grows with **d²** (quadratic in _width_) and **linearly** with _depth_ N. The vocabulary terms — `|V|·d` for embeddings, plus another `|V|·d` if the head is untied — are a **fixed tax** set by vocabulary size, not by how deep the model is.

**Worked example — why "7B" adds up.** Take d = 4096, N = 32, |V| = 50,257, FFN = 4d, head tied:

```
Per layer   = 12 · d²         = 12 × 4096²     ≈ 201 M
Stack       = N × per layer   = 32 × 201 M     ≈ 6.44 B
Embedding   = |V| × d         = 50,257 × 4096  ≈ 0.21 B
LM head     = tied → 0
─────────────────────────────────────────────────────
Total                                          ≈ 6.65 B   → a "7B" model
```

Read effects straight off the formula: **double the depth** N and you add another ~6.4 B; **widen** d from 4096 → 5120 and the stack grows by (5120/4096)² ≈ **1.56×**. Width is the expensive dial because it's squared.

_Why depth is linear but width is squared — a building analogy:_ adding a **layer** is like stacking one more **identical floor** onto a tower — the cost adds up floor by floor, so N floors cost N × (one floor). Widening **d** is different: every weight matrix inside a layer is `d × d`, so making the model wider enlarges each matrix in **both** directions at once — like growing a room's length _and_ breadth, where the floor _area_ goes up with the **square** of the side. Depth = more floors (linear); width = bigger floor area (squared). That single fact is why labs reach for depth before width when they want a cheaper way to grow a model.

**Which block dominates** — of the 12 per-layer units, **8 are the feed-forward network and 4 are attention**: **⅔ of every layer is FFN**, ⅓ is attention, norms are rounding error. That is the exact arithmetic reason compression (S6) and Mixture-of-Experts (S3) both attack the FFN first — it's simply where the weights are.

**Where the head fits** — the LM head is the `|V| × d` matrix at the very top, ~0.5 B at 8B scale (about **6.6% extra** when untied; embedding + head together are about **13.1%**). Larger models can pay it; on a 1B model the _same_ matrix is a far bigger slice, so small models often **tie** it to the embedding and pay nothing extra. Embedding + head together are the **vocabulary tax**: fixed by |V|, felt most at small scale.

**The one picture to carry** — _parameters, cost, and optimisation effort all concentrate in the same few matrices._ And keep two things separate that are easy to confuse: **parameters = the model's fixed size in memory** (set by d, N, |V|); **context length = work done per token at run time** (the O(n²) of section 4, which adds _no_ parameters at all). Making a model "bigger" and giving it a "longer context" are different levers.

---

### 11. Context length

**Intuition** — Context length, or context window, is the maximum number of tokens the model can handle at once. The important practical point is that this budget is shared. Your prompt uses part of it, and every generated token uses more of it.

**Mechanism — the limit applies to prompt plus output.** At each decoding step, the model reads all tokens currently in the context, predicts one next-token distribution, appends one token, and repeats. That means the context window is a shared budget for system prompt, user prompt, retrieved text, tool output, conversation history and the answer itself.

![Context length grows during autoregressive generation](assets/S01-context-length.svg)

**The consequence:** generated tokens count against the same budget as the prompt. A 512-token window with a 400-token prompt leaves room for about 112 tokens of answer, not 512. Every token generated shrinks what's left. This is why a long system prompt costs you twice — you pay for it on every request _and_ it eats the answer budget.

**Worked example** — With a 4,096-token context window, a 900-token system prompt, 1,700 tokens of retrieved passages, and 600 tokens of chat history leave:

```
4096 - (900 + 1700 + 600) = 896 tokens
```

So the answer can use at most about **896 tokens** before the request runs out of context. Asking for a 2,000-token answer is impossible unless you shorten the prompt, retrieve less, summarise history, or use a larger-window model.

**Tradeoff** — context length is capped not by ambition but by the O(n²) attention cost from section 4 and by KV-cache memory, which grows linearly with context and is the actual constraint in production serving (S5–S6). "Why not just use a million tokens?" is answered by memory and money, not by capability.

**Checkpoint — what Part 3 established.** The end-to-end LLM is now concrete: fixed tokenizer vocabulary, learned embedding table, repeated transformer blocks, LM head, softmax, decode loop, and context-window budget. Parameters determine model size; context determines runtime work.

---

## Part 4 · LLM Architectures, Tokenization, and LLM Landscape

_Zoom out to the map: the main architecture families, the tokenizer choices you meet in practice, and the model ecosystem you'll actually work with. Aim to **recognise and place** these, not memorise every cell._

### 12. LLM architectures

**Intuition** — There are three main transformer family shapes, and the cleanest way to distinguish them is by what each token is allowed to see. Once that is clear, the training objective, strengths, and weaknesses mostly follow from it.

|                  | **Encoder-only** (BERT, RoBERTa)                                                           | **Decoder-only** (GPT, Llama)                                         | **Encoder-decoder** (T5, BART)                                                             |
| ---------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Architecture** | Transformer encoder stacks, **bidirectional self-attention**                               | Transformer decoder stacks, **causal masking** blocking future tokens | Encoder → contextual representations; decoder generates via **cross-attention**            |
| **Objective**    | **MLM** — mask random tokens, predict from left _and_ right context                        | **CLM** — minimise cross-entropy over next-token predictions          | **Seq2seq** — translation/summarisation; T5 uses a **span-corruption** variant of MLM      |
| **Context**      | **Bidirectional**                                                                          | **Unidirectional (left-to-right)**, preserving causal structure       | Both                                                                                       |
| **Strengths**    | Comprehension — classification, **NER**, sentiment — builds dense semantic representations | Open-ended generation, dialogue, code completion, story synthesis     | Translation, summarisation, **multimodal pipelines where input and output domains differ** |
| **Weaknesses**   | **Not naturally generative** — needs adapter heads or fine-tuning for sequence output      | Less efficient for classification or bidirectional reasoning          | **Dual stacks increase training complexity and inference latency**                         |

**Mechanism — the three architecture families all descend from the Transformer idea:**

![LLM architecture families](assets/S01-architecture-families.svg)

**Mechanism — the original encoder-decoder blueprint, which all three descend from** — worth being able to sketch:

![Original Transformer encoder-decoder blueprint](assets/S01-original-transformer-blueprint.svg)

Three details the figure encodes that the prose doesn't:

- The decoder's **first** attention is **masked** (no peeking ahead); its **second** is cross-attention taking **K and V from the encoder** and Q from the decoder. That's the only place the two stacks touch.
- Outputs are **shifted right** so position _i_ predicts token _i_, never seeing it.
- **Add & Norm** appears after every sublayer — the residual-plus-normalisation pattern from section 6, repeated six times in this diagram.

And the zoom-ins, which are section 4 and section 5 in picture form: **scaled dot-product attention** = `MatMul(Q,K) → Scale → Mask (opt.) → SoftMax → MatMul(·,V)`; **multi-head attention** = `Linear ×3 (V,K,Q) → h parallel scaled-dot-product heads → Concat → Linear`.

The easiest way to remember the families:

| If the product needs...                                      | Start from...       | Why                                                      |
| ------------------------------------------------------------ | ------------------- | -------------------------------------------------------- |
| A label or embedding from text                               | **Encoder-only**    | It can read left and right context at once               |
| Open-ended text/code generation                              | **Decoder-only**    | It naturally predicts the next token                     |
| A transformed output sequence from a separate input sequence | **Encoder-decoder** | Encoder understands the input; decoder writes the output |

**Worked example** — sentiment classification. BERT: one forward pass, a classification head, done — efficient because it never needed to generate. GPT: prompt it and sample a token, hoping for "positive" — general, but you burned a generation step to get a label.

**Tradeoff / why decoder-only won anyway** — encoder-only is strictly better at classification, and encoder-decoder is cleaner for translation. Decoder-only won because **section 3 holds**: if every task can be cast as next-word prediction, one architecture covers all of them, and generality beat per-task efficiency once models got large enough. Note the line from section 6 — _we use transformers to create generative models by using only decoders_. Multimodal systems (speech-text, vision-language) still extend the encoder-decoder blueprint.

---

### 13. Tokenization

Read tokenization as three linked questions:

| Question                           | Answer                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| **What units can the model see?**  | tokens, not raw words or characters by default                                             |
| **How is the vocabulary learned?** | a tokenizer algorithm builds a fixed token inventory before model training                 |
| **Why does it matter?**            | it controls sequence length, context cost, multilingual fairness, and embedding-table size |

#### 13.1 Why subwords

**Intuition** — the framing: **common words end up in the subword vocabulary; rarer words are split into components** (sometimes intuitive, sometimes not). Worst case, a word is split into as many subwords as it has characters.

```
hat, learn          →  common words, one token each
taa##aaa##sty       →  variations
la##ern##           →  misspellings
Transformer##ify    →  novel items
```

#### 13.2 Three types of token

| Type                            | How                                                               | Problem it solves / creates                                                                                                                                    |
| ------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Word tokens** (e.g. word2vec) | One token per word                                                | **Cannot handle new words** entering after the tokenizer was trained; and **many tokens with minimal differences** — apology, apologize, apologetic, apologist |
| **Subword tokens**              | Break unknown words into smaller pieces already in the vocabulary | **Can represent new words**; the standard choice                                                                                                               |
| **Byte tokens**                 | Vocabulary of **UTF-8 bytes (256)**; **one token = one byte**     | No OOV ever; very long sequences. "Apple" → `[65][112][112][108][101]` = 5 tokens. Used by **tokenizer-free models — ByT5, CANINE**                            |

_One sentence through all four granularities. Read it top to bottom as a trade of vocabulary size against sequence length:_

![Tokenization granularities](assets/S01-tokenization-granularity.svg)

Going down the figure, **vocabulary shrinks and sequence length grows**. Since attention is O(n²) in sequence length (section 11), the bottom two buy robustness with compute. Subword sits where it does because that trade is least bad there.

**Use case — multilingual customer support.** An English support query may fit in 40 tokens, while the same meaning in Hindi or Arabic may take far more tokens if the tokenizer learned fewer useful merges for that language. The model is not "thinking harder"; the tokenizer simply represents the text less compactly. That raises latency and cost, and it can force truncation sooner for exactly the users the product should support equally.

#### 13.3 Subword algorithms

Three, all sharing the same two-part structure:

| Algorithm                      | Core idea (how the vocabulary is learned)                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Byte-Pair Encoding (BPE)**   | Start from characters; **greedily merge the most frequent adjacent pair**, over and over         |
| **Unigram language modelling** | Start from a large vocabulary; **prune the tokens whose removal costs the least likelihood**     |
| **WordPiece**                  | Merge the pair that **most increases the training corpus's likelihood** (not just raw frequency) |

Every one has **two parts** — this is the definitional split, and it's examinable:

1. A **token learner** — takes a raw training corpus and induces a vocabulary
2. A **token segmenter** — takes a raw test sentence and tokenizes it according to that vocabulary

The vocabulary is built **dynamically**: frequent words get their own tokens, rare words get split.

#### 13.4 BPE — the algorithm and a worked example

**Mechanism — the token learner, in four steps:**

| #   | Step                                                                                                            |
| --- | --------------------------------------------------------------------------------------------------------------- |
| 1   | **Pre-tokenize** the corpus into words with a rule-based splitter (whitespace and punctuation)                  |
| 2   | Build a **word dictionary with frequency counts**                                                               |
| 3   | Start from a **uni-character vocabulary** — every character that appears                                        |
| 4   | **Merge the most frequent adjacent pair**, record the merge, repeat until the target vocabulary size is reached |

The matching **token segmenter** replays the recorded merges **greedily, in the learned order**, on new text. Test-set frequencies never matter — only the order learned at training time.

**Worked example — reproduce this by hand.**

Corpus: `("hug", 10), ("pug", 5), ("pun", 12), ("bun", 4), ("hugs", 5)`

**Finding the first merge — count each adjacent pair across the whole corpus:**

| Pair          | Where it appears        | Total                                                                                          |
| ------------- | ----------------------- | ---------------------------------------------------------------------------------------------- |
| **("u","g")** | hug 10 + pug 5 + hugs 5 | **20** ✅ most frequent                                                                        |
| ("p","u")     | pug 5 + pun 12          | **17** ← _the runner-up to this first merge (17 < 20); it then evaporates once `pug` → `p·ug`_ |
| ("u","n")     | pun 12 + bun 4          | 16                                                                                             |
| ("h","u")     | hug 10 + hugs 5         | 15                                                                                             |
| ("g","s")     | hugs 5                  | 5                                                                                              |
| ("b","u")     | bun 4                   | 4                                                                                              |

_All six pairs, not just the top three — if you work this by hand you will find `("p","u") = 17`, and a table that omits it looks like you made an arithmetic error._

So `"u"` and `"g"` merge into the new token **`"ug"`**, which is added to the vocabulary.

![BPE merges the most frequent pair, every round](assets/S01-bpe-merge-steps.svg)

**The iterations:**

| Iter | Vocabulary            | Tokenization                                                                            |
| ---- | --------------------- | --------------------------------------------------------------------------------------- |
| 1    | `b, g, h, n, p, s, u` | `("h","u","g",10) ("p","u","g",5) ("p","u","n",12) ("b","u","n",4) ("h","u","g","s",5)` |
| 2    | `+ ug`                | `("h","ug",10) ("p","ug",5) ("p","u","n",12) ("b","u","n",4) ("h","ug","s",5)`          |
| 3    | `+ un`                | `("h","ug",10) ("p","ug",5) ("p","un",12) ("b","un",4) ("h","ug","s",5)`                |
| 4    | `+ hug`               | `("hug",10) ("p","ug",5) ("p","un",12) ("b","un",4) ("hug","s",5)`                      |

⚠️ **The trap, at merge 2:** once `ug` exists, the pair `("h","ug")` = 15 is sitting right there and _looks_ like the obvious next merge. But `("u","n")` = pun(12) + bun(4) = **16** still beats it, so **`un` merges second, not `hug`.** Re-count every adjacent pair each round — never assume the pair you just created wins the next one.

**Advantages** — efficient handling of rare words and subword units; reduces vocabulary size, making the model more efficient; better generalisation by breaking words into subword units.

**Limitations** — can produce **fragmented tokens for languages with complex morphology**; **may not capture semantic meaning** as effectively as other methods.

#### 13.5 SentencePiece

**Language-independent** subword tokenizer that learns **directly from raw Unicode text** with a fixed vocabulary size — **no whitespace pre-tokenizer required**, which is what makes it language-independent.

![SentencePiece versus tiktoken](assets/S01-tokenizer-pipeline-comparison.svg)

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

#### 13.6 SentencePiece vs tiktoken

The distinction, stated precisely: they differ in **what unit they merge over** (characters vs bytes) and **whether they pre-split the text with a regex before merging** (SentencePiece doesn't; tiktoken does).

```
SentencePiece BPE (Llama-2):
  Whitespace-marked:  ▁Hello,▁world!
  Tokens:             [▁Hello, ,, ▁world, !]

tiktoken BPE (Llama-3):
  Regex chunks:       [Hello, ,,  world, !]
  Tokens:             [Hello, ,, ' world', !]    ← space is inside " world"
```

**tiktoken's byte-level + regex-pretokenized design gives better compression, no OOV, and byte-exact reversibility — which is why every frontier model released after Llama-2 uses it or something like it.**

**Representative usage patterns:**

| Tokenizer family             | Vocab    | Representative model families                            |
| ---------------------------- | -------- | -------------------------------------------------------- |
| SentencePiece unigram        | 32K-250K | T5, mT5                                                  |
| SentencePiece BPE            | 32K      | Llama-2, Mistral-class models                            |
| SentencePiece BPE            | 256K     | Gemma-family models                                      |
| **tiktoken-style byte BPE**  | 128K     | Llama-3 and similar newer decoder-only families          |
| Larger byte-BPE vocabularies | ~200K    | frontier chat models optimized for long prompts and code |

⚠️ **Llama-3 switched from SentencePiece → tiktoken** for a better compression ratio — fewer tokens per byte of English and code.

**Tradeoff / the whole tokenizer decision in one line** — bigger vocabulary means fewer tokens per document, which means shorter sequences and cheaper O(n²) attention — but a bigger embedding matrix and more rarely-seen tokens. That's why vocabulary sizes cluster between 32K and 256K rather than at either extreme, and why compression ratio (tokens per byte) is the metric people actually optimise.

> **_In practice_** _— tokenization is where your API bill comes from:_
>
> - **You pay per token**, in and out. Tokenization is the invisible layer that decides how many tokens a document costs. `encoding.encode(text)` with the tokenizer for your chosen model counts them before you send — do this to estimate cost and to stay under the context window.
> - **Non-English text costs more.** The same sentence in Hindi, Arabic or code can take 2–3× the tokens of English, because the tokenizer's merges were learned mostly on English. A multilingual product's cost and latency are silently worse for exactly the users who aren't in the training-data majority — a real fairness-and-cost issue you'll meet on the job.
> - **Prompt engineering is partly token engineering:** the "model selection + prompt optimisation cuts cost 10–20×" figure is mostly about tokens — fewer, cheaper tokens per call at the same quality.

#### 13.7 Going deeper — WordPiece & byte-level BPE

Deeper tokenization knowledge, kept as reference for **Lab 1** — out of exam scope (won't be on the closed-book mid-sem) but useful for the lab and the field.

**Byte tokens vs BPE:**

|                    | Byte tokens                                                                                               | BPE                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Efficiency         | Extremely inefficient — never merges anything, so sequences are long                                      | Efficient for what it has seen                              |
| OOV handling       | Can read **any** file or character — nothing is ever unknown                                              | **"Blind" to what it doesn't know** — falls back to `[UNK]` |
| `"Café 🚀"` result | 10 tokens: `[67][97][102][195][169][32][240][159][154][128]` (`é` takes two bytes, the rocket takes four) | 3 tokens, **one of which is `[UNK]` — the failure**         |

**Byte-level BPE (GPT-2)** — UTF-8 encodes each Unicode character into 1-4 bytes, so a sentence is modelled as a **sequence of bytes rather than characters**. Starts with 256 bytes and learns to "glue" them into useful words. **Zero unknown words**, because it can always fall back to individual bytes. GPT-2's vocabulary is **50,257 = 256 byte tokens + 50,000 merges + 1 special end-of-text token** — worth knowing where that odd number comes from. `"Café 🚀"` → 2 tokens.

Example, `The sun is ☀️`:

| Word   | Raw bytes    | Token ID | Why                                                           |
| ------ | ------------ | -------- | ------------------------------------------------------------- |
| `The`  | 54 68 65     | 464      | Very common English word, merged into one token               |
| ` sun` | 20 73 75 6e  | 6035     | **The space is "glued" to the word**                          |
| ` is`  | 20 69 73     | 374      | Another space+word merge                                      |
| ` `    | 20           | 220      | A single space before the emoji                               |
| `☀️`   | E2 98 80 ... | 99321    | **One token** — common emoji, all bytes merged into one entry |

**WordPiece** — Google's tokenizer, developed to pretrain **BERT**. Very similar to BPE in training; **the actual tokenization is done differently**.

_Token learner:_ start from a small vocabulary (special tokens + initial alphabet), split words with a **`##` prefix** for non-initial pieces — `word` → `w ##o ##r ##d`. Instead of merging the most frequent pair, WordPiece **computes a score** and merges by score, **prioritising pairs whose individual parts are less frequent**:

```
score(a,b) = freq(a,b) / (freq(a) × freq(b))
```

Same corpus as BPE — `hug 10, pug 5, pun 12, bun 4, hugs 5`, split as `("h","##u","##g",10)` etc. Initial vocabulary `[b, h, p, ##g, ##n, ##s, ##u]`:

| Pair            | Score          | Value              |
| --------------- | -------------- | ------------------ |
| `("##u","##g")` | 20 / (36 × 20) | **1/36**           |
| `("##g","##s")` | 5 / (20 × 5)   | **1/20** ✅ higher |

So the **first merge is `##gs`**, not `##ug` — the opposite of BPE's answer on the same corpus, which is exactly the point of the example.

_Token segmenter:_ pre-tokenize, split, then for each word **find the biggest subword starting at the beginning**, split it off, and repeat on the remainder. With final vocabulary `[b, h, p, ##g, ##n, ##s, ##u, ##gs, hu, hug]`, the test word `hugs` tokenizes as **`["hug", "##s"]`**.

_Advantages_ — efficient handling of rare words, reduced vocabulary size, better generalisation. _Limitations_ — the scoring mechanism **adds complexity** over BPE; still fragments morphologically complex languages. WordPiece's **likelihood-based scoring** distinguishes it from BPE's **frequency-based** approach, often producing a vocabulary that better captures linguistic structure.

---

### 14. The LLM landscape

**Intuition** — This landscape is easier to learn as a chain of causes than as a list of model names. Each stage created the conditions for the next one.

_The chain, each link forcing the next:_

![LLM landscape causal chain](assets/S01-landscape-chain.svg)

**Mechanism — why this matters for the course:** the middle link is why sessions 9–16 exist at all. If anyone could pre-train, the syllabus would be about pre-training. Because they can't, it's about adaptation.

**Pre-neural (before 2010s)** — as early as 1950, a language model was used to measure the **entropy of English**; then decades of **n-gram** language models for machine translation and speech recognition.

**Neural ingredients (2010s)** — each a component the transformer needed:

| Year     | Contribution                                |
| -------- | ------------------------------------------- |
| 2003     | First **neural language model**             |
| 2014     | **Sequence-to-sequence** modelling (for MT) |
| 2014     | **Adam** optimizer                          |
| 2014     | **Attention** mechanism (for MT)            |
| **2017** | **Transformer** architecture (for MT)       |
| 2017     | **Mixture of experts**                      |
| 2018–19  | **Model parallelism**                       |

Note that attention, seq2seq and the transformer all arrived **for machine translation**. None of them were built to make chatbots.

**Early foundation models (late 2010s)** — **ELMo** (pretraining with LSTMs, fine-tuning helps tasks) → **BERT** (pretraining with a Transformer) → **T5, 11B** (cast everything as text-to-text).

**Embracing scaling, becoming more closed:**

| Model          | Size | Significance                                                           |
| -------------- | ---- | ---------------------------------------------------------------------- |
| GPT-2          | 1.5B | Fluent text, **first signs of zero-shot**, staged release              |
| —              | —    | **Scaling laws** — hope/predictability for scaling (**Kaplan** law)    |
| GPT-3          | 175B | **In-context learning**; closed                                        |
| PaLM           | 540B | Massive scale, **undertrained**                                        |
| **Chinchilla** | 70B  | **Compute-optimal scaling laws** — smaller and better, correcting PaLM |

PaLM "undertrained" followed by Chinchilla "compute-optimal" is the story of S2 in two rows: bigger stopped being automatically better.

**Worked example** — GPT-3 made scaling look like the main story: bigger model, better behaviour, new in-context learning. Chinchilla changed the lesson: a smaller model trained on more data can beat a larger undertrained one. That is why S2 treats data and compute as first-class design variables, not background details.

**Open models:**

| Org                      | Flagship model | Notable fact                                               |
| ------------------------ | -------------- | ---------------------------------------------------------- |
| EleutherAI               | GPT-J          | Built on The Pile dataset                                  |
| Meta                     | OPT 175B       | GPT-3 replication attempt; well-documented hardware issues |
| HuggingFace / BigScience | BLOOM          | Focused on data sourcing transparency                      |
| Meta                     | Llama          | —                                                          |
| Alibaba                  | Qwen           | —                                                          |
| DeepSeek                 | DeepSeek       | —                                                          |
| AI2                      | OLMo 2         | —                                                          |

**Three levels of openness** — a favourite exam question because the middle case is counter-intuitive:

| Level           | Representative case                            | What you get                                                                                                     |
| --------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Closed**      | managed proprietary model                      | **API access only**                                                                                              |
| **Open-weight** | published weights without full training recipe | **Weights available**, paper with architecture and some training details, **no full reproducibility**            |
| **Open-source** | reproducible research release                  | **Weights and data available**, paper with most details — though not necessarily rationale or failed experiments |

"Open-weight ≠ open-source" is the point: you can run the model but cannot reproduce it, because the data isn't there.

**Durable frontier family categories** — the names change quickly; the durable thing to learn is _what kind of capability each family is pushing_:

| Family                 | What it's optimizing for                                    |
| ---------------------- | ----------------------------------------------------------- |
| Large closed models    | Overall capability, served via API                          |
| Open-weight models     | Reproducible deployment without full training recipe        |
| Reasoning-tuned models | Stronger multi-step reasoning (often via test-time compute) |
| Multimodal models      | Beyond text — images, audio, video                          |
| Sparse-MoE systems     | Lower inference cost through sparse activation              |

**Tradeoff / how to study this section** — this is _landscape_, not _mechanism_. Per the subject's study rule: build the comparison table, learn the causal chain and the three openness levels, and do **not** try to memorise every model and parameter count. Specific frontier model names date within months; the openness taxonomy and the Kaplan → Chinchilla correction don't.

## Self-study / Lab / build

Before running the lab, eliminate these common confusions:

| Confusion                                  | Correct version                                                                                                |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **LLM = ChatGPT**                          | ChatGPT is a product; an LLM is the underlying model type                                                      |
| **Generative AI = LLM**                    | LLMs generate text/code; generative AI also includes image, audio, video and other generators                  |
| **Token = word**                           | A token may be a word, subword, byte, punctuation mark, or special marker                                      |
| **Token ID = embedding**                   | Token ID is an integer chosen by the tokenizer; embedding is the learned vector row selected by that ID        |
| **Embedding table = tokenizer vocabulary** | The tokenizer vocabulary is a fixed text-to-ID mapping; the embedding table is learned model weights           |
| **Attention = whole transformer**          | Attention is the token-mixing sublayer; a transformer block also has FFN, residuals and normalisation          |
| **Parameters = context length**            | Parameters are fixed learned weights; context length is runtime input/output budget                            |
| **Open-weight = open-source**              | Open-weight lets you run weights; open-source should also make training recipe/data substantially reproducible |

**536 Lab 1 is at session 1 (module M1): construct and analyse tokenization techniques.** Everything you need is in section 13 plus the extra material.

Minimum useful version, ~15 lines:

```python
from transformers import AutoTokenizer

for name in ["gpt2", "meta-llama/Llama-2-7b-hf", "meta-llama/Meta-Llama-3-8B"]:
    tok = AutoTokenizer.from_pretrained(name)
    for text in ["Tokenization matters", "Café 🚀", "Transformerify", "The sun is ☀️"]:
        ids = tok.encode(text)
        print(f"{name:35} {text:20} {len(ids):3} tokens  {tok.convert_ids_to_tokens(ids)}")
```

That single script makes concrete: SentencePiece vs tiktoken (section 13.6), why Llama-3 switched, byte fallback on the emoji, and subword splitting on the novel word. **Run it before session 2** — the compression-ratio argument only lands once you've seen the token counts differ.

---

_Exam: this session is in scope for the **closed-book mid-sem** (sessions 1–8). Full evaluation, weights, dates and course logistics live once in [`536-master.md`](../536-master.md) — not repeated per session._
