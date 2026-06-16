# AIH2 — Why the Aluminum–Water Hydrolysis Literature Contradicts Itself

A leakage-controlled, provenance-tracked analysis showing that the long-documented contradictions
in the aluminum–water hydrolysis literature (for hydrogen production) are **predominantly
methodological, not physico-chemical**.

- **Headline finding (T_B):** methodological covariates explain **~55%** of the between-study yield
  variance vs **~2%** for the physical regime (`system_class`); **temperature-control method alone
  ~33%** — the single largest cross-study driver. (Associational; survives controlling for regime.)
- **Target venue:** *Energy and AI* (leakage-controlled methodology + curated open dataset).
  IJHE remains possible if the physics pillar is later strengthened — see `results/real_v1/GO_NOGO_SUMMARY.md`.
- **Paper:** first draft in `paper/` (`main.tex` + sections); status in `paper/SUBMISSION_PLAN.md`.

> **Note on the project's arc.** This started as a "physics-validated ML resolves the contradictions"
> project (H1–H3). A disciplined, pre-registered campaign (frozen thresholds, transparent nulls, no
> rescue narratives) **refuted** H1/H2/H3, and the data instead supported the **methodological-artifact**
> answer (T_B). The history is preserved in `results/real_v1/` and the design docs under `plan/`.

## Research question and what the data answered

**RQ.** Do the apparent inter-study contradictions reflect **genuine physical parameter
interactions**, or are they **artifacts of isolated, non-standardized study conditions**? Can a
unified, provenance-tracked dataset separate the two?

**Answer (associational, n≈31 studies): predominantly artifacts.** Under study-grouped CV naive
pooling fails (optimism gap 0.62–0.85); the physical regime explains almost none of the between-study
variance while methodology explains the majority; and the flagship particle-size "contradiction" is
internally consistent within studies. *Predominantly*, not *purely* — a finer particle-size kinetics
effect operates within studies (Saceleanu 2019).

## Hypothesis scorecard (honest, pre-registered)

| hypothesis | verdict | evidence |
|---|---|---|
| **H1** particle-size sign-flip = real regime switch | ❌ **refuted** | within-study sign is consistent (5/5 negative) → cross-study artifact |
| **H2** `system_class` moderates the contradiction (yield) | ❌ **refuted** | mixed-effects: main effect n.s.; 0/8 interactions survive Holm |
| **H3** Eₐ organizes by regime (Arrhenius) | ❌ **refuted** | η²=0.36, p=0.13; liquid-metal alone spans 8.5–58 kJ/mol |
| **T_A** within-study consistent / between-study contradictory | 🟡 **partial/null** | 50% variance is between-study; within-study predictability heterogeneous (median skill −0.14) |
| **T_B** methodology explains the between-study variance | ✅ **supported** | method R²=0.55 vs regime 0.02; temperature_control 0.33 (CI excludes 0) |

## Quickstart

```bash
uv sync
uv run pytest                                              # test suite (Phase-1 pipeline on the fixture)
uv run python -m run.pipeline.run_phase1                   # leakage-controlled CV (uses data/curated/aih2_v1.csv)
uv run python tools/validate_rows.py data/wp1/extraction_rows.csv      # yield-dataset validator
uv run python tools/validate_rate_rows.py data/wp1/rate_extraction.csv # kinetic-table validator
uv run python -m src.analysis.figures.wp5_figures          # regenerate the 5 paper figures
```

## Repository map

```
plan/      concept foundation, design spec, implementation plan, FROZEN analysis-protocol.md
src/       data_module, cv, model_module, analysis/{xai, physical_validation, figures}
run/       Hydra config + pipeline entry point
data/      raw/ (gitignored PDFs), curated/aih2_v1.csv (315-row yield), wp1/rate_extraction.csv (76-row kinetic)
results/   real_v1/  — all analysis verdicts (RQ, TEST1/2, H2/H3, T_A/T_B, GO_NOGO) + figures
paper/     IJHE/Energy-and-AI first draft (main.tex + sections), references.bib, SELF_REVIEW, SUBMISSION_PLAN
vault/     Obsidian knowledge base
tests/     mirrors src/ (28 tests pass)
```

## Work breakdown (WBS) — final state

| WP | Goal | Status |
|----|------|--------|
| **WP0** | Scaffold + tested pipeline | ✅ done (28 tests pass) |
| **WP1** | Curated open dataset | ✅ done — 315 yield rows / 31 studies + 76-row kinetic table; QC 0% value error; classification audit 31/31 |
| **WP2** | Leakage-controlled CV | ✅ done — optimism gap 0.62–0.85, robust |
| **WP3** | Explainability / variance analysis | ✅ done (descriptive) — variance decomposition is the headline; ML/SHAP descriptive only |
| **WP4** | Physical validation (Arrhenius) | ✅ done → **null**; Eₐ does not organize by regime (rate data extracted + fit) |
| **WP5** | Figures | ✅ done — 5 reproducible figures (`src/analysis/figures/wp5_figures.py`) |
| **WP6** | Paper | 🟡 first draft done; remaining: compile (TeX), elsarticle frontmatter, Zenodo, submission prep (`paper/SUBMISSION_PLAN.md`) |

## Key results (every number traces to `results/real_v1/`)

- **Leakage:** random-split R² ≈ 0.55 → study-grouped R² < 0 (gap 0.62–0.85); robust to dropping the
  dominant study. (`RQ_FINDINGS.md`, `TEST1_porciuncula_robustness.md`)
- **Methodology > physics:** between-study variance explained — method covariates **0.55** vs regime
  **0.02**; temperature_control **0.33** (incremental over regime +0.47, CI [0.04, 0.77]).
  (`TB_method_variance.md`, `TB_confound_check.md`)
- **Particle-size contradiction resolved:** within-study Spearman ρ negative in **5/5** studies.
  (`TA_within_study.md`)
- **No regime structure in Eₐ:** η²=0.36 (p=0.13); liquid-metal 8.5–58 kJ/mol. (`H3_arrhenius.md`)

## Data & code availability

- **Code:** MIT (`LICENSE`). **Dataset:** CC-BY-4.0 — `data/curated/aih2_v1.csv` (yield, 315 rows) +
  `data/wp1/rate_extraction.csv` (kinetic, 76 rows), provenance-tracked, QC'd.
- **Archival:** versioned Zenodo release (DOI) — *pending user mint; see `SUBMISSION_PLAN.md` WP-DATA-RELEASE*.
- Raw third-party PDFs are **not** redistributed; the dataset records DOIs so values trace to source.
