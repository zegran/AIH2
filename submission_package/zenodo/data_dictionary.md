# AIH2 Curated Dataset — Data Dictionary

One row = one reported experimental condition for aqueous aluminum–water hydrolysis.
Scope is locked: aqueous Al hydrolysis only.

## Targets

| Column | Type | Unit | Range | Notes |
|---|---|---|---|---|
| `h2_yield_pct` | float | % | 0–100 | H₂ yield vs. theoretical 1244 mL g⁻¹ (pure Al at STP) |
| `max_rate_ml_min_g` | float | mL·min⁻¹·g⁻¹ | ≥0 | reserved; mostly null |
| `t80_min` | float | min | ≥0 | time to 80% conversion; reserved; mostly null |

## Numeric features

| Column | Type | Unit | Notes |
|---|---|---|---|
| `temperature_k` | float | K | reaction temperature |
| `alkali_conc_mol_l` | float | mol/L | alkali (NaOH/KOH) concentration; 0 if none |
| `particle_size_d50_um` | float | µm | median (D50) particle size |
| `activator_ratio` | float | — | activator-to-Al mass ratio |

## Alloy composition (wt%) — absent = 0, unreported = NaN

| Column | Type | Unit | Rule |
|---|---|---|---|
| `al_wt_pct`, `ga_wt_pct`, `in_wt_pct`, `sn_wt_pct`, `bi_wt_pct`, `mg_wt_pct`, `zn_wt_pct` | float | wt% | **`0` = element absent; `NaN` = study did not report it.** Tree models use native NaN pathways. |

## Categorical features

| Column | Levels |
|---|---|
| `alkali_type` | NaOH, KOH, none |
| `activation_method` | ball_milling, plasma, liquid_metal, none |
| `water_type` | DI, tap, sea, alkaline |
| `morphology_flag` | powder, flake, nano, foil |
| `system_class` | pure_al_alkali, al_alloy, mechanically_activated, liquid_metal_activated, waste_al |

`system_class` is the central analysis axis (real vs. methodological contradiction).

## Group key

| Column | Type | Notes |
|---|---|---|
| `study_id` | str (DOI) | grouping unit for GroupKFold / LOSO; never split across train/test |

## Provenance

| Column | Notes |
|---|---|
| `source_ref` | table/figure reference within the source paper |
| `extractor` | who/what extracted the row |
| `extraction_date` | ISO date |
| `extraction_method` | table, webplotdigitizer |

## Quality / heterogeneity covariates

| Column | Levels / Notes |
|---|---|
| `measurement_method` | `water_displacement`, `other`, `pressure`, `mass_flow`, `gc`; NaN = not reported. `other` covers closed-syringe piston and similar non-classic displacement setups. |
| `temperature_control` | `isothermal_bath`, `self_heating`. NaN not present (fully covered). Note: the `uncontrolled` category was eliminated after independent-agent re-extraction identified two coding errors (see README). |
| `vessel_type` | open, closed |
| `rate_definition` | initial, avg, max |
| `value_origin` | reported, derived |
| `quality_tier` | A, B, C — composite quality score; enables high-quality-only sensitivity analysis |

## Scope (locked)

Aqueous aluminum–water/alkaline hydrolysis for H₂ only. Out of scope: electrolysis, photocatalysis, non-aqueous routes.

## Source file

`aih2_v1.csv` — 315 yield rows from 31 independent studies, 30 columns per row.
`rate_extraction.csv` — 76 kinetic rows (activation energies, peak rates, rate constants, t₈₀).
