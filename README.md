# AIH2 — Interpretable ML for the Aluminum–Water Reaction (H₂ Production)

Physics-validated, interpretable machine learning that **resolves contradictory parameter
effects** in the aluminum–water hydrolysis literature for hydrogen production.

- **Concept foundation (immutable core):** [`plan/2026-06-14-aih2-concept-foundation.md`](plan/2026-06-14-aih2-concept-foundation.md)
- **Design spec:** [`plan/2026-06-14-aih2-design-spec.md`](plan/2026-06-14-aih2-design-spec.md)
- **Implementation plan:** [`plan/2026-06-14-aih2-phase1-implementation-plan.md`](plan/2026-06-14-aih2-phase1-implementation-plan.md)
- **Target venue:** International Journal of Hydrogen Energy (IJHE) → fallback *Energy and AI*.

## Central thesis

The Al–water hydrolysis literature is **internally contradictory** about how parameters control
H₂ yield (direction-changing particle-size effect; activation energies spanning ~3.5–102.6
kJ/mol; an inconsistent rate–yield trade-off; disagreement on which parameter dominates). These
contradictions stem from **isolated, non-standardized per-study conditions**. This is treated as
an **unsolved scientific problem (significance)**, not a missing combination (novelty).

## Research question

Do these contradictions reflect **genuine physical parameter interactions**, or are they
**artifacts of isolated study windows**? Can interpretable ML on a **unified, provenance-tracked
dataset** separate the two and recover the true parameter hierarchy?

**Hypotheses:** H1 — the particle-size sign flip is a shrinking-core regime switch
(`particle_size × {temperature, alkalinity}` SHAP interaction). H2 — contradictions are largely
explained by `system_class` + data-quality covariates. H3 — learned temperature sensitivity
yields Arrhenius-consistent Eₐ in the 3.5–102.6 kJ/mol band per `system_class`.

## Quickstart

```bash
uv sync
uv run pytest                              # run the test suite
uv run python -m run.pipeline.run_phase1   # end-to-end pipeline on the synthetic fixture
```

Outputs land in `results/metrics/cv_metrics.csv` (random-vs-grouped optimism gap) and
`results/tables/permutation_importance.csv`.

## Repository map

```
plan/      concept foundation, design spec, implementation plan
src/       data_module, cv, model_module, analysis/{xai,physical_validation}
run/       Hydra config + pipeline entry point
data/      raw/ (gitignored), curated/ (versioned), data_dictionary.md
results/   metrics, tables, figures (figures deferred)
paper/     elsarticle-ready LaTeX skeleton
vault/     Obsidian knowledge base (concept foundation, daily notes)
tests/     mirrors src/
```

---

## Work breakdown (WBS)

| WP | Goal | Output | Phase | Status | Depends on |
|----|------|--------|-------|--------|-----------|
| **WP0** | Scaffold + tested skeleton pipeline | Repo, env, modules, tests, synthetic fixture | 1 | ✅ done (28 tests pass) | — |
| **WP1** | **Literature data extraction** | Real curated dataset (≥150 floor, ~300 target), provenance + quality tiers | 1 | ✅ **done** — `data/curated/aih2_v1.csv`, **315 rows / 31 studies**, validator PASS (floor met). **QC: 0% value error** (double-extraction) + classification audit (31/31). 3 classes ≥40, 2 exploratory | WP0 |
| **WP2** | Modeling + leakage-controlled CV | Comparative models, GroupKFold/LOSO, optimism gap | 1 | ✅ **done (real data)** — optimism gap **0.62–0.85** (robust to dropping the dominant study); within-`system_class` grouped R² **+0.58** (pure_al_alkali) vs global −0.06 | WP1 |
| **WP3** | Explainability (SHAP + ALE) | SHAP main+interaction, ALE, permutation, stability | 1 | 🟡 **partial** — SHAP rank stability ~0.68 + permutation importance done; ALE/SHAP sign-by-class **figures pending** | WP2 |
| **WP4** | Physical validation | Arrhenius Eₐ per `system_class` (P1); SCM regime switch + consistency metric (P2) | 1 / 2 | 🔴 **blocked** — rigorous Arrhenius needs **rate data** (`max_rate`/`t80`, Phase 2, currently blank); SCM/consistency stubbed | WP3 |
| **WP5** | Figures | fig1–fig4 + supporting (CV-gap, calibration) | 1 (+P2 parts) | ⛔ deferred (placeholders only) | WP3, WP4 |
| **WP6** | Paper | IJHE manuscript from results | 1+2 | ⛔ not started (skeleton only) | WP4, WP5 |

Phase tags follow the design spec. Phase 2 items (max_rate/t80 targets, SCM regime switch,
consistency metric, rate–yield map) are present as **reserved columns / tested stubs**, not
implemented.

## Where we are / what's next

**Done:** concept foundation · design spec · implementation plan · **WP0 scaffold** (28 tests
pass) · **WP1 real dataset** (`data/curated/aih2_v1.csv`, 315 rows / 31 studies, QC'd) · **WP2
first real run** · partial **WP3**. The pipeline now defaults to the real dataset
(`run/conf/config.yaml`), with `data/curated/fixture_v0.csv` kept as a synthetic baseline.

**Key results so far** (random_forest, study-grouped CV; `results/real_v1/RQ_FINDINGS.md`):
- **Naive pooling fails (leakage):** random-split R² ≈ 0.56 collapses to grouped R² < 0
  (optimism gap 0.62–0.85), **robust to dropping the dominant study** → not a one-study artifact.
- **Regime-conditioning resolves the contradiction:** global grouped R² −0.06, but **within
  pure_al_alkali (9 studies) +0.58** → contradictions are regime-moderated *real* effects, not
  cross-study artifacts (strongest where statistical power exists). **Supports H2.**
- **Parameter hierarchy moderately stable** (~0.68 Spearman across folds) → relative hierarchy
  defensible.
- **Coverage honesty:** `particle_size` is thin (19% of rows, 2 classes empty) → the particle-size
  contradiction (H1) is underpowered; temperature / alkali / composition are well-covered.

**Methodologically correct next steps** (convergent-validity design):
1. Freeze an internal analysis protocol (primary test + falsifiable "real-vs-artifact" criteria).
2. **Mixed-effects model** (study as random effect) + study-level bootstrap CIs — the principled
   confound-separation test, complementing the ML, with multi-seed CIs.
3. **Targeted rate re-extraction** from the in-hand studies → regime-wise Arrhenius Eₐ (unblocks WP4 / H3).
4. Then WP5 figures + WP6 writing, on convergent (replication ∧ confound-survival ∧ physics) findings.

**Hypothesis scorecard:** H2 ✅ supported · H1 🟡 signal but data-thin → exploratory · H3 ⬜ pending rate data.

> **Important — scaffold done ≠ paper ready.** Phase 1 is the skeleton on a synthetic fixture.
> A submission-ready manuscript requires **Phase 1 + core Phase 2** (shrinking-core regime-switch
> analysis + SHAP↔physics consistency metric). See design spec §5.

## Data & code availability

- **Code:** MIT License (`LICENSE`).
- **Dataset:** CC-BY-4.0 (separate from code).
- **Archival:** versioned Zenodo release (DOI) — *pending, added after WP1*.
- **Real dataset:** `data/curated/aih2_v1.csv` (315 rows, schema-valid, QC'd). `fixture_v0.csv`
  is retained as the synthetic baseline/test fixture.
