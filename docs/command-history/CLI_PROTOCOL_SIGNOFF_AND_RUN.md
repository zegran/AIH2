# CLI Command — Protocol Sign-off + Rate Extraction + H2/H3 Run (advisor-refined)

**Context:** Both go/no-go verdicts are in — TEST1 (porciuncula) → **FAILS** (ML headline dead);
TEST2 (rate feasibility) → **PILLAR RECOVERABLE** (physics is primary). PI + advisor consensus:
protocol approved with explicit H3 criteria, rate extraction authorized with QC, sequence
mixed-effects (H2) → Arrhenius (H3) → SHAP/ALE descriptive only.

> **Four advisor corrections are folded in below (marked ⚠️ ADVISOR FIX). They override the
> earlier draft where they conflict — they fix statistical errors that would otherwise invalidate
> the physics pillar.** Reposition the paper as **"physics-guided data science"** (title/abstract).

---

## Step 1 — Finalize H3 success criteria in `plan/analysis-protocol.md` (before extraction)

**H3 (physics validation) success = BOTH of:**

1. **Regime-differentiated Eₐ.** Per-`system_class` Eₐ estimated with study-level bootstrap CIs.
   Evidence of differentiation = clear descriptive separation of class Eₐ ranges **plus** a formal
   test (Kruskal–Wallis across classes, Holm-corrected).
   ⚠️ **ADVISOR FIX:** per-class n is tiny (≈3–6 studies). **Pre-state that the descriptive
   separation + effect size (e.g. η²/ε² or class-median gap vs pooled spread) is the PRIMARY
   evidence and the p-value is secondary** — an underpowered non-significant KW at n≈4 must NOT be
   read as "no effect" and must not kill the pillar. Report the test honestly as underpowered.

2. **Convergence of ML temperature sensitivity with physics.**
   ⚠️ **ADVISOR FIX — do NOT rank-correlate 5 class points (ρ over n=5 is statistically void).**
   Replace with a defensible convergence definition:
   - (a) **Sign/monotonicity:** in every class with a usable Eₐ, the descriptive ML temperature
     effect (ALE slope / partial-dependence derivative) is **positive** (higher T → higher
     yield), consistent with a positive Eₐ; report the per-class sign and slope.
   - (b) **Ordering consistency (descriptive, not a p-gate):** rank the classes by Eₐ and by ML
     temperature-effect magnitude; report the agreement qualitatively with a **study-level block
     bootstrap** of the ordering — present uncertainty, do not claim a significance threshold over
     5 points.
   Convergence is "met" if (a) holds in all well-estimated classes and (b) shows broadly
   consistent ordering; report it as **corroborative**, not confirmatory.

**Partial success (only #1):** descriptive physics; IJHE weaker-but-possible.
**Failure (neither):** drop "physics-validated"; reframe as leakage-controlled methodology + open
dataset (Energy and AI). State plainly.

**⚠️ MANDATORY STOP after Step 1** — commit the finalized criteria and wait for PI sign-off before
extracting.

---

## Step 2 — Rate-extraction pass (20 Arrhenius-ready studies)

For each (citekeys/Eₐ already in `RATE_FEASIBILITY.md`): reported Eₐ (kJ/mol), **method**
(Arrhenius fit / isoconversional / reported), **temperature range**, **rate_definition**
(initial / max / avg / time-to-X), original fit quality if given. Curve-only (5 studies): digitize
(engauge/manual), extract rate at ≥3 T.

⚠️ **ADVISOR FIX — rate-definition confound (critical for the physics pillar):** Eₐ depends on
which rate is used (initial vs max vs time-to-conversion) and the conversion extent. Mixing Eₐ
from different rate definitions can itself manufacture spread — the very thing we are studying.
Therefore: **record `rate_definition` and `method` as columns; in Step 3.2 treat them as a
covariate / stratifier and report whether the class-Eₐ differences survive holding rate-definition
roughly constant.** If the Eₐ spread is explained by rate-definition rather than regime, say so.

**QC:** double-extract a random 20% independently; accept only within **±2 kJ/mol (Eₐ)** or
**±10% (rates)**; discrepancies → adjudicate against source.

Output: `data/curated/rate/arrhenius_dataset.csv`
(study, system_class, Ea, rate_metric, rate_definition, method, T_range, quality_flag) +
`data/curated/rate/RATE_EXTRACTION_LOG.md` (per-study provenance + QC result).

---

## Step 3 — Analysis pipeline (in order)

### 3.1 Mixed-effects meta-regression (H2 primary)
- Response `h2_yield_pct`; random intercept `study_id`; Satterthwaite df (`lmer` or `statsmodels`).
- Fixed effects: `temperature_k`, `alkali_conc_mol_l`, `system_class`, and
  `system_class × temperature_k` interactions.
- ⚠️ **ADVISOR FIX — exclude `particle_size_d50_um` from the PRIMARY model** (NaN in ~81% of rows;
  including it forces listwise deletion to a fraction of the data and biases everything). Run
  particle_size only as an **exploratory (H1) submodel on the subset that reports it** — report it
  separately, never in the primary.
- Report fixed-effect coefficients + CIs, ICC, marginal vs conditional R², **and the drop in
  between-study variance when `system_class` (+interactions) is added vs a study-only model**
  (this — not ICC alone — is the real H2 test).
- ⚠️ **ADVISOR FIX — success criterion:** ≥1 `system_class × temperature` interaction survives Holm
  (p<0.05) **AND** adding `system_class` meaningfully reduces between-study variance (report the %).
  ICC>0.2 alone is not success (it only confirms studies differ, which is expected).
- Failure → Energy and AI methodology paper.

### 3.2 Arrhenius per regime (H3 co-primary)
- Per-class Eₐ from the extracted rate data; **study-level block bootstrap (1000 resamples)** for CIs.
- Class-difference test = permutation/KW (per the Step-1 underpowered caveat).
- Convergence per Step-1 #2 (sign/monotonicity + ordering, descriptive).
- Stratify by `rate_definition` per the Step-2 confound fix.

### 3.3 Descriptive SHAP/ALE (only after H2/H3 assessed)
- **Not for inference.** Use only to visualize the mixed-model fixed effects; per-class ALE for
  T / alkali / particle_size aligned with the Eₐ findings.

⚠️ **MANDATORY STOP after 3.1** — if H2 is null, the framing changes; await PI decision before 3.2.

---

## Step 4 — Artifacts (commit; do NOT draft the paper yet)
- `results/real_v1/H2_mixed_effects_report.md`
- `results/real_v1/H3_arrhenius_regime_report.md`
- `results/real_v1/convergence_ml_physics.md`
- finalized `plan/analysis-protocol.md`
- Stop and await the next command before figures/writing.

## Rules
- Honest reporting; underpowered nulls flagged as underpowered, not as evidence of absence.
- All headline numbers: multi-seed and/or study-level bootstrap CIs; report dispersion.
- Touch no `h2_yield_pct` rows; analysis + new rate columns only. Conventional Commits; English.

## Definition of done
Steps 1, 3.1, 3.2, 3.3 artifacts written; H2 and H3 verdicts explicit with CIs; particle_size kept
exploratory-only; rate-definition confound addressed; two mandatory stops honored.
