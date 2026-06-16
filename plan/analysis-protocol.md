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
2. **H3 — physics validation (co-primary).** ⚠️ "Eₐ in-band (3.5–102.6 kJ/mol)" is **not** a
   contribution — the literature already reports in-band Eₐ. H3 has **two** pre-registered,
   falsifiable criteria (both thresholds set BEFORE computing; H3 may return null):
   - **A1 — Regime structure of the Eₐ spread.** Does `system_class` explain a meaningful share of
     the across-study apparent-Eₐ variance? Test: one-way model `Ea ~ system_class` with the
     **study as unit** (each study one Eₐ), report between-class vs within-class variance, **η²**,
     and a **cluster-bootstrap (resample studies) 95% CI** on η²; permutation p.
     - **SUPPORTED** iff η² ≥ **0.25** (large) with bootstrap-CI lower bound > 0 (permutation p<0.05)
       → the 3.5–102.6 spread is **regime-structured, not random** (resolves contradiction #2 on Eₐ).
     - **PARTIAL** iff η² ∈ [0.06, 0.25). **REFUTED** iff η² < 0.06 or CI includes 0.
   - **A2 — ML↔physics convergence.** Does the model-implied per-regime temperature sensitivity
     (fitted temperature coefficient / mean local Arrhenius slope from the descriptive ML, or a
     direct yield-vs-1/T apparent-Eₐ) agree with the **independently reported** Eₐ per regime?
     Test: per-regime comparison across the (≤5) classes that have both — directional/rank agreement
     + CI overlap of ML-implied vs reported Eₐ.
     - **SUPPORTED** iff agreement holds (same ordering / overlapping CIs) in **≥3 of the regimes**
       that have both quantities. **REFUTED** iff it disagrees in the majority.
     - ⚠️ Power caveat (stated up front): with ≤5 regimes a rank correlation is low-power; A2 is a
       convergence check, not a significance test — interpreted with explicit n_regime.

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

## Pivot — methodological-heterogeneity thesis (frozen 2026-06-16, after H2/H3 nulls)
The original RQ asks whether the contradictions are **real physical interactions** or **cross-study
artifacts**. H2 (regime moderation) and H3 (Eₐ regime structure) were refuted → the data supports the
**artifact** arm. This is the *other arm of the same pre-stated question*, not a new post-hoc claim.
Thresholds below are frozen BEFORE computing T_A/T_B (anti-HARKing). Nulls are acceptable and reported
with an explicit power statement ("no detectable effect at n≈31 studies / 3–9 per regime").

**H_meth:** Apparent inter-study contradictions are dominated by **cross-study methodological
heterogeneity**, not physico-chemical regime. Two falsifiable tests:

### T_A — within-study consistency vs between-study contradiction (PRIMARY)
1. **Variance decomposition:** null mixed model `h2_yield_pct ~ 1 + (1|study_id)`; report ICC =
   between-study variance / total.
2. **Within-study predictability:** for each study with enough conditions, predict held-out conditions
   from the others (within-study CV); skill = 1 − SSE/SS(study-mean); aggregate (median + cluster-boot CI).
3. **Sign-conflict localization:** for parameters varied within ≥2 studies (temperature, alkali_conc,
   particle_size), estimate the within-study effect SIGN per study; test whether documented sign
   conflicts occur **between** studies while each study is internally consistent.
- **Success (FROZEN):** (i) median within-study skill **> 0 with cluster-bootstrap 95% CI lower bound
  > 0** (and "clearly positive" = median ≥ 0.20), AND (ii) ≥1 contested parameter shows a
  **between-study sign conflict** with within-study sign consistency → contradictions are integration
  artifacts.

### T_B — methodological covariates explain between-study variance (UPSIDE)
0. **Coverage audit first:** fill-rate + n distinct values of `measurement_method`,
   `temperature_control`, `vessel_type`, `water_type`, `quality_tier`. Any covariate with <2 levels or
   <~10% informative coverage → declared **untestable**, not forced.
1. Mixed model `h2_yield_pct ~ physical_params + method_covariates + (1|study_id)`; quantify the
   **reduction in random-intercept (between-study) variance** from method covariates vs from
   `system_class` (physical regime). Cluster-bootstrap CIs on each reduction; Holm across covariates.
- **Success (FROZEN):** method covariates reduce between-study variance by an amount whose
  cluster-bootstrap 95% CI **excludes 0**, AND that reduction is **≥ the system_class reduction** →
  methodology is a dominant driver.

### Pre-committed venue rule (binding)
- T_A ✅ ∧ T_B ✅ → IJHE. · T_A ✅ ∧ T_B null/untestable → IJHE-borderline / Energy and AI (still solid:
  artifacts + curated dataset + leakage foil vs Das 2023 single-study ANN). · T_A null → dataset +
  leakage-benchmark paper (Energy and AI).

## Status
Protocol FROZEN (incl. H_meth + T_A/T_B). Mixed-effects H2 done (null), H3 done (null). T_A/T_B NOT yet
run — this commit freezes their criteria before computation.
