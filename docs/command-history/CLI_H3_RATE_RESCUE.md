# CLI Command — Rate-based H3 re-test (Option 1), frozen criteria, hard fallback (senior brief)

> Paste into Claude Code at the AIH2 repo root. Decision: **Option 1** — fix the known
> measurement artifact (yield is a poor rate proxy) by adding real rate data, then **re-run the
> ALREADY-FROZEN H3 criteria (A1, A2)**. This is *not* a rescue with moving goalposts: thresholds
> stay exactly as pre-registered in `plan/analysis-protocol.md`. **Pre-commit:** if H3 does not
> reach clean support, STOP and write the Energy-and-AI paper — no third attempt.

Rationale on record: A2 failed (ρ=−0.50) largely because yield saturates (pure_al ~93%) and is a
bad rate proxy. The kinetic data strengthens the open dataset regardless of the H3 outcome, so this
step is low-regret and is the only path that preserves the IJHE option.

---

## Scope (tight — do not expand)

- **Digitize the 5 curve-only studies:** `rin2021`, `jayaraman2015`, `dudoladov2016`,
  `ilyukhina2012`, `ho2016` (H₂-volume-vs-time → rate). Vision/render-based curve extraction.
- **Fit Arrhenius Eₐ** from table-rate studies already flagged ARRHENIUS-READY (~15) where Eₐ was
  not reported directly. Reuse the reported-Eₐ rows as-is.
- **No new literature.** Work only from the 31 in-hand studies. Extend `data/wp1/rate_extraction.csv`
  (currently 73 rows); keep it separate from `aih2_v1.csv` (yield).

## Rigor gates (must pass before re-running H3)

1. **Digitization QC.** Vision curve reading is error-prone. Re-digitize a ~20% sample
   independently; report point-level error. Flag any curve where axis/scale is ambiguous.
2. **Arrhenius fit quality.** Fit ln(k) vs 1/T per study; require **n_T ≥ 3**; report fit R²,
   Eₐ, and a CI on Eₐ. Drop/flag fits with R² below a stated threshold or n_T < 3 (don't force a
   line through 2 points). Fit ALL studies the SAME way (consistent k definition / rate metric).
3. **Provenance + heterogeneity.** Each new rate row carries `rate_definition`, `temp_range_k`,
   `n_temperatures`, `fit_method`, `source_ref`, `value_origin`, `quality_tier`. Heterogeneous Eₐ
   are stratified, never naively pooled. Run `tools/validate_rate_rows.py`.

## Re-run the FROZEN H3 criteria (no threshold changes)

- **A1 — regime structure of Eₐ:** `Ea ~ system_class` (study as unit) on the now rate-based Eₐ
  set; report η²/ICC, between- vs within-class variance, cluster-bootstrap CI, and the pre-set
  p-threshold result. Report all-class AND the (pre-specified) ≥3-study-class subset.
- **A2 — ML↔physics convergence, now rate-based:** compare the **rate-derived** temperature
  sensitivity per regime against the independently reported Eₐ per regime, using the SAME
  pre-registered statistic/threshold. **Honesty clause:** if a model temperature-sensitivity
  cannot be defined on a rate target without a new rate-target model, say so explicitly and report
  A2 as the pre-specified rate-vs-reported-Eₐ consistency test — do NOT redefine A2 to pass.

## Decision rule (pre-committed — binding)

- **H3 CLEAN SUPPORT** ⇔ A1 robust (meets frozen threshold, survives bootstrap + the
  ≥3-study-class check) **AND** A2 positive (frozen threshold). → paper framing = physics-validated
  regime structure; venue **IJHE**.
- **OTHERWISE (partial / null)** → **STOP the rescue.** Framing = leakage-controlled methodology +
  curated open dataset (now incl. kinetic rows); venue **Energy and AI**. No further attempts.

## Output, then STOP
- Update `results/real_v1/H3_arrhenius.md` (rate-based A1/A2, with verdict) and
  `results/real_v1/GO_NOGO_SUMMARY.md` (final framing + venue per the rule above).
- **Do not start WP5 figures or paper drafting.** Stop for user sign-off on the final framing.

## Rules
- Frozen thresholds are binding; a second null is an acceptable, reportable outcome — state it plainly.
- Kinetic data stays in `rate_extraction.csv`; never merged into the yield dataset.
- ML/SHAP remain descriptive only. Durable artifacts English; Conventional Commits; small commits.

## Definition of done
- `rate_extraction.csv` extended + QC'd + validated; digitization error reported.
- `H3_arrhenius.md` (rate-based) and `GO_NOGO_SUMMARY.md` committed with an explicit verdict and a
  single venue decision; pipeline stopped for user sign-off before any figures/writing.
