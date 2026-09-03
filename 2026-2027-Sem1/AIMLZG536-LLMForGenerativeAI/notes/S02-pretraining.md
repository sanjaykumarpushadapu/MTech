# Large Language Models for Generative AI · Session 02 · LLM Pretraining

_Deck instructor credit: Dr. Monali Mavani · Course: AIML ZG536_
_Learned 2 Aug 2026_

> **Scope note.** This note covers LLM pretraining, pretraining objectives, pretraining data, continued pretraining (CPT), domain adaptation, scaling laws, and frontier-model training recipes. Figures and explanatory diagrams are labeled by purpose where relevant.

## Why this matters

Pretraining is where an LLM acquires its broad initial capabilities. Fine-tuning and alignment build on representations learned during pretraining, while prompting relies on the model’s learned language patterns. This session explains how that happens: what objective the model is trained on, what kind of data pipeline feeds it, and how scaling laws guide decisions about model size and token count. These concepts make frontier-model reports easier to read as engineering tradeoffs.

**Running example:** We reuse four distinct paths throughout Part 3 via the FinLLaMA/BloombergGPT case studies: regular pretraining from scratch; continued pretraining (CPT) on top of an existing checkpoint; retraining from scratch on a combined dataset; and domain-specific pretraining from scratch.

---

## Part 1 · Building a large language model

_Pretraining is the foundational stage of a language model’s development. The model processes vast amounts of text and repeatedly predicts the next token in a sequence. It starts with nearly random guesses and gradually improves by adjusting its parameters across billions of training tokens. Over time, it learns statistical patterns in language, including syntax, factual associations, and relationships between concepts. The rest of this note explains where the learning signal comes from, what data feeds it, and how scaling laws guide decisions about model size and corpus size._

![Building a large language model](assets/S02-slide-04-building-an-llm.png)

### 1.1 Self-Supervised Learning

**Intuition** — An LLM's raw capability does not come from people hand-labeling millions of examples. It comes from repeatedly asking the model to predict either a masked token or the next token in a sequence. The text itself provides the answer key. That is why the process is called **self-supervised**: the supervision is already hidden inside the data. These training problems are also called **pretext tasks**.

![Self-supervised pretraining and transfer](assets/S02-self-supervised-learning.png)

At a high level, the deck presents three stages: **Stage 1** builds a large language model, **Stage 2** produces a foundation model, and **Stage 3** fine-tunes downstream models. This section focuses on the self-supervised signal used during the first of those stages. Later instruction-tuning and alignment details belong to the broader development pipeline described below, not to the definition of self-supervised learning.

_Everyday version:_ it's like a student practicing with flashcards where the answer is printed on the back of the very same card — no teacher needs to grade anything, because the material itself already contains the answer key. Cover the next word, guess it, flip and check, repeat millions of times. That is the entire supervision signal in pretraining: the text supplies both the question and the answer, so nobody has to hand-label a thing.

**Worked example** — the concrete numeric example for Stage 1's loss appears in Section 1.3, `LLM training`.

**Tradeoff / when NOT to use** — self-supervised pretraining from scratch is usually justified only when you have web-scale unlabeled text and need a general-purpose base model. If you have a narrow task and a modest labeled dataset, don't pretrain a new model—fine-tune an existing pretrained one (session 7). Reproducing a GPT-3-scale pretraining run for one narrow classification task incurs the cost of pretraining without needing the generality it provides.

---

### 1.2 Pretraining Objectives

**Intuition** — The training objective matters because it shapes what the model is directly optimized to do. If trained to predict the next token, a model is directly optimized for left-to-right continuation. If trained to reconstruct masked tokens from both sides, it learns bidirectional contextual representations that are often useful for classification; neither objective alone guarantees “understanding.”

**Mechanism** —

| Objective                              | Model family / example                                      | Attention pattern and typical use |
| -------------------------------------- | ----------------------------------------------------------- | ---------------------------------- |
| CLM / next-token prediction            | GPT-4 and other decoder-only GPT/Llama models; Claude's architecture is not publicly specified | Left-to-right causal attention; free-form generation |
| Masked-token prediction                | BERT — encoder-only                                        | Bidirectional attention; representations and classification after fine-tuning |
| Denoising span-mask prediction         | T5 — encoder-decoder                                       | Corrupt spans are reconstructed using encoder context and an autoregressive decoder |

CLM is the objective behind the decoder-only LLMs used throughout this subject. MLM is the classic BERT-style objective, while T5 uses an encoder-decoder denoising objective that reconstructs masked spans. The important distinction is what each objective trains the model to do: CLM trains left-to-right next-token prediction, whereas MLM trains bidirectional contextual representations by reconstructing masked tokens; the latter is commonly adapted to classification rather than native free-form generation, and span denoising trains an encoder-decoder model to reconstruct missing text.

_Everyday version:_ CLM is like reading a mystery novel one page at a time and guessing what happens next using only what you've read so far — you're never allowed to peek ahead. MLM is like being handed a page with a few words blacked out and figuring out each one using both the sentence before it and the sentence after it, the way you'd solve a crossword clue. The first habit builds someone who's good at continuing a story; the second builds someone who's good at understanding a passage once it's all laid out in front of them.

**Worked example** — the numeric loss calculation in Section 1.3, `LLM training`, is the CLM case, since that is what this subject's LLMs actually train on.

**Tradeoff / when NOT to use** — During training, a CLM uses a causal mask but can evaluate all positions in parallel; during inference, it generates autoregressively because each next-token distribution depends on previously generated tokens. An MLM uses bidirectional context and therefore does not natively generate free-form continuations; classification can attach a task-specific head to the encoder representation, while generation requires an autoregressive decoder or another autoregressive output mechanism.

![BERT masked-token prediction](assets/S02-clm-vs-mlm-objectives-bert.png)

![T5 denoising span-mask prediction](assets/S02-clm-vs-mlm-objectives-t5.png)

![GPT-4 next-token prediction](assets/S02-clm-vs-mlm-objectives-gpt4.png)

---

### 1.3 LLM training

**Intuition** — Training only works if the model gets a score telling it how wrong it was. In language modeling, that score comes from a simple idea: after the model predicts a probability distribution over the vocabulary, check how much probability it gave to the token that really came next. If that probability was low, the model should be penalized. If it was high, the penalty should be small. Cross-entropy is that penalty. Perplexity is the same story rewritten in a more human-readable scale.

![LLM training and cross-entropy loss](assets/S02-cross-entropy-loss.png)

**Mechanism** — For `T` next-token prediction positions, at position `t` the model receives the prefix through `wₜ`, outputs a distribution `ŷₜ` over the vocabulary, and is evaluated against target `w_{t+1}`, for `t = 1,…,T`. Since the true next token is a single token (one-hot), the general cross-entropy formula collapses to the negative log-probability of just that one correct token:

```
L_CE (T next-token targets) = (1/T) · Σ_{t=1..T}  −log ŷₜ[w_{t+1}]
```

Why this particular penalty, rather than something simpler like scoring raw accuracy (did the top prediction match)? Accuracy is not differentiable — it gives zero gradient almost everywhere, so there's no signal telling the optimizer which direction to nudge each weight. Squared error between the predicted distribution and a one-hot target is differentiable, but its gradient goes flat once the predicted probability is near either extreme, so it stops correcting a confidently-wrong prediction fast. Negative log-probability avoids both problems: for positive softmax probabilities it is smooth; its derivative with respect to the correct probability is `−1/p`, so assigning a tiny probability receives a large penalty, while its derivative with respect to a softmax logit is `p − y`. It is also the negative log-likelihood objective.

_Everyday version:_ think of a weather forecaster who says "10% chance of rain" and it pours that day. Cross-entropy fines them hard for that — they were confident and wrong. If instead they'd said "40% chance of rain," the same rainy outcome earns a much smaller fine, because they'd hedged more. Just tracking whether the forecaster's top guess ("rain" vs "no rain") was right or wrong would treat both cases the same and never teach them to be appropriately less confident — cross-entropy is the scoring rule that specifically punishes confident wrongness, which is exactly the behavior you want to train out of the model.

Training uses **teacher forcing**: at every position, the model is shown the true previous tokens, not its own guesses from earlier positions. This avoids feeding an early sampled error into later inputs during training; using model-generated history instead creates an exposure mismatch between training and inference.

Perplexity is `exp(L_CE)` when cross-entropy uses natural logarithms: it is the geometric mean of the inverse probability assigned to the observed tokens, not literally the number of choices considered. Lower is better. One caveat matters a lot in practice: perplexity is **tokenizer-dependent**. If two models use different tokenizers, their perplexity numbers are not directly comparable because the unit "token" is not the same.

**Worked example — reproduce this by hand.** Two 3-token sequences pass through a model that has _not yet been trained_:

- `"every effort moves"` → target `"effort moves you"`
- `"I really like"` → target `"really like chocolate"`

The model assigns these probabilities to the _correct_ target token at each of the 6 positions across both sequences:

| Sequence | Position | Probability assigned to the correct token | log(probability) |
| -------- | -------- | ----------------------------------------- | ---------------- |
| 1        | 1        | 2.3466 × 10⁻⁵                             | −10.6600         |
| 1        | 2        | 2.0531 × 10⁻⁵                             | −10.7936         |
| 1        | 3        | 1.1733 × 10⁻⁵                             | −11.3531         |
| 2        | 1        | 4.2794 × 10⁻⁵                             | −10.0591         |
| 2        | 2        | 1.6248 × 10⁻⁵                             | −11.0275         |
| 2        | 3        | 1.1586 × 10⁻⁵                             | −11.3657         |

Average log-probability = −10.8765. **Cross-entropy loss = −(−10.8765) = 10.8765.**

Every probability here is tiny (~10⁻⁵, roughly 1-in-100,000) because the untrained model is guessing almost uniformly across its ~50,000-token vocabulary — it hasn't yet learned to favor the correct token. That's what a loss around 10–11 nats means in plain terms. As training proceeds, this number falls; a well-trained small model on a narrow corpus can reach a loss under 1.0.

**Tradeoff / when NOT to use** — cross-entropy on held-out text is useful for comparing models when tokenization, evaluation data, and aggregation conventions are aligned; differing tokenizers make raw perplexity incomparable, while train/evaluation overlap makes the score an unreliable estimate of generalization. See the MMLU discussion above. Cross-entropy also does not directly measure whether generated text is _correct_, only whether it was _likely_ under the model's training distribution — a fluent, confident, wrong answer can still carry a good loss.

#### Modern LLM development and training pipeline

![Modern LLM development and training pipeline](assets/S02-modern-llm-development-pipeline.png)

This diagram shows the LLM development pipeline from raw data to a model prepared for use. Read it from left to right. The five blocks are stages in one workflow, not five different model architectures.

**1. Dataset — the starting material**

A dataset is a large collection of material such as books, websites, articles, code, conversations, and documents. The quality and diversity of this material strongly influence what the final model can learn. Raw data may contain duplicates, noise, harmful content, or irrelevant material, so it cannot normally be used directly.

**2. Preprocessing — prepare the training corpus**

Before training, the raw dataset is cleaned and organized:

- **Filtering:** remove or down-weight low-quality, harmful, duplicated, or irrelevant content.
- **Synthetic data:** add generated examples when they are useful and appropriately checked.
- **Mixing:** combine web text, code, Q&A, academic content, books, and other sources in selected proportions.

**Goal:** produce a training-ready corpus. Preprocessing is data engineering; the model has not learned its capabilities yet.

**3. Pretraining — learn broad language patterns**

The model is trained on the prepared corpus, usually with self-supervised **next-token prediction**. It learns statistical patterns, facts represented in the data, coding patterns, and other broad capabilities. The diagram lists several possible parts of a modern pretraining recipe:

- **Q&A format:** represent some data as questions and answers. This can help question-answering behavior, but Q&A formatting alone does not create instruction following; instruction following is mainly developed during post-training.
- **Long-context stage:** train with longer sequences so the model can process longer documents or conversations.
- **Continued pretraining:** continue next-token training from an existing checkpoint, often to adapt it to a domain or new data.
- **High-quality stage:** use a carefully curated subset, sometimes late in training, to refine the model.
- **Knowledge distillation:** train one model to reproduce useful behavior from a stronger teacher model. This is optional and can be used at different points in a model-development recipe.

**Result:** a base model with broad language capabilities. These listed items are recipe choices, not mandatory steps for every LLM.

**4. Post-training — shape useful behavior**

Post-training starts from the pretrained base model and uses narrower instruction or preference data to make its responses more useful, safe, and consistent:

- **Supervised fine-tuning (SFT):** train on human-written or curated instruction–response examples.
- **Reinforcement learning from human feedback (RLHF):** use human preferences or rankings to improve response behavior.
- **Direct preference optimization (DPO):** learn directly from preferred and rejected responses without the same separate reinforcement-learning procedure used in a traditional RLHF pipeline.
- **Online/offline methods:** use either fixed preference data (**offline**) or newly collected/on-policy feedback (**online**). Online does not necessarily mean that the model is updated continuously.
- **Knowledge distillation:** optionally transfer useful behavior from a larger teacher to a smaller model.

**Result:** an instruction-following or aligned model, rather than only a general text predictor. Post-training builds on pretraining; it does not replace it.

**5. Optimization — prepare for efficient use**

The source diagram labels the final block only as **Optimization**. In practice, this may include:

- quantization to reduce model size and memory use;
- pruning or sparsity methods to reduce computation;
- faster inference and batching;
- memory optimization;
- hardware-specific tuning for GPUs, TPUs, or NPUs.

These are common examples, not techniques explicitly specified by the slide. The goal is to make the model cheaper, faster, and easier to serve.

**Exam-friendly summary**

```text
Dataset
  ↓
Preprocessing
  • Filtering
  • Synthetic data
  • Data mixing
  ↓
Pretraining
  • Next-token prediction
  • Q&A-formatted data
  • Long-context stage
  • Continued pretraining
  • High-quality-data stage
  • Optional knowledge distillation
  ↓
Post-training
  • SFT
  • RLHF
  • DPO
  • Online/offline preference methods
  • Optional knowledge distillation
  ↓
Optimization
  • Quantization
  • Pruning/sparsity
  • Inference and hardware optimization
```

**One-line memory trick:**

> **Collect Data → Clean Data → Learn Language → Align Behavior → Optimize Deployment**

The key distinction is that **pretraining teaches broad patterns**, while **post-training shapes how the model responds to people**. The arrows represent increasing data and model readiness: raw material → clean corpus → base model → aligned model → deployable system.

#### Modern pre-training

![Modern pretraining pipeline](assets/S02-modern-pretraining.png)

**Central idea:** modern pretraining does not replace the core objective. The model still learns primarily by predicting the next token. What has become richer is the **data**, the **training stages**, and the use of **post-training** after the core pretraining phase.

**Traditional pretraining vs modern pretraining**

| Aspect | Traditional pretraining | Modern pretraining |
| --- | --- | --- |
| Data | Mostly text-only data | Rich, diverse, multilingual, balanced, and sometimes multimodal data |
| Data pipeline | Relatively simpler | More curation, synthetic-data generation, data mixing, and multimodal integration |
| Core objective | Next-token prediction | Still mainly next-token prediction |
| Training recipe | Often treated as one broad training phase | May use staged training for general knowledge, reasoning, and long context |
| After pretraining | Separate fine-tuning may follow | Instruction tuning and preference alignment usually follow as post-training |

**What the modern-pretraining side adds**

1. **Rich and diverse input data** — combine text from multiple languages and domains with better curation and more balanced sampling. Depending on the model, the data may also include code, images, audio, or other modalities.
2. **Synthetic data generation** — create additional training material with another model or a specialized data-generation process. Synthetic data must still be checked for quality, factual errors, and repeated model biases.
3. **Multimodal integration** — train the system to connect text with other modalities, such as an image and its description. The exact architecture and objective vary by model; the diagram's point is that modern training is no longer restricted to text-only input.
4. **Staged training** — the diagram illustrates a possible sequence:
   - **General knowledge:** learn broad language and world-knowledge patterns.
   - **Reasoning:** emphasize data or procedures intended to improve multi-step problem solving.
   - **Long context:** train on longer sequences so the model can use more of a document or conversation at once.

These stages are an illustrative modern recipe, not a universal schedule. Some models combine stages, repeat them, or use different names and ordering.

**Where post-training fits**

The diagram places **instruction tuning** and **preference alignment** after the core pretraining objective. This distinction is important:

- **Pretraining** builds broad representations and capabilities from large-scale data, usually through next-token prediction.
- **Post-training** uses instruction examples and preference signals to make the model follow requests, produce preferred formats, and behave more helpfully and safely.

Therefore, instruction tuning is not the same as the core pretraining objective, even though instruction-formatted data may sometimes be included in a pretraining mixture. The diagram's lower message is the key exam point: **post-training usually happens after pretraining, not inside the core next-token-prediction objective.**

**Exam-friendly summary**

```text
Traditional: mostly text-only data → next-token prediction

Modern: richer and more diverse data
        → synthetic-data generation and multimodal integration
        → staged training: general knowledge → reasoning → long context
        → post-training: instruction tuning → preference alignment

Core objective throughout pretraining: next-token prediction
```

**One-line memory trick:**

> **Same objective, richer recipe: diverse data → staged training → post-training.**

> **_In practice_** _— how this appears in production._ Real pretraining runs choose a configured sequence length and process fixed-length sequences; short documents may be packed into one sequence with end-of-text separators. Context-window sizes are model- and version-specific, so comparisons should identify the exact model variant. The batch size for gradient descent is large — the biggest GPT-3 model trained with a batch size of **3.2 million tokens** at once, not 3.2 million _examples_.

> **_Going deeper_** _— evaluating beyond loss._ Public benchmarks like **MMLU** (Massive Multitask Language Understanding, 15,908 questions across 57 subject areas) test task performance directly rather than raw next-token loss. Their real weakness is **data contamination**: since LLMs train on scraped web text and MMLU itself is on the web, a model may have seen benchmark questions during pretraining, inflating its score. Published mitigations are reporting train/test overlap directly or holding out contamination-checked splits — a genuine problem that remains unresolved in general for any benchmark built from public text.

---

## Part 2 · Pretraining Data

_If Part 1 explained how the model learns, Part 2 explains what it learns from. This is where the note shifts from objective functions to data engineering: which corpora are used, how they are mixed, and how raw scraped text gets cleaned before it ever reaches the model._

### 2.1 Data Mixture

**Intuition** — What a model reads during pretraining shapes almost everything it can do later. So "just scrape the web" is not a real recipe. The hard part is deciding what kinds of text deserve more weight, what should be filtered out, and whether the model should see all categories in the same proportion from start to finish.

![Data mixture and Llama 3 data selection](assets/S02-data-mixture-and-annealing.png)

**Two levels of data mixture**

- **Global level:** the distribution of the entire pretraining dataset.
- **Local level:** the proportions can be varied at different training stages.

The source uses **Llama 3** as an example. Its knowledge cutoff was the end of 2023, and it downsampled data categories that were over-represented on the public web — for example, **arts and entertainment** — rather than allowing web frequency alone to determine the mixture.

The detailed corpus statistics are tabulated in **Commonly Used Corpora for Pretraining** below. Keeping that table in its own section avoids mixing the source figure's mixture proportions with a separate corpus catalogue whose releases and units may differ.

Data mixture operates at two levels. First, there is the **global mix**: how much of the whole training run comes from web text, books, code, academic text, and so on. Second, there is the **local mix**: whether those proportions change at different stages of training.

_Everyday version:_ a chef doesn't dump a dish together using whatever happens to be most abundant in the pantry. They deliberately measure out more of what actually improves the dish and less of what's simply plentiful, even holding back an ingredient they have a huge supply of if it doesn't earn its place. Data mixture is the same deliberate measuring, applied to a training corpus instead of a pantry.

#### Data Curriculum

**Data curriculum** is the ordering version of the same idea. Instead of asking only "how much of each kind of data?", it asks "in what order should the model see it?" A simple curriculum may start with easy, general examples and progressively introduce more challenging or specialized ones.

![Data curriculum and staged data mixture](assets/S02-data-curriculum.png)

The source uses **Llama 3** to illustrate the result of **data annealing**: it improved the performance of a pretrained **Llama 3 8B** model, while improvements on the **405B** model were negligible. This is the slide's concrete example of the effect of a curriculum/annealing choice; it does not establish that curriculum benefits always shrink with model size.

_Everyday version:_ a curriculum is like teaching from broad fundamentals first and introducing specialized, difficult exercises later. The learner sees a deliberate progression instead of receiving every type of example in a random order.

**Worked example** — If **Stage 1** gives more weight to one data source, **Stage 2** changes the proportions, and later stages continue shifting the mix toward other sources, the model sees a deliberate data schedule rather than a random order. The diagram illustrates this progression through intermediate stages up to **Stage n**; it does not prescribe particular topics for any stage.

**Tradeoff / when NOT to use** — aggressive downsampling or curriculum ordering adds real engineering complexity: you need per-category quality scores, staged schedules, and monitoring for regressions. For a small-scale or research pretraining run without the infrastructure to track category-level provenance, a simpler uniform-sampling approach is a defensible starting point — curriculum tuning is where you spend engineering effort _after_ the basics work, not before.

#### Commonly Used Corpora for Pretraining

| Corpus | Size | Source | Latest update |
| --- | --- | --- | --- |
| BookCorpus | 5 GB | Books | Dec-2015 |
| Gutenberg | — | Books | Dec-2021 |
| C4 | 800 GB | CommonCrawl | Apr-2019 |
| CC-Stories-R | 31 GB | CommonCrawl | Sep-2019 |
| CC-NEWS | 78 GB | CommonCrawl | Feb-2019 |
| REALNews | 120 GB | CommonCrawl | Apr-2019 |
| OpenWebText | 38 GB | Reddit links | Mar-2023 |
| Pushshift.io | 2 TB | Reddit links | Mar-2023 |
| Wikipedia | 21 GB | Wikipedia | Mar-2023 |
| BigQuery | — | Codes | Mar-2023 |
| The Pile | 800 GB | Other | Dec-2020 |
| ROOTS | 1.6 TB | Other | Jun-2022 |

Dataset sizes can differ across releases and may be reported in tokens, bytes, or different filtered versions; do not assume that two entries with the same name refer to exactly the same release.

> **_Going deeper_** _— the ethics and legality of web-scraped pretraining data, a live and unresolved area._ Copyright/fair-use status of training on scraped text is legally ambiguous; a rising share of sites now opt out via `robots.txt` or Terms of Service, with unclear retroactive legal status for data already scraped; private information (phone numbers, emails) leaks through despite filtering; and pretraining corpora skew geographically and demographically toward authors in the United States and other developed countries, which shapes what "default" model behavior looks like globally. None of this is a solved problem — it's an active area of law and policy, not a settled engineering answer.

---

### 2.2 Data Preprocessing Pipeline

**Intuition** — Raw web text is messy. It contains duplicates, boilerplate, bad OCR, spam, private information, broken formatting, and many short fragments that would waste training compute if used as-is. So before the text reaches the model, it has to go through a preprocessing pipeline.

![Data preprocessing pipeline](assets/S02-data-preprocessing-pipeline.png)

**Overview flow shown in the source pipeline**

1. **Raw corpus** — collect the source material.
2. **Filtering and selection** — identify text worth retaining.
3. **De-duplication** — remove repeated or near-duplicate content.
4. **Privacy reduction** — detect and remove personally identifiable information (PII).
5. **Tokenization** — convert text into token IDs using a tokenizer such as SentencePiece or byte-level BPE.
6. **Ready to pretrain** — store the prepared token sequences for model training.

The overview graphic places filtering before de-duplication. The deck then explains the de-duplication bullets on the overview slide, expands **Data Filtering and Selection** on the next slide, and presents **Data Packing** afterward as a separate efficiency technique. Thus, the diagram's processing flow and the deck's explanatory slide order are related but not identical.

#### De-duplication

Low-quality sentences that contain repeated words and phrases can be removed. Word and n-gram (contiguous sequence of `n` tokens) overlap between documents can also flag near-duplicates. This reduces wasted compute and helps with dataset contamination, although separate train/evaluation decontamination is still needed to address benchmark leakage.

#### Data Filtering and Selection

The source presents two broad approaches:

1. **Classifier- and heuristic-based selection**
   - **Binary classifier training:** train a classifier using well-curated positive data.
   - **Language filtering:** remove text not written in the target language.
   - **Metric filtering:** remove unnatural sentences, for example using perplexity.
   - **Statistic filtering:** remove low-quality data using sentence length or punctuation distributions.
   - **Keyword filtering:** remove noisy elements such as HTML, boilerplate, or offensive words.
2. **LLM-based selection**
   - Employ language models, especially relatively small models, for data selection.
   - **Perplexity:** compute perplexity to measure how well text matches the reference model's distribution.
   - **Prompting:** directly prompt an LLM to gauge data importance.

The source cautions that LLM-based selection can be computationally intensive at large scale. For perplexity filtering, a pipeline may retain a middle band: high-perplexity text is often noisy or broken, while very-low-perplexity text can be boilerplate or duplicated templates. The thresholds are corpus- and model-dependent, not universal constants.

Safety filtering is a common additional policy stage. It can remove some clearly harmful content, but it is not perfectly clean or neutral and may reflect the biases of the classifier doing the filtering.

![Data filtering and selection](assets/S02-data-filtering-selection.png)

The concrete Llama 3 model-based curation pipeline is described later under **Model-as-a-Judge for data curation**. It combines heuristic filters, semantic deduplication, and learned quality scoring rather than relying on any single filter.

**Tradeoff / when NOT to use** — perplexity filtering and quality classifiers reduce noise but are themselves imperfect models trained on someone's notion of "quality." Over-aggressive filtering can systematically remove dialects, informal registers, or minority viewpoints that a narrow reference model scores as low-quality text. This is the same class of problem as safety-filter bias.

#### Data Packing

**Packing** combines several short documents into one training window, separated by an end-of-text token, so compute is not wasted on padding. It is an efficiency operation rather than simply another quality filter.

![Data packing](assets/S02-data-packing.png)

_Everyday version:_ think of prepping a big batch of meals for the week. Deduplication is tossing out two of the three identical bags of the same vegetable that you accidentally bought. Quality filtering is checking each item and setting aside anything spoiled or unusable before it goes anywhere near the pan. Packing is fitting several smaller, unrelated leftovers efficiently into one container with explicit boundaries; the boundaries mark where each item ends but do not by themselves prevent interaction between neighboring items.

**Worked example — packing, concretely.** Four unrelated text snippets — one about a sports team, one a fairy tale, one financial news, one a personal story — are concatenated into a single training sequence as: `[sports text] <|endoftext|> [fairy tale] <|endoftext|> [financial news] <|endoftext|> [personal story]`. The boundary token marks document ends so the model can distinguish one document from the next; by itself, however, it does not prevent cross-document conditioning. It also serves as a general sequence-termination token, not only as a packing marker. An implementation may use attention masks or loss masks when strict document isolation is required.

**Tradeoff** — packing usually improves utilization by avoiding padding, but it is not literally free: a single training sequence can contain multiple unrelated documents, so a model must learn to use the end-of-text boundary correctly and not be misled by adjacency, or it risks bleeding context across unrelated packed documents.

---

## Part 3 · Continued Pretraining (CPT) and Domain Adaptation

_Part 3 asks a practical question that comes up in real organizations: once you already have a good pretrained model, how should you adapt it to your own domain? The answer is not always "train from scratch again."_

### 3.1 Continued Pretraining (CPT)

**Intuition** — Once you have a pretrained model, there are several ways to adapt it to a new domain. They are not small variations of the same choice. They trade off cost, speed, and how much of the original broad capability survives.

**Mechanism — the three paths shown in the slide. Let `D1` denote the original/general corpus and `D2` the new domain corpus:**

| Path | What happens | Cost | Keeps general knowledge? |
| --- | --- | --- | --- |
| **Regular pretraining** | Initialize random weights and pretrain on dataset `D1`. | Full pretraining cost | N/A — this _is_ the general model |
| **Continued pretraining (CPT)** | Take the pretrained model from `D1` and further pretrain it on dataset `D2`. | Much cheaper than starting from scratch | Partially — at risk of catastrophic forgetting (Section 3.2) |
| **Retraining on the combined dataset** | Initialize random weights again and train on the union `D1 ∪ D2`. | As expensive as regular pretraining | Yes, by construction — but you pay the full cost again |

![Continued pretraining paths](assets/S02-cpt-training-paths.png)

CPT is the practical middle path in many real systems: much cheaper than full retraining, but still capable of picking up domain knowledge. The price is forgetting risk, which is why the next concept matters.

_Everyday version:_ CPT is like giving a fluent, well-read adult specialist training: the existing general foundation is retained while updates on domain text add specialization, although those updates can interfere with earlier capabilities.

**Worked example** — see Section 3.3's FinLLaMA/BloombergGPT comparison: FinLLaMA is CPT, while BloombergGPT is trained from scratch on a mixed finance-and-general corpus.

**Tradeoff / when NOT to use** — retraining on the combined dataset is generally safer against forgetting but removes the cost advantage CPT provides. Domain-specific pretraining from scratch is introduced in Section 3.3 because it is a separate domain-adaptation route, not one of the three methods compared on this slide.

---

### 3.2 Catastrophic Forgetting

**Intuition** — In sequential learning across diverse datasets or tasks over time, you want an already-capable model to learn new information without destroying what it already knew. That balance is hard. The same updates that help it specialize can also overwrite older knowledge. That failure mode is called **catastrophic forgetting**.

_Everyday version:_ think of cramming hard for a French exam the night before — by morning your French is sharp, but you notice you've become shaky on Spanish vocabulary you knew solidly last month. Your brain didn't have a way to protect the old memory while intensively building the new one, so the new learning partly overwrote it. That's catastrophic forgetting: a model aggressively learning a new domain can overwrite the general knowledge it already had, unless something specifically protects it.

**Mechanism — five mitigations, each attacking the problem differently:**

| Mitigation | How it helps |
| --- | --- |
| **Lower learning rate** | Smaller weight updates disturb existing weights less, so old knowledge is less likely to be overwritten in any single step |
| **Learning-rate (LR) warmup** | Gradually ramp the learning rate up at the start of CPT rather than jumping straight to its target value |
| **Data mixing / replay** | Blend a small percentage of the _original_ pretraining data back into CPT batches, so the model keeps seeing old-domain examples while learning the new domain |
| **EWC** (Elastic Weight Consolidation) | Add a penalty term that selectively slows learning on weights identified as critical to the old task |
| **LoRA / parameter-efficient fine-tuning (PEFT)** | Freeze the base model and train only small adapter parameters; this preserves the base checkpoint, although the active adapter can still change task behavior |

#### LR warmup

The source specifically recommends employing the **exact same learning-rate schedule used during the initial pretraining stage** for continued pretraining.

![Learning-rate warmup during continued pretraining](assets/S02-lr-warmup.png)

_Technical caveat:_ other implementations may adapt the schedule, but that is not what this slide states.

_Two of these are easiest to picture directly:_ **EWC** is like assigning a high cost to changing important whiteboard regions rather than literally preventing changes; **LoRA/PEFT** is like adding a separate layer of notes while leaving the original textbook weights frozen.

**Use case — CPT without replay, in production.** Suppose a bank continues pretraining Llama 3 8B only on internal compliance documents. After enough steps, the model may answer compliance questions better but get noticeably worse at ordinary general-language tasks it previously handled well. That is catastrophic forgetting in action. Mixing some general-domain data back into the batches is often the cheapest way to slow that damage down.

**Additional context — overfitting is different from catastrophic forgetting.** Raschka's own small-scale pretraining run makes overfitting visible even without CPT: training a tiny GPT-style model for 10 epochs on a small corpus shows training loss falling smoothly from 9.78 (epoch 1) to 0.39 (epoch 10), while _validation_ loss falls only until around epoch 8, then rises back up to 6.45 by epoch 10. Roughly 7–8% of the model's generated text at that point turns out to be **verbatim copied** from the tiny training set — the model has started overfitting so hard it is reciting training examples rather than generalizing. This is related to, but distinct from, catastrophic forgetting: overfitting memorizes the current training set, whereas catastrophic forgetting loses previously learned knowledge during later updates.

**Tradeoff / when NOT to use** — every mitigation here costs something. Lower learning rates slow adaptation; replay requires retaining an original-data slice; EWC adds implementation overhead; and LoRA/PEFT freezes the base knowledge, so it cannot by itself update knowledge already present in the base model.

---

### 3.3 Domain Adaptation

**Intuition** — Domain adaptation offers three routes, followed by two domain-specific examples. The source presents the routes first and then compares BloombergGPT with FinLLaMA.

#### Domain-adaptation paths

![Domain adaptation paths](assets/S02-adaptation-paths.png)

The source shows three routes, each with two downstream options:

1. **Regular pretraining from scratch** — train a general pretrained LLM on a large unlabeled corpus, then either use it through **in-context learning** (Option 1) or fine-tune it on labeled target data (Option 2).
2. **Continue pretraining (CPT)** — continue a pretrained LLM on a large domain-specific corpus, then use in-context learning (Option 3) or fine-tune it on labeled target data (Option 4).
3. **Domain-specific pretraining from scratch** — initialize a new model and train it on a domain-specific corpus, then use in-context learning (Option 5) or fine-tune it on labeled target data (Option 6).

The important distinction is that in-context learning changes the prompt without updating weights, whereas fine-tuning updates the model using labeled target data.

#### BloombergGPT and FinLLaMA

| | FinLLaMA | BloombergGPT |
| --- | --- | --- |
| **Approach** | Continued pretraining (CPT) | Trained from scratch on a mixed corpus |
| **Base** | Meta Llama 3 (8B), inheriting general pretrained capabilities | No pretrained base — built from scratch |
| **Parameters** | 8B | 50B |
| **Training data** | 52B financial tokens mixed with 18B general-domain tokens (roughly 75/25) | 363B finance tokens plus 345B general tokens |
| **Forgetting mitigation** | The 18B general tokens provide replay to help preserve Llama 3's original capability | Not applicable in the same sense: general knowledge was built from the start |
| **Sizing rationale** | Inherited from Llama 3's design | Adopted Chinchilla scaling laws; 50B was considered suitable for the available finance-data volume |

**Worked example** — FinLLaMA's 75/25 financial-to-general token ratio is a direct numerical example of data mixing/replay: roughly one in four training tokens is deliberately not finance-specific, helping preserve general capability while the model specializes.

**Tradeoff / when NOT to use** — FinLLaMA's CPT approach is far cheaper because it starts from an 8B checkpoint, but it retains that architecture and capacity. BloombergGPT's from-scratch approach is more expensive but allows model size and data mixture to be selected for the domain.

---

## Part 4 · Scaling Laws

_This part answers the planning question. If pretraining is expensive, how do labs decide how large the model should be and how many tokens it should see? Scaling laws are the attempt to answer that before spending the full compute budget._

### 4.1 Why Scaling Laws?

**Intuition** — Pretraining at frontier scale is too expensive for guesswork. You cannot casually try five different 400B-scale runs and keep the best one. Scaling laws exist because labs need a way to use smaller experiments to predict what larger runs are likely to do.

**Mechanism** — With a fixed compute budget, the design question is how to choose **model size** (`N`) and **dataset size** (`D`) together with the number of **training steps**; total training compute is represented by `C`. The core empirical observation is that loss often follows an approximate power-law trend as these quantities grow within the tested regime. That makes extrapolation possible, but not guaranteed: run smaller proxy experiments, fit the curve, then choose the large-run recipe before paying for the full run.

_Everyday version:_ it is like a bakery testing a recipe in a handful of small batches before committing an entire warehouse of flour and sugar to it. Scaling laws let a lab test how a recipe behaves at small scale before committing the full compute budget.

**Worked example** — Meta ran scaling-law experiments on small proxy models to choose Llama 3's pretraining data mix, then scaled the winning recipe up to 405 billion parameters.

**Tradeoff / when NOT to use** — extrapolation assumes the small-scale trend continues to the target scale, which is not guaranteed. It is most useful when the planned run is genuinely large and expensive; for a small experiment, direct comparison of a few configurations may be simpler.

![Scaling-law planning loop](assets/S02-scaling-planning-loop.png)

---

### 4.2 Three Eras of Scaling Wisdom

**Intuition** — The recommended balance between model size, training data, and compute changed as researchers understood training better. The source presents three eras rather than one timeless rule.

**Landscape — three eras, compared:**

| Era | Year | Rule of thumb | Exemplar | Numbers |
| --- | --- | --- | --- | --- |
| **Kaplan** | 2020 | Scale the model faster than the data | GPT-3 | 175B parameters · 300B tokens (~1.7 tokens/parameter) |
| **Chinchilla** | 2022 | About 20 tokens per parameter; existing giants were undertrained | Chinchilla | 70B parameters · 1.4T tokens (~20 tokens/parameter) |
| **Modern** | 2024+ | Overtrain a smaller model when inference cost dominates | Llama 3 8B | 8B parameters · 15T tokens (~1,875 tokens/parameter) |

The comparison shows why the rule changed. Kaplan emphasized using additional compute for a larger model. Chinchilla showed that many large models were **undertrained** relative to their size and that model size and data should grow together under its compute-optimal assumptions. Modern frontier recipes may deliberately train a smaller model on far more data because a model served billions of times incurs recurring inference cost.

The source comparison also gives examples of earlier models:

| Model | Size | Training tokens |
| --- | --- | --- |
| LaMDA (Thoppilan et al., 2022) | 137B | 168B |
| GPT-3 (Brown et al., 2020) | 175B | 300B |
| Jurassic (Lieber et al., 2021) | 178B | 300B |
| Gopher (Rae et al., 2021) | 280B | 300B |
| MT-NLG 530B (Smith et al., 2022) | 530B | 270B |
| Chinchilla | 70B | 1.4T |

Chinchilla's 70B model, trained compute-optimally, beat GPT-3 (175B), Gopher (280B), and MT-NLG (530B), illustrating the cost of undertraining a very large model.

A newer axis is **test-time compute**. Models such as o1 and DeepSeek-R1 spend additional compute at inference on generated reasoning steps. Modern scaling discussions therefore consider both training-time and inference-time compute.

**Worked example** — Llama 3 8B trained on 15T tokens is roughly 90 times the Chinchilla-recommended ratio of 20 tokens per parameter for an 8B model. That is consistent with deliberate overtraining, but the ratio alone does not prove that inference economics was the sole reason.

**Tradeoff / when NOT to use** — Chinchilla-style compute optimality is appropriate when training compute dominates. Overtraining a smaller model is attractive only when repeated serving makes inference cost important; for a model trained once and used lightly, the extra training data may not pay back.

![Three eras of scaling wisdom](assets/S02-three-eras-scaling.png)

_The detailed Kaplan equations and parameter-count derivation are intentionally routed to **Extra Slides §6.1**, and the detailed Chinchilla law is routed to **Extra Slides §6.2** so that the main scaling discussion stays focused on the three-era comparison and emergent abilities._

---

### 4.3 Emergent Abilities of LLMs

**Intuition** — Some capabilities appear to improve sharply once a model crosses a certain scale instead of following an obviously smooth curve. Whether this is a genuine property of scale or a measurement artifact is an active debate.

**Mechanism.** In this literature, an ability is called emergent when it is absent in smaller models but present in larger ones. Sharpness, chance-level performance, and difficulty of prediction are additional empirical claims, not consequences of the minimal definition. The Schaeffer et al. critique argues that some apparent emergence becomes a smooth curve when measured with a different metric or better statistics.

![Emergent abilities of LLMs](assets/S02-emergent-abilities.png)

**Examples.** The source lists three commonly discussed examples:

1. **In-context learning** — the model adapts its behavior from examples in the prompt without gradient updates.
2. **Instruction following** — behavior usually substantially shaped by instruction tuning rather than pretraining alone.
3. **Step-by-step reasoning** — may depend on prompting, generated intermediate steps, and the evaluation metric.

These are debated examples rather than three identical mechanisms. Treat an apparent scale threshold as an empirical claim to test, not as a guaranteed capability that will appear at a particular parameter count.

**Worked example** — An exact-match benchmark can make a smooth improvement look like a sudden jump, while a partial-credit metric may reveal the underlying gradual improvement.

**Tradeoff / when NOT to use** — do not make an unconfirmed emergent ability a load-bearing assumption in a scaling plan. Check whether the effect survives alternative metrics and statistical analyses.

---

## Part 5 · Pretraining of popular frontier models

### 5.1 Model case studies

_The source uses this as a divider for concrete frontier-model recipes. The following subsections preserve the deck's order._

### 5.2 Llama 3 Models: 3-stage pretraining process

**Intuition** — Llama 3's published recipe is a concrete frontier-scale example of how preprocessing, pretraining, post-training, and optimization can appear in one model-development pipeline.

The source introduces the recipe's named components: filtering, synthetic data, a Q&A format, a long-context stage, a high-quality stage, continued pretraining, and knowledge distillation. These labels describe components of the published recipe; they are not a universal mandatory sequence for every LLM.

![Llama 3 three-stage pretraining process](assets/S02-llama3-three-stage-pretraining.png)

### 5.3 Llama 3 Models: 3-stage pretraining process — schedule details

The detailed schedule increases configuration gradually rather than jumping directly to the final setup:

1. **Initial pretraining** — dynamic batch size and sequence length increase across three phases: 4M tokens at 4,096-token sequences; 8M tokens at 8,192-token sequences; then 16M tokens at 8,192-token sequences. The recipe uses AdamW.
2. **Long-context pretraining** — context length grows across six stages from 8K to 128K tokens, using approximately 800B tokens for the extension.
3. **Annealing** — the final stage uses a small, ultra-high-quality math-and-code subset while decaying the learning rate toward zero.

The source reports an annealing dataset of **40B tokens**, described as **0.02%** of the total dataset and used to assess data quality. It says the actual annealing used **40M tokens**, or **0.1%** of that annealing dataset. These percentages are source-reported; retain the token counts and do not infer a different total-dataset ratio from them without resolving the source's denominator.

_The recipe's gradual increases are a frontier-scale engineering choice, not a requirement that every model use these exact batch sizes or context stages._

**Worked example** — The per-step batch size increases from 4M to 16M tokens, a 4× increase executed in phases to reduce instability risk.

**Tradeoff / when NOT to use** — gradual scaling and six-stage context extension add scheduling and engineering complexity. They are easier to justify for a very expensive frontier run than for a small research run.

### 5.4 Model-as-a-Judge for data curation (Llama 3)

Llama 3's model-as-a-judge pipeline is a concrete example of the filtering and selection stage in Part 2. The source names model-based quality judgments and the models used in the curation pipeline, including fastText, RoBERTa, Llama 2, and DistilRoBERTa, together with semantic deduplication.

![Model-based data curation pipeline](assets/S02-model-based-curation.png)

### 5.5 Qwen 2 pretraining

Qwen 2 uses the previous-generation Qwen model to synthesize additional pretraining data and includes multi-task instruction data. Its two-stage recipe consists of regular pretraining followed by long-context training, growing context length from 4,096 to 32,768 tokens with high-quality lengthy data.

![Qwen 2 frontier pretraining recipe](assets/S02-frontier-recipes.png)

### 5.6 Qwen 3: 3-stage pretraining process

The source presents Qwen 3 as a three-stage pretraining process:

1. **General pretraining** — broad language ability with **30T+ tokens**, a **4K context**, and **119 languages**.
2. **Reasoning and STEM focus** — reasoning data with **5T+ tokens**, more STEM/code data, and synthetic data.
3. **Long-context annealing** — a **32K context**, long documents, and longer dependencies.

The high-quality long-context corpus is **75%** text between 16,384 and 32,768 tokens and **25%** text between 4,096 and 16,384 tokens.

The process diagram is kept separate from the following data-acquisition and labeling section.

![Qwen 3 three-stage pretraining](assets/S02-qwen3-three-stage-pretraining.png)

### 5.7 Qwen 3 pretraining data

Qwen 3 doubled Qwen 2.5's corpus from 18T to **36T (36 trillion) tokens** and expanded coverage from 29 to **119 languages/dialects**. Qwen2.5-VL supported high-quality PDF extraction; Qwen2.5, Qwen2.5-Math, and Qwen2.5-Coder generated synthetic textbooks, Q&A, instruction manuals, and code snippets.

More than **30T (30 trillion) labeled tokens** were used for educational value, fields/domains, and safety, with filtering, data combination, and instance-level data-mixture optimization. Context length is therefore also a data-mixture lever, not only a training-schedule setting.

![Qwen 3 pretraining data](assets/S02-qwen3-pretraining-data.png)

### 5.8 Gemma 2 pretraining

Gemma 2 argues that smaller models may be **undertrained**, not merely under-sized. The 27B model trains from scratch, while smaller Gemma 2 models use **knowledge distillation** from the larger model rather than simply scaling down the data recipe.

![Gemma 2 pretraining](assets/S02-gemma2-pretraining.png)

### 5.9 Gemma 4

Gemma 4 is presented as a multimodal, long-context, dual-track release. It includes pretrained **base** models trained on a massive, diverse dataset containing web, code, math, images, and audio for further specialized training, and separate **instruction-tuned** models trained further on human-annotated data to follow instructions, support multi-turn conversation and system prompts, and provide native function calling, structured JSON output, and safety filters. The pretraining corpus spans **140 languages**.

### 5.10 Cross-model comparison (synthesis)

| Model | Key pretraining idea | Detail |
| --- | --- | --- |
| **Llama 3** | Staged frontier pretraining and data curation | Three-stage schedule, long-context extension, annealing, filtering, synthetic data, and model-as-a-judge curation |
| **Qwen 2** | Self-generated training data and long-context training | Previous-generation Qwen data synthesis; 4,096 → 32,768 context growth |
| **Qwen 3** | Long-context-weighted corpus and instance-level mixture optimization | Three-stage process, 36T tokens, 119 languages/dialects, labeled data, and 75/25 long-context mixture |
| **Gemma 2** | Knowledge distillation over scale | 27B model from scratch; smaller variants distilled from the larger model |
| **Gemma 4** | Multimodal, long-context, dual-track release | Base and instruction-tuned models, native tool/structured-output features, 140 languages |

_Two ideas map onto familiar teaching patterns:_ Gemma 2's **knowledge distillation** is like a master teacher writing a condensed study guide, while Qwen 2's **self-generated data** is like a teacher writing practice questions from their own memory. The second approach can reproduce the teacher's blind spots unless carefully filtered.

**Worked example** — Qwen 3's 75/25 split controls context-length distribution; Llama 3's annealing selects a small high-quality subset late in training; FinLLaMA's 75/25 split mixes finance and general-domain tokens during CPT. These are explicit sampling decisions on different axes.

**Tradeoff / when NOT to use** — knowledge distillation requires a capable teacher and is not a way to train the first largest model in a family. Self-generated data can reinforce a model's blind spots unless quality-controlled.

---

## Extra Slides (not for exam)

_These slides are historical and supplementary. Their order is preserved separately from the examinable sequence: divider → Kaplan/Chinchilla details → GPT-1 → T5._

### 6.1 Kaplan scaling-law details

Kaplan et al. (2020) reported approximate power laws for loss as model size, dataset size, and compute increase:

```
L(N) = L∞ + (N_c / N)^αN        αN = 0.076, N_c = 8.8 × 10¹³
L(D) = L∞ + (D_c / D)^αD        αD = 0.095, D_c = 5.4 × 10¹³
L(C) = L∞ + (C_c / C)^αC        αC = 0.050, C_c = 3.1 × 10⁸
```

Here `N` is the number of non-embedding parameters, `D` is dataset size in tokens, `C` is compute in petaflop-days, `L∞` is the irreducible loss floor, and each `_c` is an empirically fitted scaling coefficient. The exponent `α` (alpha) controls how quickly loss changes with scale.

The source also gives a parameter-count approximation when attention and feedforward dimensions scale together (`d_attn = d_ff / 4 = d`):

```
N ≈ 12 · n_layer · d²
```

For GPT-3, `n_layer = 96` and `d = 12,288`:

```
N ≈ 12 × 96 × 12,288²
  = 1,152 × 150,994,944
  ≈ 174.0 billion parameters
```

This is close to GPT-3's well-known ~175B parameter count.

### 6.2 Chinchilla-law details

Chinchilla showed that many large models were **undertrained** relative to their size. Where the earlier Kaplan rule of thumb suggested scaling model size faster than data, Chinchilla found that model size and data should grow at roughly the same rate under its compute-optimal assumptions. With a 10× compute increase, both model size and data increase by roughly 3.1×. The paper's practical rule of thumb was about **20 training tokens per parameter**, not a universal minimum.

The source comparison is:

| Model | Size | Training tokens |
| --- | --- | --- |
| LaMDA | 137B | 168B |
| GPT-3 | 175B | 300B |
| Jurassic | 178B | 300B |
| Gopher | 280B | 300B |
| MT-NLG | 530B | 270B |
| Chinchilla | 70B | 1.4T |

Chinchilla's 70B model beat GPT-3, Gopher, and MT-NLG despite having fewer parameters, because those larger models were comparatively undertrained. Modern recipes may still exceed the Chinchilla ratio when recurring inference cost makes a smaller, heavily trained model preferable.

### 6.3 GPT-1 innovations

**GPT-1** is an early decoder-only pretraining recipe. It introduced a two-stage workflow: unsupervised generative pretraining on a large corpus followed by supervised fine-tuning on a task. GPT-1 uses unidirectional causal attention over left context. Its architecture has 12 transformer blocks, 768-dimensional hidden states, 12 attention heads, a 3,072-dimensional feedforward layer, about 117 million parameters, a 40,000-token byte-pair encoding (BPE) vocabulary, and GELU activations.

### 6.4 GPT-1 input and sequence details

Preprocessing used `ftfy` and spaCy on BooksCorpus. Tokenization used byte-pair encoding (BPE). Sequences were truncated or padded to 512 tokens. GPT-1 used learned positional embeddings, scaled dot-product self-attention, and 64-dimensional query, key, and value projections per head (`768 ÷ 12 = 64`).

### 6.5 GPT-1 training setup

Training used causal language modeling with cross-entropy, batches of 64 sequences, sequence length 512, Adam, 2,000-update linear warmup followed by cosine decay, 0.1 attention dropout, modified L2 regularization, 100 epochs, and a softmax output layer.

### 6.6 GPT-1 fine tuning

For downstream **fine tuning**, GPT-1 retained the unsupervised pretraining hyperparameters, added classifier dropout of 0.1, used a learning rate of `6.25e-5` (`6.25 × 10⁻⁵`), batch size 32, **3 epochs**, linear learning-rate decay with warmup over 0.2% of updates, and task-loss weight `lambda = 0.5` (`λ = 0.5`).

### 6.7 GPT-1 downstream tasks

The source labels this section **LLM downstream tasks: GPT-1**. For classification, the input is formatted with special tokens such as `<start>`, `<delim>`, and `<extract>`. The same pretrained decoder-only transformer is used, and the output vector at `<extract>` is fed into a small classifier. During fine-tuning on labeled task data, the classifier learns to map that representation to a label such as `Positive`.

![GPT-1 downstream classification task](assets/S02-gpt1-classification.png)

### 6.8 T5 overview

**T5** (Text-to-Text Transfer Transformer; Raffel et al., 2020) is an encoder-decoder model. Its central design is to reformulate NLP tasks as text-to-text problems, allowing one model and one output interface to handle different tasks.

### 6.9 T5 input-output formulation

A uniform text-to-text interface lets the same encoder-decoder model receive text and produce text for different downstream tasks. The concrete translation and MNLI examples are given in the following sections.

![T5 text-to-text task pattern](assets/S02-t5-text-to-text-pattern.png)

### 6.10 T5 attention and Prefix LM

The encoder uses bidirectional self-attention; the decoder uses causal self-attention plus cross-attention to encoder outputs.

The Prefix LM discussion distinguishes **fully-visible** attention from causal masking.

![T5 encoder and prefix-language-model attention](assets/S02-t5-attention-patterns.png)

![T5 attention masks](assets/S02-t5-attention-masks.png)

### 6.11 T5 C4 corpus and baseline design

The baseline uses two BERT-base-sized stacks and the English-only C4 corpus, filtered with `langdetect`. T5 removes LayerNorm bias, places layer normalization outside the residual path, and uses learned relative position embeddings based on key-query offsets. Its maximum-likelihood objective with teacher forcing is used during both pretraining and fine-tuning.

### 6.12 T5 task-specific prefix and translation example

To specify which task the model should perform, a task-specific text prefix is added to the original input sequence. The translation example is `translate English to German: That is good. target:` → `Das ist gut.`

### 6.13 T5 MNLI benchmark example

For MNLI, the decoder emits one of the text labels `entailment`, `contradiction`, or `neutral`. This is text-to-text prediction rather than a separate BERT-style classification head.

### 6.14 T5 vocabulary and multilingual fine-tuning data

T5 uses a shared **32,000-wordpiece SentencePiece vocabulary** for input and output. Fine-tuning samples English, German, French, and Romanian at a **10:1:1:1** ratio.

### 6.15 T5 baseline pretraining details

The T5 baseline uses two BERT-base-sized stacks with about **220 million parameters**, batch size 128 sequences, sequence length 512, an inverse-square-root learning-rate schedule with `k = 10⁴` warm-up steps, AdaFactor, dropout 0.1, and greedy decoding at test time. Its pretraining budget is `2¹⁹` steps × `2¹⁶` tokens per step = `2³⁵` tokens, about 34B, much smaller than BERT's 137B and RoBERTa's 2.2T tokens.

### 6.16 T5 baseline fine-tuning details

The baseline fine-tuning setup uses batch size 128, sequence length 512, a constant learning rate of `0.001`, and 5,000 steps per checkpoint. Its fine-tuning budget is `2¹⁸` steps × `2¹⁶` tokens per step = `2³⁴` tokens.

### 6.17 T5 fine-tuning downstream tasks

The source lists these downstream tasks:

- **Text classification:** GLUE and SuperGLUE, collections of text-classification tasks testing general language understanding.
- **Abstractive summarization:** CNN/Daily Mail.
- **Question answering:** SQuAD.
- **Translation:** WMT English to German, French, and Romanian.

### 6.18 GPT-1 and T5 comparison (synthesis)

| | GPT-1 | T5 |
| --- | --- | --- |
| Architecture | Decoder-only | Encoder-decoder |
| Parameters | ~117 million | Baseline: two BERT-base-sized stacks; ~220M in the baseline details |
| Objective | Causal language modeling | Text-to-text; every task uses the same text interface |
| Pretraining data | BooksCorpus (~7,000 books, ~800M words) | C4 — 750 GB, English-only |
| Attention pattern | Pure causal | Bidirectional encoder self-attention; causal decoder self-attention plus cross-attention |
| Position encoding | Learned absolute | Learned relative, based on query-key offsets |
| Vocabulary | 40,000 tokens, BPE | 32,000 wordpieces, shared SentencePiece input/output |
| Downstream task handling | `<extract>` vector → linear classifier | Task prefix in input text; output is text |

---

## Self-study / Lab / Build

Lab 2 ("Build end-to-end training and fine-tuning pipelines," module M2–M5) is the natural place to reproduce this session's central worked example: the cross-entropy loss calculation in Section 1.3, `LLM training`, extended into a full `train_model_simple()`-style loop — forward pass, loss, backward pass, optimizer step, periodic train/val loss logging — run against a corpus small enough to watch it overfit on purpose (matching the training log in Section 3.2, `Catastrophic Forgetting`: training loss falling smoothly while validation loss flattens then rises). Reproducing that overfitting curve by hand, once, is worth more than reading about catastrophic forgetting in the abstract.

---

_Exam: this session is in scope for the **closed-book mid-sem** (sessions 1–8). Full evaluation, weights, dates, and course logistics are documented in [`536-master.md`](../536-master.md) and are not repeated in each session note._
