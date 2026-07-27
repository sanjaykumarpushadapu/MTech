# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

> 🔴 **Slides are mandatory.** No deck → **no note is written** for that session. The handout is too coarse to define scope and the textbook is too broad; only the deck shows what this instructor taught and what they emphasised. Collect the deck for every session the same weekend, without exception.

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `Session 1- Intro.pptx` (28 sl) | ✓ T1 ch1 + ch3 · R1 full | ✓ Teams | ✅ received & extracted into note (not stored) | ✅ `notes/S01-foundations.md` |
| 2 |  |  |  |  | ☐ |
| 3 |  |  |  |  | ☐ |
| 4 |  |  |  |  | ☐ |
| 5 |  |  |  |  | ☐ |
| 6 |  |  |  |  | ☐ |
| 7 |  |  |  |  | ☐ |
| 8 |  |  |  |  | ☐ |
| 9 |  |  |  |  | ☐ |
| 10 |  |  |  |  | ☐ |
| 11 |  |  |  |  | ☐ |
| 12 |  |  |  |  | ☐ |
| 13 |  |  |  |  | ☐ |
| 14 |  |  |  |  | ☐ |
| 15 |  |  |  |  | ☐ |
| 16 |  |  |  |  | ☐ |

## Textbook

`Machine Learning in Production: From Models to Products` (Kästner, MIT Press 2025) — 847 pp, full book held in Drive.
Free online: https://mlip-cmu.github.io/book/ · CC BY-NC-ND.

| Ch | Title | PDF pages | Session |
|---|---|---|---|
| 1 | Introduction | 4–31 | S1 ✅ |
| 2 | From Models to Systems | 32–56 | S2 |
| 3 | ML in a Nutshell | 57–67 | S1 ✅ |
| 4 | When to use Machine Learning | 68–78 | S3 |
| 5 | Setting and Measuring Goals | 79–101 | S3 |
| 6 | Gathering Requirements | 102–129 | S3 |
| 7 | Planning for Mistakes | 130–159 | S3 |
| 8 | Thinking like a Software Architect | 160–187 | S4–S6 |
| 9 | Quality Attributes of ML Components | 188– | S4 |

*(Later chapters — 10 Deploying a Model, 11 Automating the Pipeline, 14–19 Quality Assurance, 23–29 Responsible ML — map to S12, S13, S10–S11 and S14. Locate by heading when needed.)*

## R1 · Tech Mahindra, *Moving from SDLC to ADLC* — **S1, S15**

Landing page: https://www.techmahindra.com/insights/whitepapers/moving-sdlc-ai-driven-software-development-lifecycle-adlc-generate-value/
PDF: `sdlc-to-adlc.pdf` (12 pp) — ✅ **read in full**.

**Correction to an earlier assumption:** I had guessed the report would "add narrative, not new examinable content." Wrong. Slide 19 reproduces only §1 of five sections. The other four contain the paper's actual argument:

| § | Content | Where it landed |
|---|---|---|
| 1 | Evolution of SDLC — the table on slide 19 | S1 §4 |
| 2 | **Opportunities from AI/GenAI** — five capabilities (Generate, Recommend, Review, Summarize, Knowledge Search); productivity gains by phase (Requirements 20%, Design 15%, Build 30%, Test 30%) | S1 §4 |
| 3 | **Why adoption fails** — Planning & Execution, Technology, Commercial, Stakeholder Management; the **AI Pair Programming** example | S1 §4 |
| 4 | **Four-stage adoption journey** — Experiment → Onboard & Pilot → Scale & Soar → Sustain (>80% usage) | S1 §4 |
| 5 | Benefits and key influencing factors | — |

Also relevant to **S15** (ADLC phases in detail), which is lecture-notes-only in the handout — so this paper is the closest thing to a source for that session.

## T2 · Nelson, *Software Engineering for Data Scientists* (O'Reilly 2024, 249 pp)

Covers **546 sessions 7, 8 and 9** — the implementation and code-sharing block.

| Ch | Title | PDF page | Session |
|---|---|---|---|
| 1 | What Is Good Code? | 20 | **S7** |
| 2 | Analyzing Code (performance) | 30 | **S7** |
| 3 | Using Data Structures | 50 | **S7** |
| 4 | Object-Oriented Programming | 65 | **S8** |
| 5 | Errors, Logging, and Debugging | 76 | **S8** |
| 6 | Code Formatting, Linting | 90 | **S8** |
| 7 | Testing Your Code | 103 | ✗ **OUT OF SCOPE** — S10 testing comes from T1 ch14–16 |
| 8 | Design and Refactoring | 117 | **S9** |
| 9 | Documentation | 131 | ✗ **OUT OF SCOPE** |
| 10 | Sharing Your Code: Version Control | 146 | **S9** |
| 11 | APIs | 163 | **S9** → `_shared/api-design.md`, **549 S1** |
| 12 | Automation | 177 | ✗ **OUT OF SCOPE** — S13 comes from T1 ch11 |
| 13 | Security | 190 | ✗ **OUT OF SCOPE** — S11 comes from T1 ch17–19 |
| 14 | Working in Software Teams | 201 | ✗ **OUT OF SCOPE** |
| 15 | Next Steps | 213 | ✗ **OUT OF SCOPE** |

**Scope: the handout cites only T2 ch1–3 (S7), ch4–6 (S8) and ch8, 10, 11 (S9). Every other T2 chapter is out of the syllabus.**
Topics that look like gaps are covered from the *other* textbook instead — testing and security come from **T1 ch14–19** at S10–S11, automation from **T1 ch11** at S13. So nothing is actually missing; T2 simply isn't the source for them.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts are **raw source, not committed** — `source/transcripts/` is gitignored. Read a transcript to build or update the note, fold the important content (instructor quotes, emphasis, off-slide clarifications) into it, then it's done. The note is the record.
