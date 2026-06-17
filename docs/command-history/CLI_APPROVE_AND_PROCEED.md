# CLI Command — Approve protocol + rate round, with two hardening gates (senior brief)

> Paste into Claude Code at the AIH2 repo root. Decisions: **protocol APPROVED**, **rate-focused
> second extraction APPROVED**, **proceed to mixed-effects (H2) + Arrhenius-per-regime (H3)**.
> Two conditions must be satisfied *before* the analysis runs (Gates A and B). Honest reporting
> only — pre-registered criteria decide verdicts; no post-hoc reframing.

The stress test verdicts stand: TEST1 FAILS (ML-prediction headline is porciuncula-driven, dead;
ML/SHAP → descriptive secondary), TEST2 PILLAR RECOVERABLE (physics is the asset). Paper identity
is now **physics + mixed-effects meta-analysis (ML descriptive)**, not "ML reveals hierarchy".
Floor = leakage/heterogeneity result (Energy and AI). Upside = H2 + H3 deliver → IJHE.

---

## GATE A — Concretize H3's success criterion before running (it is co-primary)

"Eₐ in-band" is **not** a contribution — the literature already reports in-band Eₐ. Update
`plan/analysis-protocol.md` so H3 has two pre-registered, falsifiable success criteria:

- **A1 — Regime structure of the Eₐ spread.** Test whether `system_class` explains a meaningful,
  significant share of the across-study Eₐ variance (e.g. one-way / mixed model `Ea ~ system_class`,
  study as unit; report between-class vs within-class variance, η²/ICC, cluster-bootstrap CI).
  **Success:** system_class explains a significant, non-trivial share → the 3.5–102.6 kJ/mol spread
  is **regime-structured, not random** (this directly resolves contradiction #2).
- **A2 — ML↔physics convergence.** Test whether the model-implied temperature sensitivity per
  regime (fitted temperature effect / local Arrhenius slope) agrees with the **independently
  reported** Eₐ per regime (rank correlation across regimes and/or CI overlap).
  **Success:** positive agreement → "physics-validated" is earned, not asserted.

Write both thresholds **before** computing either. State that H3 can also come back null.

## GATE B — Rate extraction discipline (same rigor as the yield pass)

Approved, but: collecting reported Eₐ is necessary, not the contribution. Build a **separate**
kinetic table `data/wp1/rate_extraction.csv` (do NOT pollute `aih2_v1.csv`) with:
`study_id, system_class, kinetic_metric (ea_kj_mol|rate_k|max_rate|t80), value, unit,
rate_definition, n_temperatures, temp_range_k, fit_method (reported|arrhenius_fit|derived),
source_ref, extraction_method (table|webplotdigitizer), value_origin, quality_tier, notes`.

- Record **method heterogeneity** per row: reaction medium, rate definition, T-range, how Eₐ was
  obtained. Heterogeneous Eₐ must not be pooled naively — stratify/flag.
- The 5 curve-only studies → WebPlotDigitizer; the ~15 reported-Eₐ → table entry with provenance.
- **Double-extract a 10–15% sample** of the kinetic rows (same QC as before); report error.
- Validate the kinetic table with a small `tools/validate_rate_rows.py` (enum/range/provenance).

**Gate:** A1/A2 criteria written + frozen; `rate_extraction.csv` populated, QC'd, validated.
Commit gates A and B before any modeling.

---

## Then run — in this order, then STOP for user sign-off

### 1. Mixed-effects meta-regression (H2 primary)
- Model: `h2_yield_pct ~ temperature_k + alkali_conc_mol_l + particle_size_d50_um +
  key composition wt% + system_class + (pre-specified interactions) + (1 | study_id)`.
- **H2 test:** does adding `system_class` + quality covariates significantly reduce the
  **between-study variance** (random-intercept variance / ICC) vs a parameters-only model?
  Report variance components before/after, with cluster-bootstrap (resample studies) CIs.
- Pre-specified interactions: `temperature × system_class`, `alkali_conc × system_class`
  (confirmatory); `particle_size × system_class` (exploratory, H1 — declare as such).
- Holm correction across the confirmatory tests. Report effect sizes + CIs, not just p.
- **Mandatory sensitivities:** porciuncula-out, high-quality-only (A-tier). A result that
  flips under either is not reported as confirmatory.

### 2. Arrhenius-per-regime (H3 co-primary)
- Run A1 (Eₐ ~ system_class structure) and A2 (ML↔physics convergence) exactly as frozen.

### 3. Write verdicts, then stop
- `results/real_v1/H2_mixed_effects.md`, `results/real_v1/H3_arrhenius.md`, and update
  `results/real_v1/GO_NOGO_SUMMARY.md` with: H2 verdict, H3 (A1+A2) verdict, and the resulting
  paper framing + venue (IJHE if H2 or H3 confirmatory; Energy-and-AI floor if both null).
- **Do not start WP5 figures or paper drafting.** Stop for user sign-off on the framing.

---

## Reporting rules
- Pre-registered criteria are binding; if H2 and/or H3 come back null, the summary says so plainly.
- Report effect sizes + CIs; multi-seed/bootstrap where stochastic; deterministic models report
  cluster-bootstrap CIs over studies.
- ML/SHAP results are descriptive only — no causal/prediction claims from them.
- Keep `aih2_v1.csv` (yield) and `rate_extraction.csv` (kinetic) separate. Durable artifacts in
  English. Conventional Commits; small logical commits.

## Definition of done
- Gates A+B committed (frozen H3 criteria, QC'd kinetic table + validator).
- `H2_mixed_effects.md`, `H3_arrhenius.md`, updated `GO_NOGO_SUMMARY.md` committed; every verdict
  explicit; sensitivities run; pipeline stopped for user sign-off before figures/writing.
