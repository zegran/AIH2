# T_B hardening — confound / robustness check (pre-write gate)

Question: is the T_B method-covariate signal genuine, or merely re-encoding study identity /
confounded with physical regime? Study-level analysis (each study = one row, modal covariate).
**Language is associational throughout** (observational data).

## Result: T_B SURVIVES — temperature-control is a genuine shared covariate, not a regime/study proxy

### (a) Shared coverage (not one-level-per-study)
temperature_control at study level: **isothermal_bath 22 · self_heating 7 · uncontrolled 2**. Multiple
studies share each level → the contrast is a real between-level comparison, not a per-study singleton.

### (b) Not confounded with physical regime
temperature_control × system_class (study counts): each method level spans **4–5 of the 5 regimes**
(isothermal_bath spans all 5; self_heating 4; uncontrolled 2). → temperature_control is **not** a 1:1
re-encoding of `system_class`.

### (c) Survives controlling for regime (incremental, bootstrapped)
Between-study study-mean-yield R²: temperature_control 0.332 · system_class 0.018 · both 0.485.
- **Incremental temperature_control | system_class = +0.467**, cluster-boot 95% CI **[+0.037, +0.772]
  → excludes 0.** Method explains between-study variance **beyond** physical regime.
- Incremental system_class | temperature_control = +0.153 (regime adds a little, not nothing).

### (d) Residual spread within the dominant level (honesty)
Within isothermal_bath (n=22) the study-mean yield still ranges [26, 100] (sd 18.7) → temperature
control is the **largest single** between-study driver but **not the only** one; other factors remain.
Per-level study-mean yield: isothermal_bath 75.5±18.7 · self_heating 86.1±9.9 · uncontrolled 32.4±33.0.

## Locked language (binding for the draft)
- Use **"methodological covariates explain / are associated with"** — never "cause" (observational).
- Claim is **"predominantly / substantially methodological"**, never "purely": regime contributes a
  small increment (+0.15 incremental), and within-method residual between-study variance remains.
- Attribution is study-level and observational → state confounding-with-unmeasured-study-attributes as
  an explicit limitation.
