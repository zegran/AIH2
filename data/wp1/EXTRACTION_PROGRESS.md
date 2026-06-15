# WP1 Phase B — Extraction Progress

*Growing log of condition-level extraction. Data: `extraction_rows.csv` (validated against the
schema). Only validated rows count.*

## Totals
- **Rows extracted: 69** (validator PASS). Per class: pure_al_alkali 6 · al_alloy 29 ·
  mechanically_activated 28 · liquid_metal_activated 6. Floor 150 / target ~300 → in progress.

## Batch 1 (2026-06-15) — 8 studies dispatched (parallel agents + QC)

| study | class | rows | note |
|---|---|---|---|
| qiao2019 | al_alloy | 28 | Tables 2–4, reported yield ratios (clean) |
| guan2019 | mechanically_activated | 28 | Tables 3/5/7, mL/g→% derived (all <1244) |
| dudoladov2016 | pure_al_alkali | 6 | Table 2 KOH/NaOH conversions, tier A (low-T) |
| meng2022 | al_alloy | 1 | Table 3 (No.6, 50 °C); rest figure-only |
| jayaraman2015 | liquid_metal_activated | 6 | calibration (text-reported 90 °C yields) |

### QC fixes applied
- `qiao2019` `activator_ratio` was wt% (15/10/5) → converted to fraction (0.15/0.10/0.05).
- `dudoladov2016` two CaCl₂/ZnCl₂ neutral-salt rows dropped (out of clean alkali scope).

### Held / issues
- **`irankhah2018` — HELD.** Several reported mL/g values exceed the theoretical max (1244),
  so the agent capped many at 100% → unreliable. Needs re-extraction with the study's own yield
  basis (its theoretical differs). Do not merge as-is.
- **`wangxy2021` — WRONG PDF (data integrity).** Archived MD/PDF body is an unrelated Portuguese
  philosophy article (correct title/DOI header only). **Re-download required.** Integrity sweep
  over all 59 confirms this is the *only* corrupt file; the other 58 contain proper content.
- **`shmelev2016`, `razavi2016` — 0 text rows.** Yield data is figure-only → figure digitization
  (render→vision per `FIGURE_EXTRACTION_METHOD.md`).

## Key finding (shapes the strategy)
Extractability is **bimodal**: table-reporting studies (qiao, guan, dudoladov) yield many rows
from text; figure-only studies (shmelev, razavi) yield ~0 and need digitization. Parallel agents
work well for table studies but their output **requires QC** (unit normalization, capping,
scope) before merging.

## Next
- Continue A-tier table-reporting studies (parallel agents + QC).
- Digitize figure-only studies (render→vision).
- Re-extract `irankhah2018` with correct yield basis; re-download `wangxy2021`.
- Recompute per-class counts each batch; aim each class ≥40 or flag exploratory-only.
