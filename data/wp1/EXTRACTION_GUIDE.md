# WP1 Phase B — Extraction Guide

How to turn an archived study into validated rows for the curated dataset. **One row = one
reported experimental condition.** Every row must pass `tools/validate_rows.py` before it counts.

## Workflow per study
1. Open `data/raw/literature/pdf/<citekey>.pdf` (+ extracted `…/md/<citekey>.md` for text/table
   location). Find every distinct reported condition (a temperature, alkali conc, particle size,
   alloy/activator combination, etc.) with a measured H2 outcome.
2. Tables → enter manually. Figure curves → digitize with **WebPlotDigitizer**; set
   `extraction_method=webplotdigitizer` (else `table`).
3. Enter one row per condition into `AIH2_WP1_extraction_sheet.xlsx` (`Extraction` tab); header is
   byte-identical to `data/curated/fixture_v0.csv`.
4. Run `uv run python tools/validate_rows.py <export.csv>` → fix all ERRORs (WARNs are advisory).

## Target column (`h2_yield_pct`)
- Yield % vs. the theoretical **1.245 L H2 per gram Al at STP**. If a study reports volume,
  derive: `yield% = volume_mL / (mass_Al_g * 1245) * 100` and set `value_origin=derived`.
- Leave `max_rate_ml_min_g` and `t80_min` **blank** (Phase 2).

## The cardinal rule: `absent = 0` vs `unreported = NaN`
- A wt% (or any) field is **`0`** only when the source states the element/quantity is **absent**.
- It is **blank (NaN)** when the source **does not report** it. Never write 0 for "not mentioned."
- Example: a pure-Al-alkali run → `ga_wt_pct=0` (truly no gallium); but if a study uses NaOH and
  never gives the molarity → `alkali_conc_mol_l` is **blank**, not 0 (validator WARNs, not errors).

## Quality tier (`quality_tier` ∈ A/B/C)
- **A** — isothermal/controlled temperature + clearly described method + directly reported value.
- **B** — minor gaps (e.g., value read from a clear figure; one metadata field inferred).
- **C** — single data point, uncontrolled temperature, derived/abstract-level, or weak provenance.
- The A-tier subset drives the **high-quality-only sensitivity run** (real-vs-artifact test).

## Provenance (every row, all required)
`study_id` = confirmed **DOI** (from `master_dois.csv`/`canonical_studies.csv`) · `source_ref`
(table/figure id) · `extractor` · `extraction_date` (ISO) · `extraction_method`.

## Metadata enums (validator-enforced)
- `alkali_type` {NaOH,KOH,none} · `activation_method` {ball_milling,plasma,liquid_metal,none} ·
  `water_type` {DI,tap,sea,alkaline} · `morphology_flag` {powder,flake,nano,foil} ·
  `system_class` {pure_al_alkali,al_alloy,mechanically_activated,liquid_metal_activated,waste_al}.
- `measurement_method` {water_displacement,mass_loss,pressure,gc} · `temperature_control`
  {isothermal_bath,uncontrolled,self_heating} · `vessel_type` {open,closed} · `rate_definition`
  {initial,avg,max} · `value_origin` {reported,derived}.

## Scope & special cases
- **In scope:** aqueous Al-water hydrolysis only. **Never** enter Mg/acid/non-aqueous rows.
- `yang2018` → keep alkaline/neutral rows, **drop acid-media rows**.
- Saline/seawater studies (`lu2017`, `buryakov2024`) → `water_type=sea`.
- `study_id` = DOI is the **CV grouping key** — never split one study across train/test.

## Targets (locked)
Total ~300 rows (floor 150). Per class: pure_al_alkali ~80 · mechanically_activated ~55 ·
waste_al ~55 · liquid_metal_activated ~50 · al_alloy ~45. A class with <40 rows is
**exploratory-only** (declared honestly, never padded).
