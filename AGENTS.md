# AGENTS.md — working rules for this repo

Rules for any AI agent working in the `MTech` repo. Read this before producing anything.

## What this repo is

Study notes for an MTech at BITS Pilani WILP. One folder per semester (`2026-2027-Sem1/`, then siblings). The notes exist to pass two kinds of exam and to survive a full-time job alongside them. Every rule below comes from that constraint.

**Current semester:** Aug–Dec 2026. Four subjects — folder name = **course code + course title exactly as the handout states it**:

| Folder | Code | Course title (handout) |
|---|---|---|
| `AIMLZG536-LLMForGenerativeAI` | AIML ZG536 | Large Language Models for Generative AI |
| `AIMLZG546-SoftwareEngineeringForML` | AIML ZG546 | Software Engineering for Machine Learning |
| `AIMLCZG549-APIDrivenCloudNativeSolutions` | AIMLC ZG549 | API-driven Cloud Native Solutions |
| `AIMLCZG521-ConversationalAI` | AIMLCZG521 | Conversational AI |

Note the prefix differs: **536 and 546 are `AIML`; 549 and 521 are `AIMLC`.** Take it from the handout, don't assume.
Read `2026-2027-Sem1/STUDY-PLAN.md` for phases, calendar and deadlines before planning any work.

## Hard rules

1. **Never commit course material.** No `.pdf`, `.ppt`, `.pptx`, `.docx`, datasets or model weights. `.gitignore` enforces this — do not weaken it. `<subject>/source/README.md` holds links only.
   **But textbooks are kept locally in `/_library/`** (gitignored, ~125 MB, nine books) so they never need re-uploading. **Always look there before asking the user for a book.** Slides and recordings still live in Drive/Teams/Taxila and are uploaded per session.
2. **Never commit secrets.** No API keys, tokens or `.env` files, in any file, including notebooks and note examples. Use `OPENAI_API_KEY` style placeholders.
3. **Don't invent syllabus content.** Session topics, dates, weights and references come from the handouts. If something isn't in a handout, mark it `⚠️ unconfirmed` rather than guessing. Wrong exam dates are worse than missing ones.
4. **Don't reproduce textbook text.** Explanations are written fresh, in plain language. Cite the chapter; don't transcribe it.
5. **One file per session**, in `<subject>/notes/`, named `S<NN>-<slug>.md` — **`S` prefix in every subject**, including 521, whose handout labels sessions `L1…L16`. Use the label `L3` in prose, the filename `S03-…`. If a note is created, update its row in `<code>-master.md` **and** in `2026-2027-Sem1/PROGRESS.md` in the same change.
6. **Lab code goes in `<subject>/labs/S<NN>-<slug>/`,** not in `notes/`. Notes link to it.

## Read the handout's session plan before asking for anything

Every handout's **Part B: Learning Plan** contains the session plan table, and it is the contract for the course. Its four columns:

| Column | Means |
|---|---|
| **Contact Session** | The session number. Some rows cover two (e.g. "10 & 11", "L15 & L16") |
| **List of Topic Title** | The topic(s) that session covers — the note's title |
| **Sub-Topics** | The breakdown within each topic — these become the note's sections, and they define examinable scope |
| **Reference** | **Where the instructor built the slides from** — a textbook chapter, a research paper, a spec, or just "Web Resources / Lecture Notes" |

Each master index reproduces this table. Its **Source** column *is* the handout's Reference column.

**Read the Reference column before requesting material.** It tells you what to ask for, what to fetch yourself, and — critically — whether anything exists behind the slides at all.

| Reference says | Do this |
|---|---|
| A textbook chapter (`T1 ch8`, `R3 ch1`) | **Check `/_library/` first — nine textbooks are already there.** Extract the cited chapters using the chapter→page map in `source/MATERIAL-LOG.md`. Only ask the user if the book isn't in `_library/` |
| A paper or public spec (ReAct, DPO, MCP spec, an Anthropic post) | **Fetch it directly** — these are public. Don't make the user upload them |
| "Web Resources", "Lecture Notes", or blank | **There is no source behind the slides.** The deck and the recording are the entire syllabus for that session. Say so in the note, and treat missing material as unrecoverable rather than reconstructable |

### The handout defines the syllabus boundary — uncited chapters are out of scope

**A textbook chapter that the handout does not cite is not part of this semester.** Textbooks are written for their own purposes and always contain far more than a course uses. The Reference column is the boundary, not a suggestion.

- **Never pull content from an uncited chapter into a session note.** Not as background, not as "useful context", not as a cross-reference that quietly imports its terminology.
- **Never recommend reading one.** Extra reading is time taken from a semester that is already short, spent on material that cannot be examined.
- **When mapping a book's chapters, mark the uncited ones explicitly as out of scope** so the map can't be misread later as a reading list.
- The only legitimate uses of an uncited chapter: the user asks about it directly, or it's needed to *build a lab that the handout does prescribe*. In both cases say plainly that it's outside the syllabus.
- Judging a chapter "relevant" is not sufficient grounds. Relevance is the instructor's call, already made, and recorded in the Reference column.

**Per-subject reference profile — this semester:**

- **546** — T1 (Kästner) and T2 (Nelson) chapters cover S1–S14. S15–S16 are lecture notes only.
- **536** — T1/T2/R1 chapters plus research papers cover most sessions. S6, S15, S16 are papers and web only.
- **521** — no textbook chapters at all; every reference is a **public paper or spec**, so fetch rather than ask.
- **549** — ⚠️ **only S1–S3 have book references (R2, R3). S4–S16 are "Web Resources, Lecture Notes."** Thirteen of sixteen sessions have nothing behind the slides. 549 decks and recordings are the highest-value artifacts of the semester; a missed 549 session cannot be reconstructed from a book.

## The slides are mandatory — no deck, no note

**A session note is never written without that session's slide deck (PDF or PPT).** The deck is not one source among several; it is the only artifact that says what *this instructor* actually taught.

Why the other sources cannot substitute:

- **The handout is too coarse.** Its Sub-Topics column is two or three lines per session. 521's entry for L1 reads "Chatbots → Agentic Systems; System Lifecycle & Architecture" — the real deck also covered tokenization with a full BPE worked example, context windows, the seven-stage lifecycle, the protocol landscape and production concerns. A note built from the handout would have missed most of the session and misjudged the weighting of the rest.
- **The textbook is too broad.** It covers what the author thought important, in the author's order, at the author's depth. The instructor selected from it, reordered it, and added material that isn't in it at all.
- **Neither shows emphasis.** Only the deck reveals that an instructor gave one topic twelve slides and another a single bullet.

**If the deck is missing:**

- Say so plainly, and **do not write the note.**
- Do not offer to "write a provisional version and revise later." A provisional note built on the wrong scope is worse than no note — it gets revised into, rather than replaced, and its errors persist.
- What you *may* do: fetch and read the session's public references so they're ready, and record their status in `source/MATERIAL-LOG.md`. That's preparation, not a note.
- Mark the session's Slides column `✗` in `source/MATERIAL-LOG.md` so the gap stays visible.

**The minimum bar for writing a session note is: the deck.** Everything else — textbook chapters, papers, transcripts — deepens a note that the deck defines. They never define one themselves.

**Corollary for the user:** the single most important thing to collect each weekend is the deck for every session. Chapters can be obtained later; a deck that was never downloaded from Teams/Taxila/Canvas may not be recoverable at all — and for 549, where thirteen of sixteen sessions have no textbook behind them, the deck plus recording *is* the syllabus.

## Intake — what arrives, and what to do with it

The user uploads material session by session and says **subject, session number, and file type** (e.g. *"549, session 3, slides + transcript"*). If the session number is missing, infer it from the master index and **state the inference** rather than silently guessing.

| Format | What is extractable | Handling |
|---|---|---|
| `.pdf` (text) | Full text and tables | `pdfplumber` |
| `.pdf` (scanned) | Nothing until OCR'd | OCR first; say that it's happening |
| `.pptx` | Slide text **and speaker notes** — notes often carry the real explanation | `python-pptx`; always read the notes slides |
| `.docx` | Full text and tables | `python-docx` |
| `.png` / `.jpg` of a diagram | Read directly | Convert to Mermaid — see below |
| `.txt` / `.srt` / `.vtt` transcript | Full text | Primary source for what the instructor emphasised |
| **`.mp4` / video** | **Nothing** | Cannot be processed. See below |

**Video cannot be transcribed here.** The sandbox has `ffmpeg`, but the only reachable network host is PyPI — Hugging Face and every model CDN return 403, so no ASR model can be fetched. The user transcribes locally (MacWhisper, or `whisper <file> --model small --output_format txt`) and uploads the text. Never claim to have watched a recording.

**Auto-generated transcripts are noisy.** Technical terms come through mangled (`RoPE` → "rope", `SwiGLU` → "swiglue", `GQA` → "GQ A"). Reconcile against the slides, which have the correct spellings, and silently use the correct term in the note. Do not ask the user to clean transcripts first.

### Add your own clarity — within the scope the handout sets

The sources define **what** is examinable. They are often poor at making it **understood**. Closing that gap is part of the job, not a liberty.

**Do add, freely:**

- **A clearer explanation** when the source's is compressed, circular or assumes something the reader doesn't have. Slides especially are written to be spoken over, so they routinely state a conclusion without the reasoning.
- **A better worked example** when the source's is missing, abstract, or doesn't expose the mechanism. Prefer concrete numbers over prose every time.
- **The tradeoff line**, which sources very often omit. If neither deck nor textbook says when *not* to use something, work it out and say so — that line is where exam marks concentrate.
- **A connection the sources don't draw** — between two topics in one session, between two subjects, or between a mechanism and the cost it implies.
- **The trap.** If a step is easy to get wrong (BPE merge 2 looks obvious and isn't; embedding row 5 is the sixth row), say so explicitly.
- **A diagram** where the source has only prose, per the Mermaid rules above.

**Never add:**

- **New topics.** Clarity operates *inside* the handout's scope; it never widens it. Explaining RoPE better in 536 S3 is right; introducing ALiBi because it's related is not.
- **Terminology the course doesn't use.** Explain in the instructor's vocabulary. A better word that appears in no exam paper is a worse word.
- **Silent invention.** If a fact isn't in a source, it is your reasoning — mark it, or make it visibly an explanation rather than a citation. Never let an addition read as though the instructor said it.
- **Depth beyond the exam.** A derivation the exam will never ask for is time taken from one it will.

**Mark clearly-added material** with a light touch — an italic aside like *"Not in the deck — this is R2 ch1"*, or *"the deck doesn't say why; here's the reason"*. The reader should always be able to tell what came from the course and what came from you, because in a disagreement with an instructor, only the course's version scores.

**The test:** would this addition help someone reproduce the concept, under time pressure, without notes? If yes, add it. If it would only impress, cut it.

### Organise by topic, never by source

**This is the most important rule in this file.** A note is one person's notebook on a topic, assembled from wherever the information happened to come from. It is not a set of source summaries stacked together.

- **Never** create sections like "From the slides" / "From the textbook" / "Part C — T1 ch3". The reader does not care which artifact a fact arrived in.
- **One topic, one place.** Everything known about the SDLC — the diagram from the slides, the reason it breaks for ML from the textbook, the instructor's aside from the transcript — lives in the SDLC section. A reader revising that topic should never need to look elsewhere in the file.
- **No duplication.** If a concept genuinely belongs to two topics, write it once in the more natural home and cross-reference from the other. Two half-explanations of the same idea in one note is the failure mode.
- **No source overrides another.** Sources *combine*. The slides' framing, the book's mechanism and the lecturer's emphasis are complementary, not competing versions to choose between. Only flag a conflict when the sources make genuinely incompatible factual claims (a date, a weight, a definition) — then present both and mark it `⚠️`.
- **Attribute lightly.** A short `Sources:` line under the topic heading is enough for looking things up later. Attribution belongs in a byline, not in the structure.
- **Order topics for learning, not for arrival.** Vocabulary before the concepts that use it; motivation before mechanism. If the textbook supplies terms the slides assume, those terms come first in the note even though the slides came first in the class.

### Layering sources

Material arrives for the same session at different times — slides first, transcript later, textbook chapter later still. **Rewrite the existing note in place; never create a second file, and never append a new source as a new section at the bottom.** New material gets distributed into the topics it belongs to.

| Source | Contributes | Wins when sources disagree |
|---|---|---|
| **Slides** | Scope — what is examinable, in the instructor's words | **Scope and terminology.** If the deck omits a textbook topic, it is probably not examinable — note it as background, don't expand it |
| **Textbook** | Depth — mechanism, worked examples, edge cases, the tradeoff line | **Explanation.** Slides compress; the book is where the argument is actually made |
| **Transcript** | Emphasis — what got ten minutes vs. thirty seconds; asides, exam hints | **Emphasis and anything said but not written** |

When a later source arrives, say in one line what changed in the note rather than re-describing the whole session.

**Textbooks: request chapters, not whole books.** A 500-page textbook covers all sixteen sessions; processing it for one session pulls in concepts the instructor has not yet introduced, which makes the note worse. If only the full book is available, ask which chapters — or take them from the master index's Source column — and extract just those pages. Never let unintroduced material leak into an early session's note.

### Images and diagrams → Mermaid

**Always extract embedded images from decks and look at them.** Slide text routinely omits what the diagram says; in 546 session 1, five of the eight concepts existed *only* as pictures. A note written from slide text alone will silently miss them.

Extraction: `python-pptx` → `shape.image.blob` for `.pptx`; `pdfplumber` / `pypdfium2` for PDFs. Write the files out, then read them.

**Convert every content-bearing diagram to a Mermaid block in the note.** Never write "see the diagram on slide 16" — the slides won't be in the exam hall and won't be in the bound open-book file unless they're in these notes.

| Diagram type | Mermaid to use |
|---|---|
| Process, cycle, pipeline | `flowchart LR` (or `TD`) |
| Layered pyramid / stack | `flowchart BT` bottom-up, one node per layer |
| Chronology, eras | `timeline` |
| Sequence of interactions | `sequenceDiagram` |
| State machine, lifecycle | `stateDiagram-v2` |
| Comparison across eras/options | **Markdown table, not Mermaid** |
| Venn diagram | **Table of the overlaps** — Mermaid has no Venn; name each intersection |
| Screenshot, photo, decorative art | **Skip it.** Not every image is a diagram |

Rules for the conversion:

- **Carry the labels across verbatim.** The exam uses the instructor's words.
- **Don't invent structure the image doesn't have.** If an arrow's direction is ambiguous, say so in the prose rather than guessing in the diagram.
- **Put the diagram under "Mechanism"**, then still write the intuition, worked example and tradeoff around it. A Mermaid block is not a substitute for the four-part explanation.
- **Keep node text short** — long labels wrap badly. Use `<br/>` for deliberate line breaks.
- **Prefer a table when the content is genuinely tabular.** A 5×3 comparison forced into a flowchart is worse than the table it should have been.
- Original images are **not** committed (they're inside the deck in Drive). The Mermaid block is the permanent record.

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

## Ask for what you need — insistently, not politely

The user has asked to be told **forcefully** when something is needed from them. A gap mentioned once, softly, at the end of a long response, gets missed — and a missed deck or an unconfirmed exam date costs marks months later.

**Every response that ends with an outstanding dependency must carry a clear ASK block.** Not a hint, not a closing offer.

Rules for the ask:

- **Put it at the end, under its own heading**, so it survives skimming.
- **Name the artifact exactly** — "the 549 session 3 deck from Teams", not "the next materials".
- **State the consequence of not having it**, concretely: *"without this, session 3's note cannot be written at all — 549 has no textbook from session 4 onward."*
- **Give a deadline where one exists**, tied to a real date in the study plan.
- **ONE ask per response.** The user has asked for this explicitly. Rank everything outstanding, ask for **only the top item**, and hold the rest. A list of five asks gets none of them done; a single clear ask gets done.
- **Move to the next only when the current one is resolved** — done, refused, or shown to be impossible. If the user answers something else and the ask is still open, repeat the *same* ask, not a new one.
- Keep a short "still outstanding, not asking yet" line if it helps them plan — but never let it become a second ask.
- **Repeat unresolved asks in the next response.** Do not assume silence means done. Something asked three turns ago and still outstanding is *more* urgent, not less — say so.
- **Distinguish blocking from optional.** "This blocks the note" and "this would improve the note" are different requests and must not be flattened together.
- **Never bury an ask inside prose.** If it needs doing, it goes in the block.

**Also flag deadline risk unprompted.** If a date in `STUDY-PLAN.md` is approaching and its milestone in `PROGRESS.md` is still unticked, raise it — even if the user asked about something else entirely. The plan exists to be enforced, not admired.

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
    ├── AIMLZG536-LLMForGenerativeAI/
    │   ├── 536-master.md        ← session index; open-book front index in Dec
    │   ├── notes/S01-….md       ← one file per session
    │   ├── labs/S05-…/          ← lab code
    │   └── source/
    │       ├── README.md        ← Drive links only
    │       ├── MATERIAL-LOG.md  ← what material exists per session
    │       └── transcripts/     ← plain-text transcripts (committable)
    ├── AIMLCZG549-APIDrivenCloudNativeSolutions/
    ├── AIMLCZG521-ConversationalAI/
    ├── AIMLZG546-SoftwareEngineeringForML/
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
