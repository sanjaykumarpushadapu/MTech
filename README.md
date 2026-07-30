# MTech — BITS Pilani WILP

Notes, labs and study material for the whole degree. One folder per semester.

## Semesters

| Folder | Term | Subjects |
|---|---|---|
| [`2026-2027-Sem1/`](2026-2027-Sem1/) | Aug–Dec 2026 | AIML ZG536 Large Language Models for Generative AI · AIML ZG546 Software Engineering for Machine Learning · AIMLC ZG549 API-driven Cloud Native Solutions · AIMLCZG521 Conversational AI |

## Rules

- **No course material in git.** Textbook PDFs, slides and datasets live in Google Drive. `.gitignore` blocks them. Each subject's `source/` holds a pointer file only.
- **One markdown file per session**, in `<subject>/notes/`, following `_templates/SESSION-TEMPLATE.md`.
- **Every session gets one note** the same weekend it's taught. The note body is what you revise from for *both* exams — there are no separate recall cards. A **condensed open-book page** is derived from it later, for the bound December file.
- **Subject notes are the primary study path.** Start from the subject master, then the session note. `_shared/` is optional secondary synthesis, not a required hop.

## Fast path

For the current semester, open `2026-2027-Sem1/README.md` first. That file is the navigation hub.

## Layout

```
2026-2027-Sem1/
├── README.md                ← semester navigation hub; where to look first
├── STUDY-PLAN.md            ← the semester plan: phases, calendar, deadlines
├── <CODE>-<CourseTitle>/    ← folder name = course code + handout's course title
│   ├── <code>-master.md     ← running index; revision homepage; open-book front index in Dec
│   ├── notes/               ← one file per session
│   └── source/              ← pointer to Drive only
├── _shared/                 ← optional synthesis notes, secondary to subject notes
└── _templates/
    └── SESSION-TEMPLATE.md
```
