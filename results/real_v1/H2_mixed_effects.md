# H2 — mixed-effects meta-regression (primary test)

Model: `h2_yield_pct ~ temp_z*C(system_class) + conc_z*C(system_class) + C(quality_tier)` with a
random intercept per `study_id` (REML). n=299 rows / 27 studies (rows missing temperature dropped;
unreported alkali conc → 0). Pre-registered criterion (`plan/analysis-protocol.md`): SUPPORTED iff
≥1 parameter:system_class interaction (or the system_class main effect) is significant at
**Holm-corrected p<0.05** with a non-negligible effect, AND survives **A/B-tier** AND
**leave-porciuncula-out**. Honest reporting; null acceptable.

## VERDICT: **NOT SUPPORTED** (refuted at the pre-registered bar)

| subset | system_class main (joint Wald) | individual interactions Holm-sig | notes |
|---|---|---|---|
| FULL (299/27) | p = **0.32** | **0/8** | best Holm 0.48 (temp×mechanically) |
| porciuncula-out (179/26) | p = **0.45** | **0/8** | best Holm 1.00 |
| A/B-tier (237/18) | p = **0.41** | **0/8** | best Holm 0.057 (temp×liquid_metal) |

- **The system_class main effect is non-significant** in FULL and both sensitivities (p = 0.32–0.45).
- **No individual parameter×system_class interaction survives Holm correction** in any subset (0/8
  every time). The closest is temp×liquid_metal in A/B-tier (raw p=0.007, **Holm=0.057** — misses).
- **Cluster bootstrap (resample studies, 90/200 converged):** system_class main effect reaches
  p<0.05 in only **34%** of resamples (median p=0.14) — not robust.

Both pre-registered clauses fail. → **H2 is NOT supported.** Conditioning on `system_class` does not
resolve the literature contradiction in a way that survives rigorous, multiplicity-controlled,
sensitivity-checked testing. This is **consistent with TEST 1** (the ML within-regime signal was
porciuncula-weighted, study-macro skill −0.31).

## Numerical caveats (stated, not used to rescue)
- The random-intercept variance is **boundary-unstable**: M0 (params-only) collapsed to between-study
  var ≈ 0, so the protocol's "does system_class *reduce* between-study variance" framing is degenerate
  here and was **not** used for the verdict (the fixed-effect joint/Holm tests were used instead).
- The manual joint Wald over all 8 interactions gave p≈1e-110 on FULL but **1.00** on A/B-tier and
  0.086 on porc-out — i.e. a singular-covariance artifact (some classes have little within-class
  temperature variation). It is reported for transparency and **explicitly not used** as evidence.

## Honest residual signal (hypothesis-generating only)
A non-robust hint of **temperature-sensitivity moderation** exists (temp×mechanically raw p≈0.06 in
FULL; temp×liquid_metal raw p≈0.007 in A/B-tier), but nothing survives Holm or the sensitivity
battery. Not reportable as confirmatory.

## Implication
The mechanism claim (H2: regime moderation) is **not defensible** on the yield data. The paper's
positive contribution now hinges entirely on **H3** (Arrhenius Eₐ regime structure) + the robust
leakage result. If H3 (A1) also fails → methodology + open-dataset floor (Energy and AI).
