# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `API driven_Lecture 1_25Jul.pptx` (72 sl) | R2 ch1 ✗ not held | ✗ | ✗ | ✅ `notes/S01-api-basics.md` |
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

## Textbooks held

### R1 · Severance, *Python for Everybody* (241 pp) — **Module 0 self-study**
Free: https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf · CC licensed

| Ch | Title | PDF page | In handout's self-study list? |
|---|---|---|---|
| 1 | Why should you learn to write programs? | 13 | ✓ (structure of a Python program) |
| 2 | Variables, expressions, statements | 31 | ✓ |
| 3 | Conditional execution | 43 | ✓ |
| 4 | Functions | 55 | ✓ |
| 5 | Iteration | 69 | ✓ |
| 6 | Strings | 79 | ✓ |
| 7 | Files | 91 | ✓ |
| 8 | Lists | 103 | ✓ |
| 9 | Dictionaries | 121 | ✓ |
| 10 | Tuples | 131 | ✓ |
| 11 | Regular expressions | 143 | ✗ **OUT OF SCOPE** |
| 12 | Networked programs | 157 | ✗ **OUT OF SCOPE** |
| 13 | Using Web Services | 171 | ✗ **OUT OF SCOPE** |
| 14 | Object-oriented programming | 179 | ✓ |
| 15 | Using Databases and SQL | 193 | ✓ |
| 16 | Visualizing data | 217 | ✓ |

**Scope:** the handout's Module 0 self-study list names ch1–10 and ch14–16. **Chapters 11–13 are not in the syllabus — do not read them for the course.**
*(If a lab later needs JSON handling in Python, ch13 is where it's covered — but that would be lab support, not syllabus, and only if a prescribed lab actually requires it.)*

### R3 · Davis, *Cloud Native Patterns* (Manning 2019, 399 pp) — **S2, S3**

| Part | Ch | Title | Book page |
|---|---|---|---|
| 1 · The cloud native context | 1 | You keep using that word: Defining "cloud-native" | 3 |
| | 2 | Running cloud-native applications in production | 26 |
| | 3 | The platform for cloud-native software | 51 |
| 2 · Cloud native patterns | 4 | Event-driven microservices | 83 |
| | 5 | App redundancy: scale-out and statelessness | 108 |
| | 6 | Application configuration | 139 |
| | 7 | The application lifecycle | 170 |
| | 8 | Accessing apps: services, routing, service discovery | 207 |
| | 9 | Interaction redundancy: retries and control loops | 231 |
| | 10 | Fronting services: circuit breakers and API gateways | 267 |
| | 11 | Troubleshooting | 295 |
| | 12 | Cloud-native data: breaking the data monolith | 320 |

**Scope: the handout cites R3 ch1 only, for sessions 2 and 3. Chapters 2–12 are OUT OF SCOPE** — do not read or draw on them, however relevant the titles look. Session 2 and 3 content comes from ch1 plus the lecture slides.

### Not held
- **R2** Gough et al., *Mastering API Architecture* — cited for S1 and S2, and the source of the Conference API self-study example.
- **R4** Treveil, *Introducing MLOps* — cited for S6.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts (`.txt`, `.srt`, `.vtt`) are small and plain text, so they **may** be committed if useful:
put them in `source/transcripts/`. They are not blocked by `.gitignore`.
