# Shared notes

Topics that appear in more than one subject. **Written once, revised many times.**

When a second course reaches a topic that already has a file here, do not write a new note. Revise this file, add a row to its "course-specific angles" table, and cross-link from the session note.

| File | Topic | First taught | Also in | Due |
|---|---|---|---|---|
| `retrieval.md` | Embeddings, ANN/HNSW, BM25, RRF | 521 S2 | 536 S12 · 549 S10–11 | 9 Aug |
| `api-design.md` | REST, OpenAPI, GraphQL, gRPC | 549 S1 | 546 S9 | 9 Aug |
| `quantization.md` | Quantization, KV-cache, inference cost | 536 S5–6 · 521 S3 | 521 S11 | 16 Aug |
| `docker-k8s.md` | Containers, Kubernetes, deployment | 549 S3 | 549 S12 · 546 S12 | 16 Aug |
| `function-calling.md` | Function calling, structured output | 521 S4 | 536 S10 · 549 S8 | 23 Aug |
| `finetuning.md` | Fine-tuning, PEFT, RLHF, DPO, GRPO | 521 S5 · 536 S7/S9 | — | 30 Aug |
| `rag.md` | Chunking, reranking, contextual, agentic RAG | 521 S7–8 | 536 S12 · 549 S10–11 · 546 S6 | 13 Sep |
| `ml-lifecycle.md` | Pipelines, MLOps, monitoring, drift | 549 S4–7 | 546 S1–2/S13 | 20 Sep |
| `evaluation.md` | Metrics, LLM-as-judge, benchmarks | 521 S10 | 536 S14 · 546 S10–11 · 549 S11 | 4 Oct |
| `agents.md` | Planning, memory, multi-agent, MCP, A2A | 521 S1/6/9/13/14 | 536 S13 · 546 S15–16 | running |

## Exam scope differs by course — this is the trap

The same topic can be **closed-book scope in one subject and open-book-only in another**. Record it per course inside each file.

The sharp case is RAG and retrieval: **closed book** for 521 (sessions 1–8, mid-sem on ~19–20 Sep), but **open book only** for 536, 549 and 546. So you must be able to reproduce RAG from memory in September, even though every other course lets you look it up in December.

Same shape for quantization and KV-cache: closed book for both 536 (S5–6) and 521 (S3).

## The payoff

Ten shared files cover material that would otherwise be written 24 times across four subjects. Getting these right in August and September is what makes October and November survivable.

> ⚠️ Note: `agents.md` here is a **study note about AI agents**. It is unrelated to `/AGENTS.md` at the repo root, which is the working-rules file for AI coding agents.
