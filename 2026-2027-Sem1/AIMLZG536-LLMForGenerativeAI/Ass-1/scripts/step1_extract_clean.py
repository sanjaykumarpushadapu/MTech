"""
Assignment 1A - Step 1: Data Collection, Extraction & Cleaning  [2 marks]

Extracts text page-by-page from every PDF in RAW_PDF_DIR, writes one .txt per
document to OUT_DIR, then applies the cleaning pipeline the brief asks for and
reports document counts before and after each stage.

Domain-agnostic: it processes whatever PDFs you put in RAW_PDF_DIR, so it runs
before the group has settled on a variant or a model.

    pip install pypdf langdetect
    python step1_extract_clean.py

Outputs
    domain_corpus/*.txt      cleaned documents  (submission deliverable)
    cleaning_stats.json      counts per stage   (Step 1 report)
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

# --------------------------------------------------------------------------
# Config - the only part you edit
# --------------------------------------------------------------------------
RAW_PDF_DIR = Path("raw_pdfs")
OUT_DIR = Path("domain_corpus")
STATS_PATH = Path("cleaning_stats.json")

MIN_CHARS = 1_000        # length filter: drop documents shorter than this
NEAR_DUP_THRESHOLD = 0.85  # Jaccard similarity above which two docs are duplicates
SHINGLE_SIZE = 5           # words per shingle for near-duplicate detection
LANGUAGE = "en"            # language filter: keep only this language
BOILERPLATE_PAGE_RATIO = 0.6  # a line on >=60% of pages is a header/footer

SEED = 42


# --------------------------------------------------------------------------
# Stage tracking - every filter records its before/after count automatically
# --------------------------------------------------------------------------
class Pipeline:
    """Runs filters over a {name: text} mapping and records counts per stage."""

    def __init__(self, docs: dict[str, str]):
        self.docs = docs
        self.stages: list[dict] = [{"stage": "raw extraction", "documents": len(docs), "removed": 0}]

    def apply(self, name: str, keep_fn) -> None:
        before = len(self.docs)
        self.docs = {k: v for k, v in self.docs.items() if keep_fn(k, v)}
        self.stages.append(
            {"stage": name, "documents": len(self.docs), "removed": before - len(self.docs)}
        )

    def replace(self, name: str, map_fn) -> None:
        """A transform rather than a filter - count is unchanged but recorded."""
        self.docs = {k: map_fn(v) for k, v in self.docs.items()}
        self.stages.append({"stage": name, "documents": len(self.docs), "removed": 0})

    def biggest_impact(self) -> dict:
        return max(self.stages[1:], key=lambda s: s["removed"], default=self.stages[0])


# --------------------------------------------------------------------------
# Extraction - page by page, as the brief specifies
# --------------------------------------------------------------------------
def extract_pages(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception as exc:  # a single corrupt page must not kill the run
            print(f"  ! {pdf_path.name}: page skipped ({exc})")
            pages.append("")
    return pages


def strip_boilerplate(pages: list[str]) -> str:
    """Drop lines repeated across most pages - running headers and footers.

    This is the extra cleaning step the brief invites ("not confined to the
    following"). Headers, footers and page numbers repeat on nearly every page
    and add nothing the model should learn, so removing them raises the signal
    density of the corpus without discarding any real content.
    """
    if not pages:
        return ""

    line_pages = Counter()
    for page in pages:
        for line in {ln.strip() for ln in page.splitlines() if ln.strip()}:
            line_pages[line] += 1

    cutoff = max(2, int(len(pages) * BOILERPLATE_PAGE_RATIO))
    boilerplate = {line for line, n in line_pages.items() if n >= cutoff}

    kept = []
    for page in pages:
        for line in page.splitlines():
            if line.strip() and line.strip() not in boilerplate:
                kept.append(line.strip())
    return "\n".join(kept)


def normalise(text: str) -> str:
    text = text.replace("­", "")           # soft hyphens from PDF layout
    text = re.sub(r"-\n(?=\w)", "", text)        # de-hyphenate across line breaks
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# --------------------------------------------------------------------------
# Filters
# --------------------------------------------------------------------------
def shingles(text: str, size: int = SHINGLE_SIZE) -> set[str]:
    words = text.split()
    return {" ".join(words[i : i + size]) for i in range(max(0, len(words) - size + 1))}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def find_duplicates(docs: dict[str, str]) -> set[str]:
    """Exact duplicates by hash, then near-duplicates by shingle overlap."""
    drop: set[str] = set()

    seen_hash: dict[str, str] = {}
    for name, text in docs.items():
        digest = hashlib.sha256(" ".join(text.split()).encode()).hexdigest()
        if digest in seen_hash:
            drop.add(name)
        else:
            seen_hash[digest] = name

    remaining = [n for n in docs if n not in drop]
    sigs = {n: shingles(docs[n]) for n in remaining}
    for i, a in enumerate(remaining):
        if a in drop:
            continue
        for b in remaining[i + 1 :]:
            if b in drop:
                continue
            if jaccard(sigs[a], sigs[b]) >= NEAR_DUP_THRESHOLD:
                drop.add(b)  # keep the first occurrence
    return drop


def detect_language(text: str) -> str:
    from langdetect import DetectorFactory, LangDetectException, detect

    DetectorFactory.seed = SEED  # langdetect is non-deterministic without this
    try:
        return detect(text[:5_000])
    except LangDetectException:
        return "unknown"


# --------------------------------------------------------------------------
def main() -> None:
    pdfs = sorted(RAW_PDF_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {RAW_PDF_DIR.resolve()} - download the corpus first.")

    print(f"Extracting {len(pdfs)} PDFs page-by-page ...")
    docs: dict[str, str] = {}
    page_counts: dict[str, int] = {}
    for pdf in pdfs:
        pages = extract_pages(pdf)
        page_counts[pdf.stem] = len(pages)
        docs[pdf.stem] = normalise(strip_boilerplate(pages))
        print(f"  {pdf.name}: {len(pages)} pages -> {len(docs[pdf.stem]):,} chars")

    pipe = Pipeline(docs)
    pipe.stages[0]["stage"] = "raw extraction (page-by-page)"

    # 1. length filter
    pipe.apply(f"length filter (>= {MIN_CHARS} chars)", lambda _, t: len(t) >= MIN_CHARS)

    # 2. deduplication
    dupes = find_duplicates(pipe.docs)
    pipe.apply("deduplication (exact + near)", lambda name, _: name not in dupes)

    # 3. language filter
    langs = {name: detect_language(text) for name, text in pipe.docs.items()}
    pipe.apply(f"language filter (keep '{LANGUAGE}')", lambda name, _: langs[name] == LANGUAGE)

    # write the cleaned corpus
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, text in pipe.docs.items():
        (OUT_DIR / f"{name}.txt").write_text(text, encoding="utf-8")

    total_chars = sum(len(t) for t in pipe.docs.values())
    top = pipe.biggest_impact()
    stats = {
        "stages": pipe.stages,
        "greatest_impact_stage": top["stage"],
        "greatest_impact_removed": top["removed"],
        "final_documents": len(pipe.docs),
        "total_characters": total_chars,
        "total_pages_extracted": sum(page_counts.values()),
        "config": {
            "min_chars": MIN_CHARS,
            "near_dup_threshold": NEAR_DUP_THRESHOLD,
            "language": LANGUAGE,
            "boilerplate_page_ratio": BOILERPLATE_PAGE_RATIO,
        },
    }
    STATS_PATH.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    # --- the Step 1 report -------------------------------------------------
    print("\n" + "=" * 62)
    print("STEP 1 REPORT - document counts before and after each stage")
    print("=" * 62)
    print(f"{'stage':<40}{'docs':>7}{'removed':>10}")
    print("-" * 62)
    for s in pipe.stages:
        print(f"{s['stage']:<40}{s['documents']:>7}{s['removed']:>10}")
    print("-" * 62)
    print(f"\nGreatest impact: {top['stage']} (removed {top['removed']})")
    print(f"Final corpus:    {len(pipe.docs)} documents, {total_chars:,} characters")
    print(f"Written to:      {OUT_DIR}/  and  {STATS_PATH}")
    print("\nNow write the inference: WHY did that stage dominate for this domain?")


if __name__ == "__main__":
    main()
