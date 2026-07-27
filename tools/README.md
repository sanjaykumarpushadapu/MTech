# tools

## `check-mermaid.mjs`

Parses every ```mermaid block in the given notes with the real Mermaid parser and
reports any that won't render. A diagram that fails to parse renders as a wall of
raw text in the note — worse than having no diagram at all — and nothing in a
plain Markdown preview warns you.

**Setup** (once) — `package.json` is committed, so this is just:

```bash
cd tools && npm install
```

**Run:**

```bash
cd tools && npm run check
```

⚠️ It must run from `tools/`, because that's where `node_modules` lives. Running
`node tools/check-mermaid.mjs` from the repo root fails with a module-not-found
error, not a diagram error — don't mistake one for the other.

Exits non-zero if any diagram fails, so it can be wired into a pre-commit hook.

Note: it strips leading `> ` before parsing, because a fenced block inside a
blockquote (the "In practice" / "Going deeper" boxes) carries the quote marker in
the raw text but not by the time a Markdown renderer reaches it.
