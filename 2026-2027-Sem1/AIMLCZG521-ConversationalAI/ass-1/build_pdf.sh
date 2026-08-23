#!/usr/bin/env bash
# Builds PS2_Group129.pdf from the executed notebook, in a more compact
# layout than plain `jupyter nbconvert --to pdf` (code inputs excluded, 10pt
# font, 0.75in margins). The report keeps markdown, tables, figures, and
# saved outputs while omitting repeated source code, which keeps the PDF under
# the assignment's 30-page report cap. Requires: run all cells in Jupyter first (outputs must
# be saved in the .ipynb), a LaTeX install (TeX Live / MacTeX with xelatex),
# and `pip install nbconvert`.
#
# Usage: ./build_pdf.sh
set -euo pipefail
cd "$(dirname "$0")"

NB="PS2_Group129.ipynb"
WORK="$(mktemp -d)"

jupyter nbconvert --to latex "$NB" --TemplateExporter.exclude_input=True --output notebook --output-dir "$WORK"

python3 - "$WORK/notebook.tex" <<'PYEOF'
import sys
path = sys.argv[1]
src = open(path, encoding="utf-8").read()

src = src.replace(r"\documentclass[11pt]{article}", r"\documentclass[10pt]{article}")
src = src.replace(
    r"\geometry{verbose,tmargin=1in,bmargin=1in,lmargin=1in,rmargin=1in}",
    r"\geometry{verbose,tmargin=0.75in,bmargin=0.75in,lmargin=0.75in,rmargin=0.75in}",
)

# Shrink syntax-highlighted code blocks.
old_hl = "\\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\\\\{\\}}"
new_hl = "\\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\\\\{\\},fontsize=\\small}"
assert old_hl in src, "Highlighting environment definition not found -- nbconvert template may have changed"
src = src.replace(old_hl, new_hl)

# Shrink plain output/verbatim blocks (print statements, tracebacks, etc.).
old_v = r"\begin{Verbatim}[commandchars=\\\{\}]"
new_v = r"\begin{Verbatim}[commandchars=\\\{\},fontsize=\small]"
n = src.count(old_v)
src = src.replace(old_v, new_v)
print(f"[build_pdf] patched {n} plain Verbatim blocks")

open(path, "w", encoding="utf-8").write(src)
PYEOF

cd "$WORK"
xelatex -interaction=nonstopmode notebook.tex >/dev/null
xelatex -interaction=nonstopmode notebook.tex >/dev/null

cp notebook.pdf "$OLDPWD/PS2_Group129.pdf"
cd "$OLDPWD"
rm -rf "$WORK"

PAGES=$(python3 -c "
from pypdf import PdfReader
print(len(PdfReader('PS2_Group129.pdf').pages))
" 2>/dev/null || echo "?")

echo "Done: PS2_Group129.pdf ($PAGES pages)"
