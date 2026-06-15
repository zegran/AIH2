# Dataset Balance Notes (WP2+ modeling)

Durable notes on known imbalances in `extraction_rows.csv` and how they MUST be handled at
modeling time. Recorded during Phase B extraction; binding for WP2-WP4.

## 1. Single-study dominance — `porciuncula2012`

- **Fact:** `porciuncula2012` (DOI `10.1590/s0104-66322012000200014`) contributes **120 of 315
  rows (~38%)** — a clean tier-A NaOH/KOH × foil/0.5 mm/1 mm × T × concentration factorial on
  pure Al. The data is real and high quality; the issue is purely *weighting / leakage geometry*.
- **Why it matters:** `study_id` is the **GroupKFold / LOSO grouping key**. One group holding ~38%
  of all rows means (a) any fold containing porciuncula is dominated by it, and (b) an unweighted
  fit lets one study's alkaline-pure-Al regime (high yield, no particle size, no composition
  variation) pull the global model.
- **Required mitigations (both, at modeling time):**
  1. **Group-balanced sample weighting.** Weight each row by `1 / n_rows(study_id)` (or a capped
     variant), so every study contributes comparably to the loss regardless of row count. Report
     the weighting scheme in WP2.
  2. **Leave-porciuncula-out sensitivity run.** Refit the full pipeline with porciuncula excluded
     and confirm the headline findings (H1 size effect, rate-yield trade-off, Arrhenius Ea) are
     unchanged in sign and direction. A finding that flips without porciuncula is not robust.
- **Do NOT** silently drop porciuncula in the main model — it carries the cleanest
  alkali-type × concentration × temperature signal (directly relevant to the contradictory-
  parameter thesis). Manage its weight; don't discard its signal.
- **Decision provenance:** user chose "take all 120" on 2026-06-15 after being shown the ~38%
  share and the CV-group-imbalance trade-off.

## 2. Exploratory-only classes (<40 rows)

- `waste_al` (20) and `liquid_metal_activated` (13) are below the 40-row exploratory threshold.
  Per the locked target rule, any per-class claim for these two is **exploratory-only** and must
  be declared as such — never padded. Class-level SHAP/ALE for these two is descriptive, not
  confirmatory. `liquid_metal_activated` is figure-heavy; reaching 40 needs figure digitization.

## 3. Morphology gap in `porciuncula2012` plate rows

- 80 of the 120 porciuncula rows are 0.5 mm / 1 mm **plate**, which is not in the `morphology_flag`
  enum {powder,flake,nano,foil} → left **blank**. Treat blank morphology as missing (not a level);
  do not impute "powder". Foil rows (40) carry `morphology_flag=foil`.

## 4. Reported-% vs pure-Al basis (`zhang2024` 3 µm rows)

- `zhang2024` 3 µm rows report mL/g > 1244 yet the study's own yield % is ≤100. We kept the
  study-reported %, treating it as the study's internal yield basis (same situation that put
  `irankhah2018` on hold). Flag in any cross-study volume reconciliation.
