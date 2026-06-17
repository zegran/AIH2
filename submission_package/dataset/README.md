# AIH2 — Aluminum–Water Hydrolysis Hydrogen dataset (v1.0.0)

A provenance-tracked dataset for hydrogen production by **aluminum–water hydrolysis**, assembled from
the published literature for cross-study analysis. It accompanies the paper *"Apparent Contradictions
in the Aluminum–Water Hydrolysis Literature are Predominantly Methodological: a Provenance-Tracked,
Leakage-Controlled Analysis"* (D. Unal).

- **License:** CC-BY-4.0 (see `LICENSE_CC-BY-4.0.txt`)
- **Version:** 1.0.0
- **Author:** Dogukan Unal (ORCID 0009-0006-5102-8013), IPEC, Industrial Project Engineering
  Consulting, Çankaya, Ankara, Türkiye
- **Code & reproducible pipeline:** <https://github.com/zegran/AIH2> (MIT-licensed)

## Files in this bundle

| File | Rows × cols | Unit of a row | Contents |
|---|---|---|---|
| `aih2_v1.csv` | 315 × 30 | one experimental **condition** | H₂ yield + physical/categorical parameters + provenance + quality metadata |
| `rate_extraction.csv` | 76 × 14 | one **kinetic measurement** | activation energy (35), peak rate (30), rate constant (6), t₈₀ (5) — reported or re-fit |
| `data_dictionary.md` | — | — | full column definitions for both tables |
| `LICENSE_CC-BY-4.0.txt` | — | — | dataset license |
| `CITATION.cff` | — | — | how to cite |

The yield table and the kinetic table are **kept separate and never merged**: different units of
analysis, provenance, and quality fields.

## Yield table (`aih2_v1.csv`) — highlights

- **Target:** `h2_yield_pct` — H₂ yield as % of the 1244 mL g⁻¹ pure-Al theoretical maximum.
- **Grouping key:** `study_id` (study DOI).
- **Regime label:** `system_class` ∈ {`pure_al_alkali`, `al_alloy`, `mechanically_activated`,
  `liquid_metal_activated`, `waste_al`}.
- **Methodology covariates:** `temperature_control`, `measurement_method`, `water_type`,
  `vessel_type`, `activation_method`, `morphology_flag`.
- Per-class composition: `pure_al_alkali` 162 rows / 9 studies, `mechanically_activated` 69 / 6,
  `al_alloy` 45 / 3, `waste_al` 20 / 8, `liquid_metal_activated` 19 / 5.
- **Missing-value convention:** absent quantities encoded as `0`; *unreported* quantities left
  missing — never conflated.

## Kinetic table (`rate_extraction.csv`) — highlights

- `kinetic_metric` ∈ {`ea_kj_mol`, `max_rate`, `rate_k`, `t80`}; `value`, `unit`.
- Fit metadata: `n_temperatures`, `temp_range_k`, `fit_method`; `value_origin` (author-reported vs
  independently re-fit); `quality_tier`, `source_ref`, `notes`.

## Provenance & quality control

- Every value traces to a study DOI and a table/figure source.
- Double extraction of ≈16% of yield rows → 52/52 exact agreement.
- `system_class` re-derived for all 31 studies from source.
- Digitized kinetic points re-read independently (≈1.5% point error).
- Arrhenius fit gate: studies failing R² ≥ 0.90 over ≥ 3 temperatures were dropped, not forced.

## Scope (locked)

Aqueous aluminum–water/alkaline hydrolysis for H₂. **Out of scope:** electrolysis, electrocatalytic
water splitting, photocatalysis, non-aqueous routes. The dataset is observational; analyses on it are
**associational, not causal**, and powered at n ≈ 31 studies (3–9 per regime).

## How to cite

See `CITATION.cff`. Please cite both this dataset (Zenodo DOI, minted on deposit) and the
accompanying paper.
