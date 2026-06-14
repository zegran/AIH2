# AIH2 — WP1 Progress Update & CLI Handoff

> **Purpose.** Bring the CLI (Claude Code) up to date on the **WP1 → step 1 (source-pool
> construction)** work completed in Cowork, and hand off the next, well-defined batch of
> tasks. Paste this file (or point the CLI at it) to onboard the agent. This supersedes the
> WP1 status in the original handoff briefing; the immutable scientific core is unchanged.

---

## 0. Status delta since the original handoff

| WP | Before | Now |
|----|--------|-----|
| WP0 — Scaffold | ✅ done | ✅ done |
| **WP1 — Source pool & extraction** | 🔜 not started | 🟡 **step 1–3 done, extraction in progress** |
| WP2–WP6 | unchanged | unchanged |

**WP1 is no longer a blank page.** A screened, provenance-tracked source pool now exists, the
extraction sheet is built and schema-locked, and the first rows are entered.

---

## 1. What WP1 produced (all under `data/wp1/`)

- `AIH2_WP1_source_pool.xlsx` — screened pool. Tabs: `README`, `Source_Pool` (IN-scope,
  filterable, with rationale + `system_class` + Consensus links), `Background_Excluded`,
  `Per_Class_Summary` (live counts).
- `AIH2_WP1_extraction_sheet.xlsx` — extraction workbook. Tabs: `README`, `Field_Guide`,
  `Extraction`. Columns map **1:1 to `data/curated/fixture_v0.csv`**. Dropdown validation on
  all categoricals. `absent=0` vs `unreported=NaN` rule enforced.
- `AIH2_WP1_source_pool.md` — human-readable pool summary + contradiction evidence.
- `extractions_v0.csv` — the 16 seed rows as raw CSV (same header as the fixture).

### Numbers
- **82** candidates screened via Consensus across 5 axes (particle size · alkali/temperature ·
  alloy/activator · waste-Al/activation · kinetics/SCM).
- **71 IN-scope** studies, **11** background/excluded.
- By `system_class` (studies): `pure_al_alkali` 26 · `waste_al` 16 ·
  `mechanically_activated` 15 · `al_alloy` 10 · `liquid_metal_activated` 4.
- **16 seed extraction rows** (headline/abstract-level, mostly tier **C**, fully provenanced).

### Contradiction signal already visible (good for the thesis)
- **Direction-changing particle size (H1):** `jayaraman2015` (30 µm < 350 µm yield),
  `martinezv2026` (inverted-U vs size, SCM R²≈0.999).
- **Eₐ spread (H3):** ~10→158 kJ/mol across the pool, bracketing the 3.5–102.6 band.
- **Rate–yield trade-off:** `davies2022mat` (Zn slows rate, keeps 99.5% yield),
  `manilevich2020` (Bi lowers rate).

---

## 2. Known limitations to fix (do not skip)

1. **`study_id` holds citekeys, not DOIs.** Schema/pipeline expect DOI as the
   GroupKFold/LOSO grouping key. Replace citekey → confirmed DOI on PDF retrieval.
2. **Seed rows are abstract-level (tier C).** Real condition-level rows require the PDFs
   (tables) and WebPlotDigitizer (figure curves). Do not treat tier-C rows as final.
3. **`buryakov2024` rows** use `water_type=sea` as the nearest level for an AlCl₃ saline
   medium — flag for review; the schema has no salt-solution level.
4. **`yang2018`** is IN *partial*: keep alkaline/neutral rows, **drop acid-media rows**.

---

## 3. Next tasks for the CLI (English, imperative)

> Precedence reminder: `concept-foundation > design-spec > implementation-plan`. Do not drift
> from the scope lock (aqueous Al hydrolysis only; no Mg/acid/non-aqueous rows in the dataset).

1. **Retrieve PDFs** for the 71 IN-scope studies (Zotero). Record the **DOI** for each and
   replace the citekey in `study_id`.
2. **Extract condition-level rows** into `data/wp1/AIH2_WP1_extraction_sheet.xlsx`
   (`Extraction` tab):
   - Tables → manual entry. Figure curves → WebPlotDigitizer (`extraction_method=webplotdigitizer`).
   - Enforce `absent=0` vs `unreported=NaN` in all wt% columns.
   - Fill `h2_yield_pct` (Phase 1 target). Leave `max_rate_ml_min_g` and `t80_min` blank (Phase 2).
   - Complete provenance (`source_ref`, `extractor`, `extraction_date`, `extraction_method`)
     and quality metadata (`measurement_method`, `temperature_control`, `vessel_type`,
     `rate_definition`, `value_origin`, `quality_tier`) on every row.
3. **Assign A/B/C quality tiers** consistently (A = isothermal + clear method + reported value;
   C = single point / uncontrolled / derived). This enables the high-quality-only sensitivity run.
4. **Double-extract a 10–15% random sample** independently; record both passes and report
   extraction error as a separate QC table.
5. **Report per-`system_class` N**; flag any class with **< 40 rows as exploratory-only**.
6. **Integrate**: when rows ≥ 150 (target ~300), write the curated file to `data/curated/`,
   update `data/data_dictionary.md`, point Hydra `data.path` at the real dataset, and rerun
   the pipeline (WP2–WP4 now produce real results, including the meaningful optimism gap).
7. **Commit** with Conventional Commits, e.g.
   `feat(data): add WP1 source pool and extraction sheet (71 studies, 16 seed rows)`.

---

## 4. Acceptance checks (run before declaring extraction done)

- [ ] `data/wp1/extraction` header is byte-identical to `data/curated/fixture_v0.csv`.
- [ ] No row has `system_class` outside the 5 locked levels; no acid/Mg/non-aqueous rows.
- [ ] All `h2_yield_pct` in [0, 100]; `alkali_type=none ⇒ alkali_conc_mol_l=0`.
- [ ] Every wt% column distinguishes `0` (absent) from blank (NaN).
- [ ] Provenance complete on every row; ≥150 rows total before any modeling claim.
- [ ] Per-class N reported; exploratory-only flags set.

---

*Generated in Cowork, WP1 step 1. Durable artifacts are English per project convention;
Turkish is for conversation/vault notes only.*
