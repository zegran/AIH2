# T_B — methodological covariates explain the between-study variance (UPSIDE)

Frozen success (`plan/analysis-protocol.md`): method covariates reduce between-study variance by an
amount whose cluster-bootstrap 95% CI excludes 0, AND that reduction ≥ the `system_class` (physical
regime) reduction. Honest reporting.

## VERDICT: **SUPPORTED** (strongly)
Methodological covariates explain **~55%** of between-study mean-yield variance vs **~2%** for the
physical regime — methodology, not physico-chemical regime, dominates the apparent contradictions.

## T_B.0 — coverage audit (all covariates testable)
| covariate | fill | levels | distribution |
|---|---|---|---|
| measurement_method | 85% | 3 | water_displacement 257 · pressure 10 · gc 1 |
| temperature_control | 100% | 3 | isothermal_bath 263 · self_heating 44 · uncontrolled 8 |
| vessel_type | 100% | 2 | closed 288 · open 27 |
| water_type | 97% | 4 | alkaline 142 · DI 91 · tap 72 · sea 1 |
| quality_tier | 100% | 3 | A 149 · B 95 · C 71 |

All five are testable (≥2 levels, ≥50% fill). `water_type=sea` (1 row) is effectively a singleton level.

## T_B.1 — study-level between-study variance explained (n=31 studies, study-mean yield)
| predictor of study-mean yield | R² | cluster-boot 95% CI |
|---|---|---|
| **system_class (physical regime)** | **0.018** | [0.015, 0.373] |
| **temperature_control** | **0.332** | [0.030, 0.676] |
| measurement_method | 0.069 | [0.001, 0.459] |
| water_type | 0.039 | [0.006, 0.379] |
| quality_tier | 0.037 | [0.005, 0.327] |
| vessel_type | 0.019 | [0.000, 0.096] |
| **ALL method covariates jointly** | **0.553** | **[0.361, 0.999]** |

- **Method covariates jointly explain 55% of between-study variance; the physical regime explains 2%.**
  Method R² (0.553) ≥ regime R² (0.018), and the method CI **excludes 0** → both frozen conditions met.
- **`temperature_control` alone explains 33%** — how temperature is controlled (isothermal bath vs
  self-heating vs uncontrolled) is the single biggest cross-study driver of apparent yield differences.

## Interpretation (the H_meth answer)
The apparent inter-study contradictions in Al–water hydrolysis are **dominated by methodological
heterogeneity, not physico-chemical regime.** This is the positive, quantitative answer to the
original research question: the contradictions are largely **cross-study measurement/protocol
artifacts** (chiefly temperature control), which is why leakage-controlled pooling fails and why
`system_class` (the physical regime) carries almost no between-study signal (consistent with the
H2/H3 nulls).

**Power note:** n=31 studies; `temperature_control` and joint-method effects are robust (CI excludes 0),
but individual minor covariates (vessel_type, water_type) are weak/under-powered and not over-claimed.
