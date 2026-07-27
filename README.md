# MTech — BITS Pilani WILP

Notes, labs and study material for the whole degree. One folder per semester.

## Semesters

| Folder | Term | Subjects |
|---|---|---|
| [`2026-2027-Sem1/`](2026-2027-Sem1/) | Aug–Dec 2026 | AIML ZG536 Large Language Models for Generative AI · AIML ZG546 Software Engineering for Machine Learning · AIMLC ZG549 API-driven Cloud Native Solutions · AIMLCZG521 Conversational AI |

## Rules

- **No course material in git.** Textbook PDFs, slides and datasets live in Google Drive. `.gitignore` blocks them. Each subject's `source/` holds a pointer file only.
- **One markdown file per session**, in `<subject>/notes/`, following `_templates/SESSION-TEMPLATE.md`.
- **Every session gets both note types** the same weekend it's taught: a closed-book card (recall) and an open-book page (lookup).
- **Shared topics go in `_shared/`,** written once and cross-linked from every subject that touches them.

## Layout

```
2026-2027-Sem1/
├── STUDY-PLAN.md            ← the semester plan: phases, calendar, deadlines
├── <CODE>-<CourseTitle>/    ← folder name = course code + handout's course title
│   ├── <code>-master.md     ← running index; revision homepage; open-book front index in Dec
│   ├── notes/               ← one file per session
│   └── source/              ← pointer to Drive only
├── _shared/                 ← cross-subject master notes (rag, agents, evaluation, …)
└── _templates/
    └── SESSION-TEMPLATE.md
```
