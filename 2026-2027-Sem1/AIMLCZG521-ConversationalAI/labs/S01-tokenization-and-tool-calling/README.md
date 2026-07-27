# 521 · Lab 1 — Tokenization and an AI bot with tool calling

Instructor-supplied notebooks from session 1 (26 Jul 2026), shared via OneDrive.

| File | What it does |
|---|---|
| `LocalGPT.ipynb` | 2 cells. Minimal local chat loop over Ollama `gemma3:1b`. Proves the local model works before anything else is attempted |
| `tavily_weather_agent.ipynb` | 19 cells. The full **weather agent** demo from deck slide 47 — the five-stage build |

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

1. **Baseline** — cell 9: LLM with no tools, so the limitation is visible first
2. **Tool definition** — cell 11: `@tool def get_weather(city: str)`; the **docstring is the tool description the LLM reads**
3. **Tool selection** — cell 13: `initialize_agent(..., verbose=True)`
4. **Execution** — cells 15–16: Tokyo, then a two-city comparison
5. **Response generation** — the agent turns raw search output into prose

**`verbose=True` is the point of the lab.** It prints the agent's thoughts and tool choices — the ReAct loop made visible. Don't turn it off.

## Prerequisites (Step 0)

1. Free **Tavily** key from https://tavily.com
2. **Ollama** from https://ollama.com, then `ollama pull llama3` (a few GB, one-time). Keep it running.
3. Never paste the key into the notebook — use a `.env` file. *"If you paste your API key directly into a notebook, it's easy to accidentally share it."*

🔴 `.env` and `*.key` are gitignored. **Never commit a Tavily key.**

## Notes

- `LocalGPT.ipynb` uses `gemma3:1b` (much smaller); the agent notebook uses `llama3`. Pull both, or edit the model name.
- Troubleshooting from the notebook: `Connection refused` means Ollama isn't running or `ollama pull llama3` was never run.
- 536 Lab 1 is *also* tokenization. See `_shared/tokenization.md` for the script that serves both.

## Status

☐ Ollama installed · ☐ `llama3` pulled · ☐ Tavily key in `.env` · ☐ `LocalGPT.ipynb` runs · ☐ agent answers the Tokyo question · ☐ ReAct trace observed in verbose output
