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
| **WP0** | Scaffold + tested skeleton pipeline | Repo, env, modules, tests, synthetic fixture | 1 | ✅ done | — |
| **WP1** | **Literature data extraction** | Real curated dataset (≥150 floor, ~300 target), provenance + quality tiers | 1 | 🟡 **in progress** — source pool built (71 in-scope studies), extraction sheet schema-locked, 16 seed rows | WP0 |
| **WP2** | Modeling + leakage-controlled CV | Comparative models, GroupKFold/LOSO, optimism gap | 1 | ⏳ skeleton done; rerun on real data | WP1 |
| **WP3** | Explainability (SHAP + ALE) | SHAP main+interaction, ALE, permutation, stability | 1 | ⏳ skeleton done; rerun on real data | WP2 |
| **WP4** | Physical validation | Arrhenius Eₐ per `system_class` (P1); SCM regime switch + consistency metric (P2) | 1 / 2 | ⏳ Arrhenius live; SCM/consistency stubbed | WP3 |
| **WP5** | Figures | fig1–fig4 + supporting (CV-gap, calibration) | 1 (+P2 parts) | ⛔ deferred (placeholders only) | WP3, WP4 |
| **WP6** | Paper | IJHE manuscript from results | 1+2 | ⛔ not started (skeleton only) | WP4, WP5 |

Phase tags follow the design spec. Phase 2 items (max_rate/t80 targets, SCM regime switch,
consistency metric, rate–yield map) are present as **reserved columns / tested stubs**, not
implemented.

## Where we are / what's next

**Done:** concept foundation · design spec · implementation plan · **WP0 scaffold** (tested,
end-to-end on synthetic fixture) · GitHub push · **WP1 step 1–3** (screened source pool of 71
in-scope studies, schema-locked extraction sheet, 16 seed rows). WP1 artifacts live under
`data/wp1/` — see `data/wp1/WP1_PROGRESS_AND_CLI_HANDOFF.md`.

**In progress → WP1 condition-level extraction.** The pipeline still runs on
`data/curated/fixture_v0.csv` (synthetic placeholder); the real dataset is being built in
`data/wp1/AIH2_WP1_extraction_sheet.xlsx`. When extracted rows reach ≥150 (target ~300), the
curated file is written to `data/curated/`, the Hydra `data.path` is pointed at it, and the
pipeline reruns to produce real results (including a meaningful optimism gap) — no code changes.

**Open WP1 items (from the handoff):** replace `study_id` citekeys with confirmed DOIs;
seed rows are tier-C abstract-level (need PDFs + WebPlotDigitizer for condition-level rows);
review `buryakov2024` (`water_type=sea` proxy for AlCl₃ saline); keep only alkaline/neutral
rows of `yang2018` (drop acid-media rows).

> **Important — scaffold done ≠ paper ready.** Phase 1 is the skeleton on a synthetic fixture.
> A submission-ready manuscript requires **Phase 1 + core Phase 2** (shrinking-core regime-switch
> analysis + SHAP↔physics consistency metric). See design spec §5.

## Data & code availability

- **Code:** MIT License (`LICENSE`).
- **Dataset:** CC-BY-4.0 (separate from code).
- **Archival:** versioned Zenodo release (DOI) — *pending, added after WP1*.
- **Note:** `data/curated/fixture_v0.csv` is synthetic and will be replaced by the real
  extracted dataset.
