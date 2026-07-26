# AGENTS.md — working rules for this repo

Rules for any AI agent working in the `MTech` repo. Read this before producing anything.

## What this repo is

Study notes for an MTech at BITS Pilani WILP. One folder per semester (`2026-2027-Sem1/`, then siblings). The notes exist to pass two kinds of exam and to survive a full-time job alongside them. Every rule below comes from that constraint.

**Current semester:** Aug–Dec 2026. Four subjects: 536 LLMs · 549 Cloud Native · 521 Conversational AI · 546 SE4ML.
Read `2026-2027-Sem1/STUDY-PLAN.md` for phases, calendar and deadlines before planning any work.

## Hard rules

1. **Never commit course material.** No `.pdf`, `.ppt`, `.pptx`, `.docx`, datasets or model weights. They are large and copyrighted; they live in Google Drive. `.gitignore` enforces this — do not weaken it. `<subject>/source/README.md` holds links only.
2. **Never commit secrets.** No API keys, tokens or `.env` files, in any file, including notebooks and note examples. Use `OPENAI_API_KEY` style placeholders.
3. **Don't invent syllabus content.** Session topics, dates, weights and references come from the handouts. If something isn't in a handout, mark it `⚠️ unconfirmed` rather than guessing. Wrong exam dates are worse than missing ones.
4. **Don't reproduce textbook text.** Explanations are written fresh, in plain language. Cite the chapter; don't transcribe it.
5. **One file per session**, in `<subject>/notes/`, named `S<NN>-<slug>.md` — **`S` prefix in every subject**, including 521, whose handout labels sessions `L1…L16`. Use the label `L3` in prose, the filename `S03-…`. If a note is created, update its row in `<code>-master.md` **and** in `2026-2027-Sem1/PROGRESS.md` in the same change.
6. **Lab code goes in `<subject>/labs/S<NN>-<slug>/`,** not in `notes/`. Notes link to it.

## Intake — what arrives, and what to do with it

The user uploads material session by session and says **subject, session number, and file type** (e.g. *"549, session 3, slides + transcript"*). If the session number is missing, infer it from the master index and **state the inference** rather than silently guessing.

| Format | What is extractable | Handling |
|---|---|---|
| `.pdf` (text) | Full text and tables | `pdfplumber` |
| `.pdf` (scanned) | Nothing until OCR'd | OCR first; say that it's happening |
| `.pptx` | Slide text **and speaker notes** — notes often carry the real explanation | `python-pptx`; always read the notes slides |
| `.docx` | Full text and tables | `python-docx` |
| `.png` / `.jpg` of a diagram | Read directly | Describe the diagram in the note; don't just cite it |
| `.txt` / `.srt` / `.vtt` transcript | Full text | Primary source for what the instructor emphasised |
| **`.mp4` / video** | **Nothing** | Cannot be processed. See below |

**Video cannot be transcribed here.** The sandbox has `ffmpeg`, but the only reachable network host is PyPI — Hugging Face and every model CDN return 403, so no ASR model can be fetched. The user transcribes locally (MacWhisper, or `whisper <file> --model small --output_format txt`) and uploads the text. Never claim to have watched a recording.

**Auto-generated transcripts are noisy.** Technical terms come through mangled (`RoPE` → "rope", `SwiGLU` → "swiglue", `GQA` → "GQ A"). Reconcile against the slides, which have the correct spellings, and silently use the correct term in the note. Do not ask the user to clean transcripts first.

**When both slides and transcript exist,** the slides define the scope and the transcript defines the emphasis. What the instructor spent ten minutes on is what the exam asks about — mark it in the note.

## How notes must be written

Follow `2026-2027-Sem1/_templates/SESSION-TEMPLATE.md`. Every concept gets four parts, in this order:

**Intuition** → **Mechanism/formula** → **Worked example** → **Tradeoff / when NOT to use**

- **The tradeoff line is mandatory.** Never leave it blank, never write "depends on the use case." Name the specific situation where the simpler alternative wins. Exam questions concentrate here.
- **The worked example must be reproducible by hand or in ≤30 lines.** A described example is not an example. For mechanism topics (attention, RoPE, KV-cache, quantization, LoRA, DPO) show the actual arithmetic on small numbers.
- **Landscape topics get a comparison table, not prose.** Decoding strategies, serving patterns, CNCF tools, benchmarks — table, one row each, columns for what/when/cost.

Every note carries **both** exam formats:

- **Closed-book card** (blockquote) — fewest words that trigger full recall. For sessions 1–8 only; that's the mid-sem scope in all four subjects.
- **Open-book detail** (collapsed `<details>`) — organised for *lookup speed under time pressure*, not for reading start to finish. All 16 sessions.

## Shared topics — the main rule

RAG, retrieval, agents, fine-tuning, function-calling, quantization, Docker/K8s, evaluation, ML lifecycle and API design each appear in **two to four** of the four subjects.

- Write the topic **once**, in `_shared/<topic>.md`, when the first course reaches it.
- When a later course reaches the same topic, **do not write a second note.** Add a row to that file's "course-specific angles" table and cross-link from the session note.
- Record the exam scope per course in the shared file — the same topic can be closed-book for one subject and open-book for another. (`rag.md` is the sharp case: mid-sem scope for 521, comprehensive-only for 549 and 536.)

## Tone

- Plain language. Define jargon on first use or don't use it.
- No filler, no motivational framing, no restating the question.
- Short sentences beat long ones. If a sentence can lose words and keep its meaning, cut them.
- Prefer a table over a list, a list over a paragraph, and a worked example over all three.
- Flag uncertainty inline with `⚠️`. Never present a guess as a fact.

## Before finishing any task

- [ ] Master index row added or updated for every note touched
- [ ] `PROGRESS.md` row ticked
- [ ] `source/MATERIAL-LOG.md` updated with what material was received
- [ ] Cross-links to `_shared/` are correct and bidirectional
- [ ] Every concept has a non-empty tradeoff line
- [ ] No PDFs, slides, datasets or secrets staged for commit
- [ ] Dates and weights match the handout, or are marked `⚠️`

## Repo layout

```
MTech/
├── AGENTS.md                    ← this file
├── README.md
├── .gitignore                   ← blocks course material; do not weaken
└── 2026-2027-Sem1/
    ├── STUDY-PLAN.md            ← phases, week-by-week calendar, deadlines
    ├── PROGRESS.md              ← one dashboard: 64 sessions × note/card/open/lab
    ├── 536-LLMs/
    │   ├── 536-master.md        ← session index; open-book front index in Dec
    │   ├── notes/S01-….md       ← one file per session
    │   ├── labs/S05-…/          ← lab code
    │   └── source/
    │       ├── README.md        ← Drive links only
    │       ├── MATERIAL-LOG.md  ← what material exists per session
    │       └── transcripts/     ← plain-text transcripts (committable)
    ├── 549-CloudNative/
    ├── 521-ConversationalAI/
    ├── 546-SE4ML/
    ├── _shared/                 ← cross-subject master notes + README index
    └── _templates/SESSION-TEMPLATE.md
```

## Key dates (all four handouts, confirmed)

| Date | Event |
|---|---|
| 10–20 Aug 2026 | Quizzes, all four subjects |
| 27 Aug – 7 Sep 2026 | 549 project 30% · 536 assignment 30% · 546 situated learning 5% |
| 19 Sep 2026 (EN) | 546 mid-sem, closed book |
| 20 Sep 2026 | 549 mid-sem (FN) · 536 mid-sem (EN), closed book |
| 29 Oct – 11 Nov 2026 | 546 Assignments I & II, 20% |
| 22 Nov 2026 | **Print and bind the open-book file** (BITS bans loose sheets) |
| 5 Dec 2026 (EN) | 546 comprehensive, open book |
| 6 Dec 2026 | 549 comprehensive (FN) · 536 comprehensive (EN), open book |

⚠️ **521 publishes no dates** — quizzes and both assignments are announced in class or on Canvas, with strictly no makeups. Treat any 521 date in this repo as inferred until confirmed.
