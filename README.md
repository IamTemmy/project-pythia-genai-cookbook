# Project Pythia: Generative AI Cookbook

A practical, notebook-driven cookbook for building, evaluating, and shipping generative AI features.

**This repo includes:** runnable tiny-model examples, a mini TF‑IDF RAG demo, and **GitHub Pages** workflow to publish the Jupyter Book.

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

Open `notebooks/00_quickstart.ipynb` and run it.
Then build the site: `jupyter-book build docs/`

### Enable GitHub Pages
1. Push to `main`.
2. In **Settings → Pages**, set **Source: GitHub Actions** (the workflow is in `.github/workflows/pages.yml`).

Generated on 2025-08-07.
