# AGENTS.md - working rules for this repo

Rules for any AI agent working in `MTech`. Read this before producing anything.
**Rules are hard unless marked "prefer".**

## 1. Repo Purpose

This repo is the user's MTech study knowledge base for BITS Pilani WILP.

The notes are a durable career reference first and exam preparation second. Exams matter, but the full session notes are the knowledge body the user revises from. Course logistics live once in the subject master index, never inside session notes.

Read `2026-2027-Sem1/STUDY-PLAN.md` before planning session-note work.

### Current Semester

Aug-Dec 2026. Folder names must match the handouts.

| Folder                                     | Code        | Course title                              |
| ------------------------------------------ | ----------- | ----------------------------------------- |
| `AIMLZG536-LLMForGenerativeAI`             | AIML ZG536  | Large Language Models for Generative AI   |
| `AIMLZG546-SoftwareEngineeringForML`       | AIML ZG546  | Software Engineering for Machine Learning |
| `AIMLCZG549-APIDrivenCloudNativeSolutions` | AIMLC ZG549 | API-driven Cloud Native Solutions         |
| `AIMLCZG521-ConversationalAI`              | AIMLC ZG521 | Conversational AI                         |

Important: 536/546 are `AIML`; 549/521 are `AIMLC`.

## 2. Non-Negotiable Gates

### Handout First

Every session note is created from the handout Learning Plan row, not from uploaded material.

The handout row decides:

### Handout-title alignment rule

When updating a session note, master index, or progress tracker, keep the session title and sub-topic wording aligned with the handout Learning Plan row. Do not invent alternate labels such as “Serving I/II”, “Reasoning I/II”, or shortened variants when the handout already provides the official wording. If the note title or master-row wording differs from the handout, correct it before considering the task complete.

Section and subsection headings inside the note must also stay aligned with the handout vocabulary. A heading may be slightly more explanatory, but it should still read like the same topic. Do not rename a handout topic into a different label just because the deck or a source file uses that phrasing.

Use the handout for the top-level session and part structure, and use the deck/PDF/paper for lower-level explanatory headings only when they make the same handout topic clearer. Lower-level headings may be reorganized for teaching flow, but they must stay within handout scope and still map back to the handout sub-topics.

Hard rule: the session title and all main Part/Section headings come from the handout. Subtitles, subheadings, and worked-example labels can come from the deck/PDF if they improve clarity, but they must never change the handout scope or replace the handout topic names at the top level.

If a slide title names a concept already covered inside an existing subsection, surface that title as a short topic label in the existing flow instead of creating a new explanatory sentence. Keep it to the title itself when the user only wants the topic name. If the label needs cleaner visual shape, make it a short subheading with no extra meaning and place it near the relevant `Mechanism` or `Intuition` block so the deck wording stays visible.

If the slide title introduces a genuinely new concept, decide whether it belongs inside the current handout row or in a different session. If it fits the current row, add it as the next appropriate subsection or concept block without creating a new session. If it belongs to a different handout row, do not import it here; log the mismatch and leave the note scoped to the current handout.

When the deck uses a short label as a teaching anchor, keep that wording visible in the note as a heading or short label instead of burying it only in prose, even if the underlying concept is already covered elsewhere. This is especially important for early definitional slides and section-divider titles that help the reader follow the sequence.

When polishing an existing note, prefer the deck's short teaching label for the visible heading when it clearly names the same concept, and reserve paraphrase for the explanatory paragraph beneath it. In other words: keep the heading deck-shaped, keep the explanation human-shaped, and avoid inventing a new label just because the deck title feels terse.

| Handout column      | Controls                                                |
| ------------------- | ------------------------------------------------------- |
| Contact Session     | Session number and whether rows combine sessions        |
| List of Topic Title | Session note title                                      |
| Sub-Topics          | Required note sections and examinable scope             |
| Reference           | Sources to read for mechanism, examples, and edge cases |

Hard completion gate: a session note is not complete until every topic and sub-topic in that session's handout Learning Plan row is explicitly taught in that same note. Missing one bullet means incomplete.

Coverage must be checked against the handout file itself, not the master index. A bullet counts as covered only when it maps to a clear heading, subsection, table row, worked example, or diagram. A keyword hit, passing mention, or implied relationship is not enough.

Uploaded PPT/PDF/papers/transcripts are teaching inputs. They do not create new session scope, rename sessions, merge sessions, split sessions differently, or add exam-scoped topics by themselves. If an upload contains older-offering material, extra material, or multiple sessions, use only the parts matching the handout row and log the mismatch in `source/MATERIAL-LOG.md`.

### Cited Sources Must Be Read

Before calling a note complete, read the exact handout row and then read/extract the sources cited in that row.

| Reference says                        | Required action                                                                                           |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Textbook chapter                      | Check `/_library/` first; extract only the cited chapter                                                  |
| Paper or public spec                  | Fetch it yourself; do not ask the user to upload public material                                          |
| Web Resources / Lecture Notes / blank | Treat the deck, and recording if available, as the teaching source; do not invent a hidden textbook layer |

Do this even when the deck looks sufficient. The deck sets instructor emphasis; references supply mechanism, examples, edge cases, and clearer figures.

If a cited source is missing, blocked, or out of reach, record the gap in `source/MATERIAL-LOG.md` and `MATERIALS-WATCHLIST.md`. Do not silently skip it or mark the note fully reviewed.

### No Deck, No Note

A session note is never written without that session's deck. The deck is the only artifact showing what this instructor actually taught and emphasized.

If the deck is missing, say so, do not write a provisional note, and mark Slides `✗` in `source/MATERIAL-LOG.md`. You may fetch public references and log them, but do not write the session note.

Also check the deck agenda slide. Agenda items count as covered only when the note teaches them as clear sections/subsections, not because nearby material is "close enough."

### Self-Contained Notes

Every session note must stand alone on any machine. It must remain complete if `/_library/`, `_shared/`, transcripts, handouts, local PDFs, or scratch files are absent.

Use local resources as inputs, not crutches. If a textbook, transcript, paper, lab, or `_shared/` note has a better explanation, fold that value into the session note. Never leave core understanding only in auxiliary material.

A session note may mention conceptual overlap with another subject, but it must never tell the reader to go to another subject's note to understand the current one. If background is needed, restate the minimum explanation inside the current note.

Every session-note touch includes a self-containment review.

## 3. Material Scope

### Out of Scope Means Out

A chapter the handout does not cite is not part of this semester. Do not pull from it, recommend it, or use it to expand exam-scope note bodies. Mark it `OUT OF SCOPE` in chapter maps.

Exceptions: the user directly asks, or a prescribed lab requires it. State clearly that the material is outside syllabus scope.

### Per-Subject Source Profile

| Subject | Source profile                                                                              |
| ------- | ------------------------------------------------------------------------------------------- |
| 549     | Only S1-S3 have books. S4-S16 are Web Resources / Lecture Notes, so decks are highest value |
| 521     | No textbook; references are public papers/specs, so fetch them                              |
| 536     | T1/T2/R1 chapters + papers cover most sessions; S6, S15, S16 are papers/web only            |
| 546     | T1/T2 chapters cover S1-S14; S15-S16 are lecture notes only                                 |

### Never Commit Raw Course Material

Do not commit `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, datasets, weights, transcripts, or secrets. `.gitignore` enforces this; do not weaken it.

Textbooks live in `/_library/` and are gitignored. Look there before asking the user for a book.

Secrets use placeholders only, such as `OPENAI_API_KEY`.

## 4. Intake Workflow

The user uploads per session and ideally names subject, session number, and file type. If session number is missing, infer from the master index and state the inference.

### Subject Is Never Inferred From `_library/` Naming

If the user uploads a file (paper, deck, transcript) without stating which subject it belongs to, **ask** before doing any work. Do not guess the subject by matching the upload against an existing `_library/` filename prefix, such as treating an uploaded paper as belonging to 536 because a file named `536-P1-...` already exists there. That naming can be stale, wrong, or a leftover assumption from an earlier session, and reusing it silently propagates the error into session notes across the wrong subject.

This applies even when the paper's content plausibly fits the guessed subject. Plausibility is not confirmation. One question up front costs less than reverting edits in the wrong subject's notes later.

Never trust a deck filename alone, either. Verify identity from title slide, agenda, footers, section dividers, and topic sequence against the handout Learning Plan row.

If one deck contains multiple sessions, split it by handout scope and log the split in `source/MATERIAL-LOG.md`. If the boundary is ambiguous, stop and ask; do not blend two sessions.

| Format                      | Extract with    | Required care                                       |
| --------------------------- | --------------- | --------------------------------------------------- |
| `.pptx`                     | `python-pptx`   | Read slide text, speaker notes, and embedded images |
| `.pdf` text                 | `pdfplumber`    | Extract text and inspect figures where relevant     |
| `.pdf` scanned              | OCR first       | Say OCR is happening                                |
| `.docx`                     | `python-docx`   | Use for handouts and transcripts                    |
| `.txt/.srt/.vtt` transcript | direct          | Reconcile noisy terms against slides                |
| `.mp4` / video              | impossible here | Never claim to have watched or transcribed it       |

Always extract and look at deck images. Slide text often omits equations, shapes, or labels that are only in images.

Auto-transcripts are noisy. Correct obvious terms silently, such as `RoPE`, `SwiGLU`, `GQA`, and `KV-cache`.

## 5. Session Note Contract

Follow `2026-2027-Sem1/_templates/SESSION-TEMPLATE.md`.

One file per session:

```text
<subject>/notes/S<NN>-<slug>.md
```

Use the `S` prefix in every subject, including 521. The handout may say `L1`, but filenames still use `S01-`. Use `L1` only in prose when referring to the 521 handout wording.

Creating a note must update:

| Artifact                 | Required update                              |
| ------------------------ | -------------------------------------------- |
| `<code>-master.md`       | Note row / status                            |
| `PROGRESS.md`            | Deck/note/open/lab status                    |
| `source/MATERIAL-LOG.md` | What arrived, what was read, what is missing |
| `MATERIALS-WATCHLIST.md` | New or resolved blocking material gaps       |

Lab code lives in `<subject>/labs/S<NN>-<slug>/`, never in `notes/`.

### Required Structure

1. Title: `<Subject Name> · Session NN · <Handout Topic Title>`
2. One line: `*Learned <date>*`
3. `## Why this matters`
4. Body: `## Part N · <title>` then `### N. <Concept>`
5. `## Self-study / Lab / build`
6. Exam footer linking to the master index

Do not add a hand-written `## Topics` index. The headings already form the navigable outline and cannot drift.

Course logistics, admin, deck-errata, source notes, and build logs do not belong in session notes unless they materially change scope or interpretation.

The `## Why this matters` section must answer three things clearly: what this session teaches, why it matters in practice, and what the reader should be able to explain after reading it.

### Teaching Flow First

Write session notes as one coherent learning path, not as a stitched summary of separate sources. The reader should be able to move through the note without needing to reconstruct the logic from deck order, textbook order, or paper order.

You may reorder material within the handout scope when that makes the concept easier to learn, but do not rename, drop, or silently merge handout topics. Add short bridge sentences and checkpoints where needed so each part feels connected to the next.

### Every Concept Must Teach

Each concept must include, in this order:

```text
Intuition -> Mechanism -> Worked example -> Tradeoff / when NOT to use -> Diagram
```

Rules:

- Tradeoff is never blank and never "depends on the use case." Name the specific case where the simpler option wins.
- Worked examples must be reproducible by hand or in <=30 lines of code.
- Verify arithmetic by running it before writing it.
- Landscape topics get comparison tables.
- Hard concepts need a plain-language on-ramp and a short everyday analogy.
- Dense math must be signposted as skimmable on first pass, with the key takeaway stated plainly.
- More explanation belongs at hard spots, not everywhere.
- Lead with the answer or concept name first; do not bury the key definition in the second half of a subsection.

### Use Case Grounding

Every concept needs one grounding example that states a real problem and how the concept resolves it, not mechanism in the abstract alone. Check for this in the same pass as the Tradeoff.

- Prefer a real-world/production scenario tied to the subject's domain (fraud detection, a bank's compliance corpus, a support-ticket pipeline, a Kubernetes flash-sale autoscale, a misrouted chatbot intent) over an invented toy sentence.
- A short toy example (e.g. "Alice called Bob" vs "Bob called Alice" to isolate word order) is acceptable only when it is the clearest way to isolate the mechanism, not as a default.
- Format: `**Use case — <short label>.**`, 3-5 lines, in the note's existing voice. Fold into the Worked example or Tradeoff subsection if that reads more naturally than a standalone block.
- Skip sections that are purely definitional, notational, or a taxonomy/comparison table. Do not force a scenario onto a shape table or a vocabulary list.
- If a Worked example, `***In practice***` box, or Tradeoff paragraph already answers "what breaks without this and how is it fixed," that already satisfies the gate. Do not add a second example on top of it.

### Wording Pass

Before marking a note reviewed, read it end to end for:

- Ambiguous sentences that need a re-read to parse
- Jargon used before it is defined
- The same concept named two different ways in different sections of the same note
- Decorative or vague metaphors that do not actually clarify anything (the canonical bad example: "predicting text and generating text are the same machine, run in two directions") — cut them or replace with a direct statement of what is actually happening
- Compressed, mechanical phrasing that sounds like a lecture dump rather than a human teacher

A wording pass never changes technical correctness, formulas, tables, numbers, or the Intuition → Mechanism → Worked example → Tradeoff → Diagram order.

Write session notes in a human-first teaching voice. Prefer short direct sentences, natural transitions, and plain-language setup before dense terminology. The reader should feel guided through the concept, not exposed to a compressed summary of it.

Readability is a completion gate, not a nice-to-have. If one subsection stacks too many new ideas, quotes, cautions, and examples without a pause, split it with a short bridge sentence, a small table, or a clearer sequence. A note should never require the reader to mentally unpack a dense lecture dump before the teaching point becomes clear.

Every touched note also gets a plain-language pass. Ask: could an intelligent non-specialist follow this section without already knowing the jargon? If not, add one short plain-English bridge before the dense block. In practice this means:

- define acronyms and specialist terms at first use in ordinary words
- put one plain-language sentence before any dense table or formula-heavy block
- explain what a comparison is really comparing before presenting the table
- do not stack three or four unfamiliar terms in one sentence without unpacking them
- if a lay reader would likely ask "what is that?" or "why does that matter?" answer it immediately, not three paragraphs later

When a deck teaches a topic through a staged visual build-up, preserve that teaching path in the note. Do not collapse six visual steps from the deck into one dense paragraph if those steps are carrying the explanation. The note does not need a slide-by-slide clone, but it must preserve the same learning progression in prose, diagrams, or both.

`## Why this matters` is required in every session note, but it must stay tight. Default length: **3-5 lines**. It should do only three things: state what the session teaches, why it matters in this subject, and what the reader should be able to explain after reading it. Do not turn it into career marketing, a generic motivational paragraph, or a second introduction to the whole note.

Optional depth blocks are allowed when useful:

| Block                | Use                                                             |
| -------------------- | --------------------------------------------------------------- |
| `***In practice***`  | Production tools, auth, rate limits, retries, cost, conventions |
| `***Going deeper***` | Deeper mechanism or adjacent concept outside course depth       |

Use `Going deeper` as the only optional-depth label. Do not introduce `Extra depth` as a second phrasing for the same idea.

Optional material must stay inside `***In practice***` or `***Going deeper***` blocks. Do not promote beyond-scope material into a top-level `###` concept unless the handout itself makes it part of the session scope.

Mark beyond-course depth clearly and keep it out of exam-scoped claims.

### Source Style

Session notes state knowledge directly.

Do not write:

- `Reference:`
- `T1`, `R2`, `ch3`
- "the deck says"
- "the source says"
- "in the instructor's own words"
- "spoken version first"
- "worth memorising verbatim"
- "quotable"
- "the deck copied"

Do not reproduce textbook text. Explain in fresh words. Where origin is itself the knowledge, such as REST = Fielding 2000, GraphQL = Facebook 2015, or BPE = Sennrich 2016, that fact may stay.

If the deck or handout names a topic but no source teaches it, write the missing explanation yourself and mark it with a short aside such as `*filled-in reasoning for this syllabus item*`.

## 6. Organization Rules

### Organize by Topic, Never by Source

Never create sections like "From slides", "From textbook", or "From paper."

One topic, one place. Slide figure, textbook mechanism, transcript aside, and model-added clarity all live inside the relevant topic section.

Layer new material into the existing note. Never create a second note for a later source and never append a new source summary at the bottom.

Use the smallest effective edit when improving a study-stable note: add the missing subsection, replace the weak example, clarify the paragraph, or redraw the diagram. Do not rewrite the whole note unless the structure itself is broken.

### Subjects Are Self-Contained

No cross-subject links in session notes. Do not write `see 546 S9`, `shared with 536`, or point to `_shared/` as required reading.

Same-subject navigation is fine, such as "see section 4" or "S14".

If a topic appears in multiple subjects, each subject must teach it fully from that subject's angle. Duplication is intentional.

`_shared/` is optional synthesis. A session note may duplicate `_shared`; it must never depend on it.

## 7. Diagram Rules

Every concept in every session note and `_shared/` note needs at least one clear diagram.

### SVG First, Mermaid Fallback

First reuse an existing suitable SVG in `notes/assets/`. If none exists, create an authored SVG:

```text
<subject>/notes/assets/S<NN>-<figure-slug>.svg
```

Use Mermaid only when:

- No suitable SVG exists yet
- The structure is a tiny abstract flow
- Mermaid is genuinely clearer than an SVG

Do not keep Mermaid beside an SVG if both teach the same picture. The SVG replaces the Mermaid unless the Mermaid teaches a genuinely different abstraction.

An SVG is not done until the note embeds it:

```md
![clear alt text](assets/S<NN>-<figure-slug>.svg)
```

Before saying complete, verify:

1. The note has the SVG link.
2. The linked SVG file exists.
3. No duplicate Mermaid remains for the same concept.
4. No unused SVG files remain in `notes/assets/`.

Do not commit original slide screenshots, extracted deck images, textbook images, or paper figures.

### Diagram Source Order

1. Convert the deck's own figure after looking at it.
2. Check cited textbook chapters for clearer figures.
3. Check cited papers/public specs for canonical diagrams.
4. Draw your own, marked `(my own)` when needed.

Carry important labels across using course terminology. Do not invent structure the source does not support; if an arrow is ambiguous, explain it in prose.

### Deck Visual Parity

Deck images are not optional decoration. When auditing or updating a session note, check whether the deck is teaching any concept mainly through diagrams, staged screenshots, token flow examples, tables, or side-by-side visual comparisons. If yes, mirror that explanatory value in the note with authored diagrams, clearer tables, or a stepwise worked example.

A note fails this gate if the prose mentions a concept that the deck explains visually, but the note does not preserve the visual reasoning the learner needs to follow it.

Minimum review questions for every touched session note:

- Which deck visuals are doing real teaching work rather than just illustrating a sentence?
- Does the note preserve those visuals' learning sequence in a self-contained way?
- Are there any sections where the deck is easier to understand than the note because the note flattened a visual explanation into compressed prose?

### Visual QA Is Mandatory

A diagram that merely parses, links, or renders is not done. It must teach clearly at note width.

Check every touched diagram for:

- Correct labels and source-shape fit
- Visible arrows and arrowheads
- No avoidable crossing or overlapping arrows
- No tiny unreadable text
- No cramped bottom or caption area
- No cut-off edges
- No decorative clutter
- No misleading simplification

If a diagram only works when crowded into one canvas, split it into smaller stages or separate figures instead of forcing all flows into one image. Prefer a simpler diagram that teaches clearly over a dense one that technically fits.

If the user flags one example of a recurring issue, audit the whole touched note for that issue. Do not fix only the named diagram.

Render and inspect SVGs when tooling allows. If rendering is unavailable, keep the diagram simpler and state that only syntax/link validation was possible.

### Mermaid Direction

`LR` is not the default.

| Use               | When                                              |
| ----------------- | ------------------------------------------------- |
| `flowchart TD`    | 6+ boxes, branching/converging flows, long labels |
| `flowchart LR`    | <=5 boxes, short labels, strictly linear          |
| `flowchart BT`    | Built-up-from-parts diagrams                      |
| `timeline`        | Eras or dated evolution                           |
| `sequenceDiagram` | Protocol handshakes with named participants       |
| Markdown table    | Comparisons and Venn-style intersections          |

For X-vs-Y, prefer one diagram with two subgraphs. Inside a subgraph, `direction TB` may override the parent.

Quote Mermaid labels containing punctuation such as `(`, `)`, `:`, `,`, `#`. Avoid `end` as a node id. Prefer plain text over HTML styling.

## 8. Open-Book Pages

Each session has two artifacts:

| Artifact               | Purpose                                        | Rule         |
| ---------------------- | ---------------------------------------------- | ------------ |
| `notes/S<NN>-...md`    | Full knowledge, never printed                  | Write first  |
| `openbook/S<NN>-...md` | Two-page lookup sheet for bound open-book exam | Derive later |

Never write the condensed page before the full note. If behind, drop the condensed page, not the note.

Follow `_templates/OPENBOOK-TEMPLATE.md`. Hard limit: two sides of A4.

Open-book pages keep formulas, symbol meanings, comparison tables, tradeoff lines, diagrams, and worked-example answers. They cut long prose, full walkthroughs, and depth blocks.

BITS bans loose sheets. The bound open-book file must be printed and bound by 22 Nov 2026.

## 9. Tone and Communication

Write plainly. Define jargon on first use.

Prefer:

```text
table > list > paragraph > vague prose
worked example > all of them
```

Flag uncertainty inline with `⚠️`. Never present a guess as fact.

Own mistakes plainly and state the wrong belief so it is not repeated.

When asking the user for material:

- Ask for one thing only: the top blocker.
- Put the ask under its own heading at the end.
- Name the artifact exactly.
- State the consequence of not having it.
- Repeat unresolved blocking asks in later turns.
- Distinguish blocking from optional.

## 10. Materials Watchlist

Read `2026-2027-Sem1/MATERIALS-WATCHLIST.md` at the start of session-note tasks.

Update it whenever material arrives or a new material gap appears.

Raise dated items unprompted near their blocking date.

Verify delivered files before filing them. Titles collide; check page count, publisher, table of contents, and fit against the cited reference.

## 11. Finish Checklist

Run these before finishing:

```bash
cd tools && npm run check
git status --short
```

Do not eyeball the checklist:

- [ ] Handout row checked directly from `.docx`/`.pdf`
- [ ] Every handout topic and sub-topic explicitly covered in the same note
- [ ] Handout-cited sources read/extracted or gaps recorded
- [ ] Deck/session identity verified from slide contents, not filename alone
- [ ] Mixed decks split by handout scope and logged
- [ ] Deck agenda items covered or genuine gaps recorded
- [ ] Deck visuals that carry explanation were preserved with equivalent note visuals, tables, or stepwise teaching flow
- [ ] Every concept has Intuition, Mechanism, Worked example, Tradeoff, and Diagram
- [ ] Arithmetic in worked examples was executed
- [ ] Note is self-contained; no core knowledge lives only in `_shared/`, labs, transcripts, or local sources
- [ ] No source references or source-framing prose in session notes
- [ ] No cross-subject links in session notes
- [ ] Diagrams parse, are linked, are visually QA'd, and have no unused SVG duplicates
- [ ] Master index, `PROGRESS.md`, `MATERIALS-WATCHLIST.md`, and `source/MATERIAL-LOG.md` updated where needed
- [ ] Condensed page, if present, was derived from the full note
- [ ] No PDFs, slides, datasets, transcripts, weights, or secrets are staged
- [ ] Dates and weights match handouts or are marked `⚠️`

Do not run `git commit` from the sandbox. It can create `.git/*.lock` files that the sandbox cannot remove. Stage work if requested, then give the user the commit command.

## 12. Repo Layout

```text
MTech/
├── AGENTS.md
├── .gitignore
├── tools/
└── 2026-2027-Sem1/
    ├── STUDY-PLAN.md
    ├── MATERIALS-WATCHLIST.md
    ├── PROGRESS.md
    ├── <CODE>-<CourseTitle>/
    │   ├── <code>-master.md
    │   ├── notes/S01-....md
    │   ├── notes/assets/S01-....svg
    │   ├── openbook/S01-....md
    │   ├── labs/S01-.../
    │   └── source/
    │       ├── README.md
    │       ├── MATERIAL-LOG.md
    │       └── transcripts/      # gitignored
    ├── _shared/                  # optional synthesis only
    ├── _library/                 # gitignored textbooks
    └── _templates/
```

## 13. Key Dates

| Date               | Event                                                                 |
| ------------------ | --------------------------------------------------------------------- |
| 10-20 Aug 2026     | Quiz window; 549 and possibly 521 only per current resolved plan      |
| 27 Aug-7 Sep 2026  | 549 project/assignments, 536 assignment, 546 situated learning window |
| 19 Sep 2026 EN     | 546 mid-sem, closed book                                              |
| 20 Sep 2026 FN     | 549 mid-sem, closed book                                              |
| 20 Sep 2026 EN     | 536 mid-sem, closed book                                              |
| 29 Oct-11 Nov 2026 | 546 Assignments I & II                                                |
| 22 Nov 2026        | Print and bind open-book file                                         |
| 5 Dec 2026 EN      | 546 comprehensive, open book                                          |
| 6 Dec 2026 FN      | 549 comprehensive, open book                                          |
| 6 Dec 2026 EN      | 536 comprehensive, open book                                          |

521 dates are announced in class or Canvas and have no makeups. Treat any 521 date as unconfirmed until verified.

536 S8 and 521 S8 are revision sessions; those mid-sems cover seven sessions of new material, not eight.
