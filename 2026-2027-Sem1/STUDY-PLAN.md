# MTech Sem 1 · Aug–Dec 2026 · Study Plan

BITS Pilani WILP · 536 LLMs · 549 Cloud Native · 521 Conversational AI · 546 SE4ML
Built 26 Jul 2026 · revised after session-1 material arrived.
Weekends = 4 contact sessions (2h each) + a 2–3h lab block. Weekdays = 1h per subject. **~17h/week committed** — see §3.

---

## 0. The five non-negotiables

1. **Notes are written the same weekend the session happens.** 15 min after each class, while it's still warm. Never "I'll do it before the exam" — that is how the December cluster becomes unsurvivable.
2. **Every weekday hour starts with cold recall, not reading.** Close the notes, say what last session covered, *then* open them and fix what was fuzzy. Re-reading feels productive and isn't.
3. **Every concept gets a "when NOT to use this" line.** That single line is where the marks concentrate — mid-sem and comp questions are overwhelmingly tradeoff questions.
4. **Shared topics are written once, in `_shared/`.** RAG, agents, fine-tuning, function-calling, Docker/K8s and evaluation each appear in 2–4 courses. The second course to reach a topic is revision, not new learning. This is the single biggest time saver in the semester.
5. **Bind the open-book file before December.** BITS rule: no loose sheets. Printing and binding is a 2-day errand — it goes in the calendar on 22 Nov, not 4 Dec.

---

## 1. Phase map

| Phase | Dates | What it is | What matters |
|---|---|---|---|
| **P0 · Pre-semester** | now → 31 Jul | 549 Python self-study, repo + tooling setup | Only thing genuinely due before classes |
| **P1 · Ramp** | 1–9 Aug | Sessions 1–2. Establish the weekly loop | Habit > content. Get the loop working |
| **P2 · Quiz window** | 10–20 Aug | ⚠️ **549 + 521 only.** 536 has no quiz; 546's is in September | **Lighter than planned** — use freed evenings for `_shared/` notes |
| **P3 · First crunch** | 27 Aug – 7 Sep | 549 project 30% + 536 assignment 30% + 546 situated learning 5% | **Three** deliverables in one window. Start day 1 |
| **P4 · Mid-sem run-up** | 8–18 Sep | Sessions 1–8 consolidation **+ 🔴 546 Assignment I (10%) lands here** | Contested, not clear. 536 & 521 mid-sems cover **7** sessions, not 8 |
| **P5 · Mid-sems** | 19–20 Sep | 546 Sat EN · 549 FN + 536 EN Sun · 521 in window | Closed book, sessions 1–8 |
| **P6 · Second half** | 26 Sep – 14 Nov | Sessions 9–16 | Open-book pages, not cards. **Rolling revision of S1–8 starts in October** |
| **P7 · 546 assignments** | 29 Oct – 11 Nov | 546 Asgn I & II, 20% | Overlaps sessions 14–15. Plan the collision |
| **P8 · Comp prep** | 15 Nov – 4 Dec | Front index (16–20 Nov), print + bind (21–22 Nov), lookup drills | Retrieval speed, not new understanding |
| **P9 · Comps** | 5–6 Dec | 546 Sat EN · 549 FN + 536 EN Sun · 521 early Dec | Open book, all 16. ⚠️ Sat-night turnaround into a Sunday double |

**Three pressure points:** 27 Aug–7 Sep · 19–20 Sep · 5–6 Dec. Everything else is buffer. Protect the buffer.

---

## 2. Pre-semester (now → 31 Jul) — the only work due before classes

You have ~5 days. This is the highest-leverage week of the semester because it's the only one with no incoming material.

| Day | Task |
|---|---|
| Mon 27 Jul | Repo skeleton: `2026-2027-Sem1/{536,549,521,546}/{source,notes}`, `_shared/`, `_templates/`. Commit. |
| Tue 28 Jul | 549 Python self-study **part 1** — Severance ch1–8 (why program, variables, conditionals, functions, iteration, strings, files, lists). Skim if known; the point is to find gaps, not to read every page. |
| Wed 29 Jul | 549 Python **part 2** — ch9, 10, **14, 15, 16** (dicts, tuples, OOP, databases & SQL, visualising data). ⚠️ **Skip ch11–13 — regex, networked programs and web services are NOT in the handout's self-study list.** Write `S00-python-selfstudy.md` with only what you didn't already know. |
| Thu 30 Jul | Tooling: Colab + VS Code working, OpenAI/Anthropic API keys with a hard spend cap, Docker Desktop installed, `git` push tested. |
| Fri 31 Jul | Read all four handouts end to end. Put every known date in your phone calendar with a 7-day advance alert. Set a weekly Canvas/eLearn check reminder (Wed 8pm). |

**Why Python first:** it's the prerequisite for 549's five labs *and* 521's ten labs. Every hour spent here in July saves three in September.

---

## 3. Weekly engine

Same shape every week. Don't redesign it mid-semester.

| Day | Slot | What happens |
|---|---|---|
| **Sat** | 2 classes + 2×15 min | Class → immediately: concept list, closed-book card stubs, "what confused me" line |
| **Sun** | 2 classes + 2×15 min | Same |
| **Sun** | **+ 2–3h lab block** | **The week's primary lab.** Protected time, not overflow — see below |
| **Mon** | 536 LLMs · 1h | Sharpest hour — theory-heaviest subject. Mechanism topics: reproduce one worked example **by hand**. Landscape topics: comparison table only |
| **Tue** | 549 Cloud Native · 1h | Layer-map maintenance (containers → orchestration → serverless → observability). Hang each new tool on a layer with one line. Never study internals |
| **Wed** | 521 Conversational AI · 1h | Build the minimal runnable version. ReAct loop, tiny RAG, memory store, MCP server — 30 lines each. It clicks when the code runs, not when the slide is read |
| **Thu** | 546 SE4ML · 1h | Apply the week's module to your one running example (fraud detection). Same system, every module, all semester |
| **Fri** | 1h · second lab / flex | The week's **second** lab, or overflow, or the thing that went wrong. If nothing's pending: write the week's `_shared/` note |

**The weekday hour, precisely:**
`recall last session cold (10 min) → fix what was fuzzy (20 min) → write the open-book page (30 min)`

Note what changed: **the lab is no longer a 15-minute tail on the weekday hour.** It never fitted there.

### Why labs need their own block

The four handouts prescribe **29 labs** — 521:10 · 536:8 · 546:6 · 549:5 — plus 8 webinars and 2 case studies. Over ~16 teaching weeks that's **roughly two labs a week, every week**. A lab that actually runs (fine-tuning a model, standing up a Kubernetes deployment, building a testing framework) is 2–4 hours. Fifteen minutes at the end of a tired weekday hour was never going to touch it.

So: **one protected weekend block for the week's main lab, Friday's hour for the second.** If only one lab is due, Friday reverts to flex.

**Honest arithmetic.** This raises committed time to roughly **17 hours a week**: 8h classes + 1h same-day notes + 2.5h lab block + 5h weekdays. That is a lot alongside a full-time job, and it is the real number — the previous version of this plan quietly understated it by pretending labs were free. Better to see it now and plan around it than to discover it in week 5.

**If 17 hours isn't available**, cut in this order: (1) Friday's second lab — do the minimum version that runs, (2) open-book pages for comprehensive-only sessions, backfilled in November, (3) never the same-day notes or the cold recall, because those are what make the other hours work.

### Rolling revision — from October onward

After the 20 Sep mid-sem, sessions 1–8 get no further attention until comp prep. That's **eleven weeks of decay on half the comprehensive syllabus**, and it's how December becomes a cliff.

Fix, from week 10 (early October): **split the opening recall in two.**

`recall last session (5 min) → recall one OLD session, rotating (5 min) → fix what was fuzzy (20 min) → write the open-book page (30 min)`

Rotate the old session by number: week 10 → S1, week 11 → S2, and so on. By mid-November every early session has been retrieved cold at least once. **Cost: zero extra minutes.** It is the highest-return change in this document.

---

## 4. Week-by-week calendar

Weekend = contact session number. Sessions 1–8 are mid-sem scope (closed book); 9–16 add to the comprehensive (open book).

### August

| Wk | Weekend | Sessions | Weekday focus | Deadlines |
|---|---|---|---|---|
| 1 | **1–2 Aug** | S1 all four | 536 S1 foundations & tokenization · 549 S1 API basics · 521 L1 agentic systems · 546 S1 foundations — **choose the running example now**. **Sun block: 536 Lab 1 + 521 Lab 1, both tokenization — do them together, one sitting** | — |
| 2 | **8–9 Aug** | S2 | 549 cloud-native evolution · 521 L2 embeddings/HNSW/BM25+RRF · start `_shared/retrieval.md` · **Sun block: 521 Lab 2** | **Quiz window opens 10 Aug** |
| 3 | **15–16 Aug** | S3 | Quizzes: **549 only** (536 has none, 546's is in Sep) — one evening, light skim of S1–S2 first. 521 L3 model landscape ↔ 536 quantization — **write `_shared/quantization.md` once, use twice** · **Sun block: 521 Lab 3 hybrid search** | Quizzes (all 4) by 20 Aug |
| 4 | **22–23 Aug** | S4 | 549 DS/ML intro ↔ 546 ML lifecycle — same content, one note. 521 L4 ReAct + function calling · **Sun block: 546 Lab 2 GR4ML** | Watch for project/assignment briefs |
| 5 | **29–30 Aug** | S5 | **Crunch begins.** 549 project + 536 assignment + 546 situated learning all live. Weekday hours *and* the Sun block go to deliverables; notes drop to bare concept lists — **except 549, whose slides+recording must still be collected (no textbook exists for S4 onward)**. Do 546 situated learning (5%, 3 days) first and clear it | 549 project · 536 assignment · 546 situated learning all open 27 Aug |

### September

| Wk | Weekend | Sessions | Weekday focus | Deadlines |
|---|---|---|---|---|
| 6 | **5–6 Sep** | S6 | Crunch continues; Sun block still on deliverables. 521 L6 memory systems. Reuse lab code in the deliverables — that's what "project-as-you-go" buys you. **549 S5 has Lab 1 (data pipeline) — do the minimum that runs** | **549 project + 536 assignment due ~7 Sep** |
| 7 | **12–13 Sep** | S7 (+S8) | Last new mid-sem material. **Backfill the notes the crunch cost you.** Convert all S1–S8 to closed-book cards; build the one-page concept-name checklist per subject. Sun block → backfill, not labs | Mid-sem scope closes |
| 8 | **19–20 Sep** | **MID-SEMS** | Mon–Fri before: cover-and-recite the checklists, 4 subjects rotating. No new reading, no labs | **546 Sat EN · 549 FN + 536 EN Sun · 521 in window** |
| 9 | **26–27 Sep** | S9 | Reset. Switch note mode: open-book pages, not cards. 521 L9 multi-agent · **Sun block: 521 Lab 5b naïve RAG** | — |

### October

| Wk | Weekend | Sessions | Weekday focus | Deadlines |
|---|---|---|---|---|
| 10 | **3–4 Oct** | S10 | 549 S10 RAG ↔ 521 L10 evaluation. `_shared/rag.md` and `_shared/evaluation.md` now pay off — revise, don't relearn. **Rolling revision starts: opening recall now covers last session + S1** | — |
| 11 | **10–11 Oct** | S11 | 549 RAG metrics · 521 cost optimization/prompt caching · **Advanced RAG lab** (Sun block) · rolling: **S2** | — |
| 12 | **17–18 Oct** | S12 | 549 Docker/K8s deployment ↔ `_shared/docker-k8s.md` (started at S3) · 521 security/prompt injection · **Guardrails lab** (Sun block) · rolling: **S3** | — |
| 13 | **24–25 Oct** | S13 | 521 MCP deep dive — build an actual MCP server (Sun block), best-retained hour of the semester · 549 IoT · rolling: **S4** | 546 assignments release ~29 Oct |
| 14 | **31 Oct – 1 Nov** | S14 | **546 assignments live.** Thu hour + Sun block → assignment. 521 L14 A2A + orchestration lab (Friday) · rolling: **S5** | 546 Asgn I & II window |

### November

| Wk | Weekend | Sessions | Weekday focus | Deadlines |
|---|---|---|---|---|
| 15 | **7–8 Nov** | S15 | 546 assignments continue (Sun block) · 521 L15 ethics/governance ↔ 546 governance — one note · rolling: **S6** | **546 Asgn I & II due ~11 Nov** |
| 16 | **14–15 Nov** | S16 | Last sessions. **Weekdays 16–20 Nov: build the front index** — every master index must have all 16 rows filled, note files named correctly, cross-links resolving. This is the week that makes binding on the 22nd possible · rolling: **S7, S8** | Course content complete |
| 17 | **21–22 Nov** | Revision | Front index was built 16–20 Nov, so this weekend is **print, then bind**. Nothing else. Sun lab block is retired — no labs remain | 🔴 **Bind by 22 Nov** |
| 18 | **28–29 Nov** | Revision | Open-book *drills*: pick a random topic, time yourself finding it in the bound file. Target <60 sec. Fix the index where you fail | — |

### December

| Wk | Weekend | Sessions | Weekday focus | Deadlines |
|---|---|---|---|---|
| 19 | **5–6 Dec** | **COMPREHENSIVES** | Mon–Fri: tradeoff lines only — "when NOT to use X" for every concept. That's the exam. **Sat night is the tightest 12 hours of the semester**: 546 finishes Saturday evening, then 549 (FN) and 536 (EN) both fall on Sunday. Plan Saturday night deliberately — 549 index drill only, sleep, 536 on Sunday afternoon between papers | **546 Sat EN · 549 FN + 536 EN Sun · 521 early Dec** |

---

## 5. Deadline watchlist

| Date | What | Weight | Status |
|---|---|---|---|
| 10–20 Aug | Quizzes ×4 | 5–10% each | ☐ |
| ~27 Aug – 7 Sep | 549 project | **30%** | ☐ |
| ~27 Aug – 7 Sep | 536 assignment / lab exam | **30%** | ☐ |
| 27 Aug – 7 Sep | 546 situated learning (3 days) | 5% | ☐ |
| 19 Sep (EN) | 546 mid-sem (closed) | 30% | ☐ |
| 20 Sep FN | 549 mid-sem (closed) | 30% | ☐ |
| 20 Sep EN | 536 mid-sem (closed) | 30% | ☐ |
| ~19–20 Sep | 521 mid-sem (closed) | 30% | ☐ |
| ~15 days each | 521 Assignment 1 & 2 | 20% | ☐ ⚠️ dates announced in class only |
| 29 Oct – 11 Nov | 546 Assignments I & II | 20% | ☐ |
| **22 Nov** | **Print + bind open-book file** | — | ☐ |
| 5 Dec (EN) | 546 comprehensive (open) | 40% | ☐ |
| 6 Dec FN | 549 comprehensive (open) | 35% | ☐ |
| 6 Dec EN | 536 comprehensive (open) | 35% | ☐ |
| ~early Dec | 521 comprehensive (open) | 40% | ☐ |

⚠️ **521 has no published dates** — quizzes and both assignments are "announced in class or on Canvas," with **strictly no makeups**. Check Canvas every Wednesday. This is the highest-risk item in the semester and it's a calendar risk, not a knowledge risk.

### ✅ EC-1 resolved from the session-1 recordings — the handouts were wrong

Three of four instructors stated EC-1 aloud in their first session. **Where handout and instructor disagree, the instructor wins.**

| Subject | Handout said | **Actual, from the recording** |
|---|---|---|
| **536** | Quiz 5% + Assignment 30% | ❌ **No quizzes at all.** EC-1 = **35%, two GROUP assignments** forming one end-to-end project. Must run on the **BITS remote lab, not your laptop** |
| **546** | Quiz 10–20 Aug; Assignments I & II both 29 Oct–11 Nov | 🔴 **Assignment I (10%) is BEFORE the mid-sem.** Quiz is **15 min, 15–20 questions, "just before the mid sem"** — *not* in the August window. Individual-vs-team **still undecided** |
| **549** | Quiz 5% + Project/Assignment 30% | ✅ **Quiz 5% + TWO assignments at 15% each = 35%.** No dates announced yet |
| **521** | Quiz ×3 best-of-2 10% + Assignments 20% | ✅ **Handout is correct — ×3, best 2 of 3.** Slide 26's "×2" is wrong. One bad quiz is free; sit all three |

### 🔴 Three changes this forces on the calendar

**1. The August quiz window is nearly empty.** The plan has "4 quizzes, 10–20 Aug" as phase P2. In fact **536 has no quiz at all**, and **546's quiz is in September, just before the mid-sem**. Only 549 and possibly 521 have anything in that window — and 549's date isn't announced. **P2 is now a light phase, not a busy one.** Use the freed evenings for the shared notes.

**2. A 10% deliverable lands inside the mid-sem run-up.** 546's Assignment I falls before 19 Sep with a **two-week** completion window — i.e. somewhere in early-to-mid September, exactly where the plan assumed clear air for closed-book revision. **Treat 8–18 Sep as contested, not clear.**

**3. Mid-sem scope is smaller than the handouts imply.** **536 session 8 and 521 session 8 are both revision sessions** — the instructors said so. So those two closed-book papers cover **seven** sessions of new material, not eight. 546's instructor: *"the mid sem happens after session 7 or session 8."*

### Lab environments — confirmed, and they differ per subject

| Subject | Environment | From when | Cost |
|---|---|---|---|
| **536** | 🔴 **BITS remote lab — mandatory for assignments.** *"In laptop, no."* Colab only for very small models | manual to be shared | free |
| **546** | **Virtual lab** for all demos and coding; **AWS Console Lab** from ~sessions 13–14 | virtual lab after session 2 | 💰 **both free — "not chargeable"** |
| **521** | **Local**: Ollama + `llama3` on your own machine, plus a free Tavily key | now — notebooks already issued | free |
| **549** | not stated | — | — |

*Set up 536's remote lab access and 521's Ollama before the crunch, not during it.*

### Where material actually lives — it differs by subject

| Subject | Materials | Announcements & assignments |
|---|---|---|
| 536 | MS Teams | Taxila |
| 546 | MS Teams + Taxila | **Taxila** — *"everything will be on Taxila only"* |
| 549 | **MS Teams** — handout, per-session deck, **and the session's code**, in the shared folder | MS Teams |
| 521 | — | **Canvas** |

**Three different portals.** Check Taxila, Teams and Canvas — not one of them.

---

## 6. Shared notes — build order

Write each once, in `_shared/`, the first time any course reaches it. Revise (don't rewrite) when the next course arrives.

| Note | First taught | Reused by | Build by |
|---|---|---|---|
| `retrieval.md` — embeddings, ANN/HNSW, BM25, RRF | 521 L2 | 549 S10–11 | 9 Aug |
| `quantization.md` — INT8/INT4, QLoRA, KV-cache | 521 L3 + 536 | — | 16 Aug |
| `function-calling.md` — schemas, ReAct, error handling | 521 L4 | 536, 549 S8 | 23 Aug |
| `finetuning.md` — FT vs prompting, LoRA/QLoRA, DPO/GRPO | 521 L5 + 536 | — | 30 Aug |
| `agents.md` — planning, memory, multi-agent, MCP, A2A | 521 L1/L6/L9/L13/L14 | 536 | running |
| `rag.md` — chunking, re-ranking, contextual, agentic | 521 L7–8 | 549 S10–11, 536 | 13 Sep |
| `docker-k8s.md` — containers, orchestration, deployment | 549 S3 | 549 S12 | 16 Aug |
| `evaluation.md` — metrics, LLM-as-judge, benchmarks | 521 L10 | 546, 536, 549 | 4 Oct |
| `ml-lifecycle.md` — pipelines, MLOps, monitoring, drift | 549 S4–S7 | 546 (most of it) | 20 Sep |

**Biggest single win:** `rag.md` + `retrieval.md`. 549 sessions 10–11 are a lighter pass over 521 L2 and L7–8. Because 521 needs them for the *mid-sem* (closed book) and 549 only for the *comprehensive* (open book), writing them properly in September makes October's 549 weeks nearly free.

---

## 7. The one project, four layers

Same application all semester — a RAG assistant over your own documents:

- **521** owns the agent: ReAct loop, memory, tools, MCP interface, guardrails
- **536** owns the model: quantization, fine-tuning/DPO, decoding, serving cost
- **549** owns the infrastructure: API layer, Docker, K8s, pipeline, deployment
- **546** owns the discipline: requirements, testing, monitoring, drift, governance

Let it grow out of the labs rather than building it separately. When an assignment drops, you're extending something that already runs instead of starting cold — which is also the honest answer to the plagiarism checks, since the work is provably yours and incremental in git history.

---

## 8. Contingency rules

Decide these now, while calm, so you're not deciding them at 11pm in September.

- **The week doesn't fit?** Committed load is ~17h/week (8h classes + 1h same-day notes + 2.5h lab block + 5h weekdays). Cut in this order: Friday's second lab → open-book pages for comprehensive-only sessions → *never* the same-day notes or the cold recall.
- **Behind by one session?** Skip the open-book page, keep the closed-book card. Cards are recoverable later; understanding isn't.
- **Behind by a week?** Drop 546 first (least cumulative, most recoverable), never 549 (5 credits, most cumulative).
- **Crunch collision (Aug 27–Sep 7)?** Notes go to bare concept lists for those two weeks. Deliverables at 30% outweigh notes. Backfill on 12–13 Sep.
- **Lab won't run?** 30-minute cap, then write down the error, move on, ask in class. Debugging alone past 30 minutes is the worst hour-per-mark rate available.
- **A weekday hour disappears (work, travel, fatigue)?** Don't double up the next day. Take the 10-minute recall for that subject on Friday and move on. The habit surviving matters more than any single hour.
- **Sick or overloaded for a whole weekend?** Get the session recordings, but treat cold recall of the *previous* session as the priority. Falling one session behind is fine; losing the loop is not.

---

## 9. Assumptions to verify in week 1

- First contact session weekend is 1–2 Aug and sessions run one per subject per weekend. If your actual schedule doubles some sessions, the mid-sem-scope deadline (S1–S8 complete) shifts — re-check against Canvas in week 1.
- Sessions 7 and 8 are shown as a doubled weekend on 12–13 Sep to fit 8 sessions before the 19 Sep mid-sem. 521's handout pairs L7 & L8, and **536's session 8 is a revision session** — so 536 only has 7 sessions of new mid-sem material, which eases the fit. Confirm 546 and 549.
- 521 exam dates are inferred from the shared exam weekends, not published. Confirm on Canvas.
- All four handouts confirm the same mid-sem scope rule: **contact sessions 1–8, closed book**; comprehensive covers all topics, open book.
