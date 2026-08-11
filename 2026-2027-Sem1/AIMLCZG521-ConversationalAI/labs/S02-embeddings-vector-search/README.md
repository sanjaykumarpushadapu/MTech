# 521 · Lab 2 — Embeddings and contextual vectors

Instructor-supplied notebook currently held for Session 2.

| File | What it does |
|---|---|
| `Embedding-distilbert.ipynb` | Loads `distilbert-base-uncased`, inspects model specs, extracts contextual token embeddings, and compares `bank` in river vs finance contexts using cosine similarity |

## What the notebook proves

| Idea | What to notice |
|---|---|
| DistilBERT is an encoder-only model | It is built for understanding and representation, not text generation |
| Token embeddings become contextual embeddings | The final vector for a word changes after self-attention mixes in surrounding words |
| The same word can mean different things | `bank` near `river` and `bank` near `account` are no longer treated as one fixed meaning |
| Cosine similarity is a quick diagnostic | It shows whether two vectors still point in similar semantic directions |

## Note map

| Notebook idea | Read in the note |
|---|---|
| Encoder-only model for representation | `notes/S02-retrieval.md` · section 2 |
| Static vs contextual embeddings | `notes/S02-retrieval.md` · section 2 |
| Self-attention creates context-aware vectors | `notes/S02-retrieval.md` · sections 2 and 4 |
| Cosine similarity interpretation | `notes/S02-retrieval.md` · section 8 |

## Run checklist

1. Install `transformers`, `torch`, `numpy`, and `scikit-learn`.
2. Run the model-load cell for `distilbert-base-uncased`.
3. Run the river-bank and finance-bank examples.
4. Compare the cosine score with the interpretation table in the notebook.
5. Write one sentence explaining why the final vector changed.

## Remaining Lab 2 scope

The held notebook covers embeddings, contextual vectors, and cosine similarity. The handout lab row also names text-to-speech, rule-based systems, and sentiment analysis. Keep those as open until the instructor shares files for them or confirms they are not part of this offering's Lab 2 package.
