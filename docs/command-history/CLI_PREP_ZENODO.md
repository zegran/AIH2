# CLI Command — Prepare the Zenodo deposit (both routes), 100% pre-filled

> Paste into Claude Code at the AIH2 repo root. Goal: make the Zenodo deposit require zero writing
> from the user — prepare the exact files and the exact metadata for BOTH routes. The user only
> uploads + clicks Publish (their account; we cannot publish for them). No fabrication; author =
> Dogukan Unal (ORCID 0009-0006-5102-8013, IPEC, Çankaya, Ankara, Türkiye).

## Route A (recommended) — dataset-only record (clean; excludes the unpublished manuscript)
1. Build a self-contained bundle `release/aih2_dataset_v1/` containing ONLY:
   - `aih2_v1.csv` (315 yield rows) · `rate_extraction.csv` (76 kinetic rows)
   - `data_dictionary.md` (schema) · `README.md` (dataset card: scope lock, provenance, QC summary,
     per-class N, column definitions, units, `absent=0` vs `unreported=NaN` rule)
   - `LICENSE_CC-BY-4.0.txt` · `CITATION.cff`
   - (optional, for reproducibility) `wp5_figures.py` + `pubstyle.py` copy.
   Zip it to `release/aih2_dataset_v1.zip`.
2. Write `release/ZENODO_METADATA.md` — a ready-to-paste block with EXACT values:
   - **Title:** Aluminum–Water Hydrolysis Hydrogen-Yield and Kinetics Dataset (provenance-tracked,
     leakage-aware), v1.0
   - **Resource type:** Dataset
   - **Creators:** Unal, Dogukan — ORCID 0009-0006-5102-8013 — IPEC, Industrial Project Engineering
     Consulting, Çankaya, Ankara, Türkiye
   - **Description:** 2–3 sentences from the abstract, dataset-focused (what it is, 315+76 rows /
     31 studies, QC'd, scope = aqueous Al–water hydrolysis, intended for leakage-controlled ML).
   - **License:** Creative Commons Attribution 4.0 (CC-BY-4.0)
   - **Keywords:** aluminum–water hydrolysis; hydrogen production; curated dataset; machine learning;
     data leakage; reproducibility; reaction kinetics
   - **Version:** 1.0.0 · **Language:** English
   - **Related identifiers:** "is supplement to" → GitHub `https://github.com/zegran/AIH2`;
     leave a slot "is supplement to → [paper DOI when available]".
3. Write `release/ZENODO_STEPS.md` — click-path: zenodo.org → New upload → drag the zip →
   paste each metadata field from ZENODO_METADATA.md → Publish → copy the minted DOI.

## Route B (one-click) — whole-repo GitHub Release via the integration the user already enabled
1. Ensure `.zenodo.json` (repo root) is complete and accurate (title, creators with ORCID, license
   CC-BY-4.0, keywords, description) — Zenodo reads it automatically on release.
2. Write `release/ZENODO_STEPS.md` (Route B section): GitHub → Releases → Draft a new release →
   tag `v1.0.0` → Publish release → Zenodo auto-archives the **entire repo** + mints the DOI.
   ⚠️ Note in the steps: this publishes everything in the repo (incl. the unpublished manuscript and
   `docs/command-history/`); prefer Route A if that is not desired.

## After either route
- The user pastes the minted **DOI** back; a follow-up command replaces `\todo{Zenodo DOI}` in the
  paper (Data Availability + conclusion) and adds the dataset DOI to `CITATION.cff` / references.

## Rules / Definition of done
- `release/aih2_dataset_v1.zip` + `ZENODO_METADATA.md` + `ZENODO_STEPS.md` + verified `.zenodo.json`
  committed + pushed. Bundle contains only the intended data/docs (no manuscript in Route A).
- All metadata pre-filled verbatim; user action reduced to upload + Publish. Report both routes and
  recommend Route A. Stop for the user to deposit and return the DOI.
