# WP1 Phase B — Extraction Progress

*Growing log of condition-level extraction. Data: `extraction_rows.csv` (validated against the
schema). Only validated rows count.*

## Totals
- **Rows extracted: 119** (validator PASS). Per class: **al_alloy 45 (≥40 ✓)** ·
  mechanically_activated 32 · pure_al_alkali 18 · **waste_al 11** · liquid_metal_activated 13.
  Floor 150 / target ~300 → in progress.
- Studies attempted: 26 (15 productive). `al_alloy` cleared the ≥40 rule.

## Batch 4 (2026-06-15) — 5 waste_al studies (>100% exclude rule active)
| study | class | rows | note |
|---|---|---|---|
| buryakov2023met | waste_al | 6 | 2M AlCl3 medium, 90–94% (water_type unmapped — see caveat) |
| fadhilah2023 | waste_al | 2 | NaOH/NaAlO2 64/96% (derived) |
| ho2016 | waste_al | 1 | Al cans+Ni, 100% (1350 mL/g excluded by >100 rule) |
| gupta2025 | waste_al | 1 | Al6063 scrap (3 rows excluded by >100 rule) |
| tekade2020 | — | 0 | rates / fractional-conversion figures only |

The **>100% exclude rule worked**: gupta (3 rows), ho2016 (1), david2012 (9) all correctly dropped.
⚠️ Caveat: `buryakov2023met` reacts in **2M AlCl3** (chloride-salt medium) — no `water_type` enum
fits {DI,tap,sea,alkaline}, left blank. Same will apply to other chloride-salt media (e.g.
`buryakov2024`). Worth a `water_type=salt` level if more such studies enter.

## Batch 3 (2026-06-15) — 5 studies (waste_al start + push al_alloy/mech)
| study | class | rows | note |
|---|---|---|---|
| liuyh2017 | al_alloy | 16 | Al-Bi/Al-Sn fresh+air-exposed, reported % |
| chen2020 | mechanically_activated | 4 | Bi(OH)3 composite, derived mL/g (<1244) |
| mezulis2023 | waste_al | 1 | 1M NaOH 92% (tier B) |
| yolcular2020 | — | 0 | yield figure-only |

### EXCLUDED — david2012 (9 rows, >100% yield) — decided 2026-06-15
All 9 yields were **>100%** (104–106%): waste Al **dross** has co-reactive Zn/Ni/Mg so H2 per
gram of *Al* exceeds the pure-Al theoretical. **Decision: exclude** (yield basis contaminated;
target stays ≤100). Rule now applies to all waste_al/dross studies — see `EXTRACTION_GUIDE.md`.

## Batch 2 (2026-06-15) — 8 studies (thin-class focus)
| study | class | rows | note |
|---|---|---|---|
| wen2018 | pure_al_alkali | 8 | Al(OH)3-catalyst, ~95% across T (tier C) |
| ilyukhina2012 | liquid_metal_activated | 5 | gallam-activated, range-midpoint (tier C) |
| prabu2021 | pure_al_alkali | 4 | Table 2 Al(OH)3 phases, reported % (tier B) |
| fischman2020 | liquid_metal_activated | 1 | slurry 93.4% (tier C) |
| lu2017 | liquid_metal_activated | 1 | saline 57.1% (water_type=sea, tier C) |
| tan2016, godart2019, noland2020 | — | 0 | yield figure-only / thermo / rates-only |

QC: `wen2018` activator_ratio blanked (was Al(OH)3 catalyst fraction, not a metal-activator
ratio — consistency with `prabu2021`).

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
