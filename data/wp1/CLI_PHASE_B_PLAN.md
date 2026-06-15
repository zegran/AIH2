# CLI Command — AIH2 WP1 Phase B (condition-level extraction) detailed plan

> Paste into Claude Code at the AIH2 repo root. Anchored on the readiness report:
> **59 in-scope studies, 100% full text in hand**; per class — pure_al_alkali 18,
> mechanically_activated 11, waste_al 11, liquid_metal_activated 10, al_alloy 9.
> Goal of Phase B: turn the archive into the real curated dataset. **Only extracted, QC'd rows
> count.** Durable artifacts in English.

---

## Targets (locked)

- **Total rows:** ~300 (range 300–500). **Hard floor 150** to model at all.
- **Per-class row targets** (each must clear ≥40 to make headline claims; below 40 = exploratory-only):
  - pure_al_alkali → ~80 · mechanically_activated → ~55 · waste_al → ~55 ·
    liquid_metal_activated → ~50 · al_alloy → ~45.
- Schema: rows map **1:1** to `data/curated/fixture_v0.csv` header (the pipeline reads this).
- Scope lock unchanged: aqueous Al-water hydrolysis only; no Mg/acid/non-aqueous rows.

---

## Step 0 — Pre-flight housekeeping (do first, commit separately)

1. **Reconcile to ONE canonical 59-study list.** The batch manifests disagree slightly
   (report 59 vs 61 PDFs vs 58 master_dois rows). Produce `data/wp1/canonical_studies.csv`
   (citekey, doi, system_class, has_pdf, has_md_text, quality_tier_provisional) as the single
   source of truth. Resolve duplicates/`_v2` and confirm the count is exactly 59. Per-class
   counts must equal 18/11/11/10/9.
2. **Fix the git working tree.** With no git process running, remove `.git/index.lock`; add a
   `.gitattributes` normalizing line endings (`* text=auto eol=lf`) so the ~100 CRLF-only
   "modified" files stop appearing as changes; re-stage cleanly.
3. **Generate extracted text for PDFs lacking it.** ~20 archived PDFs have no `data/raw/literature/md/`
   text. Run text extraction (pdfplumber/pymupdf) → `data/raw/literature/md/<citekey>.md` so every
   study has machine-readable text for table location. Flag scanned/image-only PDFs for OCR.
4. **Provenance/integrity note (Sci-Hub batch).** The numerical data extracted from any paper is
   not copyrightable — extract and cite normally. But do **not** redistribute Sci-Hub-sourced PDFs
   (keep `data/raw/` gitignored; never push PDFs to GitHub/Zenodo). For the studies actually used
   in the final dataset, record a `legit_access_todo` flag in `canonical_studies.csv` for papers
   that still need a legitimate copy (library/ILL/author request) before submission.

**Gate:** canonical 59 list exists; git tree clean; every study has PDF + text; integrity flags set.

---

## Step 1 — Build the extraction workflow (before entering data)

1. **Validator script** `tools/validate_rows.py` (stdlib + pandas/openpyxl) that checks the
   `Extraction` tab of `data/wp1/AIH2_WP1_extraction_sheet.xlsx` and reports per-row errors:
   - header identical to `data/curated/fixture_v0.csv`;
   - `h2_yield_pct` numeric in [0, 100];
   - `alkali_type==none` ⇒ `alkali_conc_mol_l==0`; if alkali_type∈{NaOH,KOH} ⇒ conc>0;
   - wt% columns: value is 0 (absent), blank/NaN (unreported), or 0–100 — never negative/>100;
     enforce the **absent=0 vs unreported=NaN** distinction (flag suspicious all-zero alloy rows);
   - `system_class` ∈ {pure_al_alkali, al_alloy, mechanically_activated, liquid_metal_activated, waste_al};
   - all categorical enums valid (alkali_type, activation_method, water_type, morphology_flag,
     measurement_method, temperature_control, vessel_type, rate_definition, value_origin);
   - provenance complete: study_id (DOI), source_ref, extractor, extraction_date, extraction_method;
   - `quality_tier` ∈ {A,B,C}; `value_origin` ∈ {reported,derived};
   - Phase-2 columns (`max_rate_ml_min_g`, `t80_min`) empty;
   - output: error list + **per-`system_class` row counts** + exploratory-only flags (<40).
2. **Row-entry conventions doc** `data/wp1/EXTRACTION_GUIDE.md`: how to read a paper into rows
   (one row = one reported condition); A/B/C tier rubric (A = isothermal + clear method + reported
   value; B = minor gaps; C = single point / uncontrolled / derived); when to use
   `value_origin=derived` (e.g. yield% = volume_mL/(mass_g·1245)·100); `yang2018` → drop acid rows.
3. Wire `validate_rows.py` to run after each extraction batch (and ideally as a pre-commit check).

**Gate:** validator runs green on the existing 16 seed rows (fix any that fail).

---

## Step 2 — Calibration extraction (1 study) to measure rows/study

1. Extract **`jayaraman2015`** first (direct H1 evidence — inverted particle-size effect): enter all
   reported conditions as rows; tables manually, figure curves via WebPlotDigitizer
   (`extraction_method=webplotdigitizer`).
2. Run the validator; fix to green.
3. Record rows obtained and time taken → **rows/study estimate**. Re-project total rows and
   per-class feasibility from the measured rate.

**Gate:** one fully-validated study in the sheet; rows/study measured.

---

## Step 3 — Scale extraction, class by class

1. Work class by class toward the per-class targets, **A-tier (parametric, well-documented) studies
   first** so each class banks high-quality rows early.
2. Prioritize within-scope contradiction evidence: `martinezv2026` (H1 inverted-U + SCM),
   `davies2022mat` / `manilevich2020` (rate–yield), `meroueh2020` (grain-size × liquid metal, H1).
3. Keep `study_id` = confirmed DOI (from `master_dois.csv`); never split a study across train/test.
4. After ~15–20 studies, recompute per-class rows; if a class is tracking below 40, flag it and
   pull more of its studies forward (or accept exploratory-only and document it).

**Gate:** ≥150 total rows AND each class either ≥40 or explicitly flagged exploratory-only.

---

## Step 4 — Quality control (credibility layer)

1. **Double-extract a random 10–15% of rows independently**; compute extraction error
   (mean abs. diff on `h2_yield_pct`, disagreement rate on categoricals) → `data/wp1/qc_double_extraction.csv`
   + a short summary table. This pre-empts the "contradiction = extraction artifact" objection.
2. Confirm A/B/C tiers are applied consistently; produce the per-class N report.
3. Verify no out-of-scope rows leaked in.

**Gate:** extraction-error table exists; QC summary written.

---

## Step 5 — Integrate and rerun the pipeline

1. At ≥150 rows (target ~300): write the curated file to `data/curated/aih2_v1.csv`; update
   `data/data_dictionary.md` (note real data replaces the synthetic fixture).
2. Point Hydra `data.path` (in `run/conf/config.yaml`) at the new file — **no code changes**.
3. Rerun WP2–WP4: leakage-controlled CV (GroupKFold/LOSO by `study_id`), SHAP main+interaction,
   Arrhenius Eₐ per `system_class`. Confirm the **optimism gap** (≈0 on synthetic) is now meaningful.
4. Run the **high-quality-only (A-tier) sensitivity rerun** — the decisive real-vs-artifact test.

**Gate:** pipeline produces real metrics + SHAP + Arrhenius on real data; optimism gap reported.

---

## Rules
- Every row fully provenanced + tiered before it counts. Validator must pass before commit.
- `absent=0` ≠ `unreported=NaN` in all wt% columns — never conflate.
- Leave Phase-2 columns blank. Keep raw PDFs gitignored; never redistribute Sci-Hub PDFs.
- All identifiers/notes/reports in English. Conventional Commits, small logical commits.

## Definition of done (Phase B)
- ≥150 rows (target ~300), each class ≥40 or flagged exploratory-only.
- `validate_rows.py` green; `qc_double_extraction.csv` + per-class N report present.
- Curated file in `data/curated/`, Hydra repointed, WP2–WP4 rerun, optimism gap + A-tier
  sensitivity reported.
- Suggested commits: `feat(tools): row validator + extraction guide` · `feat(data): extract <citekey> (N rows)` · `feat(data): curated v1 (NNN rows) + repoint pipeline`.
