# AGENTS.md — working rules for this repo

Rules for any AI agent working in `MTech`. Read before producing anything. **Rules are hard unless marked "prefer".**

## 1 · What this repo is

Study notes for an MTech at BITS Pilani WILP. One folder per semester.

**Purpose: a durable career knowledge base.** These notes are the long-term reference the user carries into their work. Exams (closed-book mid-sem, open-book comprehensive) are a real but *secondary* constraint — **the knowledge body itself is what you revise from.** There are no separate recall cards. Course logistics live **once** in the subject master index, never in a session note.

**Current semester:** Aug–Dec 2026. Folder name = course code + course title from the handout:

| Folder | Code | Course title |
|---|---|---|
| `AIMLZG536-LLMForGenerativeAI` | AIML ZG536 | Large Language Models for Generative AI |
| `AIMLZG546-SoftwareEngineeringForML` | AIML ZG546 | Software Engineering for Machine Learning |
| `AIMLCZG549-APIDrivenCloudNativeSolutions` | AIMLC ZG549 | API-driven Cloud Native Solutions |
| `AIMLCZG521-ConversationalAI` | AIMLC ZG521 | Conversational AI |

⚠️ **536/546 are `AIML`; 549/521 are `AIMLC`.** Take it from the handout.

Read `2026-2027-Sem1/STUDY-PLAN.md` before planning work.

## 2 · Hard rules

1. **Never commit course material** — no `.pdf`, `.ppt(x)`, `.doc(x)`, datasets, weights. `.gitignore` enforces it; do not weaken it.
2. **Textbooks live in `/_library/`** (gitignored, 9 books). **Look there before asking the user for a book.**
3. **Never commit secrets.** Placeholders only (`OPENAI_API_KEY`).
4. **Never invent syllabus content.** Topics, dates, weights, references come from handouts. Unknown → `⚠️ unconfirmed`, never a guess.
5. **Never reproduce textbook text.** Explain fresh, in your own words — and **don't cite the source in the note** (no `T1`/`R2`/`ch3`, no "the deck"). The note carries knowledge, not references.
6. **One file per session**, `<subject>/notes/S<NN>-<slug>.md` — **`S` prefix in every subject**, including 521 (whose handout says `L1…L16`; use `L3` in prose, `S03-` in the filename). Creating a note updates its row in `<code>-master.md` **and** `PROGRESS.md` in the same change.
7. **Lab code lives in `<subject>/labs/S<NN>-<slug>/`**, never in `notes/`.
8. **Transcripts are never committed.** Read → fold into the note → done. `source/transcripts/` is gitignored.
9. **Notes must remain portable across machines.** A session note must still be complete and understandable if `/_library/`, `/_shared/`, transcripts, local PDFs, or other gitignored resources are absent on another machine or under another model. Use those resources to build the note, but never make the note depend on them to carry core knowledge.
10. **Every session-note touch includes a self-containment review.** Whenever you create, expand, or revise a session note, re-check that the session note itself still carries the full explanation needed for study. If a textbook chapter, transcript, handout bullet, paper, lab, or `_shared/` note contains a clearer explanation, extra mechanism, better example, or missing sub-topic, fold that value back into the session note instead of leaving it only in the auxiliary material.

## 3 · The handout is the contract

Every handout's **Part B: Learning Plan** table governs the course:

| Column | Means |
|---|---|
| **Contact Session** | Session number; some rows cover two |
| **List of Topic Title** | The note's title |
| **Sub-Topics** | The note's sections — **and the definition of examinable scope** |
| **Reference** | Where the instructor built the slides from |

**Verify coverage against the handout verbatim, not against a summary of it.** Read the `.docx`/`.pdf` itself (`python-docx`, `pdfplumber`) and check every bullet. A master-index row is a derived summary and can silently drop a sub-topic — 549's "Mocking" survived three reviews that way, because the word appeared in the note only inside *To Kill a Mockingbird*. A handout bullet counts as covered only when the note contains a **clear, dedicated explanation of that exact topic** that a reviewer can point to by section heading or clearly bounded subsection — not a passing mention, not a keyword hit, and not an example that happens to use the same word.

**Also check the deck's own agenda slide.** It is the instructor's contract for that session and can differ from the handout in both directions — 546's agenda promised four blocks and the deck delivered three, ending before "Types of ML Domains". An agenda item counts as covered only when the note teaches it as a section or clearly identifiable subsection that a reviewer can point to immediately; do not mark it covered because nearby material is "close enough."

### What the Reference column tells you to do

| Reference says | Do |
|---|---|
| A textbook chapter | **Check `/_library/` first.** Extract the cited chapter only |
| A paper or public spec | **Fetch it yourself** — these are public. Don't make the user upload them |
| "Web Resources" / "Lecture Notes" / blank | **Nothing exists behind the slides.** Treat the deck, and the recording if available, as the only teaching sources while building the note; do not invent a hidden textbook layer |

### Uncited chapters are out of scope

**A chapter the handout does not cite is not part of this semester.** Never pull content from one into a note; never recommend reading one; mark them `OUT OF SCOPE` in chapter maps. Relevance is the instructor's call, already made in the Reference column. Only exceptions: the user asks directly, or it's needed for a lab the handout prescribes — say plainly that it's outside the syllabus.

**Per-subject profile:**

- **549** — ⚠️ only S1–S3 have books. **S4–S16 are "Web Resources, Lecture Notes"** — 13 of 16 sessions have nothing behind the slides. Highest-value decks of the semester.
- **521** — no textbook at all; every reference is a public paper or spec → fetch, don't ask.
- **536** — T1/T2/R1 chapters + papers cover most sessions; S6, S15, S16 are papers/web only.
- **546** — T1/T2 chapters cover S1–S14; S15–S16 are lecture notes only.

## 4 · No deck, no note

**A session note is never written without that session's deck.** The deck is the only artifact stating what *this instructor* taught.

- **The handout is too coarse** — 521's L1 entry is two bullets; the real deck covered eight topics including a full BPE worked example.
- **The textbook is too broad** — the author's selection, order and depth, not the instructor's.
- **Neither shows emphasis** — only the deck reveals twelve slides on one topic and a single bullet on another.

**If the deck is missing:** say so, **do not write the note**, and do not offer a "provisional version" — it gets revised into rather than replaced, and its errors persist. You *may* fetch the session's public references and log them. Mark Slides `✗` in `source/MATERIAL-LOG.md`.

## 5 · Intake

The user uploads per session and says **subject, session number, file type**. If the session number is missing, infer from the master index and **state the inference**.

**Never trust a deck filename alone.** PPTs/slides are sometimes mixed across sessions, reused from older offerings, or bundled with extra material. Before using any deck, verify its session identity from the title slide, agenda slide, slide footers, section dividers, and topic sequence against the **handout Learning Plan row**. If slides from multiple sessions appear in one file, split the extraction **by handout session scope**: match slide topics to the handout's Contact Session, Topic Title, and Sub-Topics, then use only the matching slides for the current note. Record the mixed-deck fact and the session split in `source/MATERIAL-LOG.md`. If the handout-based boundary is ambiguous, stop and ask for the correct session mapping; do not blend two sessions into one note.

| Format | Extract with | Note |
|---|---|---|
| `.pptx` | `python-pptx` | **Always read speaker notes AND embedded images** (`shape.image.blob`) |
| `.pdf` (text) | `pdfplumber` | |
| `.pdf` (scanned) | OCR first | Say that it's happening |
| `.docx` | `python-docx` | |
| transcript `.txt/.srt/.vtt/.docx` | direct | Primary source for emphasis |
| **`.mp4` / video** | **impossible** | See below |

⚠️ **Video cannot be transcribed here.** `ffmpeg` exists but only PyPI is reachable — every model CDN returns 403, so no ASR model can be fetched. The user transcribes locally (MacWhisper, or `whisper <file> --model small --output_format txt`). **Never claim to have watched a recording.**

**Auto-transcripts are noisy** — `RoPE`→"rope", `SwiGLU`→"swiglue", `GQA`→"GQ A". Reconcile against the slides and silently use the correct term. Don't ask the user to clean them.

**Always extract and LOOK AT deck images.** Slide text routinely omits what the figure says: 536's transformer equations, embedding numbers and LM-head shapes existed *only* as images, and a first pass missed all of them. Reading the image count in a log is not the same as looking at the images.

## 6 · How notes are written

Follow `2026-2027-Sem1/_templates/SESSION-TEMPLATE.md`.

**A session file contains the subject's knowledge and nothing else.** No navigation aids, no admin, no logistics, no deck-errata to-dos. Test: *"is this knowledge, or is it about the note?"* If the latter, it doesn't belong.

**A session file must stand on its own on any machine.** Another copy of the repo may not have `/_library/`, transcripts, handouts, or local scratch material available. Therefore the note itself must contain the explanation, mechanism, examples, diagrams, and tradeoffs needed to study the topic without depending on a local-only file being present.

**The body must teach the topic before any optional follow-up.** A reader should be able to stop before `Self-study / Lab / build` and still have a complete study note for the session. Labs, notebooks, and optional exercises may reinforce the note; they must not carry missing core explanation.

### Structure

1. **Title** — `<Subject Name> · Session NN · <Topic>`, then one line: `*Learned <date>*`. Nothing else.
2. **Why this matters** — 2–4 sentences on the career payoff.
3. **Body** — `## Part N · <title>` with a one-line italic gloss beneath, then `### N. <Concept>`, then `#### N.M` sub-sections.
4. **Self-study / Lab / build.**
5. **Exam-scope footer** — one italic line + link to the master.

**No `## Topics` index.** The `## Part` / `### N.` headings already are the outline, and every viewer renders them as a navigable TOC that cannot drift. A hand-written index was built with one-line summaries and a Depth column, then removed: all 19 "mechanism" concepts turned out to be exactly the 19 carrying a Mechanism block and a worked example, so the column restated what the section already showed, and half the one-liners restated the concept's own `**Intuition**` line.

> **One fact, one place.** Before adding any summary, index or status column, ask whether the thing being summarised is already visible. A "where it's used later" column was also tried: it duplicated each concept's `Cross-link:` line and **disagreed with it within a day** — 4 of 23 rows, before the change was even committed.

### Every concept, in this order

**Intuition** → **Mechanism** → **Worked example** → **Tradeoff / when NOT to use**

Plus **at least one clear diagram** — Mermaid when Mermaid is genuinely readable, authored SVG when a slide/textbook/paper-style figure is clearer. All are mandatory; the checklist in §13 verifies them.

- **No source references.** A note states the knowledge directly — no `*Reference:*` line, no "the deck says…", no textbook codes (`T1`, `R2`, `ch3`) or textbook-author citations in the prose. The knowledge stands on its own. Where an origin *is* the knowledge (REST = Fielding 2000, GraphQL = Facebook 2015, BPE = Sennrich 2016), that's a fact worth keeping — a citation of *the textbook* is not.
- **No source-framing prose.** Do not write meta-phrases such as "in the instructor's own words", "spoken version first", "worth memorising verbatim", "quotable", "the deck copied", or "the source says". Convert them into direct knowledge statements. A note should read like the subject itself, not commentary about where the wording came from.
- **Source-availability facts belong outside the teaching flow unless they change the knowledge.** "No textbook exists for this session", "the deck omitted this topic", or "the lab notebook differs from the slide demo" may be recorded only when they materially affect scope, grading, or how the concept must be interpreted. Do not let routine note prose drift into build-log commentary.
- **No cross-subject links.** Each subject's notes are self-contained. Never link or point to another subject's session (`→ 546 S9`, "shared with 536", "you'll also see this in 521"). Same-*subject* navigation ("section 4", "S14") is fine. If a topic recurs in two subjects, each note covers it fully on its own — separateness over reuse.
- **No hidden dependence on local resources.** Do not write notes that require the reader to open `/_library/`, a transcript, a deck image folder, or an optional `_shared/` note to understand the core content. Those resources can inform the note; they are not part of the note's delivery contract.
- **Tradeoff is never blank** and never "depends on the use case." Name the specific situation where the simpler option wins.
- **The worked example must be reproducible by hand or in ≤30 lines.** A *described* example is not an example. For mechanism topics, show arithmetic on small numbers — and **verify the arithmetic by running it** before writing it down.
- **Landscape topics get a comparison table**, not prose.

**Depth blocks**, where a concept has real-world weight — blockquoted, italic-marked as beyond-course:

- ***In practice*** — the tools, auth/rate-limit/retry realities, conventions, what production adds.
- ***Going deeper*** — deeper mechanism or a useful adjacent concept the course skips.

### Organise by topic, never by source

**The most important rule here.** A note is one notebook on a topic, assembled from wherever facts came from — not a stack of source summaries.

- **Never** create "From the slides" / "From the textbook" sections.
- **One topic, one place.** Slide diagram + textbook mechanism + instructor's aside all live in that topic's section. If the handout names a topic separately, it still needs a clearly findable home in the note — ideally its own heading or a clearly named subsection, not a sentence buried inside another section.
- **No duplication.** If a concept spans two topics, write it in the more natural home and cross-reference.
- **No source overrides another** — they combine. Flag `⚠️` only on genuinely incompatible factual claims (a date, a weight, a definition).
- **Order for learning, not arrival.** Vocabulary before the concepts using it; motivation before mechanism.

### Layering sources

Material arrives over time. **Rewrite the note in place. Never create a second file; never append a new source as a new bottom section.**

| Source | Contributes | Wins on |
|---|---|---|
| **Slides** | Scope, in the instructor's words | **Scope and terminology** |
| **Textbook** | Mechanism, examples, edge cases | **Explanation** |
| **Transcript** | Emphasis, asides, exam hints | **Emphasis, and anything said but not written** |
| **You (the model)** | Clarity no source states | **Nothing on fact or scope** — always marked as yours |

⚠️ **The deck is not automatically more current than the handout.** Decks get rebuilt each offering and carry errors the handout doesn't. When they conflict on assessment, the handout wins unless the user says otherwise — this was learned by getting 521's quiz count wrong.

**Request chapters, not whole books.** A 500-page book covers all 16 sessions; processing it for one pulls in concepts not yet introduced and makes the note worse.

**Use local resources as inputs, not crutches.** `/_library/`, gitignored transcripts, copied handouts, and optional shared notes are working materials for the agent, not study dependencies for the reader. Anything needed to understand or revise the session later must be folded into the session note itself.

**Session notes outrank supporting notes.** If `_shared/` notes, labs, later uploads, or newly found references explain something better than the current session note does, the fix is to strengthen the session note. Never leave the best explanation only in `_shared/`, only in a lab README, or only in a local source file.

**Revise with the smallest effective change.** When improving an existing session note, prefer the smallest edit that fully fixes the problem: add the missing subsection, replace the weak example, clarify the ambiguous paragraph, or redraw the confusing diagram. Do not widen the blast radius unless the current structure itself is the problem.

### You are a source too — add your own clarity

The sources define **what** is examinable. They are often poor at making it **understood**. Closing that gap is expected on every session of every subject, not a special case.

**Add freely:** a clearer explanation where the source is compressed or circular · a better worked example with concrete numbers · **the tradeoff line**, which sources routinely omit · a connection the sources don't draw · **the trap** (BPE merge 2 looks obvious and isn't; embedding row 5 is the sixth row) · a diagram where there's only prose · career depth in ***In practice*** / ***Going deeper*** blocks.

**When the deck or handout names a topic but no source teaches it, write it yourself** and flag it inline as filled-in. Both cases so far — 549's mocking, 546's ML domains — were syllabus items with no slide behind them. A named topic with no content is a gap the user finds in the exam hall.

**Never add:** new topics *into the exam-scoped body* (beyond-course material goes in marked depth blocks) · replacement terminology in the body (a better word that appears in no exam paper scores nothing) · **silent invention** — if it isn't in a source, mark it as your reasoning · padding.

**Mark model-added clarification only when it affects exam interpretation**, and do it without source-framing prose. Use a short italic aside such as *"filled-in reasoning for this syllabus item"*. In a disagreement with an instructor, only the course's version scores.

**The test:** does this help the reader *reproduce the concept under exam pressure* or *use it competently on the job*? If neither, cut it.

### Write for the average student — the comprehension bar

**Every note must be followable by an average student** — a working professional with a CS background but rusty maths — not only by someone who already knows the topic. Clearing that bar is a hard requirement, not a nice-to-have. Correct-but-impenetrable is a fail.

- **Plain-language on-ramp before any dense mechanism.** One sentence saying what a symbol or step *does* in words, before the formula does it in symbols — *"softmax turns a list of scores into probabilities that add to 1."* The formula still follows; it's just no longer the reader's first contact with the idea.
- **One concrete everyday analogy per hard concept.** Q/K/V as a group chat, idempotency as an elevator button, an API contract as a restaurant menu, workflow-vs-agent as recipe-vs-chef. Keep it short — the analogy is scaffolding, the mechanism still carries the weight.
- **Signpost heavy arithmetic as skimmable on a first pass**, and state the one sentence to walk away with, so cognitive load never blocks the idea. A worked example the reader skips in fear teaches nothing.
- **More explanation belongs at the hard spots, not everywhere.** Padding an already-clear section raises load and works against comprehension — the enemy is confusion *and* volume. Add the on-ramp where a reader stalls; leave the easy sections tight.
- **Every handout topic and sub-topic must be explicitly covered in the note.** Do not treat a syllabus item as "covered" because it is only implied, briefly named, partially folded into another section, or matched by keyword search alone. On review, check each handout bullet against the note and record the exact heading or subsection where it is taught. If you cannot point to one immediately, treat the topic as missing and add the explanation, worked example, diagram, or decision rule until it is **clearly present, easy to find, and learnable on its own**.
- **Review notes as growing artifacts, not one-shot writes.** A session note may start from slides and later gain clarity from transcripts, papers, labs, and comparisons with other sessions. On every later pass, actively look for what is still weak, compressed, missing, stale, or harder to understand than it needs to be, and strengthen the note in place.
- **Once a note is study-stable, later edits must be minimal and structure-preserving.** Improve old notes when they are incomplete, unclear, stale, or weaker than later supporting material — but do not keep re-authoring them. After the main consolidation pass, prefer small targeted fixes (missing topic, clearer example, corrected fact, better diagram, tighter wording) over moving sections around or rewriting the whole teaching flow.
- **Do not create “half in one place, half elsewhere” notes.** If a concept starts in the session note, finish teaching it there. Do not leave the intuition in the session note and the mechanism in a lab, or the overview in the session note and the worked example only in `_shared`.

**The comprehension test:** could an average student, reading this section cold, follow it without reaching for a second source? If not, add the on-ramp or the analogy — don't just restate the formula louder.

## 7 · Diagrams

**Every concept in every note — session notes and `_shared/` notes alike — has at least one clear diagram, with SVG first and Mermaid only as fallback.** First reuse an existing suitable SVG in `notes/assets/`; if none exists, create a clean authored SVG under `<subject>/notes/assets/S<NN>-<figure-slug>.svg` and embed it in the note. Use Mermaid only when an SVG is unavailable, unnecessary for the teaching shape, or when a small abstract flow is clearer as Mermaid. Do not keep a Mermaid diagram beside an SVG if both teach the same picture; the SVG replaces the Mermaid unless the Mermaid adds a genuinely different abstraction.

Sources, in order of preference:

1. **Convert the deck's own figure** — extract the images and look at them.
2. **Check cited textbook chapters** for a clearer figure, even when the deck figure is weak or missing. Track the source in working notes or `source/MATERIAL-LOG.md`, not as a citation inside the session note.
3. **Check cited papers/public specs** for canonical diagrams when the handout or deck names the paper/spec, or when the user explicitly asks for a paper-level visual pass. Use the paper only to strengthen an already-scoped topic unless the user explicitly broadens scope.
4. **Draw your own**, marked `(my own)`. A comparison table often hides a structure worth drawing; the point is usually the *relationship*, not the cells.

**Carry labels across verbatim** — the exam uses the instructor's words. **Don't invent structure the image lacks**; if an arrow is ambiguous, say so in prose. The Mermaid block or authored SVG is the permanent record — never write "see the diagram on slide 16."

**Match the source figure's teaching shape when possible.** Mermaid diagrams should resemble the slide/textbook diagram in **structure and learning intent**: same main boxes, same grouping, same flow direction when it is readable, same contrast, and same important arrows. They do **not** need to be pixel-perfect, decorative, or visually identical. If the source figure is crowded, has crossing arrows, or cannot be represented cleanly in Mermaid, simplify the layout while preserving the information and state any lost visual nuance in prose.

**Use authored SVG recreations as the normal target, not a special exception.** For any important figure from a **slide, textbook chapter, paper, public spec, or research diagram** where the learner benefits from visual teaching shape — boxes, miniature bars, grouped panels, captions, visual hierarchy, or print-safe layout — create or reuse a clean SVG under `<subject>/notes/assets/S<NN>-<figure-slug>.svg` and embed it in the session note. Do **not** commit the original slide screenshot, extracted deck image, textbook image, or paper figure. The SVG must be self-contained, readable at note width, and clear at the bottom/caption area. Keep a Mermaid fallback only when no suitable SVG exists yet or when Mermaid teaches a different abstraction such as a tiny tensor-shape flow; remove it when it duplicates the SVG. Apply this rule consistently across **all session notes**, not only 536.

**An SVG file is not done until the note uses it.** After creating or finding an SVG, immediately replace the matching Mermaid block or placeholder in the session note with `![clear alt text](assets/S<NN>-<figure-slug>.svg)`. Then verify three things before saying complete: the note has the SVG link, the linked SVG file exists, and no duplicate Mermaid diagram remains for the same concept. Unused SVG files in `notes/assets/` are unfinished work, not completed diagram work.

**Visual QA is mandatory, not user-policed.** After creating or editing Mermaid/SVG diagrams, review every touched diagram as an examiner-reader: labels correct, source figure's main shape preserved, arrows present, arrowheads visible, no crossing/overlapping arrows where avoidable, no cramped bottom/caption area, no tiny unreadable text, no decorative clutter, and no misleading simplification. **A diagram that merely parses, links, or renders is not done.** It must also be clear, readable, and textbook/slide-like enough to teach the concept at note width. If it is technically valid but visually weak, floating, crowded, cut off, arrow-ambiguous, or harder to learn from than the prose, fix it before saying the task is complete. If the user flags one example of a recurring class of issue — missing arrows, crossed arrows, bad bottom text, duplicate Mermaid/SVG, unclear copied slide figure — audit the whole touched note for that class before finishing. Do not fix only the one named by the user. When tooling allows, render the SVG/diagram and inspect the image, not only the XML/text. If rendering is unavailable, keep the diagram simpler and state that only syntax/link validation was possible.

**Prefer clean diagrams over exhaustive ones.** A Mermaid block should expose the structure at a glance, not reproduce every sentence from the source. Fewer boxes, shorter labels, and a clear stage flow beat dense diagrams with crossing lines. If `timeline` or `sequenceDiagram` becomes cluttered or tool-fragile, rewrite it as a clean `flowchart TD` instead.
**Do not leave overlapping or crossing arrows when a clearer layout is possible.** If arrows overlap, reverse the flow direction (`LR` ↔ `TD`), stack the stages vertically, split one busy node into two simpler nodes, or replace a loop-back arrow with a "next state" box. The reader should be able to trace every path without visual ambiguity.

### Direction is a decision, not a default

`LR` is **not** the default.

| Use | When |
|---|---|
| **`flowchart TD`** | 6+ boxes · **anything that branches or converges** · labels over ~25 chars |
| **`flowchart LR`** | ≤5 boxes, short labels, strictly linear |
| **`flowchart BT`** | Something is *built up* from parts |
| **`timeline`** | Eras or dated evolution |
| **`sequenceDiagram`** | A protocol handshake with named participants |
| **A Markdown table** | Comparisons, and Venn diagrams (Mermaid has no Venn — name each intersection) |

A wide `LR` diagram scrolls sideways on screen and is **cut off** on the printed open-book file. 15 diagrams here were written `LR` and had to be flipped.

**For an X-vs-Y section, draw ONE diagram with two `subgraph`s, not two diagrams.** The contrast *is* the content, and two stacked diagrams make the reader hold one in memory while scrolling to the other. Inside a `subgraph`, `direction TB` overrides the parent.

⚠️ **Label gotchas:** quote any label containing `(` `)` `:` `,` `#` · `end` is a reserved word and cannot be a node id · `<br/>` works inside quoted labels, but `<b>`/`<i>` don't render everywhere — prefer plain text.

**Validate before committing** — a diagram that fails to parse renders as a wall of raw text, and nothing in a Markdown preview warns you:

```bash
cd tools && npm run check
```

## 8 · The condensed open-book page

The comprehensives are open book, and BITS bans loose sheets — everything must be **printed and bound by 22 Nov**. The notes cannot be that file: four subjects × 16 sessions ≈ **1,500 pages**, which no one navigates in 60 seconds under exam pressure.

So each session has **two artifacts, in a strict order**:

| Artifact | Purpose | When |
|---|---|---|
| `notes/S<NN>-….md` | The knowledge. Full length. **Never printed.** Revised from for the closed-book mid-sem | Same weekend as the class |
| `openbook/S<NN>-….md` | **Two pages.** Lookup only, for the bound December file | Derived later — deferrable |

**The condensed page is derived, never authored.** It is a mechanical squeeze of a note that already exists. If you find yourself working out new understanding while writing one, stop — that belongs in the note.

Follow `_templates/OPENBOOK-TEMPLATE.md`. **Hard limit: two sides of A4.**

| Goes on the page | Stays in the note |
|---|---|
| Every formula, with symbols named | The Intuition prose |
| Every comparison table | The full worked-example walkthrough |
| **Every tradeoff line** — marks concentrate here | ***In practice*** / ***Going deeper*** blocks |
| The diagrams — fastest thing to find on a page | Longer explanatory prose and optional cross-links |
| Worked-example *answers* | The reasoning that produced them |

**If it doesn't fit in two pages, cut prose.** Never cut a formula, a comparison table or a tradeoff line.

**Bound file target: ~130 pages required, ~180 with optional extras.** Required core: master index (4) + 64 condensed session pages (~130). The 10 condensed `_shared/` pages (~40) are **optional synthesis** — print them only if they earn their space in revision; a subject's own condensed pages must stand alone without them (§9). Subject pages are the primary path; `_shared/` is secondary.

⚠️ **Order matters.** A note without its condensed page is recoverable in an afternoon in November. A condensed page written *before* the note is a summary of nothing, and the understanding it was supposed to compress never gets built. **Never write the condensed page first**, and when behind, always drop the condensed page rather than the note.

## 9 · Subjects are self-contained — no sharing, no cross-links

Some topics appear in two to four subjects (RAG, tokenization, agents, …). **Each subject covers its own topics fully, in its own notes.** When a topic recurs in another subject, **write it again there** from that subject's angle — do not point to another subject's note, and do not factor it into a shared file that both link to. Separateness beats reuse: a reader in one subject should never need another subject's notes.

- **No `_shared/` cross-links from session notes**, and no "→ 546 S9 / shared with 536" pointers anywhere.
- Same-*subject* navigation ("section 4", "see S14") is fine.
- The small duplication of re-explaining a shared topic per subject is the intended cost — it keeps each subject a clean, standalone reference on any machine, even when `_shared/` notes are missing or intentionally not printed.
- **A session note may duplicate `_shared`; it must never depend on `_shared`.** If a shared note explains something better, more clearly, or more completely than a session note does, strengthen the session note. Never leave the better explanation only in `_shared`.

## 10 · Tone

- Plain language; define jargon on first use or don't use it.
- No filler, no motivational framing, no restating the question.
- Prefer a table over a list, a list over a paragraph, and a worked example over all three.
- Flag uncertainty inline with `⚠️`. Never present a guess as a fact.
- **Own mistakes plainly and say what the wrong belief was**, so it isn't repeated. Don't bury a correction inside a summary of new work.

## 11 · Ask for what you need — insistently

The user has asked to be told **forcefully**. A gap mentioned softly at the end of a long response gets missed, and a missed deck costs marks months later.

- **ONE ask per response.** Rank everything outstanding; ask only the top item. Five asks get none done.
- **Its own heading, at the end**, so it survives skimming.
- **Name the artifact exactly** — "the 549 session 3 deck from Teams", not "the next materials".
- **State the consequence** — *"without this, session 3 cannot be written at all; 549 has no textbook from session 4 onward."*
- **Repeat unresolved asks next turn.** Silence is not completion; an ask outstanding three turns is *more* urgent.
- **Move on only when resolved** — done, refused, or shown impossible.
- **Distinguish blocking from optional.** Never flatten them together.
- **Flag deadline risk unprompted** when a `STUDY-PLAN.md` date nears with its `PROGRESS.md` milestone unticked.

## 12 · The materials watchlist

`2026-2027-Sem1/MATERIALS-WATCHLIST.md` tracks every outstanding deck, textbook and setup task **with the date it starts blocking work**.

- **Read it at the start of any session-note task**, and check the item you're about to need.
- **Raise its dated items unprompted**, in the response nearest the date — the user asked to be told forcefully, and a reminder that waits to be asked for is not a reminder.
- **Update it whenever material arrives or a need is discovered.** A gap found and not recorded will be re-discovered from scratch three weeks later.
- ⚠️ **Verify a delivered file is the cited work before filing it.** Titles collide: a 9-page vendor whitepaper called *Generative AI in Action* is not Bahree's Manning book of the same name. Check page count, publisher and table of contents, and say plainly when an upload doesn't match the reference.

## 13 · Before finishing any task

Run these, don't eyeball them:

```bash
cd tools && npm run check          # every diagram parses; no LR diagram too wide
git status --short                 # nothing binary or secret staged
```

- [ ] **Every handout topic and sub-topic explicitly covered** — checked against the handout file itself, not the master index; no implied coverage, no keyword-only matches
- [ ] Every deck agenda item explicitly covered, or the gap flagged inline in the note
- [ ] Deck/session identity verified from slide contents and the handout Learning Plan, not filename alone; mixed-session slide decks were split by handout scope or flagged before writing
- [ ] Every concept has: Intuition · Mechanism · Worked example · Tradeoff · diagram
- [ ] Important source figures checked across the deck, cited textbook chapters, and cited papers/public specs; useful ones recreated as clean Mermaid or authored SVG; original slide/textbook/paper images were not committed
- [ ] Touched diagrams were visually QA'd for readability, source-shape fit, correct labels, and clear bottom/caption spacing
- [ ] **An average student could follow every concept cold** — plain-language on-ramp before dense maths, one everyday analogy per hard concept, heavy arithmetic signposted as skimmable
- [ ] The **session note itself** contains the strongest available explanation — nothing important left only in `_shared/`, labs, transcripts, or local source material
- [ ] The **teaching flow is complete inside the note body** — no concept split across session note + lab/shared file in a way that forces the reader to jump out for core understanding
- [ ] No source references (no `*Reference:*`, `T1`/`R2`/`ch3`, "the deck") and no cross-subject links
- [ ] Any arithmetic in a worked example was actually executed
- [ ] Master index row + `PROGRESS.md` row updated
- [ ] `MATERIALS-WATCHLIST.md` updated if material arrived or a new gap appeared
- [ ] If a condensed open-book page exists, it was derived from the note — not written first
- [ ] `source/MATERIAL-LOG.md` records what arrived and what was missing
- [ ] No PDFs, slides, datasets or secrets staged
- [ ] Dates and weights match the handout, or are marked `⚠️`

⚠️ **Do not run `git commit` from the sandbox.** It creates `.git/*.lock` files it cannot then remove, and the next commit fails with a misleading "another git process is running". **Stage the work and give the user the commit command.**

## 14 · Repo layout

```
MTech/
├── AGENTS.md                    ← this file
├── .gitignore                   ← blocks course material; do not weaken
├── tools/                       ← check-mermaid.mjs + package.json (node_modules gitignored)
└── 2026-2027-Sem1/
    ├── STUDY-PLAN.md            ← phases, calendar, deadlines
    ├── PROGRESS.md              ← dashboard: 64 sessions × deck/note/open/lab
    ├── <CODE>-<CourseTitle>/
    │   ├── <code>-master.md     ← session index + ALL course logistics
    │   ├── notes/S01-….md       ← the knowledge, full length, never printed
    │   ├── openbook/S01-….md    ← 2-page lookup sheet, derived from the note
    │   ├── labs/S01-…/
    │   └── source/
    │       ├── README.md        ← links only
    │       ├── MATERIAL-LOG.md  ← what exists per session
    │       └── transcripts/     ← gitignored; read, fold in, discard
    ├── _shared/                 ← optional synthesis notes (secondary to subject notes) + README index
    ├── _library/                ← 9 textbooks, gitignored — CHECK HERE FIRST
    └── _templates/  SESSION-TEMPLATE.md · OPENBOOK-TEMPLATE.md
```

## 15 · Key dates (all four handouts, confirmed)

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

⚠️ **521 publishes no dates** — announced in class or on Canvas, **no makeups**. Treat any 521 date here as inferred until confirmed.

⚠️ **536 S8 and 521 S8 are revision sessions** — two of the four mid-sems cover **seven** sessions of new material, not eight.
