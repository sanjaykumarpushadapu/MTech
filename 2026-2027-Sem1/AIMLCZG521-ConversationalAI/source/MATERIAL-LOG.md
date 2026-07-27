# Material log

What raw material exists for each session, and whether it has been processed into notes.
Fill this in **when you get the material**, not when you process it — the gap is the point.

Legend: ✓ have · ✗ missing · — n/a

> 🔴 **Slides are mandatory.** No deck → **no note is written** for that session. The handout is too coarse to define scope and the textbook is too broad; only the deck shows what this instructor taught and what they emphasised. Collect the deck for every session the same weekend, without exception.

| S | Slides (.pptx) | Textbook ch | Recording | Transcript | Processed → notes |
|---|---|---|---|---|---|
| 1 | ✓ `Session-1-Foundations-of-ConvAI.pdf` (56 sl) | ✓ T1 *Building Effective Agents* · *Landscape of AI Agents* | ✗ | ✗ | ✅ `notes/S01-foundations.md` |
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


## T1 — Official documentation (primary textbooks, all public)

| Source | URL | Status | Sessions |
|---|---|---|---|
| Anthropic, **Building Effective Agents** (Dec 2024) | anthropic.com/engineering/building-effective-agents | ✅ fetched | **S1** (workflows vs agents, when not to) · **S9** (the five patterns) · **S4** (tool/ACI design) |
| OpenAI **function calling** docs | platform.openai.com | ☐ | S4 |
| **MCP** specification | modelcontextprotocol.io | ☐ | S13 |
| **A2A** specification | official spec | ☐ | S14 |

**R2 — core research papers** (all public, fetch when the session arrives)

| Paper | Session |
|---|---|
| *The Landscape of AI Agents* (Masterman et al., arXiv:2404.11584) | ✅ S1 |
| Dense Passage Retrieval (Karpukhin et al., 2020) | S2 |
| ReAct (Yao et al., 2023) | S4 |
| Direct Preference Optimization (Rafailov et al., 2023) | S5 |
| MemGPT (2023) | S6 |
| Anthropic Contextual Retrieval (2024) | S7–8 |
| MetaGPT (2024) | S9 |
| Judging LLM-as-a-Judge / MT-Bench (2023), GAIA | S10 |
| Anthropic prompt caching docs | S11 |
| Anthropic Responsible Scaling Policy | S15–16 |

**Nothing here needs uploading.** Give the session number and these get fetched.

## Scope rule

521 cites **no textbook chapters** — every reference is a specific public paper or spec, listed per session in `521-master.md`. **The named paper is the scope.** Related work it cites, or later papers by the same authors, are out of the syllabus unless the handout names them.

## Where things live

Recordings and slides stay in Google Drive / Canvas — never in this repo.
Transcripts (`.txt`, `.srt`, `.vtt`) are small and plain text, so they **may** be committed if useful:
put them in `source/transcripts/`. They are not blocked by `.gitignore`.
