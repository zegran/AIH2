# WP1 — Literature Source Pool

> Canonical note for the WP1 literature source pool and extraction state. Built in Cowork
> (WP1 step 1). Source of truth artifacts: `data/wp1/` (handoff:
> `data/wp1/WP1_PROGRESS_AND_CLI_HANDOFF.md`). Linked from [[00-Hub]]; scope governed by
> [[concept-foundation]].

## State
WP1 step 1–3 done: screened pool + schema-locked extraction sheet + 16 seed rows.
**Ingest done for the first download batch: 35/71 IN-scope studies have full text archived**
(`data/raw/literature/`, gitignored) with `vault/Papers/` stubs and resolved DOIs. 36 studies
still to retrieve (see `data/wp1/INGEST_GAP_REPORT.md`). Condition-level extraction in progress.
Hard floor 150, target ~300; switch the curated dataset only at ≥150 rows.

### Obtained vs missing (after Sci-Hub batch 2 → 46/71 in hand, 25 missing)
- pure_al_alkali 20/26 · al_alloy 6/10 · mechanically_activated 9/15 ·
  liquid_metal_activated 3/4 · waste_al 8/16. (batch 2 added 11; see `STILL_MISSING_25.md`.)
- Earlier snapshot (after first ingest, 35/71): pure_al_alkali 15 · al_alloy 4 ·
  mechanically_activated 9 · liquid_metal_activated 3 · waste_al 4.
- **At-risk for ≥40 rows:** al_alloy, liquid_metal_activated, waste_al (few obtained studies).
- **Priority missing (contradiction evidence):** `martinezv2026` (H1 inverted-U),
  `davies2022mat` (rate–yield), `manilevich2020` (rate–yield).
- Ingest artifacts: `data/wp1/ingest_manifest.csv`, `INGEST_GAP_REPORT.md`, `resolved_dois.csv`.

### Phase A — full citations of the 36 missing (DOIs resolved)
`data/wp1/PHASE_A_MISSING_36.md` (+ `phase_a_missing_36.csv`): Crossref-resolved, verified DOIs.
**33/36 have a DOI** (7 confirmed-bib, 6 verified-high, 18 medium, 2 preprint); **3 unresolved**
(`saroukanian2020`, `manilevich2021b` book chapter, `singh2019`). Next: per-DOI Unpaywall/OA
reachability check (access-gated, OA-only).

## Artifacts (`data/wp1/`)
- `AIH2_WP1_source_pool.xlsx` — screened pool (Source_Pool / Background_Excluded /
  Per_Class_Summary tabs).
- `AIH2_WP1_extraction_sheet.xlsx` — extraction workbook; columns map 1:1 to
  `data/curated/fixture_v0.csv`; dropdown validation; `absent=0` vs `unreported=NaN` enforced.
- `AIH2_WP1_source_pool.md` — human-readable pool + contradiction evidence.
- `extractions_v0.csv` — 16 seed rows (header byte-identical to the fixture; verified).

## Numbers
- 82 candidates screened via Consensus across 5 axes (particle size; alkali/temperature;
  alloy/activator; waste-Al/activation; kinetics/SCM).
- **71 IN-scope**, 11 background/excluded.
- Studies per `system_class`: `pure_al_alkali` 26 · `waste_al` 16 · `mechanically_activated` 15
  · `al_alloy` 10 · `liquid_metal_activated` 4.
- 16 seed extraction rows (abstract-level, mostly tier C, fully provenanced).

## Contradiction evidence already visible (supports the thesis)
- **H1 — direction-changing particle size:** `jayaraman2015` (30 µm yields more than 350 µm);
  `martinezv2026` (inverted-U vs size, SCM R²≈0.999).
- **H3 — Eₐ spread:** ~10→158 kJ/mol across the pool, bracketing the 3.5–102.6 band.
- **Rate–yield trade-off:** `davies2022mat` (Zn slows rate, keeps 99.5% yield);
  `manilevich2020` (Bi lowers rate).

## Known limitations to fix (do not skip)
1. `study_id` holds **citekeys, not DOIs** — replace with confirmed DOI on PDF retrieval
   (DOI is the GroupKFold/LOSO grouping key).
2. Seed rows are **tier-C abstract-level** — real condition-level rows need PDFs (tables) +
   WebPlotDigitizer (figure curves). Not final.
3. `buryakov2024` uses `water_type=sea` as nearest level for an AlCl₃ saline medium — flag for
   review (schema has no salt-solution level).
4. `yang2018` is IN **partial**: keep alkaline/neutral rows, drop acid-media rows.

## Acceptance checks before declaring extraction done
- Extraction header byte-identical to `data/curated/fixture_v0.csv` (✓ for seed CSV).
- No `system_class` outside the 5 locked levels; no acid/Mg/non-aqueous rows.
- All `h2_yield_pct` in [0,100]; `alkali_type=none ⇒ alkali_conc_mol_l=0`.
- Every wt% column distinguishes `0` (absent) from blank (NaN).
- Provenance complete on every row; ≥150 rows before any modeling claim.
- Per-`system_class` N reported; any class <40 rows flagged exploratory-only.

## Next (CLI)
Retrieve PDFs (DOIs) → extract condition-level rows → assign A/B/C tiers → double-extract
10–15% QC → report per-class N → integrate to `data/curated/` at ≥150 rows and rerun WP2–WP4.
See `README.md` WBS and `plan/2026-06-14-aih2-design-spec.md` for status and rules.
