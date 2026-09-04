# Assignment 1A — 4-Person Sprint Plan

**Course:** AIML ZG536 · **Weight:** EC-1 group project · **Marks:** 15 (Part A 10 · Part B 5)
**Window:** Fri 4 Sep → due ~Sun 7 Sep 2026 · **Crew:** 4

Assignment 1A is one pipeline: raw domain PDFs → continual pre-training (CPT) → QLoRA
instruction fine-tuning. The pipeline is *sequential*, so the split below is by **workstream
ownership**, not by "everyone grabs two steps". Each person owns a lane end-to-end and hands
a named artifact to the next lane.

---

## 0 · Lock-in call — Friday evening, 45 minutes, all four

Nothing starts until these five are decided and written down. Changing any of them later
costs a re-run.

1. **Variant + domain.** One of V1–V6 from `Enterprise_Variants_All_Assignments.pdf`, or a
   custom one. V3 (RBI/SEBI regulatory) and V6 (ISO 9001 / GFR 2017 procurement) have the
   cleanest downloadable English PDF corpora. V4 (clinical) adds a mandatory disclaimer
   string on every response — extra rubric surface.
2. **Model.** See the recommendation below.
3. **The three domain prompts** — locked, never edited. They are reused in Step 3 (baseline),
   Step 4 and B3. Plus **three general prompts** for the Step 5B forgetting check
   (capital of France / water boils at / speed of light).
4. **Shared folder + filename contract.** Exactly the names in the Handoffs table below.
5. **Remote lab access confirmed for all four.** Assignments run on the BITS remote lab, not
   laptops. Colab only handles the very small models.

### Model recommendation

Pick **Qwen2.5-1.5B** for the sprint, not a 7B.

- Part A is **full-parameter** CPT. A 7B in bf16 with Adam states needs roughly 80 GB+ of
  optimizer/gradient memory — tight-to-impossible on a contended lab A100, and a failed run
  on Saturday night has no recovery room.
- Qwen2.5 base ships a **ChatML chat template** in `tokenizer_config.json`, which is what
  B2 requires ("formatted with the model's chat template"). Most base models don't, and
  discovering that on Sunday costs hours.
- A 1.5B CPT run finishes in minutes, so a bad loss curve can be re-run instead of accepted.
- The rubric rewards the **analysis** — loss curve, PPL drop, forgetting table — not
  parameter count. Both PDFs explicitly permit any model ("You are free to choose any domain
  and any model"; "students are encouraged to experiment with different models").

If Saturday finishes early and the lab is free, re-run at 7B as a bonus. Do not bet the
grade on it.

---

## 1 · Who owns what

| | Owner | Steps owned | Marks | First action |
|---|---|---|---|---|
| **P1** | Corpus & Instruction Data | Step 1 + B1 | 4 | Start downloading PDFs immediately — longest lead time, needs no GPU |
| **P2** | Packing & CPT Training | Step 2 + Step 4 | 4 | Write the packing script against P1's first few files |
| **P3** | Model Audit & Evaluation | Step 3 + Step 5 | 4 | Load model, run architecture audit — needs no corpus, can start at hour 0 |
| **P4** | QLoRA & Submission | B2 + B3 + assembly | 3 + integration | Verify the lab environment, build the notebook skeleton |

P4 carries fewer marks by rubric but owns notebook integration, HTML export, GPU scheduling
and the final packaging — in practice the load is even.

---

## 2 · Handoff contracts

Agree these filenames at hour 0. A lane is "done" when its artifact exists with these names.

| From → To | Artifact | Must contain |
|---|---|---|
| P1 → P2 | `domain_corpus/*.txt` | Cleaned, English-only, deduplicated text |
| P1 → P2 | `cleaning_stats.json` | Doc counts **before and after each filter**, and which step cut most |
| P2 → P3 | `packed_train.parquet`, `packed_eval.parquet` | 90/10 split; eval never seen in training |
| P2 → P3 | `pack_stats.json` | Total tokens, avg doc length in tokens, number of packed sequences |
| P2 → P3, P4 | `cpt_ckpt/` | Final CPT model **and** tokenizer |
| P3 → P4 | `baseline_generations.json` | Base-model output on the 3 locked domain prompts |
| P3 → P4 | `ppl_results.json` | Base PPL, CPT PPL, % reduction |
| P3 → P4 | `forgetting_table.md` | 3 general prompts, base vs CPT, Retained/Degraded verdict |
| P1 → P4 | `instruction_train.jsonl`, `instruction_eval.jsonl` | 80/20 split, counts reported, exact generation prompt template if synthetic |
| all → P4 | notebook section + written inferences | Every step needs justification — this is graded |

---

## 3 · The sprint

### Block 1 — Friday evening (~3 h) · goal: prove the pipeline runs

- **All** — 45-min lock-in call (section 0).
- **P1** — download 8–10 domain PDFs; write the extract + clean script; ship the **first 5
  cleaned `.txt` files** fast so everyone else unblocks.
- **P3** — load the model on the lab; architecture audit (decoder layers, attention heads,
  hidden size, head dim); confirm `lm_head` output dim equals vocab size; run and save the
  **baseline generations** on the 3 locked prompts.
- **P2** — write the packing script: BOS/EOS wrap per doc, concatenate to one flat stream,
  slice to context length, save Parquet. Test on P1's first 5 files.
- **P4** — verify `transformers` / `peft` / `bitsandbytes` / `trl` all import on the lab;
  create the notebook skeleton with the 8 titled sections; set up the shared folder.

> **Friday gate — the vertical slice.** Before anyone sleeps, a **20-step CPT run on 5
> documents must complete**. The output will be worthless; that is fine. The point is to
> surface every environment bug — install failures, tokenizer mismatch, OOM, checkpoint
> paths — while there are still two days left. Scale up Saturday on a pipeline you know works.

### Block 2 — Saturday (full day) · goal: CPT trained and evaluated

- **P1 (AM)** — finish the full corpus; run the cleaning pipeline; record counts before and
  after **each** filter; identify the highest-impact step. Hand off.
- **P2 (AM)** — pack the full corpus; report total tokens, avg doc length, sequence count;
  carve the 10% held-out eval split.
- **P3 (AM)** — write the perplexity harness; run **base-model PPL** on the holdout.
- **P2 (PM)** — **the CPT run.** Custom `TrainerCallback` logging loss every step. Watch the
  first loss value: 2–4 is healthy, ≈10.8 means the model initialised randomly — stop and fix
  the loading, do not train through it. Save `cpt_ckpt/`.
- **P3 (PM)** — CPT PPL on the same holdout; % reduction (expect 10–40%); forgetting table.
- **P1 (PM)** — begin the instruction dataset from the cleaned `.txt` — the second-longest pole.
- **P4 (all day)** — fold Steps 1–3 into the notebook as they land; own the GPU schedule.

### Block 3 — Sunday (full day) · goal: QLoRA done, inferences written

- **P1 (AM)** — finish `instruction_dataset.jsonl`; 80/20 split with counts; record the exact
  synthetic-generation prompt template if an LLM was used (explicit rubric item).
- **P4 (AM–PM)** — QLoRA on `cpt_ckpt/`: 4-bit via bitsandbytes, `peft`, `SFTTrainer` with the
  chat template. **Adapter B** (r=16, α=32, `q_proj`,`v_proj`) is the sensible default.
- **P4 (PM)** — B3: run the trained adapter on the same 3 locked domain prompts.
- **P3 (PM)** — write the Step 5 inferences; build the base vs CPT vs adapter comparison.
- **All (evening)** — **inference-writing session.** Every step needs written justification.
  Both PDFs say "detailed inferences and observations are mandatory". This is the most
  commonly skipped work and it is worth real marks.

### Block 4 — Sunday night / Monday morning · buffer and submit

- **P4** — restart kernel, run the notebook **top to bottom**, export HTML with outputs.
- Package the four deliverables (section 5).
- Final rubric pass against section 6, then submit.

---

## 4 · GPU discipline

One A100 slot at a time. Contention rises sharply near the deadline.

| When | Who | Job |
|---|---|---|
| Fri eve | P3, then P2 | Architecture audit + baseline (~30 min), then the smoke CPT |
| Sat PM | **P2** | The real CPT run — protected slot |
| Sat late | P3 | Base + CPT perplexity |
| Sun | P4 | QLoRA training |

**The CPT run must finish Saturday.** If it slips to Sunday there is no room for a second attempt.

---

## 5 · Submission deliverables

- `Assignment1A.ipynb` — notebook **with outputs**, Steps 1–5 and B1–B3, inferences throughout
- `Assignment1A.html` — exported HTML of the notebook, with outputs
- `instruction_dataset.jsonl` — final instruction/response pairs
- `domain_corpus/*.txt` — the cleaned text files from Step 1

---

## 6 · Definition of done — the numbers that must appear

Marks attach to reported figures, not just working code. The notebook must state:

- Doc counts before and after **each** cleaning step, and the highest-impact step
- Total token count, average document length in tokens, number of packed sequences
- Total trainable parameters; decoder layers, attention heads, hidden size, head dim
- Confirmation that `lm_head` output dim equals vocab size
- Loss curve plot, with the plateau point identified
- Base PPL, CPT PPL, and the **percentage reduction**
- Forgetting table: 3 general prompts, both models, Retained/Degraded verdict per row
- Instruction dataset train/eval counts, and the exact generation prompt template
- Adapter config used, and B3 observations on the 3 locked prompts

---

## 7 · Risk register

| Risk | Signal | Response |
|---|---|---|
| Model initialised randomly | Start loss ≈10.8 instead of 2–4 | Fix `from_pretrained`; do not train through it |
| Tokenizer mismatch | Garbage generations; vocab ≠ `lm_head` dim | One tokenizer id everywhere, always the model's own |
| OOM during CPT | CUDA OOM | Smaller model, gradient checkpointing, lower batch + higher grad accumulation |
| Catastrophic forgetting | General prompts clearly degrade in 5B | Cut LR 10× or halve `max_steps`, re-run |
| No chat template | `SFTTrainer` errors in B2 | Qwen2.5 ships ChatML; otherwise set `tokenizer.chat_template` and document it |
| Corpus too small | PPL drop under 10% | Add documents, or train more epochs on the same corpus |
| GPU contention | Queue near the deadline | CPT finishes Saturday — non-negotiable |

---

## 8 · Downstream note

Per the variants guide, assignments **1B, 2A, 2B and 2C reuse the same `.txt` corpus and
`instruction_dataset.jsonl`** built here. No new data collection later. P1's lane is an
investment across five deliverables — clean it properly once.
