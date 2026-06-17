# AIH2 dataset card

A provenance-tracked dataset for hydrogen production by **aluminum–water hydrolysis**, assembled from
the published literature for cross-study analysis. Released with the paper *"Apparent Contradictions
in the Aluminum–Water Hydrolysis Literature are Predominantly Methodological."*

- **Data license:** CC-BY-4.0  ·  **Code license:** MIT  ·  **Version:** 1.0.0
- **Full column definitions:** see [`data/data_dictionary.md`](data_dictionary.md).

## Files

| File | Rows × cols | Unit of a row | Contents |
|---|---|---|---|
| `data/curated/aih2_v1.csv` | 315 × 30 | one experimental **condition** | H₂ yield + physical/categorical parameters + provenance + quality metadata |
| `data/wp1/rate_extraction.csv` | 76 × 14 | one **kinetic measurement** | activation energy (35), peak rate (30), rate constant (6), t₈₀ (5) — reported or re-fit |

The yield table and the kinetic table are **kept separate and never merged**: they have different
units of analysis, provenance, and quality fields.

## Yield table (`aih2_v1.csv`) — schema highlights

- **Target:** `h2_yield_pct` — H₂ yield as % of the 1244 mL g⁻¹ pure-Al theoretical maximum.
- **Grouping key:** `study_id` (study DOI) — the unit for leakage-controlled evaluation.
- **Physical parameters:** `temperature_k`, `alkali_conc_mol_l`, `particle_size_d50_um`,
  `activator_ratio`, elemental composition (`al_wt_pct`, `ga_wt_pct`, `in_wt_pct`, `sn_wt_pct`,
  `bi_wt_pct`, `mg_wt_pct`, `zn_wt_pct`).
- **Regime label:** `system_class` ∈ {`pure_al_alkali`, `al_alloy`, `mechanically_activated`,
  `liquid_metal_activated`, `waste_al`} — verified against source materials/methods.
- **Methodology covariates:** `temperature_control`, `measurement_method`, `water_type`,
  `vessel_type`, `activation_method`, `morphology_flag`.
- **Provenance:** `source_ref`, `extractor`, `extraction_date`, `extraction_method`, `value_origin`.
- **Quality:** `quality_tier` ∈ {A, B, C}.

Per-class composition: `pure_al_alkali` 162 rows / 9 studies, `mechanically_activated` 69 / 6,
`al_alloy` 45 / 3, `waste_al` 20 / 8, `liquid_metal_activated` 19 / 5. **Missing-value convention:**
absent quantities are encoded as `0`; *unreported* quantities are left missing — the two are never
conflated.

## Kinetic table (`rate_extraction.csv`) — schema highlights

- `kinetic_metric` ∈ {`ea_kj_mol`, `max_rate`, `rate_k`, `t80`}; `value`, `unit`.
- Fit metadata: `n_temperatures`, `temp_range_k`, `fit_method` (e.g. Arrhenius ln k vs 1/T).
- `value_origin` distinguishes author-reported from independently re-fit values; `quality_tier`,
  `source_ref`, `notes`.

## Provenance & quality control

- Every value traces to a study DOI and a table/figure source.
- **Double extraction:** ≈16% of yield rows re-extracted independently → 52/52 exact agreement.
- **Classification audit:** `system_class` re-derived for all 31 studies from source.
- **Digitized kinetic points** re-read independently (≈1.5% point error).
- **Arrhenius fit gate:** studies failing R² ≥ 0.90 over ≥ 3 temperatures were *dropped, not forced*.

## Scope (locked)

Aqueous aluminum–water/alkaline hydrolysis for H₂. **Out of scope:** electrolysis, electrocatalytic
water splitting, photocatalysis, and non-aqueous routes. The dataset is observational (assembled from
heterogeneous published conditions); analyses on it are **associational, not causal**, and statements
are powered at n ≈ 31 studies (3–9 per regime).

## How to cite

Cite the Zenodo archive (DOI to be minted on deposit) and the paper. See the repository for the
reproducible pipeline and figure scripts: <https://github.com/zegran/AIH2>.
