# AIH2 — Frozen Analysis Protocol (internal pre-registration)

**Frozen:** 2026-06-16, after the go/no-go stress tests (`results/real_v1/GO_NOGO_SUMMARY.md`).
**Dataset:** `data/curated/aih2_v1.csv` (315 rows / 31 studies, QC'd, classification-verified).
**Purpose:** lock the primary tests and success/failure criteria BEFORE running them, to prevent
HARKing/p-hacking. After this freeze, the primary test and its decision rule may not be changed in
response to results; deviations must be logged as deviations.

## Why this freeze exists (test outcomes that shaped it)
- **TEST 1 FAILED:** the ML within-`pure_al_alkali` cross-study signal (+0.58) is porciuncula-weighted,
  not a per-study replication signal (study-macro skill −0.31). → **ML/SHAP demoted to descriptive.**
- **TEST 2 PASSED:** Arrhenius/rate data is abundant (20/31 ARRHENIUS-READY, ~15 reported Eₐ). →
  **physics pillar (H3) elevated to co-primary.**

## Hypotheses (priority + role)
- **H2 (PRIMARY, confirmatory):** the apparent literature contradictions are moderated by
  `system_class` — i.e. parameter→yield (and/or parameter→rate) relationships differ by regime after
  between-study heterogeneity is absorbed.
- **H3 (CO-PRIMARY, confirmatory, physics):** apparent activation energies organize by `system_class`
  and lie in the 3.5–102.6 kJ/mol band; the ML/empirical temperature sensitivity agrees with the
  literature Eₐ per regime.
- **H1 (EXPLORATORY only):** the particle-size sign flip is a shrinking-core regime switch. Declared
  exploratory due to thin coverage (particle_size in 19% of rows; 2 classes empty). No confirmatory
  claim will be made on H1.

## Confound model
`study_id` is the primary confounder (each study = its own uncontrolled apparatus/measurement window).
The unit of inference is the **study**, not the row. Data-quality covariates (`quality_tier`,
`value_origin`, `measurement_method`) are modeled/controlled.

## Confirmatory analyses (pre-specified — exact tests)
1. **H2 — mixed-effects meta-regression** (primary test).
   - Model: linear mixed model, `h2_yield_pct ~ standardized(parameters) + system_class +
     parameter:system_class + quality_tier` with **random intercept per `study_id`** (random slopes
     where estimable).
   - Parameters entered: `temperature_k`, `alkali_conc_mol_l`, `particle_size_d50_um` (where present),
     composition summaries.
   - **Success criterion (pre-stated):** H2 is SUPPORTED iff ≥1 `parameter:system_class` interaction
     (or the `system_class` main effect) is significant at **Holm-corrected p < 0.05** with a
     non-negligible standardized effect, AND it survives the **high-quality-only (tier A/B) sensitivity**
     AND the **leave-porciuncula-out sensitivity**. H2 is REFUTED iff no interaction survives correction.
2. **H3 — physics validation.**
   - Build the literature/derived apparent-Eₐ distribution per `system_class` (direct extraction +
     digitization per `RATE_FEASIBILITY.md`).
   - **Success criterion:** H3 is SUPPORTED iff apparent-Eₐ is in 3.5–102.6 kJ/mol for **≥3 classes**
     AND the empirical/ML temperature sensitivity rank-correlates with the per-regime literature Eₐ.
     REFUTED iff Eₐ is mostly out-of-band or the temperature effect is uncorrelated with literature Eₐ.

## Descriptive (NOT confirmatory)
- **Leakage / optimism gap** (random vs study-grouped CV): reported as an established methodological
  finding (robust; gap 0.62–0.85, survives porciuncula removal). Not a causal claim.
- **ML feature importance / SHAP / ALE:** descriptive lenses on association only. Explicitly **not**
  used to assert causal physical effects or a "true hierarchy"; any hierarchy statement is qualified
  as leakage-controlled association with the stability caveat (~0.68).

## Statistical standards (mandatory for every headline number)
- **Multi-seed:** ≥5 seeds (0,1,2,7,42); report mean ± sd. Never a single seed.
- **Study-level bootstrap CIs:** ≥1000 resamples **of studies** (not rows) for any reported effect/skill.
- **Metric choice:** prefer **MAE + skill-score vs mean baseline** over R² at n_study ≲ 8 (R² unstable).
- **Multiple comparisons:** the family of per-class × per-parameter interaction tests gets
  **Holm (or Benjamini–Hochberg)** correction; report both raw and corrected p.
- **Sensitivities required:** high-quality-only (tier A/B) and leave-porciuncula-out for every
  confirmatory claim.

## Locked limitations (stated up front, not as post-hoc excuses)
- porciuncula2012 = 38% of rows / 74% of pure_al_alkali → group-weighting + porciuncula-out mandatory.
- particle_size thin (19%; al_alloy & mechanically empty) → H1 exploratory only.
- n_study = 31 (1–9 per regime) → most per-regime claims are power-limited; pure_al_alkali is the
  only ≥9-study regime.
- OA-only curation → selection bias; defended via quality-tier sensitivity, documented as a limitation.

## Framing decision rule (set in advance)
- H2 supported ∧ H3 supported → **IJHE, physics-validated mechanism paper.**
- H2 refuted ∧ H3 supported → physics-Eₐ-descriptive + leakage paper (still IJHE-plausible).
- H2 refuted ∧ H3 refuted → **leakage-methodology + open-dataset paper (Energy and AI).**

## Status
Protocol FROZEN. **Mixed-effects model NOT yet run.** Awaiting user sign-off + decision on the
rate-focused second extraction pass before any confirmatory modeling.
