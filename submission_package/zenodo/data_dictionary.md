# AIH2 Curated Dataset — Data Dictionary

One row = one reported experimental condition for aqueous aluminum–water hydrolysis.
Scope is locked by the concept foundation: aqueous Al hydrolysis only.

## Targets

| Column | Type | Unit | Range | Phase | Notes |
|---|---|---|---|---|---|
| `h2_yield_pct` | float | % | 0–100 | 1 | H2 yield vs. theoretical 1.245 L H2/g Al at STP |
| `max_rate_ml_min_g` | float | mL·min⁻¹·g⁻¹ | ≥0 | 2 | reserved, nullable |
| `t80_min` | float | min | ≥0 | 2 | time to 80% conversion; reserved, nullable |

## Numeric features

| Column | Type | Unit | Notes |
|---|---|---|---|
| `temperature_k` | float | K | reaction temperature |
| `alkali_conc_mol_l` | float | mol/L | alkali (NaOH/KOH) concentration; 0 if none |
| `particle_size_d50_um` | float | µm | median (D50) particle size |
| `activator_ratio` | float | – | activator-to-Al mass ratio |

## Alloy composition (wt%) — `absent=0` vs `unreported=NaN`

| Column | Type | Unit | Rule |
|---|---|---|---|
| `al_wt_pct`, `ga_wt_pct`, `in_wt_pct`, `sn_wt_pct`, `bi_wt_pct`, `mg_wt_pct`, `zn_wt_pct` | float | wt% | **`0` means the element is absent; `NaN` means the study did not report it.** Tree models keep NaN. |

## Categorical features

| Column | Levels |
|---|---|
| `alkali_type` | NaOH, KOH, none |
| `activation_method` | ball_milling, plasma, liquid_metal, none |
| `water_type` | DI, tap, sea, alkaline |
| `morphology_flag` | powder, flake, nano, foil |
| `system_class` | pure_al_alkali, al_alloy, mechanically_activated, liquid_metal_activated, waste_al |

`system_class` is the central analysis axis (real vs. artifact contradiction).

## Group key

| Column | Type | Notes |
|---|---|---|
| `study_id` | str (DOI) | grouping unit for GroupKFold / LOSO; never split across train/test |

## Provenance

| Column | Notes |
|---|---|
| `source_ref` | table/figure reference within the source |
| `extractor` | who/what extracted the row |
| `extraction_date` | ISO date |
| `extraction_method` | table, webplotdigitizer |

## Quality / heterogeneity

| Column | Levels / Notes |
|---|---|
| `measurement_method` | water_displacement, mass_loss, pressure, gc |
| `temperature_control` | isothermal_bath, uncontrolled, self_heating |
| `vessel_type` | open, closed |
| `rate_definition` | initial, avg, max |
| `value_origin` | reported, derived |
| `quality_tier` | A, B, C (composite quality; enables high-quality-only sensitivity run) |

## N thresholds

- Hard floor to model at all: **150 rows**.
- Target: **~300 rows** (range 300–500) from ~40–80 studies.
- Any `system_class` with **< 40 rows** is **exploratory-only** (no headline claims).

## Current file

`data/curated/fixture_v0.csv` is a **synthetic, schema-conforming fixture** used to develop and
test the pipeline before real literature extraction (WP1). It is clearly labeled synthetic and
will be replaced by the real curated dataset.
