# Materials watchlist

**Everything still needed, with the date it starts blocking work.** Checked at the start of every session that touches a listed item, and raised **unprompted** as its date approaches — the user asked to be told forcefully rather than politely.

*Last checked: 04 Sep 2026 — 549 S04 (Lecture 4, 37 slides) and S05 (the "Lecture 5 & 6" deck, 90 slides) were received, slide-audited, and noted; the same 90-slide deck was then split into two session notes at its natural slide 61/62 boundary (S05 = slides 1–61, S06 = slides 62–90) per user request, with the S06 note flagging up front that it does not teach S6's actual handout topic (API-driven ML Pipelines) — that topic's own deck remains a genuine gap. The 549 handout was sourced from an uploaded copy to scope S04–S07 — the repository-relative `_handouts/` copy is still absent from the checkout; restore it so a future session does not need a fresh upload. 521 renumbered to instructor contact sessions: S02 Embeddings & Vector Search, **S03 ANN Search & Hybrid Retrieval**, **S04 Model Landscape & Cost Engineering**. The attached S03/S04 decks were revalidated slide-by-slide and remain held and noted. The external 536 handout was rechecked and now maps the fine-tuning deck to S04; the handout's Training and Attention Efficiency topic is S07. The repository-relative handout copies remain absent. 11 of 12 books held; only Kimothi (536 R3) outstanding. 521 L2 DistilBERT notebook held; remaining Lab 2 items still unverified.*

> **Ownership:** each subject's `source/MATERIAL-LOG.md` is the compact current ledger for that subject. This file contains only cross-subject blockers, requests, and reminders; do not copy full session-status tables here.

---

## 🔴 Blocking now

| Item | Subject | Portal | Why it blocks |
|---|---|---|---|
| **Remaining L2 lab items** | **521** | Canvas | `Embedding-distilbert.ipynb` is held, but the handout lab row also names text-to-speech, rule-based systems, and sentiment analysis; those files still need either upload or instructor confirmation that they are not issued separately |
| **S2 deck** | 546 | Taxila | Reading (Kästner ch1–2) already held |
| **S2 transcripts** | all four | Teams export | Not blocking, but useful for resolving instructor emphasis and EC/date conflicts |

**Every weekend, all semester: collect four decks.** This row never leaves the table.

---

## 📚 Textbooks — status against every T/R cited in all 16 sessions

### ✅ Held in `_library/` (11)

| | 536 | 546 | 549 |
|---|---|---|---|
| **T1** | J&M, *Speech & Language Processing* | Kästner, *ML in Production* | — |
| **T2** | Alammar, *Hands-On LLMs* | Nelson, *SE for Data Scientists* | — |
| **R1** | Raschka, *Build an LLM from Scratch* | Tech Mahindra, SDLC→ADLC | Severance, *Python for Everybody* |
| **R2** | ✅ **Bahree, *Generative AI in Action*** — received 27 Jul | *fetchable* | Gough, *Mastering API Architecture* |
| **R3** | ⚠️ **Kimothi — the only book still missing** | *fetchable* | Davis, *Cloud Native Patterns* |
| **R4** | — | *fetchable* | ✅ **Treveil, *Introducing MLOps*** — received 27 Jul |

**521 needs no books** — every reference is a public paper or spec.

### ⚠️ Still missing — commercial, only the user can supply

| Ref | Book | 🔴 Ask by | Needed for | Note |
|---|---|---|---|---|
| **536 R3** | Kimothi, *A Simple Guide to Retrieval Augmented Generation* (Manning) | **20 Sep 2026** | **536 S12** — RAG (~Oct) | Single-chapter citation (ch6). **The last missing book.** |

> ⚠️ **Name collision — do not file the wrong document.**
> `1_Generative-AI-in-Action-eBook.pdf` (uploaded 27 Jul) is a **9-page, 2,100-word vendor marketing paper** — *"Adoption Trends, Emerging Use Cases, and Tips for IT Leaders"*. Zero mentions of Manning, chapters, embeddings, vectors or LangChain.
> **536 R2 is Amit Bahree's ~450-page Manning book of the same name.** Different document entirely. The whitepaper has no place in the syllabus and was not added to `_library/`.

### ✅ Missing but public — fetch, never ask

| Ref | What | Needed | Verified |
|---|---|---|---|
| 546 R2 | Apollo autonomous-driving ML case study (2020) | S2 | — |
| 546 R3 | Microsoft, *SE for ML: A Case Study* (ICSE 2019) | S2 | ✅ PDF URL confirmed 27 Jul |
| 546 R4 | Schneider, *Generative to Agentic AI* (arXiv:2504.18875) | S2 | ✅ confirmed CC-BY 27 Jul |
| 546 R5 | CNCF AI WG, *Cloud Native AI* (2024) | S2 | — |
| 546 R6 | GR4ML | S3 | — |
| 549 R5 | HuggingFace · LangChain · Ragas · k8s · Docker · CNCF | S4+ | — |

---

## 📅 Forced-reminder schedule

Raise these **unprompted**, in the response nearest the date, whether or not the user asked:

| Date | Raise |
|---|---|
| **Every weekend** | The four session decks. Non-negotiable |
| **Next 536 note touch** | Use the externally supplied handout already verified; keep it outside Git unless a repository copy is explicitly required |
| **20 Sep 2026** | 🔴 **Ask for 536 R3 (Kimothi)** — right after the mid-sems, ~3 weeks before S12 needs it. The last outstanding book |
| **Before 546 S2** | Fetch 546 R2–R5 myself; don't ask |
| **Before 546 S3** | Fetch GR4ML myself |
| **1 Nov 2026** | 🔴 If Kimothi is still missing, say so plainly and write S12 from T1 ch11 + T2 ch8 + **R2 Bahree ch7** + `_shared/rag.md`, marking the R3 gap in the note |
| **16–20 Nov 2026** | Front index week — every master row filled, every note named right |
| **22 Nov 2026** | 🔴 **Print + bind.** BITS bans loose sheets |

## Non-material items still open

| Item | Owner | By |
|---|---|---|
| 549 Python self-study (Severance) | user | overdue |
| Ollama + Tavily set up for 521 L1 | user | before L2 |
| BITS remote-lab access for 536 | user | before 536 L2 |
| 521 assignment dates — Canvas only, **no makeups** | user | check Canvas every Wednesday |
