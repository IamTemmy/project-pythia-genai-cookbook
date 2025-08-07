# Project Pythia: Generative AI Cookbook

A practical, notebook-driven cookbook for building, evaluating, and shipping generative AI features.

## Quickstart

```bash
# Option A: Conda
conda env create -f environment.yml
conda activate pythia
python -m ipykernel install --user --name pythia --display-name "Pythia (conda)"

# Option B: venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name pythia --display-name "Pythia (venv)"
```

Open `notebooks/00_quickstart.ipynb` and run it end-to-end.

## Repo layout
See `docs/` for the Jupyter Book site sources. Use `.env` (from `.env.example`) for API keys; never commit secrets.

Generated on 2025-08-07.
