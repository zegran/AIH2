# RQ-answering evidence — first real-data analysis (2026-06-16)

Dataset: `data/curated/aih2_v1.csv` (315 rows, 31 studies, QC'd, class-verified). Model:
random_forest (most robust under grouped CV). All numbers single-seed unless noted — **multi-seed
CIs still pending** (reporting-standard gap, see Caveats).

## Research question
Do the apparent literature contradictions reflect **real physical parameter interactions**, or are
they **artifacts of isolated cross-study conditions**? Can explainable ML unify the scattered
literature to make this distinction and reveal the true relative parameter hierarchy?

## Evidence

### 1. Naive pooling fails — and it is not a one-study artifact (leakage precondition)
Random-split CV looks decent (tree R² ≈ 0.55–0.57) but **study-grouped CV collapses to R² < 0**
(optimism gap 0.62–0.85). Removing the dominant study (porciuncula, 38% of rows) **does not rescue
it** (gap still 0.48–0.73; grouped R² still < 0). → You genuinely cannot pool the literature naively;
random CV massively overstates generalization. This is the methodological precondition, **not** the
answer to the distinction question (a negative grouped R² is by itself ambiguous between "artifact"
and "insufficient data").

### 2. Regime-conditioning RESOLVES the contradiction (the distinction answer) ⭐
Within-class grouped CV (predict held-out studies **within one system_class**), random_forest:

| scope | studies | rows | grouped R² |
|---|---|---|---|
| GLOBAL (all classes pooled) | 31 | 315 | **−0.058** |
| pure_al_alkali | 9 | 162 | **+0.581** |
| liquid_metal_activated | 5 | 19 | +0.069 |
| mechanically_activated | 6 | 69 | −0.237 |
| waste_al | 8 | 20 | −0.244 |
| al_alloy | 3 | 45 | −1.798 |

In the **best-powered regime (pure_al_alkali, 9 independent studies)**, cross-study prediction
**works** (R²=+0.58) — whereas pooling all regimes destroys it (−0.06). This is the signature that
the apparent contradictions are **regime-moderated REAL interactions**, not cross-study noise: within
one physical regime the parameter→yield map is consistent across independent labs; mixing regimes is
what manufactures the "contradiction." **The answer quality tracks statistical power**: classes with
3–8 studies are underpowered/inconclusive (small n), so this is established for pure_al_alkali and
remains open for the thin classes.

### 3. The parameter hierarchy is moderately stable (the hierarchy claim)
SHAP importance ranking aggregated to original features, mean pairwise Spearman across grouped folds:
**0.66 / 0.68 / 0.70** (seeds 0 / 42 / 7). → Despite poor *predictive* R² across regimes, the
*relative* parameter hierarchy is moderately stable, so a relative hierarchy claim is defensible
(moderate, not strong). Caveat: in-sample permutation importance ranked particle_size #1, but
particle_size is present in only 19% of rows and partly proxies study identity — the grouped-fold
SHAP version is the trustworthy one.

### 4. Coverage honesty (fitness of the data for each leg of the RQ)
Per-class non-null coverage of the contradiction variables:

| class | particle_size | temperature | alkali_conc |
|---|---|---|---|
| pure_al_alkali | 25% (7 studies, 3 vary) | 100% | 91% |
| al_alloy | **0%** | 100% | 100% |
| mechanically | **0%** | 86% | 94% |
| liquid_metal | 63% (1 vary) | 100% | 68% |
| waste_al | 35% (1 vary) | 70% | 70% |

- **temperature / alkali_conc / composition (wt%): well-covered** across classes → the parameter
  hierarchy + temperature and concentration effects are well-supported.
- **particle_size: thin** — only 19% of rows (59/315), 5 studies vary it, **2 classes have none**.
  The particle-size-specific cross-class sign-flip is underpowered as a *headline*.

## Verdict
The RQ **is answerable with this data**, and the data **is paper-fit** — provided the headline is
framed on what the data supports:
- **Headline = regime-moderation + leakage:** apparent contradictions dissolve once you condition on
  `system_class` and control study leakage; pure_al_alkali is the flagship regime (within-regime
  cross-study R²=0.58). This directly answers the distinction question.
- **Relative hierarchy:** defensible at moderate stability (~0.68), strongest on the well-covered
  axes (temperature, alkali_conc, composition).
- **Particle_size:** a *supporting / exploratory* contradiction where data permits, **not** the sole
  headline (too thin; 2 classes empty).

## Caveats / open items (reporting standard)
- Single-seed point estimates — **multi-seed CIs required** before any claim is final.
- 4 of 5 classes are small-study (3–8) → within-class results there are indicative, not conclusive.
- **Arrhenius Eₐ validation needs RATE data** (Phase 2; `max_rate_ml_min_g`/`t80_min` currently blank).
  Physics validation from yield alone is a crude proxy only.
- Group-weighting (1/n_rows per study) not yet applied; ALE sign-by-class figures not yet generated.

## Next
group-weighting + multi-seed CIs · SHAP/ALE sign-by-class figures (the contradiction visual) ·
decide whether to boost thin classes (figure digitization) to extend result 2 beyond pure_al_alkali.
