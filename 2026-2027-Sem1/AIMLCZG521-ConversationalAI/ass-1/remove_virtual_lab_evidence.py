from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


REPORT = Path("PS2_Group129_Report.docx")
UPDATED_REPORT = Path("PS2_Group129_Report_updated.docx")
document = Document(REPORT)

evidence_captions = {
    "Recovered Virtual Lab evidence: Task 2 executed CPU timing and embedding-shape output.",
    "Recovered Virtual Lab evidence: Task 3 metric definitions and pair-selection setup.",
    "Recovered Virtual Lab evidence: Task 3 ranking and normalization checks (0/5 and 25/25).",
    "Recovered Virtual Lab evidence: Task 8 exact cross-model comparison over 300 queries.",
}

for paragraph in list(document.paragraphs):
    if paragraph.text in evidence_captions:
        previous = paragraph._p.getprevious()
        if previous is not None and previous.tag == qn("w:p") and previous.xpath(
            './/*[local-name()="drawing"]'
        ):
            previous.getparent().remove(previous)
        paragraph._p.getparent().remove(paragraph._p)
    elif paragraph.text == "Virtual Lab Evidence" or paragraph.text.startswith(
        "The following recovered screenshots"
    ):
        paragraph._p.getparent().remove(paragraph._p)

document.save(UPDATED_REPORT)
UPDATED_REPORT.replace(REPORT)