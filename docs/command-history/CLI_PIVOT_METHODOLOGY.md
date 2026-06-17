# CLI Command — Pivot to the methodological-heterogeneity thesis (pre-register + T_A/T_B)

> Paste into Claude Code at the AIH2 repo root. We are NOT abandoning the original research
> question — we are reporting the answer the data supports: the apparent contradictions are
> **cross-study methodological artifacts**, not genuine physico-chemical regime disagreement.
> Pre-register the new claim + success criteria BEFORE running (anti-HARKing). Accept nulls.
> Honest reporting only. Stop after verdicts for user sign-off — no figures/writing yet.

## Confirmed novelty (Consensus, 2026-06-16) — use in framing
- The Al–water hydrolysis ML literature has **one** prior model: **Das et al. 2023, *Fuel*** — a
  **single-study, in-sample ANN (R²≈0.998)**. It is the perfect foil: it reports near-perfect
  prediction *within one study's data* — exactly the generalization illusion our leakage analysis
  exposes across the literature.
- Existing reviews (Musicco 2025; Xiao 2021; du Preez 2021) are **qualitative narrative**
  comparisons. **No** prior work unifies the literature into a provenance-tracked dataset, applies
  leakage-controlled evaluation, or **quantitatively attributes the contradictions to methodology
  vs physics.** That is the gap.
- Individual studies already show methodological covariates matter (vessel insulation —
  Urbonavičius 2023; water type — Bolt 2020), motivating T_B.

## New thesis (pre-register in `plan/analysis-protocol.md`)
**H_meth:** Apparent inter-study contradictions are dominated by cross-study methodological
heterogeneity, not physico-chemical regime. Operationalized as two falsifiable tests:

### T_A — within-study consistency vs between-study contradiction (PRIMARY; robust by design)
1. **Variance decomposition:** null mixed model `h2_yield_pct ~ 1 + (1|study_id)`; report ICC
   = between-study / total. High ICC ⇒ the variance lives between studies.
2. **Within-study predictability:** for every multi-condition study, fit parameter→yield within
   that study; report within-study skill (vs that study's mean). Aggregate (median, distribution).
3. **Sign-conflict localization:** for parameters varied within ≥2 studies (temperature,
   alkali_conc, particle_size), estimate the within-study effect direction per study; test whether
   documented sign-conflicts occur **across** studies while each study is internally consistent.
   **Success (frozen):** (i) median within-study skill clearly positive, AND (ii) the parameter
   sign-conflicts are between-study, not within-study → contradictions are integration artifacts.

### T_B — methodological covariates explain the between-study variance (UPSIDE)
0. **Coverage audit first:** report fill-rate + variation of `measurement_method`,
   `temperature_control`, `vessel_type`, `water_type`, `quality_tier`. Any covariate too sparse to
   test → declare untestable, do not force it.
1. Mixed model `h2_yield_pct ~ physical_params + method_covariates + (1|study_id)`; quantify the
   **reduction in between-study (random-intercept) variance** attributable to method covariates,
   vs the reduction attributable to `system_class` (the physical regime, already shown ~null).
   Cluster-bootstrap CIs; Holm across method covariates.
   **Success (frozen):** method covariates significantly reduce between-study variance (stated
   threshold) and explain ≥ as much as physical regime → methodology is a dominant driver.

## Pre-committed venue rule (binding)
- **T_A success ∧ T_B success** → strong contribution (methodology relocates the contradiction);
  target **IJHE**.
- **T_A success ∧ T_B null/untestable** → still a solid paper: "contradictions are cross-study
  integration artifacts; within-study physics is consistent" + curated dataset + leakage foil
  (Das 2023); target **IJHE-borderline / Energy and AI**.
- **T_A null** (unlikely) → fall back to the dataset + leakage-benchmark paper (Energy and AI).

## Discipline (binding)
- Freeze T_A/T_B success thresholds in `plan/analysis-protocol.md` BEFORE computing them.
- Mirror-discipline on nulls: report any null as "no detectable effect at n≈31 studies / 3–9 per
  regime," never "no effect exists." Add an explicit power/limitation statement.
- Cluster-bootstrap (resample studies) CIs on every headline number; effect sizes + CIs, not just p.
- ML/SHAP descriptive only. Kinetic table stays separate. Touch no data rows (analysis-only).
- Durable artifacts English; Conventional Commits; small commits.

## Output, then STOP
- `results/real_v1/TA_within_study.md`, `results/real_v1/TB_method_variance.md`, and update
  `results/real_v1/GO_NOGO_SUMMARY.md` with both verdicts + the venue per the rule.
- Do NOT start WP5 figures or WP6 writing. Stop for user sign-off on the framing.

## Definition of done
- `plan/analysis-protocol.md` updated with H_meth + frozen T_A/T_B criteria (committed before running).
- `TA_within_study.md`, `TB_method_variance.md`, updated `GO_NOGO_SUMMARY.md` committed; both
  verdicts explicit; coverage audit + power statement included; pipeline stopped for user sign-off.
