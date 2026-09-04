# Assignment 1A — Full Execution Plan

**Course:** AIML ZG536 · **Marks:** 15 (Part A 10 · Part B 5) · **Crew:** 4
**Effort:** ~2.5–3 working days

> ⚠️ **The brief sets no deadline.** Neither PDF in this folder states a submission date.
> Confirm it on Canvas or the Ops mail. The schedule in §5 is relative — compress or spread it
> to fit whatever date you're given.

**Sourced only from the two briefs in this folder.** The 4-person split is our own constraint;
the brief does not specify a group size.

---

## Contents

| § | Section |
|---|---|
| 1 | [What we are building](#1--what-we-are-building) |
| 2 | [Prerequisites](#2--prerequisites) |
| 3 | [Decisions to lock](#3--decisions-to-lock) |
| 4 | [Who owns what](#4--who-owns-what) |
| 5 | [Schedule](#5--schedule) |
| 6 | [**The eight steps**](#6--the-eight-steps) ← the actual work |
| 7 | [Submission](#7--submission) |
| 8 | [Risk register](#8--risk-register) |

---

## 1 · What we are building

One pipeline, eight graded steps:

```
domain PDFs
   │
   ├─ Step 1  extract + clean          → domain_corpus/*.txt
   ├─ Step 2  tokenize + pack          → packed_train/eval.parquet
   ├─ Step 3  load model + audit       → baseline_generations.json
   ├─ Step 4  CPT training             → cpt_ckpt/
   ├─ Step 5  perplexity + forgetting  → ppl_results.json
   │
   ├─ B1      instruction dataset      → instruction_dataset.jsonl
   ├─ B2      QLoRA adapter            → adapter/
   └─ B3      final evaluation         → observations
```

Part A turns a general model into one that **speaks your domain** (CPT). Part B turns that into
one that **answers questions** in it (QLoRA instruction tuning).

---

## 2 · Prerequisites

🕒 = needs lead time, start at hour zero.

**Accounts & access**
- 🕒 Hugging Face account + access token
- 🕒 Licence acceptance for gated models — see warning below
- Compute: T4 (16 GB, free Colab) for the small-model column, or A100 / L40S (BITS remote lab) for the 7–8 B column
- Persistent storage — Step 4 says save the checkpoint there; a Colab session disk does not survive a disconnect
- External LLM access, only if B1 uses synthetic generation

> 🔴 **Gated on Hugging Face** — will not download until you accept the terms, approval takes
> minutes to a day: `mistralai/Mistral-7B-v0.1` · `meta-llama/Meta-Llama-3-8B` · `google/gemma-7b`
>
> **Ungated:** `Qwen/Qwen2.5-*` · `HuggingFaceTB/SmolLM2-*` · `TinyLlama/TinyLlama-1.1B-*` ·
> `openai-community/gpt2-*` · `microsoft/biogpt-large` · `stanford-crfm/BioMedLM`

**Libraries** — `transformers`, `peft`, `bitsandbytes`, `trl`, `torch` (all named in the brief);
plus a PDF extractor (`pypdf`/`PyMuPDF`/`pdfplumber`), `pyarrow`/`pandas` for Parquet,
`matplotlib` for the loss curve, `langdetect`/`fasttext` for the English filter.

**Verify every import before Step 1 begins.** `bitsandbytes` fails at *import*, not install.

---

## 3 · Decisions to lock

45 minutes, all four. Changing any of these later costs a re-run.

1. **Variant + domain** — V1–V6, or custom.
   🔴 A custom use case **adds a fifth deliverable**: its template in the V2–V6 format, submitted
   as a separate doc. Pick V1–V6 and that requirement disappears.
2. **Model** — one id, used in Steps 2, 3, 4 and B2. Check gating first.
   **Recommended: `Qwen/Qwen2.5-1.5B`** — ungated, ships a ChatML chat template (B2 needs one),
   and full-parameter CPT fits comfortably. A 7B needs ~80 GB with optimizer states.
3. **Three domain prompts** — locked forever. Used in Step 3, Step 4 and B3.
4. **Three general prompts** — for Step 5B (capital of France / water boils at / speed of light).
5. **Instruction-dataset size** — brief says only "suitable size". Fix it now: **500 pairs → 400 / 100**.
6. **Filenames** — exactly as written in §6.

---

## 4 · Who owns what

| | Owner | Steps | Marks |
|---|---|---|---|
| **P1** | Corpus & Instruction Data | Step 1 · B1 | 4 |
| **P2** | Packing & CPT Training | Step 2 · Step 4 | 4 |
| **P3** | Model Audit & Evaluation | Step 3 · Step 5 | 4 |
| **P4** | QLoRA & Submission | B2 · B3 · notebook assembly | 3 + integration |

---

## 5 · Schedule

| Block | Effort | P1 | P2 | P3 | P4 |
|---|---|---|---|---|---|
| **1** Setup | 3–4 h | Step 1 — first 5 files | write Step 2 script | **Step 3 complete** | verify imports, notebook skeleton |
| **2** Train | 1 day | Step 1 done → handoff | **Step 2, then Step 4** | Step 5A base PPL → **Step 5 done** | assemble Steps 1–3 |
| **3** Tune | 1 day | **B1 done** | — | write Step 5 inferences | **B2, then B3** |
| **4** Ship | ½ day | inferences | inferences | inferences | run notebook top-to-bottom, export HTML |

> **Block 1 gate:** a 20-step CPT run on 5 documents must complete before Block 1 closes. The
> output is worthless — the point is flushing out environment bugs while there's recovery room.

**Step 4 must finish in Block 2.** Steps 5, B2 and B3 are all blocked behind that checkpoint.

---

## 6 · The eight steps

---

### Step 1 — Data Collection, Extraction & Cleaning · 2 marks · P1

**Produces:** `domain_corpus/*.txt`, `cleaning_stats.json`

**Do this:**
1. Download 8–10+ domain PDFs from your variant's listed sources into `raw_pdfs/`.
2. Extract text **page-by-page** (the brief's wording) with `pypdf` / `PyMuPDF`; join the pages
   and write **one `.txt` per PDF** into `domain_corpus/`.
3. Record the raw document count.
4. **Length filter** — drop documents under a threshold (e.g. 1 000 characters). Record the count after.
5. **Deduplication** — exact hash, or near-duplicate via MinHash/shingles. Record the count after.
6. **Language filter** — `langdetect`, keep `en` only. Record the count after.
7. *Optional but worth marks:* the brief says the pipeline is "not confined to the following".
   Add one more step — strip repeated headers/footers, drop boilerplate pages, normalise
   whitespace — and justify it. That justification is exactly the "inference" the rubric wants.
8. Write `cleaning_stats.json` with every count.

**Report:** document counts **before and after each step**, and **which step had the greatest
impact** on corpus size.

**Done when:** cleaned `.txt` files exist, stats are recorded, and a short paragraph explains
which filter dominated and why that makes sense for your domain.

---

### Step 2 — Tokenization & Packed Dataset · 2 marks · P2

**Needs:** Step 1 output · **Produces:** `packed_train.parquet`, `packed_eval.parquet`, `pack_stats.json`

**Do this:**
1. `tok = AutoTokenizer.from_pretrained(MODEL_ID)` — the **same** id as Step 3. Never train a
   custom tokenizer; the brief is explicit that reusing the pretrained one preserves vocabulary
   alignment during CPT.
2. For each `.txt`: `ids = [tok.bos_token_id] + tok(text).input_ids + [tok.eos_token_id]`.
   BOS/EOS mark document boundaries inside the packed stream.
3. Concatenate every document's ids into **one flat list**.
4. Slice that stream into fixed-length chunks equal to the model's **context window**
   (`config.max_position_embeddings`). Drop the trailing remainder. No padding — that's the point
   of packing, and it's what gives full GPU utilisation.
5. Hold out **10%** of the chunks as the evaluation split (Step 5A needs it, and it must never be
   seen in training). Remaining 90% is training.
6. Save both as **Parquet**.

**Report:** total token count · average document length in tokens · total number of packed sequences.

**Done when:** both Parquet files exist and the three figures are printed.

---

### Step 3 — Model Loading & Architecture Inspection · 2 marks · P3

**Produces:** `baseline_generations.json`

**Do this:**
1. `model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.bfloat16)`.
   **On T4 the brief also requires** `model.gradient_checkpointing_enable()`. On A100 either
   full precision or bf16 is fine.
2. **Parameter count** — `sum(p.numel() for p in model.parameters() if p.requires_grad)`.
3. **Architecture audit** from `model.config`: `num_hidden_layers` (decoder layers),
   `num_attention_heads`, `hidden_size`, and head dim = `hidden_size // num_attention_heads`.
4. **`lm_head` check** — confirm `model.lm_head.out_features` equals `config.vocab_size`. This is
   the sanity check that your tokenizer and model actually match.
5. **Baseline inference** — generate on the 3 locked **domain** prompts and save the text; this is
   the "before" evidence you compare against later.
   *Also generate on the 3 **general** prompts now, while the base model is loaded* — Step 5B needs
   base-model general outputs, and doing it here saves a reload.

**Report:** trainable parameters · layers, heads, hidden size, head dim · the `lm_head` confirmation
· the baseline generations.

**Done when:** `baseline_generations.json` holds 6 outputs (3 domain + 3 general) and the audit
figures are printed.

---

### Step 4 — CPT Training Loop & Loss Analysis · 2 marks · P2

**Needs:** Step 2 + Step 3 · **Produces:** `cpt_ckpt/`, the loss curve

**Do this:**
1. **Wrap the packed dataset in a PyTorch `Dataset` class** (explicit brief wording). `__getitem__`
   returns `input_ids` and `labels` — for causal LM they're the same tensor; the model shifts
   internally.
2. Configure `TrainingArguments` — learning rate around `2e-5`, a warmup, `bf16=True`, gradient
   accumulation to reach a sensible effective batch, and `logging_steps=1` so the callback sees
   every step.
3. **Loss callback** — subclass `TrainerCallback`, override `on_log`, append `logs["loss"]` to a list.
4. Run `Trainer(...).train()`.
5. 🔴 **Check the first logged loss immediately.** 2–4 means the pretrained weights loaded
   correctly. **≈10.8 means the model initialised randomly** — stop, fix the loading, do not train
   through it. If loss diverges or spikes, lower the learning rate or lengthen warmup.
6. Plot **loss vs training step** and identify where it **plateaus**.
7. `model.save_pretrained("cpt_ckpt")` **and** `tokenizer.save_pretrained("cpt_ckpt")` — to
   persistent storage. Part B and Step 5 both depend on this.

**Report:** the loss curve plot · the starting loss · where it plateaus.

**Done when:** `cpt_ckpt/` contains model *and* tokenizer, and the curve is plotted with the
plateau called out.

---

### Step 5 — Evaluation: Perplexity & Catastrophic Forgetting · 2 marks · P3

**Needs:** `packed_eval.parquet` + `cpt_ckpt/` · **Produces:** `ppl_results.json`, `forgetting_table.md`

#### 5A — Domain perplexity

`PPL = exp( −(1/N) Σ log P(tᵢ | t₁…tᵢ₋₁) )`

**Do this:**
1. Write one evaluation loop: `model.eval()`, `torch.no_grad()` — **no gradients, no training**,
   as the brief specifies.
2. Accumulate token-level cross-entropy over `packed_eval.parquet`, then
   `ppl = exp(total_loss / total_tokens)`.
3. Run it twice on the **same** split: once for the **base** model, once for the **CPT** model.
4. `reduction% = (base − cpt) / base × 100`.

**Report:** base PPL · CPT PPL · percentage drop. A successful run drops domain perplexity
**10–40%**. Lower domain PPL after CPT = successful domain adaptation.

#### 5B — Catastrophic forgetting

**Do this:**
1. Generate on the 3 **general** prompts with **both** models (base outputs already saved in Step 3).
2. Build a side-by-side table with a **verdict column**.

| Prompt | Base output | CPT output | Verdict |
|---|---|---|---|
| The capital of France is… | … | … | Retained / Degraded |

**If outputs degrade badly:** learning rate was too high or training ran too long — cut LR 10× or
halve `max_steps` and re-run. That usually preserves the domain gain.

**Done when:** both perplexities, the percentage, and a 3-row verdict table exist — plus a
paragraph on whether the trade-off was worth it.

---

### B1 — Instruction Dataset Creation · 2 marks · P1

**Needs:** Step 1 output · **Produces:** `instruction_dataset.jsonl`, `instruction_train.jsonl`, `instruction_eval.jsonl`

**Do this:**
1. Chunk the cleaned `.txt` files into ~50 readable passages.
2. Generate **10 instruction/response pairs per passage → 500 pairs**, either by hand/heuristic or
   synthetically via an external LLM. The brief's suggested template:
   > *"Read the text below and generate 10 instruction-response pairs in JSON format based ONLY on
   > this text. Each entry must have instruction and response keys."*
3. 🔴 **Save the exact prompt template you used** — the brief requires it in the submission if you
   went synthetic.
4. Validate the JSONL: every line is one object with an `instruction` key and a `response` key.
   Responses must be derived **from your domain text**, not invented.
   *(V4 clinical only: every response must carry the educational-use disclaimer.)*
5. Shuffle, then split **80/20** → 400 train / 100 eval.

**Report:** train count and eval count · the exact generation prompt template.

**Done when:** all three JSONL files validate and the counts are printed.

---

### B2 — QLoRA Fine-Tuning · 2 marks · P4

**Needs:** `cpt_ckpt/` + B1 output · **Produces:** `adapter/`

**Do this:**
1. `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)`.
2. Load **`cpt_ckpt/`** — not the original base model — with that quantization config.
3. `prepare_model_for_kbit_training(model)`.
4. Pick **one** adapter and state why:

   | Adapter | r | α | Target modules | Effect |
   |---|---|---|---|---|
   | A · low | 8 | 16 | `q_proj`, `v_proj` | Faster; may underfit |
   | **B · balanced** | **16** | **32** | **`q_proj`, `v_proj`** | **Good quality/cost — default** |
   | C · high | 32 | 32 | `q_proj`, `v_proj`, `o_proj` | Best quality; slower; more VRAM |

   `LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj","v_proj"], task_type="CAUSAL_LM")`
5. Format every pair with the model's **chat template** —
   `tok.apply_chat_template([{"role":"user","content":instruction}, {"role":"assistant","content":response}], tokenize=False)`.
   If the tokenizer has no template, set `tok.chat_template` yourself and document it.
6. Train with `SFTTrainer` on the 400-pair training split.
7. Save the adapter.

**Report:** the adapter config chosen and the reasoning · training loss.

**Done when:** the adapter loads onto `cpt_ckpt/` and generates without error.

---

### B3 — Evaluation Analysis · 1 mark · P4

**Do this:**
1. Run the trained adapter on **the same 3 locked domain prompts** from Step 3.
2. Put all three stages side by side:

| Prompt | Base (Step 3) | CPT (Step 4) | CPT + adapter (B2) |
|---|---|---|---|

3. Write the observations: did the base model ramble? Did CPT make it fluent in domain vocabulary
   but still complete rather than answer? Did the adapter make it actually *respond* to the
   instruction? That progression is the finding the whole assignment is built to demonstrate.

**Done when:** the three-way table exists with a written analysis.

---

## 7 · Submission

| File | Contents |
|---|---|
| `Assignment1A.ipynb` | Notebook **with outputs** — Steps 1–5, B1–B3, inferences throughout |
| `Assignment1A.html` | Exported HTML of the notebook, with outputs |
| `instruction_dataset.jsonl` | Final instruction/response pairs |
| `domain_corpus/*.txt` | Cleaned text files from Step 1 |
| *custom variant only* | The custom-variant template, in the V2–V6 format |

**Final checks:** restart the kernel and run **top to bottom** · every step has a written inference
(the brief calls this mandatory twice) · every figure in the step sections above is visible in the
output.

**Optional, no marks:** a chat loop routing queries to different adapters via `model.set_adapter()`.

---

## 8 · Risk register

| Risk | Signal | Response |
|---|---|---|
| Gated model not approved | 401/403 on load | Accept the licence at hour zero, or use an ungated model |
| `bitsandbytes` import fails | ImportError at runtime | Match the wheel to the CUDA build — catch it in Block 1 |
| Model initialised randomly | **Start loss ≈10.8** not 2–4 | Fix `from_pretrained`; never train through it |
| Tokenizer mismatch | `lm_head` dim ≠ vocab size | One tokenizer id everywhere, always the model's own |
| OOM during CPT | CUDA OOM | Smaller model · gradient checkpointing · lower batch, higher grad accumulation |
| Catastrophic forgetting | 5B outputs clearly degrade | Cut LR 10× or halve `max_steps`, re-run |
| No chat template | `SFTTrainer` errors in B2 | Qwen2.5 ships ChatML; else set `tok.chat_template` and document it |
| Corpus too small | PPL drop under 10% | More documents, or more epochs |
| Checkpoint lost | Session disconnect | Save `cpt_ckpt/` to mounted persistent storage |
| GPU contention | Queue near the deadline | Step 4 finishes in Block 2 — non-negotiable |

---

## 9 · Downstream note

Assignments **1B, 2A, 2B and 2C reuse the same `.txt` corpus and `instruction_dataset.jsonl`**
built here — no new data collection later. Clean it properly once.
