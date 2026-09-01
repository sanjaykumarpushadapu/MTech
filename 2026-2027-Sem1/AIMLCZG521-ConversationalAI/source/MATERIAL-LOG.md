# AIMLC ZG521 · Conversational AI · Material Log

**Last reconciled:** 01 Sep 2026
**Path convention:** paths below are relative to this subject folder.

This is the canonical subject-level ledger for material availability, scope checks, durable outputs, and active gaps. Keep detailed audit prose in Git history; do not append a new recheck block here for every pass.

Legend: `✓` complete · `partial` incomplete · `✗` missing · `—` not applicable.

## Current source state

| Item | Current status |
|---|---|
| Handout | Historically checked against L1–L3. The matching April 2026 handout was found in the user's external course folder, but the repository `_handouts/` copy is absent. Reattach or restore the path before the next scope-changing update. |
| Raw decks, recordings, transcripts, notebooks | External or ignored inputs; no raw course material belongs in Git. |
| Canonical outputs | Session notes in `notes/`, lab READMEs/code in `labs/`, and this material ledger. |

## Session material status

| Contact session | Handout map / topic | Material held | Durable output | Current gap |
|---|---|---|---|---|
| S01 | L1 · Foundations of Conversational AI | ✓ Foundations deck; transcript; Lab 1 notebooks; public agent paper | ✓ `notes/S01-foundations.md`; `labs/S01-tokenization-and-tool-calling/README.md` | none known |
| S02 | L2 · Embeddings & Vector Search | ✓ Embeddings deck; DistilBERT notebook; DPR paper | ✓ `notes/S02-retrieval.md` | Lab 2 still lacks text-to-speech, rule-based-systems, and sentiment-analysis confirmation/files |
| S03 | L2 · ANN Search & Hybrid Retrieval | ✓ ANN/hybrid deck, 62 slides | ✓ `notes/S03-ann-hybrid-retrieval.md` | Hybrid-search lab code remains open |
| S04 | L3 · Model Landscape & Cost Engineering | ✓ Model-landscape deck, 39 slides; QLoRA paper knowledge | ✓ `notes/S04-model-landscape.md` | none known |
| S05–S16 | Remaining handout topics | ✗ decks not held | ☐ no notes yet | collect each deck before writing |

## Lab status

| Lab | Status |
|---|---|
| 1 · Tokenization and tool calling | ✓ notebooks held; README maps the runnable material |
| 2 · Similarity, text-to-speech, rule-based systems, sentiment | `partial`; only embeddings/similarity is confirmed |
| 3 · Hybrid search | `partial`; deck is processed, runnable lab code is still missing |
| 4–10 | ✗ later material not held |

## Public references

521 has no textbook requirement; fetch public papers/specifications when a session needs them.

| Reference | Session | Status |
|---|---|---|
| *The Landscape of AI Agents* | S01 | ✓ processed |
| *Dense Passage Retrieval* | S02/S03 | ✓ processed/logged |
| *QLoRA* | S04 | ✓ deck-aligned knowledge used; full arXiv text fetch remains optional |
| ReAct, DPO, MemGPT, contextual retrieval, MetaGPT, MCP, A2A, governance sources | S05+ | later |

## Durable decisions

- 521 filenames follow instructor contact sessions: **S01=L1, S02=L2 embeddings, S03=L2 ANN/hybrid, S04=L3**. Handout L-numbers remain the scope mapping.
- The S03 deck audit checked all **62** source slides; the S04 deck audit checked all **39**. Coverage passed for both notes using temporary working inventories, which are not retained.
- Title/logistics/recap/reference slides were checked and routed to the master where appropriate; substantive content belongs in the session note.

## Storage rule

Recordings, decks, transcripts, and raw PDFs stay outside Git or in ignored source folders. The durable record is the note or lab README, not the raw input.
