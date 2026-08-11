# 521 · Lab 1 — Tokenization and an AI bot with tool calling

Instructor-supplied notebooks from session 1 (26 Jul 2026), shared via OneDrive.

| File | What it does |
|---|---|
| `byte_pair_encoding.ipynb` | 25 cells. Builds BPE from scratch on a tiny corpus, applies learned merges to new words, then compares with Hugging Face tokenizers and the GPT-2 tokenizer |
| `LocalGPT.ipynb` | 7 cells (2 code). Minimal local chat loop over Ollama `gemma3:1b`. Proves the local model works before anything else is attempted |
| `tavily_weather_agent.ipynb` | 20 cells (8 code). The full **weather agent** demo from deck slide 47 — the five-stage build |

## BPE notebook

Run `byte_pair_encoding.ipynb` before the agent notebooks. It makes the tokenization section concrete:

| Notebook step | What it proves |
|---|---|
| Start from characters | BPE does not need every full word in the vocabulary |
| Count adjacent pairs | The merge decision is frequency-driven, not semantic |
| First merge `("u", "g") -> "ug"` | Frequent chunks become reusable subword tokens |
| Encode `bug` as `["b", "ug"]` | A new word can be represented if its pieces are known |
| Encode `mug` as `["[UNK]", "ug"]` | Character-level BPE still fails if a character was absent from the base vocabulary |
| Inspect GPT-2 tokenization | Production tokenizers use large learned vocabularies and byte-level fallbacks |

## The stack she chose, and why it matters

**Everything runs locally and free.** No OpenAI key required.

| Component | Choice |
|---|---|
| LLM | **Ollama** running `llama3` locally (`ollama pull llama3`) — *"Nothing here is sent to any paid API"* |
| Search tool | **Tavily** — free tier, needs a `tvly-…` key |
| Framework | LangChain — `langchain`, `langchain-community`, `langchain-ollama` |
| Agent type | **`AgentType.ZERO_SHOT_REACT_DESCRIPTION`** — the ReAct loop from S4, already in use at S1 |
| Secrets | `python-dotenv` + `getpass` |

⚠️ **This differs from the deck.** Slide 47 describes the demo using the *native OpenAI API*; the notebook uses **Ollama + LangChain**. Follow the notebook — it's what she actually ran.

## The five-stage build (deck slide 47, realised in the notebook)

Cell numbers below are the **code** cells; each links back to the note section it demonstrates (note → cell map lives in the note's *Lab / build* section).

1. **Baseline** — Step 4, cell 10: LLM connected, no tools yet, so the limitation is visible first → note **Transformers & LLMs — the brain of modern conversational AI** (*"LLMs can't take actions"*)
2. **Tool definition** — Step 5, cell 12: `@tool def get_weather(city: str)`; the **docstring is the tool description the LLM reads** → note **Protocol landscape** (the ACI point)
3. **Tool selection** — Step 6, cell 14: `initialize_agent(..., verbose=True)` — the model picks the path → note **Workflows vs agents — and when not to build one** and **The seven-stage agent lifecycle**
4. **Execution** — Step 7, cells 16–17: Tokyo, then a two-city comparison → note **The seven-stage agent lifecycle** (tool invocation)
5. **Response generation** — the agent turns raw search output into prose → note **The seven-stage agent lifecycle** (response stage)

**`verbose=True` is the point of the lab.** It prints the agent's thoughts and tool choices — the ReAct loop made visible. Don't turn it off.

## Prerequisites (Step 0)

1. Free **Tavily** key from https://tavily.com
2. **Ollama** from https://ollama.com, then `ollama pull llama3` (a few GB, one-time). Keep it running.
3. Never paste the key into the notebook — use a `.env` file. *"If you paste your API key directly into a notebook, it's easy to accidentally share it."*

🔴 `.env` and `*.key` are gitignored. **Never commit a Tavily key.**

## Notes

- `LocalGPT.ipynb` uses `gemma3:1b` (much smaller); the agent notebook uses `llama3`. Pull both, or edit the model name.
- Troubleshooting from the notebook: `Connection refused` means Ollama isn't running or `ollama pull llama3` was never run.
- 536 Lab 1 is *also* tokenization, but this lab README is self-contained so it can be used without `_shared/`.

## Status

☐ `byte_pair_encoding.ipynb` runs · ☐ first BPE merge verified · ☐ GPT-2 tokenizer inspected · ☐ Ollama installed · ☐ `llama3` pulled · ☐ Tavily key in `.env` · ☐ `LocalGPT.ipynb` runs · ☐ agent answers the Tokyo question · ☐ ReAct trace observed in verbose output
