# T_A — within-study consistency vs between-study contradiction (PRIMARY)

Frozen success (`plan/analysis-protocol.md`): (i) median within-study skill > 0 with cluster-boot
95% CI lower > 0 (clearly positive ≥0.20) AND (ii) ≥1 parameter with a between-study sign conflict +
within-study consistency. Honest reporting; nulls reported with a power statement.

## VERDICT: **NULL at the frozen bar** (part (i) fails) — with two real supporting findings

### T_A.1 — between-study variance (robust manual decomposition)
The MixedLM null-model ICC was boundary-degenerate (random-intercept collapsed to 0). Robust manual
one-way decomposition: **η²_study = 0.496 → ~50% of yield variance lives between studies.** Study
identity is the single largest variance source. (Supports the premise that the variance is between
studies.)

### T_A.2 — within-study predictability → **FAILS frozen bar**
Within-study CV (RF, leave-one-out / 5-fold), skill vs the study's own mean, 14 studies with ≥5 rows
and varying parameters:
- **median within-study skill = −0.145**, cluster-boot 95% CI **[−0.447, +0.233]**; positive in
  **5/14** studies.
- Strongly predictable studies exist (porciuncula 0.23, qiao 0.84, zhang 0.86, guan/xiao positive),
  but small or composition-varied studies give negative skill, dragging the median below 0.
- **Power statement:** at within-study n = 5–120 with leave-one-out RF, within-study predictability is
  **heterogeneous and not uniformly positive** — *no detectable uniform within-study predictability at
  these sample sizes*. This is a power-limited null, not proof that within-study physics is inconsistent.

### T_A.3 — sign-conflict localization (a substantive finding)
Within-study effect sign (Spearman of yield vs parameter) per study that varies it:
- **particle_size_d50_um: 5/5 studies NEGATIVE** (smaller particle → higher yield; ρ −0.29 to −0.87).
  **No between-study sign conflict.** → The headline H1 "particle-size contradiction" does **not**
  appear as a within-study sign disagreement; the apparent literature contradiction was an artifact of
  comparing different size *ranges*/regimes, not a genuine direction flip. This retires H1 cleanly.
- temperature_k: 5 +, 1 − (n=3 ALEX nano outlier), 3 ~0 → weak between-study conflict, mostly positive.
- alkali_conc_mol_l: only 1 study varies it within-study → **untestable** for conflict.

## Bottom line
Between-study variance is high (50%) and the particle-size "contradiction" dissolves into a consistent
negative within-study effect — both consistent with the methodological-artifact thesis. But the
pre-registered T_A gate (uniform within-study predictability) is **not** met at n≈31 (median skill
−0.14). T_A is reported as **null at the frozen bar**. The decisive evidence for H_meth comes from T_B.
