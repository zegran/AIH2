# H3 — physics validation (Arrhenius), RATE-BASED re-test (Option 1)

Frozen criteria unchanged (`plan/analysis-protocol.md`). After the rate-focused round (digitized 4
curve-only studies + Arrhenius fits from tabulated rate-vs-T), the per-study Eₐ set grew from 14 → 17
studies; `liquid_metal_activated` went from 1 → 4 Eₐ. Honest reporting; a second null is acceptable.

## VERDICT: **NOT clean support** → A1 REFUTED, A2 REFUTED → (per binding rule) **STOP. Venue = Energy and AI.**

The rate data **weakened, not strengthened**, the regime-structure hypothesis: the honest
`liquid_metal_activated` Eₐ is **not a tight cluster** but spans **8.5–58 kJ/mol**, which is what
refutes A1 once that class is properly populated.

## Rigor gates (all passed before re-running H3)
- **Digitization QC:** ilyukhina2012 re-digitized independently → 2050/2450/3100 vs 2080/2480/3120
  mL·g⁻¹·min⁻¹ (**point error ~1.5%**, Eₐ unchanged 8.5→8.6). PASS.
- **Arrhenius fit quality (ln k vs 1/T, n_T≥3, R²≥0.90):**
  - dudoladov2016 (table, KOH) Eₐ=58.0±9.4, R²=0.987 — PASS
  - ilyukhina2012 (digitized peak rate) Eₐ=8.5±1.6, R²=0.991 — PASS
  - jayaraman2015 (digitized 1/t50) Eₐ=32.8±9.3, R²=0.979 — PASS
  - **rin2021 DROPPED** — 5-point fit R²=0.846 (<0.90); value unstable (43→24 on one flagged point).
  - **ho2016 DROPPED** — t50 unreadable (first sample ≈10 s, already ~80% plateau) AND additive
    confounded with temperature (only 3 no-additive curves). No forced fit.
- **Provenance/heterogeneity:** every new row carries fit_method, R²/CI, n_T, temp_range, proxy,
  medium; validated by `tools/validate_rate_rows.py` (76 rows PASS).

## A1 — regime structure of Eₐ (rate-enriched, study as unit, n=17)
Per-study median Eₐ (kJ/mol): pure_al_alkali 52.0 (n=5), waste_al 47.4 (n=3),
**liquid_metal_activated 36.2 (n=4, values 8.5/32.8/39.6/58.0)**, al_alloy 39.2 (n=1),
mechanically_activated 23.7 (n=4).

| analysis | η² | permutation p | boot 95% CI | verdict |
|---|---|---|---|---|
| **≥3-study subset (now 4 classes, incl. liquid_metal)** | 0.361 | **0.129** | [0.127, 0.808] | **REFUTED** |
| all 5 classes | 0.361 | 0.216 | [0.121, 0.816] | REFUTED |

η² fell from 0.47 (pre-rescue, when liquid_metal was a single point) to **0.36** because the honest
4-study liquid_metal Eₐ has very high within-class variance (8.5–58). The earlier "borderline p=0.049"
held only because liquid_metal was then a singleton; with it properly populated, **system_class does
not explain a significant share of the Eₐ spread.** (Using the old 3-class subset that excludes the
inconvenient liquid_metal would be moving the goalposts — not done.)

## A2 — ML↔physics convergence (honesty clause invoked)
A valid A2 requires a **rate-target** temperature-sensitivity. The project's ML model is yield-target,
and yield is a poor proxy (pure_al_alkali saturates ~93%): yield–T slope vs median Eₐ gives Spearman
ρ=−0.20 (p=0.75) — no convergence. **Per the pre-registered honesty clause, A2 is NOT redefined to
pass**: ML↔physics convergence cannot be established without building a new rate-target model (out of
scope). The legitimate extraction-consistency check (derived vs reported Eₐ, e.g. wanghq2017 derived
45.9 ≈ reported 45.92, R²=0.997) validates the *digitization method* but is not the A2 ML↔physics test.
**A2 = not positive.**

## Honest scientific takeaway (real finding, even though H3 is null)
With rigorous rate data, **apparent activation energy does not cleanly organize by `system_class`** —
`liquid_metal_activated` alone spans near-barrierless (8.5, gallam) to 58 kJ/mol. The contradictions
in the literature are **not** resolved into a tidy per-regime physics signal; the within-regime spread
is as large as the between-regime spread. This is a substantive, publishable negative result.
