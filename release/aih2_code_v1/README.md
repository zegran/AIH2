# AIH2 Analysis Code — v1

Reproducible analysis pipeline for:
**"Apparent Contradictions in the Aluminum–Water Hydrolysis Literature are Predominantly Methodological"**

## Contents

- `src/` — Python source package (ML models, variance decomposition, figures)
- `run/` — Hydra-configured experiment entrypoints and configs
- `tools/` — Utility scripts (compliance gate, lint, BibTeX fetch)

## Requirements

Python ≥ 3.10; dependencies managed with `uv`:

```bash
uv sync
```

## Reproducing the main results

```bash
# Variance decomposition (T_B)
uv run python3 src/analysis/figures/wp5_figures.py

# Leakage-controlled CV (requires data/curated/aih2_v1.csv)
uv run python3 run/pipeline/run_phase1.py
```

The curated dataset (`data/curated/aih2_v1.csv`, 315 yield rows from 31 studies)
is released separately at https://doi.org/10.5281/zenodo.20750297 (CC-BY-4.0).

## License

MIT — see LICENSE
