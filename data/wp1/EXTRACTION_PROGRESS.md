# WP1 Phase B — Extraction Progress

*Growing log of condition-level extraction. Data: `extraction_rows.csv` (validated against the
schema). Only validated rows count.*

## Totals
- **Rows extracted: 315** (validator PASS). **Hard floor 150: MET.** Per class:
  **pure_al_alkali 162 (✓)** · **mechanically_activated 69 (✓)** · **al_alloy 45 (✓)** ·
  liquid_metal_activated 19 (exploratory-only) · waste_al 20 (exploratory-only).
- ✅ **Double-extraction QC done** (`QC_DOUBLE_EXTRACTION.md`): 52 rows (~16.5%) re-extracted
  independently → **52/52 yield values exact (0% value error)**. 1 class-label error caught +
  fixed (`dudoladov2016` → liquid_metal_activated).
- ✅ **Classification audit done** (2026-06-16): all 31 studies' `system_class` re-derived from
  source by 9 agents → every label correct after the dudoladov fix (0 further changes). Gallium-
  eutectic boundary rule documented in `EXTRACTION_GUIDE.md`. **Central analysis axis verified.**
- Studies attempted: 42 (29 productive). ⭐ **H1 evidence**: `martinezv2026` particle-size
  inverted-U; `zhang2024` 3µm vs 25µm (95% vs 34% at 45 °C — strong size effect). ⭐ **Rate–yield
  trade-off (2nd contradiction)**: `davies2022mat` Al-Bi-Zn — Zn slows the rate but keeps ~99.5%
  yield; NaCl & high water-ratio drop both together.
- ⚠️ **`porciuncula2012` (120 rows) INGESTED** (user decision 2026-06-15: take all). One `study_id`
  is now ~38% of the dataset → **CV-group imbalance**. Binding mitigations recorded in
  `DATASET_BALANCE_NOTES.md`: (1) group-balanced sample weighting `1/n_rows(study_id)`, (2)
  leave-porciuncula-out sensitivity run. Do NOT drop it from the main model — it holds the cleanest
  alkali-type × conc × T signal.

## Batch 6 (2026-06-15) — 8 studies (mechanically + pure_al_alkali); +47 rows (porciuncula held)
| study | class | rows | note |
|---|---|---|---|
| preez2018 | mechanically_activated | 16 | Al-Sn-In ternary + mass-ratio series, reported % |
| davies2022mat | mechanically_activated | 10 | ⭐ Al-Bi-Zn rate–yield trade-off; water-quality/NaCl |
| zhang2024 | pure_al_alkali | 10 | 3µm vs 25µm × 5T (H1 size effect; Table 3) |
| xiao2020 | mechanically_activated | 7 | Bi/GNS composites, derived mL/g (<1244) |
| xiao2018 | mechanically_activated | 4 | Al-Bi-Sn tap water, reported % (Table 4) |
| razavi2013 | — | 0 | yield Fig.4 only / "no reaction" qualitative |
| tekade2018n | — | 0 | rates + fractional conversion X_B only (not absolute yield) |
| **porciuncula2012** | pure_al_alkali | **(120 held)** | tier-A factorial; balance decision pending |

QC notes: `zhang2024` 3µm rows have mL/g >1244 but the study's own reported % is ≤100 (kept as
reported, like a per-study yield basis); `davies`/`preez` use a gas mass-flow meter →
`measurement_method` blank (no enum); `davies` filtered-water & NaCl rows → `water_type` blank.

## Batch 5 (2026-06-15) — 8 studies (pure_al_alkali + waste_al)
| study | class | rows |
|---|---|---|
| rin2021 | pure_al_alkali | 9 (Ni-Li-B catalyst) |
| trowell2022 | pure_al_alkali | 5 (supercritical water) |
| knoks2025 | waste_al | 4 (dross RM/SOW/HDC/Alw1) |
| yavor2013 | pure_al_alkali | 3 (ALEX nano) |
| martinezv2026 | waste_al | 3 (⭐ H1 inverted-U) |
| wanghq2017 | pure_al_alkali | 2 (choline-OH / NaOH) |
| urbonav2024 | waste_al | 2 (plasma; 8 OVER-100 excluded) |
| deng2010 | pure_al_alkali | 1 |

⚠️ Validator caught 1 error (choline-hydroxide row: `alkali_type=none` + a conc → blanked the conc;
non-NaOH/KOH bases and salt media like AlCl3 don't map to the alkali enum — a known edge case).
OVER-100 rule again worked (urbonav 8, trowell/deng/martinezv all ≤100).

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
