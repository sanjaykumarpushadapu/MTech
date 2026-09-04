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

### AGENTS Compliance Is Automatic

Every task that creates or edits files must be done under this `AGENTS.md` contract automatically. The user should not have to ask, "did you follow the agent rules?"

Before editing, identify which AGENTS gates apply to the task. After editing, run the applicable checks and state the result in the final response. If a hard gate could not be checked, say exactly which gate remains open and why. Do not answer as if the work is complete when an applicable AGENTS gate was skipped.

For session-note, lab, source-log, master-index, progress, or watchlist work, the minimum required compliance pass is:

- Read `STUDY-PLAN.md` and `MATERIALS-WATCHLIST.md`.
- Check the session's handout Learning Plan row directly from the handout file when the task touches session scope, title, topic coverage, lab scope, or completion status.
- Verify uploaded material against the handout row and deck/session identity before changing scope.
- Keep notes self-contained; never leave core knowledge only in a notebook, `_shared/`, transcript, slide, PDF, or local scratch file.
- Update all tracking files affected by the change.
- When touching material intake or scope, enumerate every `MATERIAL-LOG.md` in the repository. Fully reconcile the affected subject log(s) against the current checkout, and scan the other logs only for cross-subject scope, numbering, or path collisions. Do not append repetitive audit history: each log is a compact current snapshot, while Git history preserves detailed chronology. Record unavailable external materials as current gaps rather than treating historical verification as a current file check.
- Run `cd tools && npm run check` and `git status --short` before the final response. If the Windows shell passes repository globs literally and the bundled check fails for that reason, run each checker with an explicit tracked-file list, record the shell limitation, and do not claim the failed bundled command passed.

The final response must include a short compliance line, for example: `AGENTS check: handout row checked, tracking updated, repo checks passed; open gap: S02 remaining lab files not held.` Keep it concise, but do not omit it.

### Repeated Pushback Means Re-Verify, Not Re-Explain

If the user questions the same claim, format choice, or compliance status more than once in a conversation — even worded differently each time — treat the second instance as a signal to re-check the underlying evidence directly (the source file, the deck's actual media/XML, the current repo state), not as a cue to restate the rule or explain it more clearly. A confident restatement of a prior conclusion is not verification of it, and a thorough audit of one thing (e.g., a text/topic keyword sweep) does not stand in for verifying a different thing the user is actually asking about (e.g., an image audit) — name explicitly which check was actually run before claiming the point is settled. When re-checking confirms the original claim, say so and show what was checked. When it doesn't, say so plainly and fix it before responding again.

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

### Deck-title section split

The top-level `##` Part/session headings follow the handout (above). Beneath them, the `###`/`####` topic headings should mirror the deck: **give each distinctly-titled deck slide its own section, and use the deck's exact slide title as the heading** (lightly de-corrupted for PDF ligature errors, e.g. `Produc7on` → `Production`). This keeps the note's topic structure a mirror of the deck the instructor taught from, and makes a slide findable by its title.

- **One titled slide, one section.** Do not merge two separately-titled deck slides under a single heading, and do not bury a titled slide as a "worked example", "exercise", or sub-bullet inside another section. If the deck gives it a title and a slide, the note gives it a heading. (S01: the *Lifecycle Example — Banking* slide and the *Exercise: Map the Agent Lifecycle* slide are their own sections, not blocks under the pipeline heading. S02: *HNSW: Memory Layout* and *Parameter Tuning: HNSW* are two sections, not one merged "Memory Layout and Parameter Tuning".)
- **Carry the deck's numbering when it has one.** If the deck numbers its topic slides (`1. Tokenization — The Foundation`, … `6. Production Concerns …`), reproduce those numbers in the headings. If the deck does not number its topics, a note-local sequential numbering is fine — but keep it contiguous, and renumber the following sections after any split.
- **Several slides sharing one title** (a multi-slide build-up — e.g. the five `BERT Pipeline` slides) fold into the single deck-titled section; do not emit five near-identical headings.
- **Synthesis sections keep their own name.** When a section has no single corresponding deck slide — a bridge/intro the note adds, or handout scope the deck doesn't cover (e.g. BM25/DPR/RRF absent from the S02 deck) — give it a plain descriptive heading. Do not invent a fake deck title.
- After any retitle or split, re-run the coverage checker: a heading word the checker was matching against (e.g. "mathematics") can disappear in a rename and surface a false negative to fix in the body.

### Fact-level source ownership and leakage gate

Coverage and heading order do not prove that details live under the correct source topic. Before editing a deck-backed note, create a temporary fact-ownership ledger for every substantive slide: title, named models/algorithms, figures, examples, mechanisms, and every important number or percentage, with one deliberate note destination for each. Treat each source-titled section as a closed boundary during drafting. Do not place a later slide's number, example, mechanism, or figure interpretation in an earlier or adjacent section merely because the topics are related. If the deck intentionally repeats a fact, record both source occurrences; otherwise classify it as **exact source detail**, **intentional synthesis**, **clearly labeled additional context**, or **unresolved**. Synthesis belongs under an explicitly named synthesis section and must not be used to satisfy slide-level coverage. Before finalizing, run a targeted leakage scan over adjacent slides, repeated-title slides, divider/extra-slide boundaries, and all distinctive numbers/named items, then manually verify every hit against the ledger. A passing `52/52` coverage result is not a substitute for this fact-level ownership check.

### Part/topic hierarchy

Use a consistent hierarchy in session notes: `## Part N · ...` for major handout-aligned Parts, `### N.M ...` for the main topics within that Part, and `#### ...` for source-slide subtopics or details. Do not use one global topic-number sequence across Parts, and do not introduce unnumbered peer headings that visually compete with the Part's numbered topics. Extra or non-examinable material gets its own parent `##` section and its own local topic numbering.

### Diagram interpretation and learner-facing explanations

When converting a pipeline or model diagram into study notes, distinguish **what the source lists** from **what the source proves**. A bullet placed under a stage is not automatically a mandatory step, a universal practice, or evidence that the stage directly causes the stated capability. Preserve the source's order and labels, then qualify optional recipe choices, repeated cross-stage techniques, and benefits that depend on data or implementation. Keep the learner-facing explanation simple: use a numbered flow, purpose, output, and one memory aid, while retaining a short accuracy caveat where simplification could mislead. In particular, do not claim that Q&A formatting alone creates instruction following, that online training is necessarily continuous, or that standard deployment optimizations are specified by a source slide when the slide only says `Optimization`.

### Capture a Temporary Slide Audit at Intake

**The moment a deck is uploaded, before writing or editing the note, create a temporary slide inventory** in the OS temp directory or an ignored subject-level audit directory. It must contain one row per source slide — slide number, title, and named items (models, algorithms, frameworks, protocols, figures, and table labels). Include title, agenda, disclaimer, objectives, recap, and reference slides too; if a slide is routed to the master index, leave its named-items cell blank rather than omitting the row.

Do not create or commit `<subject>/source/S<NN>-slide-inventory.md` by default. A permanent inventory is justified only for an ambiguous multi-session split or when the user explicitly requests a durable source index. Delete the temporary inventory after the audit unless it is needed for one of those documented reasons.

Before accepting the audit, read the source's actual page/slide count from PDF/PPTX metadata and assert that the temporary inventory row count matches it exactly. A coverage result such as `52/52` is not evidence of full coverage when the source has 62 slides and the temporary inventory has only 52 rows.

**Verify coverage by matching, not by reading.** First run the checker in all-slide mode to validate temporary inventory completeness, then run the normal substantive-content check:

```bash
cd tools
node check-slide-coverage.mjs <temporary-inventory.md> <note.md> --all
node check-slide-coverage.mjs <temporary-inventory.md> <note.md>
```

It reports every named item absent from the note. Judge each hit: a genuine omission gets added to the note; a false positive (PDF character corruption, a spelling variant, a word the note phrases differently) gets pruned from the temporary inventory so the signal stays clean. The gate is a clean run, recorded as a compact result in `source/MATERIAL-LOG.md` when useful.

Reading the deck and concluding "this looks covered" is not a coverage check. That judgement repeatedly passed notes that had dropped named items, collapsed the deck's own structure, and replaced concrete lists with an ellipsis. Matching is not a judgement call.

### Learner-note provenance boundary

Keep source provenance and audit identifiers out of learner-facing notes unless the user explicitly requests them. Do not add bookkeeping labels such as `Source slide N`, `(source slide 30)`, visual IDs, or coverage verdicts to headings or prose. Keep those details in temporary audit evidence or the compact material ledger. Preserve exact mapping with clean deck titles as headings, one section for each distinctly titled slide, and bounded subheadings when repeated-title slides share one section.

**Mandatory final preflight:** scan every changed learner-facing note for audit-only provenance patterns before finalizing. Any hit is a failure unless the user explicitly requested those labels in the note.

### Respect the Deck's Own Deferrals

When a source marks a topic as covered later — "(Module 2)", "we'll see this in L7", "detail next session", "more on this later" — **name the point, name where it is covered, and stop.** Do not teach the deferred material now. The instructor chose the order; pre-empting it buries this session's own point under material the reader has no grounding for, and duplicates the later session badly. If you are explaining the mechanism behind a fix the source postponed, you have left this session's scope.

**Match the source's weight.** How much the note says about something tracks how much the source says:

| Source gives | Note gives |
| ------------------------------ | ------------------------------------------------------------ |
| A one-line warning or aside     | About a line — not its own subsection                        |
| A table                         | The same rows, with the source's own labels — no invented rows, no dropped rows, no renamed categories |
| A full slide of mechanism       | Full treatment, with all required blocks                      |

Your own clarity work — an analogy, a worked example, a plain-English bridge — is still expected and still welcome. It exists to explain **what the source teaches**. It must never open up what the source postponed, and never reshape what the source presented.

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

### Exhaustive Cross-Checks, Not Spot Checks

When a deck, handout, or paper is provided to check a note against, that is a completeness audit, not a review. Extract and read every page or slide, not a sample — the user is trusting this check specifically because they cannot re-verify it line by line themselves. A missed slide is a missed exam point, not a minor oversight. Do not report a note as complete or aligned without having actually walked the whole source.

When source content overlaps with something the note already covers, check whether the source presents it as its own distinct point (its own heading, its own slide, its own labeled block) before folding it into an existing section. If the source gives it a name and a place, the note should too, even if the underlying idea is covered elsewhere — don't silently merge a source's own structure into a differently-labeled section just because the ideas rhyme. If genuinely unsure whether something is "already covered" or "quietly merged," treat it as missing and give it a visible home matching where the source put it.

### Draft-to-Source Reconciliation

Reading every slide before writing is necessary but not sufficient — synthesis drops things. Writing a note from memory of "I read the whole deck" misses one-line mentions: a fourth named example buried in a bullet, a paper citation given once, a naming distinction that only appears in a single sentence. These get seen during extraction and then quietly dropped during writing, because writing summarizes rather than transcribes.

After a note is drafted from a source, do a second, separate pass: work through the extracted source text bullet by bullet (or slide by slide) and check each concrete fact, named model, named example, and cited paper off against the draft. Do not consider the note checked until this reconciliation pass has actually happened — "I read the source already" is not the same claim as "I verified the draft still has everything the source had."

### Source-figure fidelity is a separate gate

Slide coverage and clean visual QA do not prove that the note preserved the source's illustrations. During reconciliation, enumerate every substantive source figure, diagram, chart, and table image by slide number. For each one, confirm that the note embeds the original asset, uses a clearly labelled faithful recreation, or explicitly records why it is omitted. A conceptually similar replacement is not evidence that the source figure was preserved. **When preserving an image from a source slide, use PNG format only; do not convert the source slide image into SVG.** SVG is permitted only for a newly authored explanatory diagram that is clearly labelled as a recreation rather than the source image. When an original figure is copied into the note, retain visible provenance or copyright wording from the source where practical.

**Classify every source slide image before editing assets:** (a) a genuine figure, chart, diagram, or visual workflow; (b) a table or text screenshot that should normally be transcribed into Markdown/text; or (c) no image. Do not create a PNG for text-only slide content, and do not delete a genuine figure merely because the surrounding explanation is textual. Keep a temporary slide-to-asset map with the classification and destination note section. After editing, verify that every intended asset has one note reference, every reference resolves, and no orphan asset remains; visually inspect each newly added or restored image at native resolution. **An asset-reference check reporting zero missing, duplicate, or orphan files proves only internal consistency; it does not prove source completeness. Independently compare the source-slide inventory with the note's asset map and record every substantive source visual as preserved, transcribed, or deliberately omitted with a reason.**

**Detail-crop placement rule:** When one source visual is split into multiple readable crops, give each crop one bounded learner-facing destination. Place each crop immediately beside or before the explanation for its own route/panel/topic, in source order, under a short deck-shaped subheading or caption. Do not group all crops at the start of a section and explain them later. Pair distinctive labels, numbers, options, and annotations with the crop that contains them. Inspect every crop boundary for clipped labels or remnants of neighboring panels, then update asset assertions and rerun orphan/reference checks.

**Hard gate:** Do not begin source-asset edits or claim figure coverage until the rendered slide inventory and slide-to-asset map exist, contain a nonzero row for every source slide, and match the source slide count exactly. A post-hoc reference check never substitutes for this source-first audit.

### Top-Level Section-Order Gate

Before assigning Part numbers, writing learner-facing cross-references, or doing pedagogical restructuring, extract the ordered top-level topic blocks from the source and the note. Map each note `##` section to its first and last source-slide numbers, then assert that the mapped intervals are monotonically increasing. A coverage pass, fact-ownership pass, or correct heading list does **not** prove that complete sections are in the right order. Re-run this assertion after every section move. If a pedagogical reorder is intentional, record the exception and rationale in temporary reconciliation evidence; otherwise restore the source order. Never infer Part 4/Part 5 identity from an earlier note, filename, or plausible teaching progression. Keep learner-facing cross-references name-based so a later reorder cannot silently make them wrong.

**PowerPoint media audit rule:** Do not inventory source visuals by checking only ordinary `PICTURE` shapes. Inspect slide XML relationships, `a:blip` media references, image placeholders, grouped content, and rendered slides; placeholder-backed figures can be substantive source images even when `python-pptx` does not expose them as picture shapes. Inspect annotation/ink layers separately and exclude pen marks from preserved assets unless the source explicitly treats them as instructional content.

### Default to More, Not Less

Session notes exist to teach and to be revised from. When extending a note from new source material, prefer including a genuinely useful fact, number, named model, or example over trimming for length. Concision is a wording-quality goal (see Wording Pass) — write clean sentences, cut filler — not a content-quantity ceiling. Cutting real source content to keep a note short is the wrong tradeoff in this repo. A longer note that teaches more is preferred over a shorter one that teaches less, as long as every addition is accurate, sits under the right heading, and doesn't duplicate something already there.

**"More" means more facts, rows, examples, and named items — not more words for the same point.** A second analogy, a duplicate diagram, or a paragraph re-explaining what a table already shows is over-cooking, not teaching (see the Wording Pass over-cooking and meta-aside bullets). Default to more *content*; default to fewer *restatements*.

## 3. Material Scope

### Documentation ownership

Keep each fact in one canonical place:

- `<subject>/source/MATERIAL-LOG.md` — current subject-level material availability, scope checks, durable outputs, and active gaps. Keep it compact; do not append repetitive audit narratives.
- `MATERIALS-WATCHLIST.md` — cross-subject blockers, requested uploads, and reminders only; do not duplicate full session ledgers.
- Temporary deck-audit files — one-row-per-slide working evidence used during intake and coverage checks; keep them outside Git or in an ignored audit directory, and delete them after verification unless a permanent index is explicitly justified.
- `<code>-master.md` — course navigation, handout scope, and note status; never point to a note that does not exist.
- `notes/` — durable teaching content; `labs/` — runnable lab material; `_shared/` — optional synthesis; `_templates/` — reusable templates.

Use Git history for detailed audit chronology. Before changing a material ledger, reconcile its current tables and paths instead of adding another dated narrative block.

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

The user uploads per session and ideally names subject, session number, and file type. If session number is missing, infer it only from the source contents and the handout Learning Plan row, and state the inference.

### Subject and Session Identity Come From Evidence, Not Filenames

If the user uploads a file (paper, deck, transcript) without stating which subject it belongs to, **ask** before doing any work. Do not guess the subject by matching the upload against an existing `_library/` filename prefix, such as treating an uploaded paper as belonging to 536 because a file named `536-P1-...` already exists there. That naming can be stale, wrong, or a leftover assumption from an earlier session, and reusing it silently propagates the error into session notes across the wrong subject's notes.

This applies even when the paper's content plausibly fits the guessed subject. Plausibility is not confirmation. One question up front costs less than reverting edits in the wrong subject's notes later.

**Never use an uploaded deck's filename as authoritative subject or session metadata.** Filenames such as `CS-4`, `S04`, `Session4`, `Lecture-4`, or `L4` may be aliases, old numbering, course-provider numbering, handout numbering, or arbitrary upload names; `CS-4` and `S04` can refer to the same deck, and a filename number can disagree with the repository session number. Treat the filename only as an untrusted clue.

Resolve identity in this order:

1. Read the deck's title slide, agenda, footers, section dividers, and topic sequence.
2. Match that internal evidence to the subject's handout Learning Plan row and the repository master index.
3. Use the handout's contact-session mapping as the canonical repository session ID (`S<NN>`); keep any handout/module/lecture alias in the source log or prose, not as a replacement for `S<NN>`.
4. If filename and content disagree, record the conflict and follow the content + handout mapping. If content and handout still disagree or the subject is uncertain, stop and ask before writing or moving anything.

If one deck contains multiple sessions, split it by handout scope and log the split in `source/MATERIAL-LOG.md`. If the boundary is ambiguous, stop and ask; do not blend two sessions.

### Every Deck Gets a Temporary Slide Audit

**The moment any deck is uploaded — every subject, every session, including re-uploads and decks that look already covered — run the temporary slide-audit protocol before writing or editing the note.** Do not create a committed `S<NN>-slide-inventory.md` by default. Keep the complete slide → home verdict table in the temporary workspace; it is QA evidence, not permanent study documentation. A permanent inventory is allowed only for an ambiguous multi-session split or an explicit user request, and the reason must be recorded in the material log.

| Format                      | Extract with    | Required care                                       |
| --------------------------- | --------------- | --------------------------------------------------- |
| `.pptx`                     | `python-pptx`   | Read slide text, speaker notes, and embedded images |
| `.pdf` text                 | `pdfplumber`    | Extract text and inspect figures where relevant     |
| `.pdf` scanned              | OCR first       | Say OCR is happening                                |
| `.docx`                     | `python-docx`   | Use for handouts and transcripts                    |
| `.txt/.srt/.vtt` transcript | direct          | Reconcile noisy terms against slides                |
| `.mp4` / video              | impossible here | Never claim to have watched or transcribed it       |

Always extract and look at deck images. Slide text often omits equations, shapes, or labels that are only in images.

### Upload audit protocol (runs automatically on EVERY uploaded file)

**Any file uploaded for a session is itself the trigger — run this protocol in full, unprompted.** It does not matter whether the note doesn't exist yet (first write), already exists (re-audit the note against the deck), or the same deck is being re-uploaded later (re-verify from scratch). "The note was already written / already audited" is never a reason to skip — an existing note is exactly the case that hides stale gaps. Do not wait to be asked to audit; do not assume a prior pass was complete.

Do not rely on the master index, the note's history, or a prior audit — **only the rendered source is authoritative.** Run all six steps in one pass; the reason past audits kept surfacing "new" gaps is that they were done partially. Do not declare the audit done until every slide has a verdict.

1. **Read the source count, render every slide to an image, and look at it.** `pdftoppm`; if poppler is missing, `PyMuPDF`/`fitz` or `pdf2image`. Text extraction silently drops image-only slides (a graphic that extracts as just its title) and every label that lives inside a diagram. Reading extracted text is not the same as seeing the slide. Assert that the rendered-image count and temporary inventory row count both equal the source count.
2. **Go slide-by-slide, in deck order**, and give **each** slide a verdict: mapped to a note heading, a genuine gap (fix it now), or logistics → master (see step 5). The full slide → home table is the audit deliverable; an inventory alone or a summary sentence is not a substitute.
3. **Apply all three coverage levels — a slide passes only if it clears every one:**
   - **Presence** — the slide's content is in the note at all.
   - **Findability + title** — it sits under a heading a reviewer can point to by name; for a slide that is its own distinct topic, **mirror the slide's own title verbatim** as the (sub)section heading. Content buried in another section's prose or under a bold lead-in is a **gap**, not a pass — fix placement and title.
   - **Fidelity** — every **named item, number, label, and worked-example value** on the slide is present and matches (algorithm names like WordPiece, framework/model names, stats, example figures). "The topic is covered" is not enough if a named item on the slide is missing or altered. Facts are carried verbatim; prose is rewritten fresh.
4. **Check every named entity explicitly.** Walk the slide's algorithms, frameworks, models, protocols, tools, stats, and worked-example numbers as a literal list — each is present, or a deliberate omission you can justify (recap/agenda/summary slides carry nothing new).
5. **Logistics slides go to the master, not the note** (evaluation scheme, course architecture, learning outcomes, textbooks, prerequisites, references) — their absence from the note is correct. Cross-check them against the master, but **never copy a deck logistics slide over the master**: when a deck slide and the confirmed handout/recording disagree, the handout/recording wins (a deck slide can be wrong — e.g. a quiz count). Flag the discrepancy; do not "fix" the master to match the deck.
6. **Deliverable:** the complete slide → home table with exactly one row for every source slide, every gap fixed in the same pass, and a short list of deliberate omissions with reasons. "Matches the index" is never the finish line — only "every slide has a verdict against the rendered source" is.

**This protocol is also the definition of done for *writing* a note from a deck, not only for re-auditing one.** Every gap a later audit finds — a dropped table column, an algorithm named on a slide but absent from the note, a buried subsection, a changed number — exists because the first write skipped a step above. Run all six steps on the first write and there is nothing left for an audit to catch. A note is not "written"; it is written *and* reconciled slide-by-slide against the rendered deck.

**You are the QA — the user is not.** Never report a note or audit as complete on the strength of extracted text, "the topic is present", or a prior pass. It is complete only when you have (a) rendered and actually looked at every slide, (b) produced the slide → home verdict table with a line for every slide, and (c) walked each slide's named items — every table column, algorithm, model, framework, statistic, and worked-example value — as a literal checklist. If you cannot show that table, the audit is not done. Do not make the user find the gap; finding it is your job, and the table is how you prove you did it.

### Independent Final-Gate Rule: Coverage Is Not Correctness

A passing `check-slide-coverage.mjs` result is only one gate. Before claiming a deck-backed note is fully checked, run and keep separate evidence for all of these:

1. **Source identity/count:** independently verify the PPTX/PDF page count and assert that the temporary inventory, rendered-image set, and slide → home verdict table have exactly the same row/count coverage.
2. **Findability:** map every distinctly titled substantive slide to a deliberate note heading or an explicitly justified master-index destination. Content buried under a neighbouring heading is not a pass.
3. **Fact fidelity:** compare every formula, operator, unit, label, named item, table value, and worked-example number against the rendered source; execute arithmetic examples rather than trusting transcription.
4. **Visual fidelity:** create a source-first visual inventory and map every substantive figure, chart, diagram, table image, and image-backed placeholder to a native asset, faithful crop, searchable transcription, or justified omission. A note-side `0 missing / 0 orphan` result is only internal reference integrity.
5. **Post-edit recheck:** after any heading, formula, number, or asset change, rerun the relevant coverage and reference checks and inspect every changed visual at native resolution and expected note display width.

The final response must distinguish these results explicitly: **rendered**, **textually covered**, **factually checked**, and **visually reconciled**. Never collapse them into “fully reviewed” when one gate was skipped, unavailable, or represented only by a keyword/asset-reference check. If an applicable gate cannot run, report it as an open gap instead of converting a partial pass into a completion claim.

Auto-transcripts are noisy. Correct obvious terms silently, such as `RoPE`, `SwiGLU`, `GQA`, and `KV-cache`.

## 5. Session Note Contract

### Master Index Carries a "Modules at a glance" Table

Every `<code>-master.md` gets a `## Modules at a glance` table, placed right before `## Session index`. Source it from the handout's own Part A module structure (its "Modules:" list, or numbered/`M`-prefixed module headers) — do not invent a grouping; use the handout's.

Columns: `Module | Theme | Sessions` (or `Module | Sessions | Hours` when the handout's modules already carry hour counts and map close to 1:1 with sessions, as in 536 — hour weighting is the useful signal there, not a theme grouping).

If a session's topic straddles two modules, or a module gets revisited by a later session out of its original block (as 549's Cloud Native module is extended by S12), say so in a one-line note under the table rather than silently picking one side.

This table is separate from and does not replace the full `## Session index` table — it's the one-glance shape of the course; the session index is the operational detail.

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
4. Body: `## <part title>` (topic-only major grouping) then `### <Concept>` sections
5. `## Self-study / Lab / build`
6. Exam footer linking to the master index

**Headings carry no numbers.** Part and section headings are topic-only — `## Chatbots to Agentic Systems`, `### The six components`, not `## Part 1 · …` or `### 4. …`. Numbered headings read as a rigid list and force every cross-reference to track a number; topic names read as an organised outline and never go stale.

**Cross-reference by name, never by number, and never point forward to future course sessions.** Within a note, refer to another section by its name ("see *Production concerns*", "expanded under *The six components*"), never "section 11". Do **not** add pointers to material taught in later sessions of the course ("session 11", "L7–L8", "Module 2", "full treatment in L4") — at this session the reader hasn't met them, so they are noise; teach the point here and let later sessions stand on their own. The only allowed session references are the exam-scope footer (which states which sessions the exam covers) and a self-reference to the current session.

Do not add a hand-written `## Topics` index. The headings already form the navigable outline and cannot drift.

Course logistics, admin, deck-errata, source notes, and build logs do not belong in session notes unless they materially change scope or interpretation.

The `## Why this matters` section must answer three things clearly: what this session teaches, why it matters in practice, and what the reader should be able to explain after reading it.

### Teaching Flow First

Write session notes as one coherent learning path, not as a stitched summary of separate sources. The reader should be able to move through the note without needing to reconstruct the logic from deck order, textbook order, or paper order.

You may reorder material within the handout scope when that makes the concept easier to learn, but do not rename, drop, or silently merge handout topics. Add short bridge sentences and checkpoints where needed so each part feels connected to the next.

### Every Concept Must Teach

Each concept must include, in this order:

```text
Intuition -> Mechanism -> Worked example -> Tradeoff / when NOT to use
```

The four **text** blocks are the **default order** — follow it unless the content genuinely reads better otherwise, and then only for a teaching reason: a *motivation* example may precede the Mechanism (cost economics before the algorithm); a Worked example may follow the Tradeoff when it *demonstrates* the tradeoff's advice (state the responses, then show them applied). Deviate for flow, never at random.

**Placement of diagrams and depth blocks is content-driven, not a fixed slot.** Every concept has **at least one diagram**; put it where it best illustrates — after the Intuition as a visual overview, or after the Mechanism when it depicts the parts that block just introduced. A depth block (`In practice` / `Going deeper`) sits next to what it illustrates — usually at the section's end, but beside the Mechanism when that's what it deepens (e.g. a self-attention example belongs next to the attention mechanism, not exiled to the bottom).

**Consistency is about structure, not cosmetics.** The standard *is*: every concept has the four blocks, a real intuition, a labelled worked example, a clear diagram, and a non-blank tradeoff. Do **not** reorder a section's blocks or relocate its diagrams/depth blocks just to make sections look identical on a fast scroll — a section's teaching flow always wins over visual uniformity. Rigid uniformity that makes a section read worse is a regression, not a cleanup.

Rules:

- The **Intuition** is a real intuition — a concrete mental model of what the concept *is* and why it works, in the reader's own terms: a reframe, an analogy, or a walk-through they can picture and hold ("a reasoning system that happens to speak your language"; "protocols are the USB-C moment"; "picture one request handled end to end"). It is **not** any of these four failure modes:
  - **(a) meta-commentary** about importance or exam-relevance — "the spine of the course, learn this cold, likely on the mid-sem";
  - **(b) a bare definition** — "the maximum tokens a model can hold";
  - **(c) a list of terms with no mapping** to what each one is or does — "the six jobs: understand, track, look up, act, respond, remember" (say which component each *is*);
  - **(d) a section-agenda or summary** — "Four axes.", "the argument, stated as a contrast:".

  Lead with the mental model; a definition, a mapping, or a "this matters / likely on the exam" note may *follow* it but must never *be* it. Test: if the Intuition were the only thing a reader saw, would they come away understanding *what the thing is and why* — not just that it exists, or that it's important?
- Tradeoff is never blank and never "depends on the use case." Name the specific case where the simpler option wins.
- Worked examples must be reproducible by hand or in <=30 lines of code.
- Verify arithmetic by running it before writing it.
- The required blocks stay **identifiable** even when a heading mirrors a slide title. If the worked example lives under a descriptive/slide-titled subsection (e.g. `#### Use Case: …`), keep a `**Worked example**` label on it so the block is still recognisable as the required one — a compliance scan (and a reader) must be able to point to each of the four blocks by name. Mirroring the slide title and labelling the block are not in conflict; do both.
- Landscape topics get comparison tables.
- Hard concepts need a plain-language on-ramp and a short everyday analogy.
- Dense math must be signposted as skimmable on first pass, with the key takeaway stated plainly.
- More explanation belongs at hard spots, not everywhere.
- Lead with the answer or concept name first; do not bury the key definition in the second half of a subsection.

### Learner-first topic-opening gate

For every substantive concept, the opening must help a new learner answer these questions before or while entering the source mechanism:

1. **What is it?** Give a plain-language definition or mental model.
2. **Why is it needed?** State what a general, naive, or simpler approach may fail to do.
3. **What changes in practice?** Give a concrete before/after contrast, preferably in the subject's domain.
4. **How does the source implement it?** Then introduce the source's routes, stages, mechanisms, examples, or figures.
5. **What is the tradeoff?** State when the approach is costly, risky, or unnecessary.

A generic agenda sentence, a list of routes, or a bare definition does not satisfy this gate. When the learner supplies a clearer explanation, treat it as the preferred pedagogical structure and merge it into the note, correcting only unsupported technical claims. This gate is separate from source coverage: a note can contain every source fact and still fail if the learner cannot tell what the topic means, why it matters, and what changes after applying it. Skip the full pattern only for genuinely notational, purely definitional, or comparison-only sections.

### Use Case Grounding

Every concept needs one grounding example that states a real problem and how the concept resolves it, not mechanism in the abstract alone. Check for this in the same pass as the Tradeoff.

- Prefer a real-world/production scenario tied to the subject's domain (fraud detection, a bank's compliance corpus, a support-ticket pipeline, a Kubernetes flash-sale autoscale, a misrouted chatbot intent) over an invented toy sentence.
- A short toy example (e.g. "Alice called Bob" vs "Bob called Alice" to isolate word order) is acceptable only when it is the clearest way to isolate the mechanism, not as a default.
- Format: `**Use case — <short label>.**`, 3-5 lines, in the note's existing voice. Fold into the Worked example or Tradeoff subsection if that reads more naturally than a standalone block.
- Skip sections that are purely definitional, notational, or a taxonomy/comparison table. Do not force a scenario onto a shape table or a vocabulary list.
- If a Worked example, `***In practice***` box, or Tradeoff paragraph already answers "what breaks without this and how is it fixed," that already satisfies the gate. Do not add a second example on top of it.

### Algorithm Motivation

Decks and textbooks usually teach how a named algorithm or technique works (the steps, the formula) and skip why it exists — what breaks with the naive/simpler alternative, and what problem this specific design fixes. For every named algorithm or technique a section teaches, answer three things in plain language, not just describe the mechanism:

- The problem: what goes wrong with the obvious naive/simpler approach.
- The fix: how this specific algorithm solves that problem.
- One everyday, non-technical analogy or example — something a person with no ML/CS/software background could follow. Not a comparison to another technical alternative; a real-world picture (a kitchen, a filing cabinet, a librarian, a weather forecaster — whatever fits).

Write the analogy yourself when the source material doesn't supply one; fold it in seamlessly, right after the technical explanation, in the note's existing voice. Do not mark it as filled-in or add a "not in the source" caveat — this is a normal part of teaching, not an exception.

Skip this for sections that don't name a specific algorithm or technique (pure landscape/comparison tables, notation, taxonomy). Check the existing Tradeoff and Worked example first — if one of them already states the problem, the fix, and gives a concrete picture, the gate is already satisfied; only the analogy may still be missing.

### Wording Pass

Before marking a note reviewed, read it end to end for:

- Ambiguous sentences that need a re-read to parse
- Jargon used before it is defined
- The same concept named two different ways in different sections of the same note
- Decorative or vague metaphors that do not actually clarify anything (the canonical bad example: "predicting text and generating text are the same machine, run in two directions") — cut them or replace with a direct statement of what is actually happening
- Compressed, mechanical phrasing that sounds like a lecture dump rather than a human teacher
- **Over-cooking — the same point taught more than once.** One concept gets **one** analogy: if it already has a working analogy or a clear plain-English explanation, a second one is padding, not clarity. Never keep the same structure as both an ASCII sketch **and** an SVG (or two SVGs) — pick the clearer one and delete the other. Do not follow a table or worked example with a paragraph that re-explains what it already showed.
- **Meta-asides and exhortations.** Cut "worth stating in an exam answer", "the most X in this table", "if you learn one thing, learn Y", and similar commentary — state the substance and let it stand. Say a thing once; repeating it for emphasis reads as filler.

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
- "the deck's own", "the deck marks", "the deck's structure" — any phrase that names the deck/slide/handout as the reason something is organized a certain way. State the content directly instead of narrating where it came from.

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

**Keep cross-references clear and factual — never vague or editorial.** A pointer says plainly *what* is in the target section and *why* it's relevant here: "section 5 lists the frameworks" is fine; "section 5 lists twelve of them approvingly" is not — it's awkward, and readers can't tell what "approvingly" is doing. **Any count or fact inside a cross-reference ("twelve frameworks", "three types", "the six components") must match what the target section actually contains** — a stale count is a factual error. Re-verify the number against the target whenever either section changes; if you don't want to maintain a count, don't state one ("the frameworks in section 5", not "the twelve frameworks").

**Never choreograph the reader's order.** A section must read naturally on its own — do not instruct the reader *when* or *how* to read it relative to another section. Ban phrasings like "read this caution *before* section 5", "read this table as an at-a-glance and section 4 as the detailed version", or "section 4 is the full picture, treat this as the preview." These read as confusing meta-navigation. State the point directly, and if another section genuinely extends it, use only a plain pointer — "expanded in section 4" — never a reading instruction. Test: if a sentence is telling the reader how to sequence their reading rather than teaching the topic, cut it.

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

### Analogy Parity

If a section's prose carries an everyday analogy (per Algorithm Motivation), the diagram teaching that same concept must carry a short version of it too — a caption line or an in-box label, not just a mention in the surrounding text. Check this in the same pass as Visual QA, not as a separate step: a diagram audit that only checks rendering (cut-off text, overlapping arrows) and never checks content parity against its own paragraph will miss this every time.

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

**Chat replies are short by default.** The note/deliverable is where detail belongs; the chat reply is a receipt, not a report. State what changed, the verification result, and any blocker — a few lines, not a recap of every edit. Do not re-explain the diff, restate the whole file, or list every heading; the user can read the file. Expand only when the user asks for detail. This applies to every prompt.

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

- [ ] Temporary slide inventory/verdict table was complete, matched the source slide count, and `check-slide-coverage.mjs` was run clean; delete it after verification unless a permanent index is justified
- [ ] Handout row checked directly from `.docx`/`.pdf`
- [ ] Every handout topic and sub-topic explicitly covered in the same note
- [ ] Handout-cited sources read/extracted or gaps recorded
- [ ] Deck/session identity verified from slide contents, not filename alone
- [ ] Mixed decks split by handout scope and logged
- [ ] Deck agenda items covered or genuine gaps recorded
- [ ] Every distinct deck title has a deliberate, findable note heading or a documented master-index destination; no buried titled-slide content
- [ ] Formulas, operators, units, labels, and worked-example numbers were compared with the rendered source and arithmetic was executed
- [ ] Deck visuals that carry explanation were preserved with equivalent note visuals, tables, or stepwise teaching flow
- [ ] Every concept has Intuition, Mechanism, Worked example, Tradeoff, and Diagram
- [ ] Arithmetic in worked examples was executed
- [ ] Note is self-contained; no core knowledge lives only in `_shared/`, labs, transcripts, or local sources
- [ ] No source references or source-framing prose in session notes
- [ ] No cross-subject links in session notes
- [ ] Diagrams parse, are linked, are visually QA'd, and have no unused SVG duplicates
- [ ] Source-figure media audit run directly against the pptx (`a:blip`/PICTURE-shape inspection per the PowerPoint media audit rule, not a visual skim) for every deck this note draws on — every genuine content image found is preserved as PNG, used as a clearly labelled recreation, or explicitly recorded as omitted with a reason. Authoring an SVG for a concept does not satisfy this — it is a separate check against the deck's own media, done even when the note's diagrams already look complete.
- [ ] Source visual inventory and note asset map were reconciled in both directions; zero missing/orphan note assets alone was not treated as source-figure completeness
- [ ] Master index, `PROGRESS.md`, `MATERIALS-WATCHLIST.md`, and `source/MATERIAL-LOG.md` updated where needed
- [ ] Condensed page, if present, was derived from the full note
- [ ] No PDFs, slides, datasets, transcripts, weights, or secrets are staged
- [ ] Dates and weights match handouts or are marked `⚠️`

**Green is necessary, not sufficient.** A clean `npm run check` and a clean `check-slide-coverage.mjs` run do not by themselves make a note complete or a compliance line honest — the coverage tool only knows the named items in the temporary inventory, and `check:framing` matches a narrow regex. Before claiming done, do a by-eye pass for what the scripts miss:

- **Source-framing the regex misses.** Phrases that name the source as the reason for content — "the deck cites/notes/shows/marks/quotes", "the slide's", "the handout says" — are violations even when `check:framing` passes. State the content directly.
- **Internal-number consistency.** Every figure repeated in a `## Why this matters`, self-study, summary, or open-book line must match the note's own worked example (e.g. a fusion score quoted in the lab equals the score computed in the RRF section).
- **Split-induced duplication.** After moving or splitting sections, re-read the seams: a concept must not be taught twice across two notes or in adjacent sections.

Do not write "no open gaps" on the strength of green checks alone.

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
    │       └── MATERIAL-LOG.md
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
