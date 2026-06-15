# Double-Extraction QC Round (2026-06-15)

Independent second-pass re-extraction to estimate the extraction error rate of
`extraction_rows.csv`. Each study was re-extracted from scratch by a fresh agent with no access to
the original rows; results were diffed against the committed data and adjudicated against the
source.

## Sample (52 rows ≈ 16.5% of 315), stratified by class + risk type

| study | class | rows | risk type sampled |
|---|---|---|---|
| porciuncula2012 (Table 5) | pure_al_alkali | 20 | dominant study + my programmatic transcription |
| zhang2024 | pure_al_alkali | 10 | reported %, clean grid, H1 size effect |
| davies2022mat | mechanically_activated | 10 | contradiction evidence, blank-enum edge cases |
| jayaraman2015 | liquid_metal_activated | 6 | derived mL/g→% (unit-conversion risk) |
| dudoladov2016 | (pure_al_alkali → fixed) | 6 | tier-A, sub-zero, activation classification |

## Result

- **Yield-value agreement: 52/52 EXACT (0 value errors).** Every re-extracted hydrogen-yield value
  matched the committed value to 1 decimal, including all 20 porciuncula Table-5 cells (verifying
  both the original agent's matrix AND the programmatic generation) and all 6 derived jayaraman
  mL/g→% conversions.
- **1 metadata error found and fixed (study-level):** `dudoladov2016` was classified
  `pure_al_alkali` but its material is commercial Al **milled with 10 wt% Ga-In-Zn liquid eutectic
  (60:20:20)** (source lines 183-192) — i.e. **liquid-metal-activated**. Fixed: `system_class →
  liquid_metal_activated`, `activation_method → liquid_metal`, `activator_ratio 0.111 → 0.10`
  (10 wt% of total). Composition (Ga 6 / In 2 / Zn 2, Al 90) and `particle_size_d50_um=300` (source:
  "average particle size of 300 µm", OCR'd "300 mm") were already CORRECT and kept. Canonical
  records (`canonical_studies.csv`, `master_dois.csv`) updated to match. Net: pure_al_alkali
  168→162, liquid_metal_activated 13→19.
- **2 false-alarm DOI flags:** the QC prompts for `jayaraman2015` and `dudoladov2016` carried wrong
  "fixed" DOIs (my prompt error). Both agents correctly flagged the mismatch; the **committed** DOIs
  (`10.4236/epe.2015.79041`, `10.1016/j.ijhydene.2015.11.122`) are correct and match the canonical
  records. No data change.
- **Minor tier disagreement (no change):** the QC davies agent assigned `quality_tier=A` to
  self-heating rows; the committed B/C is more correct (A requires isothermal control).

## Estimated error rates

- Value-level (the target column): **0 / 52 ≈ 0%**.
- Study-level metadata: **1 / 5 studies** had a class-label error (caught + fixed).

## Follow-up (recommended, not yet done)

- **Targeted classification audit of `pure_al_alkali` (162 rows).** dudoladov shows the provisional
  class in `canonical_studies.csv` can mislabel a gallium/eutectic-activated study as
  pure_al_alkali. Re-check the other pure_al_alkali studies for any that are actually
  liquid-metal- or mechanically-activated (look for Ga/In/Sn/Zn eutectic milling, added activators).
  This protects the central analysis axis (`system_class`) before WP2 modeling.
