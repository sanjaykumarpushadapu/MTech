"""
Run this ONCE on a machine WITH internet (e.g. your personal laptop) to save
the two models Task 2/Task 3 need into ./models/. Then copy the whole `models`
folder to the office laptop (same location: ass-1/models/). The notebook's
resolve_model() will pick them up automatically and run offline -- no Hugging
Face download, no SSL handshake error behind the corporate proxy.

    pip install -r requirements.txt
    python download_models.py
"""
import os
from sentence_transformers import SentenceTransformer

MODELS = [
    ("distilbert-base-uncased", "models/distilbert-base-uncased"),
    ("BAAI/bge-large-en-v1.5",  "models/bge-large-en-v1.5"),
]

os.makedirs("models", exist_ok=True)
for hf_id, out_dir in MODELS:
    print(f"Downloading {hf_id} ...")
    SentenceTransformer(hf_id).save(out_dir)
    print(f"  saved to {out_dir}/")

print("\nDone. Copy the whole 'models/' folder to the office laptop's ass-1/models/.")
