# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

> 🔴 **Slides are mandatory.** No deck → **no note is written** for that session. The handout is too coarse to define scope and the textbook is too broad; only the deck shows what this instructor taught and what they emphasised. Collect the deck for every session the same weekend, without exception.

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `API driven_Lecture 1_25Jul.pptx` (72 sl) | ✓ **R2 ch1 read** | ✓ Teams | ✅ received & extracted into note (not stored) | ✅ `notes/S01-api-basics.md` |
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

### R2 · Gough, Bryant & Auburn, *Mastering API Architecture* (O'Reilly 2023, 289 pp) — **S1, S2**

| Part | Ch | Title | PDF page | Session |
|---|---|---|---|---|
| I · Designing, building, testing | 1 | Design, Build, and Specify APIs | **41** | **S1 ✅ · S2** |
| | 2 | Testing APIs | 65 | ✗ **OUT OF SCOPE** |
| II · API traffic management | 3 | API Gateways: Ingress Traffic Management | 93 | ✗ **OUT OF SCOPE** |
| | 4 | Service Mesh: Service-to-Service Traffic Management | 125 | ✗ **OUT OF SCOPE** |
| III · Operations and security | 5 | Deploying and Releasing APIs | 163 | ✗ **OUT OF SCOPE** |
| | 6 | Operational Security: Threat Modeling for APIs | 183 | ✗ **OUT OF SCOPE** |
| | 7 | API Authentication and Authorization | 205 | ✗ **OUT OF SCOPE** |
| IV · Evolutionary architecture | 8 | Redesigning Applications to API-Driven Architectures | 229 | ✗ **OUT OF SCOPE** |
| | 9 | Using API Infrastructure to Evolve Toward Cloud Platforms | 247 | ✗ **OUT OF SCOPE** |
| | 10 | Wrap-up | 263 | ✗ **OUT OF SCOPE** |

**Scope: the handout cites R2 ch1 only** (sessions 1 and 2). Chapters 2–10 are outside the syllabus, however relevant the titles look — API gateways and service mesh are covered in 549 **S3** from R3 and lecture notes, not from R2.

Ch1 contents (all in scope): intro to REST · **Richardson Maturity Model** · REST standards & structure · collections, pagination, filtering · error handling · OpenAPI specification, code generation, validation, mocking, detecting changes · **API versioning & semantic versioning** · implementing RPC with gRPC · **modeling exchanges and choosing an API format** (north–south vs east–west, high-traffic services, large payloads, vintage formats) · multiple specifications.
The **Conference API** running example the deck names as self-study lives here.

### Not held
- **R4** Treveil, *Introducing MLOps* — cited for S6.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts are **raw source, not committed** — `source/transcripts/` is gitignored. Read a transcript to build or update the note, fold the important content (instructor quotes, emphasis, off-slide clarifications) into it, then it's done. The note is the record.

## Handout topic with no deck slide — session 1

⚠️ The handout lists **mocking** for session 1 (*"OpenAPI spec, mocking, semantic versioning,
tools"*) and the instructor read the line aloud in class, but **no slide covers it** — the only
occurrence of "mock" anywhere in the deck is *To Kill a Mockingbird* in a GraphQL sample response.

Written up in note section 4.1 from the OpenAPI toolchain (Prism, openapi-generator, contract
tests), flagged in the note as filled-in. It is a named syllabus item, so treat it as examinable.
