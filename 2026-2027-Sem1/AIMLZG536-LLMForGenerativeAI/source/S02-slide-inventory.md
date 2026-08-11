# 536 · S02 slide inventory

Derived index of the session-2 deck (`CS-2 LLM Training.pptx`), captured at intake so coverage can be re-checked without re-uploading the deck. Slide numbers, titles, and the named items on each slide only — no slide prose.

Verify with:

```bash
cd tools && node check-slide-coverage.mjs \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/source/S02-slide-inventory.md \
  ../2026-2027-Sem1/AIMLZG536-LLMForGenerativeAI/notes/S02-pretraining.md
```

| Slide | Title | Named items |
|---|---|---|
| 1 | Dr. Monali Mavani | Large, Models |
| 2 | Large Language Models for Generative AI | Large, Models |
| 3 | Agenda | Adaptation, CPT, Domain, Laws, LLM, Objectives, Pre, Pre-training, Pretraining, Scaling |
| 4 | Building a large language model | Building, Picture |
| 5 | Model learns the structure of language simply by reading vast amounts | BERT, GPT, Learning, Model, Picture, Self-Supervised |
| 6 | Pre-training Objectives | Causal, CLM, Masked, MLM, Modeling, Objectives, Picture, Pre-training |
| 7 | LLM training | LLM |
| 8 | Modern LLM development and training pipeline | LLM, Modern |
| 9 | Modern pre-training | Modern, Picture |
| 10 | Data mixture | Downsample, Global, Knowledge, Llama, Picture |
| 11 | Data Curriculum | Curriculum, Llama, LLMs, Picture |
| 12 | Commonly Used Corpora for Pre-training | Commonly, Corpora, Picture, Pre-training |
| 13 | Data Preprocessing pipeline | Helps, Picture, Preprocessing |
| 14 | Data Filtering and Selection | Filtering, Keep, Perplexity, Picture, PPL |
| 15 | Data Packing | Packing, Picture |
| 16 | Continued Pre-training (CPT) | Continued, CPT, Picture, Pre-training, Regular, Retraining, Taking |
| 17 | Catastrophic forgetting | Catastrophic, Consolidation, Elastic, EWC, LoRA, Lower, PEFT, Weight |
| 18 | LR warmup |  |
| 19 | Domain Adaptation | Adaptation, CPT, Domain, Domain-Specific, FinLlama, Picture, Pre-training, Regular |
| 20 | Domain Adaptation | Adaptation, Base, BloombergGPT, Catastrophic, Chinchilla, CPT, Domain, Domain-Specific, Forgetting, Llama, Meta, Model, Pre-training, Strategy, Trained |
| 21 | Model case studies | Model |
| 22 | Llama 3 Models: 3-stage pretraining process | Llama, Models, Picture |
| 23 | Llama 3 Models: 3-stage pretraining process | AdamW, Annealing, Batch, Early, Gradual, Increased, Initial, Length, Llama, Models, Phase, Practice, Scaling, Sequence, Size, Stability, Stable |
| 24 | Model-as-a-Judge for data curation (Llama 3) | DistilRoBERTa, Llama, Meta, Model-as-a-Judge, Picture, RoBERTa-family, Wikipedia |
| 25 | Qwen 2 pretraining | Picture, Qwen, Training, Use |
| 26 | Qwen 3 : 3-stage pretraining process | High, Picture, Qwen |
| 27 | Qwen3 Pretraining Data | Picture, Pretraining |
| 28 | Gemma 2 pre training | Gemma, Picture, Small, Smaller |
| 29 | Gemma 4 | Base, Gemma, Instruction-Tuned, JSON, Models, Native, Released, Trained |
| 30 | Why scaling laws? | Dataset, Fit, INSIGHT, LLAMA, Lock, Loss, Meta, Model, PRACTICE, Predictable, QUESTION, Set, Test, THE, Training |
| 31 | Three eras of scaling wisdom | AND, AXIS, Beat, Big, Chinchilla, COMPUTE, DeepSeek-R1, EXEMPLAR, Existing, Gopher, GPT-3, Inference, Kaplan, Llama, Modern, MT-NLG, NEW, Overtrain, RULE, Scale, TEST-TIME, THUMB |
| 32 | Emergent abilities of LLMs | Ability, Appearing, Emergent, LLMs, Picture, Schaeffer, Sharpness, Unpredictability |
| 33 | Emergent abilities of LLMs | Emergent, Formally, GPT-3, In-context, Instruction, LLMs, Step-by-step |
| 34 | References | Abilities, BloombergGPT, Build, Ch-2, Chinchilla, Compute-Optimal, Dan, Emergent, Finance, Herd, HuggingFaceTB, Jan, Jurafsky, Kaplan, Large, Laws, Llama, Mirage, Model, Models, RASCHKA, Report, Research, Scaling, Scratch, SEBASTIAN, Speech, Survey, Technical, Training |
| 35 | Extra Slides (not for exam) | Extra |
| 36 | Scaling Laws - Kaplan et al., 2020 | GPT-3, Kaplan, Laws, Led, Performance, Picture, Scaling |
| 37 | Kaplan laws | Chinchilla, Hoffmann, Kaplan, Laws, Rule, Scaling, Showed, Thumb |
| 38 | Innovations | Activation, Architecture, Attention, BERT, Context, Encoding, Error, Feedforward, GELU, GPT-1, Heads, Hidden, Key, Layers, Linear, Model, Network, Number, Pair, Parameters, Pre-training, Pretraining, Size, Unit, Vocabulary |
| 39 | Input and Sequence Details | Attention, BooksCorpus, BPE, Encoding, GPT-1, Input, Length, Mechanism, Pair, Pre, Sequence, Uses |
| 40 | Training Setup | Adam, Batch, BooksCorpus, Causal, Cosine, Cross-Entropy, Dataset, GPT-1, Learning, Length, Linear, Loss, Modeling, Next-Token, Objective, Optimizer, Output, Prediction, Rate, Schedule, Sequence, Size, Training, Uses |
| 41 | Fine tuning | Fine, GPT-1, Same |
| 42 | LLM downstream  tasks: GPT-1 | Extract, Feed, GPT-1, Idea, Input, Linear, LLM, Output, Pass, Positive, Start, Take, Transformer |
| 43 | T5 (Text-to-Text Transfer Transformer) | Baseline, Encoder-Decoder, Lee, NLP, Pre-train, Raffel, Same, Text-to-Text, Transfer, Transformer |
| 44 | T5 (Text-to-Text Transfer Transformer) | Baseline, Encoder-Decoder, Lee, NLP, Pre-train, Raffel, Same, Text-to-Text, Transfer, Transformer |
| 45 | T5 Attention – Prefix LM | Attention, Causal, Das, English, Fully-visible, German, Input, Output, Prefix, Sequence, Target |
| 46 | Proposed “Colossal Clean Crawled Corpus” (C4) , 750 GB, the Common Cra | Attention, Baseline, Clean, Colossal, Common, Corpus, Crawled, Datasets, English, Layer, Learned, Norm, Roughly, TensorFlow, Transformer |
| 47 | To specify which task the model should perform, a task-specific (text) | Das, English, Example, German, Input, Output, Prefix, Training |
| 48 | MNLI benchmark example (Multiclass classification with 3 classes ‘enta | BERT, Hypothesis, Input, Label, MNLI, Output, Prefix, Premise, T5-, Transformer |
| 49 | 49 | English, French, German, Pre-training, Romanian, SentencePiece, T5-, Trained, Vocabulary |
| 50 | T5- Baseline (Pre-training details) | Baseline, Pre-training, T5- |
| 51 | Batch Size: 128 | Baseline, Batch, Fine-tuning, Length, Size, T5-, Training |
| 52 | Text classification: GLUE and SuperGLUE (collection of text classifica | Abstractive, CNN, Daily, Downstream, English, Fine-tuning, French, German, GLUE, Mail, Romanian, SuperGLUE, T5-, Translation, WMT |
