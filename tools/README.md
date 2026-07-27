# tools

## `check-mermaid.mjs`

Parses every ```mermaid block in the given notes with the real Mermaid parser and
reports any that won't render. A diagram that fails to parse renders as a wall of
raw text in the note — worse than having no diagram at all — and nothing in a
plain Markdown preview warns you.

**Setup** (once):

```bash
cd tools && npm init -y && npm install mermaid jsdom
```

**Run** (from the repo root):

```bash
node tools/check-mermaid.mjs 2026-2027-Sem1/AIML*/notes/*.md 2026-2027-Sem1/_shared/*.md
```

Exits non-zero if any diagram fails, so it can be wired into a pre-commit hook.

Note: it strips leading `> ` before parsing, because a fenced block inside a
blockquote (the "In practice" / "Going deeper" boxes) carries the quote marker in
the raw text but not by the time a Markdown renderer reaches it.
