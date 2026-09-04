# Assignment 1A — 4-Person Execution Plan

**Course:** AIML ZG536 · **Marks:** 15 (Part A 10 · Part B 5)
**Effort:** ~2.5–3 working days across 4 blocks · **Crew:** 4

> ⚠️ **The brief sets no deadline.** Neither `Assignment 1A - CPT and SFT.pdf` nor
> `Enterprise_Variants_All_Assignments.pdf` states a submission date. Confirm it on Canvas or
> the Ops mail. The blocks in §5 are therefore **relative** — run them back-to-back if the
> date turns out to be tight, or spread them out if there is room.

**Sourced only from the two briefs in this folder.** Marks, steps, deliverables, the model
table and the failure signals all come from those PDFs. The 4-person split is our own
constraint — the brief does not specify a group size.

Assignment 1A is one pipeline: raw domain PDFs → continual pre-training (CPT) → QLoRA
instruction fine-tuning. The pipeline is *sequential*, so the split is by **workstream
ownership**, not by "everyone grabs two steps". Each person owns a lane end-to-end and hands
a named artifact to the next lane.

---

## Contents

| § | Section | Read it when |
|---|---|---|
| 1 | [Prerequisites](#1--prerequisites) | Before anything else — some items need lead time |
| 2 | [Decisions to lock](#2--decisions-to-lock) | At the kickoff call |
| 3 | [Who owns what](#3--who-owns-what) | Assigning lanes |
| 4 | [Handoff contracts](#4--handoff-contracts) | Whenever a lane finishes |
| 5 | [The four blocks](#5--the-four-blocks) | Day to day execution |
| 6 | [GPU discipline](#6--gpu-discipline) | Scheduling compute |
| 7 | [Definition of done](#7--definition-of-done) | Before submitting |
| 8 | [Submission deliverables](#8--submission-deliverables) | Packaging |
| 9 | [Risk register](#9--risk-register) | When something breaks |
| 10 | [Downstream note](#10--downstream-note) | Planning later assignments |

---

## 1 · Prerequisites

Everything below is implied by the briefs. Items marked 🕒 need **lead time** — start them at
hour zero, not when you first need them.

### 1.1 Accounts and access

| Need | Why the brief requires it | Owner |
|---|---|---|
| 🕒 **Hugging Face account + access token** | Every model in the selection table is pulled with `from_pretrained('<model-id>')` | all four |
| 🕒 **Gated-model licence acceptance** | See the warning below — approval is not instant | P3 |
| **Compute tier** | Brief pairs T4 (16 GB, free Colab) with the small-model column, A100 / L40S (BITS remote lab) with the 7–8 B column | all four |
| **Persistent storage** | Step 4 says save the CPT checkpoint "to persistent storage" — a Colab session disk does not survive a disconnect | P2 |
| **External LLM access** *(optional)* | Only if B1 uses synthetic generation rather than manual/heuristic pairs | P1 |

> 🔴 **Three of the brief's A100 recommendations are gated on Hugging Face** and need licence
> acceptance before the weights will download:
> `mistralai/Mistral-7B-v0.1` · `meta-llama/Meta-Llama-3-8B` · `google/gemma-7b`
>
> Approval can take anywhere from minutes to a day. **Open the model page and accept the terms
> at hour zero**, or pick an ungated model and skip the risk entirely:
> `Qwen/Qwen2.5-*` · `HuggingFaceTB/SmolLM2-*` · `TinyLlama/TinyLlama-1.1B-*` ·
> `openai-community/gpt2-*` · `microsoft/biogpt-large` · `stanford-crfm/BioMedLM`
>
> This is the single most likely thing to cost you a day for no academic reason.

### 1.2 Python libraries

Named directly in the brief:

| Library | Used for | Brief's wording |
|---|---|---|
| `transformers` | model, tokenizer, Trainer, callback | "`AutoModelForCausalLM.from_pretrained()`", "`AutoTokenizer.from_pretrained()`", "custom `TrainerCallback`" |
| `peft` | LoRA adapters | Part B2 |
| `bitsandbytes` | 4-bit quantization | Part B2 |
| `trl` | `SFTTrainer` | Part B2 |
| `torch` | Dataset class, training loop | "Wrap the packed dataset in a PyTorch Dataset class" |

Implied by the required outputs:

| Library | Used for |
|---|---|
| a PDF extractor — `pypdf`, `PyMuPDF` or `pdfplumber` | Step 1: "use any standard PDF extraction library" |
| `pyarrow` / `pandas` | Step 2: "Save as Parquet" |
| `matplotlib` | Step 4: "plot loss vs. training step" |
| a language detector — `langdetect` or `fasttext` | Step 1: "retain only English-language documents" |
| `datasets` | convenient for the packed/instruction splits |

**Verify every import before Block 1 ends.** `bitsandbytes` is the usual troublemaker — it
compiles against a specific CUDA build and fails at import, not at install.

### 1.3 Data

- **Domain PDFs** from the source sites listed under your chosen variant (V1–V6), or your own
  for a custom variant. Target 8–10 documents minimum; more if you have A100 headroom.
- The brief allows any domain: *"You are free to choose any domain and any model."*

### 1.4 Concepts the group should already have

Continual pre-training vs. fine-tuning · causal-LM next-token loss · tokenization and
vocabulary alignment · perplexity · LoRA / QLoRA rank and alpha · catastrophic forgetting.
The brief assumes these; it explains only perplexity in any depth.

---

## 2 · Decisions to lock

45 minutes, all four, before any work starts. Changing any of these later costs a re-run.

1. **Variant + domain.** One of V1–V6, or a custom one. V3 (RBI/SEBI regulatory) and V6
   (ISO 9001 / GFR 2017 procurement) have the cleanest downloadable English PDF corpora.
   V4 (clinical) adds a mandatory disclaimer string on every response — extra rubric surface.
   🔴 **A custom use case adds a fifth deliverable.** The variants guide requires you to label
   it a custom enterprise variant, build the template "in the same format as given for V2–V6",
   and **submit it as a separate doc**. Pick V1–V6 and that requirement disappears.
2. **Model** — see the recommendation below. Check its gating status first (§1.1).
3. **The three domain prompts** — locked, never edited. Reused in Step 3 (baseline), Step 4
   and B3. Plus **three general prompts** for the Step 5B forgetting check
   (capital of France / water boils at / speed of light).
4. **Instruction-dataset size.** The brief only says "suitable size", so fix a number now:
   **500 pairs → 400 train / 100 eval**. Without it, P1's lane has no finish line.
5. **Shared folder + filename contract** — exactly the names in §4.

### Model recommendation

Pick **Qwen2.5-1.5B**, not a 7B.

- Part A is **full-parameter** CPT. A 7B in bf16 with Adam states needs roughly 80 GB+ of
  optimizer and gradient memory — tight-to-impossible on a contended A100, and a run that
  dies late in Block 2 leaves no recovery room.
- Qwen2.5 base ships a **ChatML chat template** in `tokenizer_config.json`, which is what B2
  requires ("formatted with the model's chat template"). Most base models don't, and finding
  that out in Block 3 costs hours.
- **Ungated** — no licence wait (§1.1).
- A 1.5B CPT run finishes in minutes, so a bad loss curve gets re-run instead of accepted.
- The rubric rewards the **analysis** — loss curve, PPL drop, forgetting table — not parameter
  count. Both PDFs explicitly permit any model.

If Block 2 finishes early and the lab is free, re-run at 7B as a bonus. Don't bet the grade on it.

---

## 3 · Who owns what

| | Owner | Steps | Marks | First action |
|---|---|---|---|---|
| **P1** | Corpus & Instruction Data | Step 1 + B1 | 4 | Start downloading PDFs immediately — longest lead time, no GPU needed |
| **P2** | Packing & CPT Training | Step 2 + Step 4 | 4 | Write the packing script against P1's first few files |
| **P3** | Model Audit & Evaluation | Step 3 + Step 5 | 4 | Accept model licences, then run the architecture audit — needs no corpus |
| **P4** | QLoRA & Submission | B2 + B3 + assembly | 3 + integration | Verify every import, build the notebook skeleton |

P4 carries fewer rubric marks but owns notebook integration, HTML export, GPU scheduling and
final packaging — in practice the load is even.

---

## 4 · Handoff contracts

Agree these filenames at kickoff. A lane is "done" when its artifact exists under its name.

| From → To | Artifact | Must contain |
|---|---|---|
| P1 → P2 | `domain_corpus/*.txt` | Cleaned, English-only, deduplicated text |
| P1 → P2 | `cleaning_stats.json` | Doc counts **before and after each filter**, and which step cut most |
| P2 → P3 | `packed_train.parquet`, `packed_eval.parquet` | 90/10 split; eval never seen in training |
| P2 → P3 | `pack_stats.json` | Total tokens, avg doc length in tokens, number of packed sequences |
| P2 → P3, P4 | `cpt_ckpt/` | Final CPT model **and** tokenizer |
| P3 → P4 | `baseline_generations.json` | Base-model output on the 3 domain **and** 3 general prompts |
| P3 → P4 | `ppl_results.json` | Base PPL, CPT PPL, % reduction |
| P3 → P4 | `forgetting_table.md` | 3 general prompts, base vs CPT, Retained/Degraded verdict |
| P1 → P4 | `instruction_train.jsonl`, `instruction_eval.jsonl` | 80/20 split, counts, exact generation prompt template if synthetic |
| all → P4 | notebook section + written inferences | Every step needs justification — this is graded |

---

## 5 · The four blocks

### Block 1 — Setup and smoke test (~3–4 h) · goal: prove the pipeline runs

- **All** — the kickoff call (§2). Confirm §1 prerequisites are actually in place.
- **P1** — download 8–10 domain PDFs; write the extract + clean script (the brief asks for
  **page-by-page** extraction, one `.txt` per document); ship the **first 5 cleaned files
  fast** so everyone else unblocks.
- **P3** — load the model (**on T4 the brief requires bf16 + gradient checkpointing**; on A100
  either is fine); architecture audit — decoder layers, attention heads, hidden size, head dim;
  total trainable parameters; confirm `lm_head` output dim equals vocab size. Save baseline
  generations on the 3 domain prompts **and the 3 general prompts** while the base model is
  loaded, so Step 5B later needs only the CPT half.
- **P2** — write the packing script: BOS/EOS wrap per doc, concatenate to one flat stream,
  slice to context length, save Parquet. Test on P1's first 5 files.
- **P4** — verify `transformers` / `peft` / `bitsandbytes` / `trl` all import; create the
  notebook skeleton with its 8 titled sections; set up the shared folder.

> **Block 1 gate — the vertical slice.** Before Block 1 closes, a **20-step CPT run on 5
> documents must complete**. The output will be worthless; that is the point. It surfaces
> every environment bug — install failures, tokenizer mismatch, OOM, checkpoint paths — while
> there is still recovery room. Block 2 then scales up a pipeline you know works.

### Block 2 — Corpus, CPT, evaluation (~1 full day) · goal: CPT trained and evaluated

- **P1** — finish the full corpus; run the cleaning pipeline; record counts before and after
  **each** filter; identify the highest-impact step. Hand off.
- **P2** — pack the full corpus; report total tokens, avg doc length, sequence count; carve
  the 10% held-out eval split.
- **P3** — write the perplexity harness (cross-entropy loop, **no gradients, no training** —
  the brief says so explicitly); run base-model PPL on the holdout.
  *Blocked on P2's `packed_eval.parquet` — take P2's packing first.*
- **P2 (main slot)** — **the CPT run.** Wrap the packed dataset in a **PyTorch `Dataset`
  class** (explicit Step 4 wording). Custom `TrainerCallback` logging loss every step. Watch
  the first loss: 2–4 is healthy, ≈10.8 means the model initialised randomly — stop and fix
  loading, do not train through it. Save `cpt_ckpt/`.
- **P3 (after checkpoint)** — CPT PPL on the same holdout; % reduction (expect 10–40%);
  the forgetting table.
- **P1 (later)** — begin the instruction dataset — the second-longest pole.
- **P4 (throughout)** — fold Steps 1–3 into the notebook as they land; own the GPU schedule.

### Block 3 — Instruction data, QLoRA, inferences (~1 full day)

- **P1** — finish `instruction_dataset.jsonl` to the agreed 500-pair target; 80/20 split with
  counts; record the exact synthetic-generation prompt template if an LLM was used.
- **P4 (main slot)** — QLoRA on `cpt_ckpt/`: 4-bit bitsandbytes, `peft`, `SFTTrainer` with the
  chat template. **Adapter B** (r=16, α=32, `q_proj`,`v_proj`) is the sensible default.
- **P4 (after training)** — B3: run the adapter on the same 3 locked domain prompts.
- **P3** — write the Step 5 inferences; build the base vs CPT vs adapter comparison.
- **All (end of block)** — **inference-writing session.** Every step needs written
  justification; both PDFs say detailed inferences are mandatory. Most commonly skipped work,
  and worth real marks.

### Block 4 — Assembly and submission (~half day)

- **P4** — restart kernel, run the notebook **top to bottom**, export HTML with outputs.
- Package the deliverables (§8), walk the definition of done (§7), submit.

---

## 6 · GPU discipline

One A100 slot at a time. Contention rises sharply near any deadline.

| Block | Who | Job |
|---|---|---|
| 1 | P3, then P2 | Architecture audit + baseline (~30 min), then the smoke CPT |
| 2 | **P2** | The real CPT run — protected slot |
| 2 (late) | P3 | Base + CPT perplexity |
| 3 | P4 | QLoRA training |

**The CPT run must finish inside Block 2.** Perplexity, the forgetting table, the QLoRA adapter
and B3 are all blocked behind that one checkpoint, so leaving it to Block 3 removes any chance
of a second attempt.

---

## 7 · Definition of done

Marks attach to reported figures, not just code that ran. The notebook must state:

- [ ] Doc counts before and after **each** cleaning step, and the highest-impact step
- [ ] Total token count, average document length in tokens, number of packed sequences
- [ ] Total trainable parameters
- [ ] Decoder layers, attention heads, hidden size, head dimension
- [ ] `lm_head` output dim equals vocabulary size
- [ ] Packed dataset wrapped in a PyTorch `Dataset` class
- [ ] Loss curve plotted, with the plateau point identified
- [ ] Base PPL, CPT PPL, and the **percentage reduction**
- [ ] Forgetting table: 3 general prompts, both models, Retained/Degraded verdict per row
- [ ] Instruction dataset train/eval counts
- [ ] The exact synthetic generation prompt template
- [ ] Adapter configuration used
- [ ] B3 observations on the 3 locked prompts
- [ ] Written inferences under **every** step

---

## 8 · Submission deliverables

| File | Contents |
|---|---|
| `Assignment1A.ipynb` | Notebook **with outputs** — Steps 1–5 and B1–B3, inferences throughout |
| `Assignment1A.html` | Exported HTML of the notebook, with outputs |
| `instruction_dataset.jsonl` | Final instruction/response pairs |
| `domain_corpus/*.txt` | Cleaned text files from Step 1 |
| *custom variant only* | The custom-variant template doc, in the V2–V6 format |

**Optional extension, no marks:** a CLI or notebook chat loop routing domain queries to
different adapters via keyword or intent rules, demonstrating `model.set_adapter()`.

---

## 9 · Risk register

| Risk | Signal | Response |
|---|---|---|
| Gated model not approved | 401/403 on `from_pretrained` | Accept the licence at hour zero, or switch to an ungated model (§1.1) |
| `bitsandbytes` import fails | ImportError at runtime, not install | Match the wheel to the CUDA build; catch it in Block 1, not Block 3 |
| Model initialised randomly | Start loss ≈10.8 instead of 2–4 | Fix `from_pretrained`; do not train through it |
| Tokenizer mismatch | Garbage generations; vocab ≠ `lm_head` dim | One tokenizer id everywhere, always the model's own |
| OOM during CPT | CUDA OOM | Smaller model, gradient checkpointing, lower batch + higher grad accumulation |
| Catastrophic forgetting | General prompts clearly degrade in 5B | Cut LR 10× or halve `max_steps`, re-run |
| No chat template | `SFTTrainer` errors in B2 | Qwen2.5 ships ChatML; otherwise set `tokenizer.chat_template` and document it |
| Corpus too small | PPL drop under 10% | Add documents, or train more epochs on the same corpus |
| Checkpoint lost | Colab disconnect wipes session disk | Save `cpt_ckpt/` to mounted persistent storage |
| GPU contention | Queue near the deadline | CPT finishes in Block 2 — non-negotiable |

---

## 10 · Downstream note

Per the variants guide, assignments **1B, 2A, 2B and 2C reuse the same `.txt` corpus and
`instruction_dataset.jsonl`** built here — no new data collection later. P1's lane is an
investment across five deliverables, so clean it properly once.
