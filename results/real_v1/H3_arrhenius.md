# H3 — physics validation (Arrhenius), co-primary

Two pre-registered criteria (`plan/analysis-protocol.md`). Inputs: `data/wp1/rate_extraction.csv`
(per-study representative Eₐ = median of a study's Eₐ rows) + `data/curated/aih2_v1.csv` (yield–T).
Honest reporting; null acceptable.

## VERDICT: **NOT robustly supported (PARTIAL)** — A1 borderline, A2 refuted

### A1 — regime structure of the Eₐ spread
Per-study Eₐ (study as unit), median kJ/mol: pure_al_alkali 52.0 (n=5), waste_al 47.4 (n=3),
mechanically_activated 23.7 (n=4), al_alloy 39.2 (n=1), liquid_metal_activated 39.6 (n=1).

| analysis | η² | permutation p | boot 95% CI | verdict |
|---|---|---|---|---|
| **all 5 classes (primary)** | 0.473 | **0.184** | [0.148, 0.892] | **REFUTED** (p≥0.05) |
| well-powered 3 classes (≥3 studies) | 0.470 | 0.049 | [0.117, 0.888] | borderline SUPPORTED |

η² is large (~0.47) but the permutation significance is **fragile**: the primary all-class test fails
(p=0.18), and the 3-class subset only just crosses 0.05 (p=0.049) with a very wide bootstrap CI. The
**descriptive** finding is real and physically plausible — `mechanically_activated` composites have
markedly **lower apparent Eₐ** (median 24, range 12–52) than `pure_al_alkali` (52, range 41–72) and
`waste_al` (47) — but it does **not** clear a robust pre-registered bar. **A1 = borderline / not robust.**

### A2 — ML↔physics convergence
Per-regime yield–temperature slope vs median reported Eₐ:

| system_class | dyield/dT (%/K) | median Eₐ (kJ/mol) |
|---|---|---|
| al_alloy | 1.386 | 39.2 |
| liquid_metal_activated | 0.289 | 39.6 |
| mechanically_activated | 0.738 | 23.7 |
| pure_al_alkali | −0.096 | 52.0 |
| waste_al | 0.775 | 47.4 |

Spearman ρ = **−0.500** (p=0.391, n_regime=5) — **opposite to the expected positive direction.**
**A2 = REFUTED.** Root cause (stated honestly): **yield is a poor proxy for temperature sensitivity**
here — `pure_al_alkali` has the highest Eₐ but a flat/slightly-negative yield–T slope because its
yields are near-saturated (~93%), so a yield-based "temperature sensitivity" cannot track Eₐ. A valid
A2 needs **rate-based** temperature sensitivity, which requires digitizing the 5 curve-only rate studies
(`rin2021, jayaraman2015, dudoladov2016, ilyukhina2012, ho2016`) — not yet done.

## Bottom line
H3 is **not robustly supported on the current data**: a suggestive (borderline) Eₐ regime structure
(A1) but no confirmed ML↔physics convergence (A2, blocked by the yield-proxy limitation). A proper
rate-based A2 (after curve digitization) is the only path to a clean "physics-validated" claim.
