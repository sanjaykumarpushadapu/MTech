# 536 · Lab environment

Environment support files for the 536 notebooks. This is setup material, not a numbered teaching lab.

| File | Purpose |
|---|---|
| `setup_env.sh` | Creates the persistent Kubeflow/NFS virtual environment and installs the pinned LLM baseline |
| `check_env.py` | Checks the interpreter, package versions, CUDA, and 4-bit support |

Run both commands from this directory on the notebook data volume:

```bash
bash ./setup_env.sh
./venv/bin/python ./check_env.py
```

The generated `venv/` and `llm_baseline_requirements.txt` are local environment artifacts and are not committed.
