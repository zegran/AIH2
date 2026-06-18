# T_B — methodological covariates explain the between-study variance (UPSIDE)

Frozen success (`plan/analysis-protocol.md`): method covariates reduce between-study variance by an
amount whose cluster-bootstrap 95% CI excludes 0, AND that reduction ≥ the `system_class` (physical
regime) reduction. Honest reporting.

> **UPDATED 2026-06-18:** Post-IRR adjudication corrected 3 coding errors (see `paper/CHANGELOG_CRITIC_FIXES.md`).
> Numbers below are the CORRECTED post-adjudication values. Original pre-correction values are noted
> where changed. The headline direction is unchanged and strengthened.

## VERDICT: **SUPPORTED** (strongly — post-correction)
Methodological covariates explain **~72%** of between-study mean-yield variance vs **~2%** for the
physical regime — methodology, not physico-chemical regime, dominates the apparent contradictions.
*(Pre-correction: ~55% vs ~2%.)*

## T_B.0 — coverage audit (all covariates testable, post-correction)
| covariate | fill | levels | distribution |
|---|---|---|---|
| measurement_method | 89% | 5 | water_displacement 237 · other 67 · mass_flow 3 · pressure 7 · gc 1 |
| temperature_control | 100% | 2 | isothermal_bath 271 · self_heating 44 |
| vessel_type | 100% | 2 | closed 288 · open 27 |
| water_type | 97% | 4 | alkaline 142 · DI 91 · tap 72 · sea 1 |
| quality_tier | 100% | 3 | A 149 · B 95 · C 71 |

`temperature_control` now has 2 levels only (the `uncontrolled` category was eliminated: both studies
were coding errors, corrected to `isothermal_bath` during IRR adjudication).
`measurement_method` now has 5 levels (added `other` and `mass_flow` from corrections).

## T_B.1 — study-level between-study variance explained (n=31 studies, study-mean yield) — CORRECTED

| predictor of study-mean yield | R² (corrected) | cluster-boot 95% CI | R² (pre-correction) |
|---|---|---|---|
| **system_class (physical regime)** | **0.018** | [0.015, 0.373] | 0.018 (unchanged) |
| **measurement_method** | **0.425** | [0.024, 0.806] | 0.069 |
| **temperature_control** | **0.081** | [0.002, 0.240] | 0.332 |
| water_type | 0.039 | [0.006, 0.379] | 0.039 |
| quality_tier | 0.037 | [0.005, 0.327] | 0.037 |
| vessel_type | 0.019 | [0.000, 0.096] | 0.019 |
| **ALL method covariates jointly** | **0.717** | **[0.443, 1.000]** | 0.553 |

- **Method covariates jointly explain 72% of between-study variance; the physical regime explains 2%.**
  Method R² (0.717) ≥ regime R² (0.018), and the method CI **excludes 0** → both frozen conditions met.
- **`measurement_method` alone explains 43%** — hydrogen measurement apparatus is the single biggest
  cross-study driver of apparent yield differences (n=25 studies reporting apparatus details; 6 have NaN).
- **`temperature_control` explains 8%** (was 33% — TC was the old lead; correcting the 2 uncontrolled
  coding errors shifted the lead to measurement apparatus).

## Interpretation (the H_meth answer)
The apparent inter-study contradictions in Al–water hydrolysis are **dominated by methodological
heterogeneity, not physico-chemical regime.** This is the positive, quantitative answer to the
original research question: the contradictions are largely **cross-study measurement/protocol
artifacts** (chiefly hydrogen measurement apparatus choice), which is why leakage-controlled pooling
fails and why `system_class` (the physical regime) carries almost no between-study signal (consistent
with the H2/H3 nulls).

**Power note:** n=31 studies; `measurement_method` and joint-method effects are robust (CI excludes 0),
but `temperature_control` CI [0.002, 0.240] is wide and the lower bound barely excludes 0.
Individual minor covariates (vessel_type, water_type) are weak/under-powered and not over-claimed.
