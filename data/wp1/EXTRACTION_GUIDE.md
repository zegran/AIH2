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
- **Yield > 100% rule (decided 2026-06-15):** a reported/derived yield exceeding 100% of the
  *pure-Al* theoretical (1244 mL/g) — common for waste/dross with co-reactive Zn/Ni/Mg — is
  **EXCLUDED**. It signals a contaminated yield basis, not a clean Al-hydrolysis yield. The
  validator enforces `h2_yield_pct ∈ [0,100]`. Document such studies as waste_al heterogeneity.

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

## system_class assignment (decision rules — verified by audit 2026-06-16)
`system_class` is the **central analysis axis**; assign it from how the Al was *prepared*, not from
the reaction medium. Decide in this order:
1. **waste_al** — feedstock is waste/scrap/dross/recycled Al (cans, machining chips, industrial
   dross, construction scrap). **Waste source wins** even if later ball-milled or alkali-treated
   (e.g. `buryakov2023met`, `ho2016`, `urbonav2024`, `gupta2025` scrap-alloy dust).
2. **liquid_metal_activated** — Al activated by a **gallium-based liquid metal / eutectic**
   (Ga, Ga-In, Ga-In-Sn/Galinstan, Ga-In-Zn, gallam). ⚠️ **This wins over mechanically_activated
   even when the eutectic is milled into the Al** — the gallium penetrating grain boundaries is the
   activator, milling is just the contacting method (`dudoladov2016`, `ilyukhina2012`,
   `jayaraman2015`, `fischman2020`, `lu2017`). **But** a *minor* Ga dopant (~1 wt%) among several
   milled additives (In/Sn/Bi₂O₃) is **not** a eutectic-activation system → mechanically_activated
   (`guan2019`).
3. **al_alloy** — Al **melt-alloyed/cast** with other metals (induction/furnace melting, then
   cast/atomized). Gas atomization of a co-melted Al-Bi/Al-Sn melt is still al_alloy
   (`qiao2019`, `liuyh2017`, `meng2022`).
4. **mechanically_activated** — Al **ball-milled** with Bi/Sn/In/salt/carbon additives into a
   composite (no gallium eutectic, no melting). XRD typically shows "no alloy formed during milling".
5. **pure_al_alkali** — commercial/pure unalloyed Al (foil/powder/granule/nano) with **no** alloying
   or activation. A catalyst in the **solution** (Al(OH)₃, Ni-B, Ni-Li-B) keeps the row here as long
   as the Al metal itself is unmodified.

## Scope & special cases
- **In scope:** aqueous Al-water hydrolysis only. **Never** enter Mg/acid/non-aqueous rows.
- `yang2018` → keep alkaline/neutral rows, **drop acid-media rows**.
- Saline/seawater studies (`lu2017`, `buryakov2024`) → `water_type=sea`.
- `study_id` = DOI is the **CV grouping key** — never split one study across train/test.

## Targets (locked)
Total ~300 rows (floor 150). Per class: pure_al_alkali ~80 · mechanically_activated ~55 ·
waste_al ~55 · liquid_metal_activated ~50 · al_alloy ~45. A class with <40 rows is
**exploratory-only** (declared honestly, never padded).
