# AIH2 — WP1 Data-Readiness Report (pre-extraction milestone)

*2026-06-15. Marks the end of literature-archive assembly and the start of Phase B
(condition-level extraction). Companion files: `master_dois.csv`, `ARCHIVE_CURATION.md`,
`archive_quality_52.csv`, `WP1_EXCLUDED.md`, `CONSENSUS_CANDIDATES.md`.*

## 1. Headline

**The in-scope literature archive is assembled: 59 studies, 100% full text in hand, every
`system_class` now feasible for the ≥40-row rule.** The project is ready to move from
*acquisition* to *extraction*.

## 2. Archive composition (59 active studies)

| system_class | studies | ≥40-row feasibility | notes |
|---|---|---|---|
| pure_al_alkali | 18 | ✅ ample | foundational + recent mix |
| mechanically_activated | 11 | ✅ | all reputable (IJHE/Energy/MDPI) |
| waste_al | 11 | ✅ | incl. H1 study `martinezv2026` |
| liquid_metal_activated | 10 | ✅ (was the gap at 3) | +7 from Consensus (Ga-In/EGaIn) |
| al_alloy | 9 | ✅ | +2 from Consensus (kravchenko2005, changying2017) |
| **total** | **59** | **all classes feasible** | study target (40–80) exceeded |

## 3. How it was assembled

| stage | source | added |
|---|---|---|
| Ingest 1 | initial PDF+MD batch | 35 |
| Batch 2 | Sci-Hub (OA) | 11 |
| Batch 3 | MDPI gold-OA (PDF+MD) | 6 |
| Batch 4 | Consensus search → OA + green-OA | 9 |
| Curation | removed `li2019` + `sykhyi2024` (weak venue) | −2 |
| **Active pool** | | **59** |

Raw PDFs (+ MD where available) live under `data/raw/literature/` (gitignored); each study has a
`vault/Papers/<citekey>.md` stub and a verified DOI in `master_dois.csv`.

## 4. Quality

- Original 50: ~46 are Q1/Q2 reference-grade (Elsevier IJHE/Energy/Fuel, RSC, J. Hazard. Mater.,
  J. Alloys Compd., MDPI).
- New 9 strengthen the base with **high-citation foundational** work: `kravchenko2005` (241),
  `ilyukhina2012` (119), `lu2017` (43), `fischman2020` (30), `slocum2020` (27), `parmuzina2009`
  (22), `meroueh2020` (grain-size × liquid metal → directly supports **H1**).
- One known weak venue retained for cause: `jayaraman2015` (SCIRP) — a primary H1 source; its
  rows will be quality-tier C and the venue noted in the paper's limitations.

## 5. Excluded (21 total, with ledger)

- **19 unreachable** (paywalled Elsevier/Springer or no-DOI) → `WP1_EXCLUDED.md`, do-not-resuggest.
  Still citable for motivation (reported Eₐ/yield) but contribute no extracted rows.
- **2 curation removals** (`li2019` conference proceedings, `sykhyi2024` obscure/0-cite).

## 6. Pipeline readiness (WP0)

Phase 1 scaffold is built and verified: 28 tests pass, ruff clean, end-to-end pipeline runs on a
synthetic fixture (load → grouped/LOSO CV → SHAP/ALE → Arrhenius). **Swapping the real curated
dataset in needs no code changes** — point Hydra `data.path` at it once rows land.

## 7. Readiness gates

| gate | target | status |
|---|---|---|
| Study count | 40–80 in-scope | ✅ 59 |
| Per-class study supply | each class can reach ≥40 rows | ✅ all classes |
| Source quality | peer-reviewed, tiered | ✅ A/B/C tiering ready |
| Pipeline | tested, data-swappable | ✅ |
| **Extracted rows** | **≥150 floor, ~300 target** | ⏳ **Phase B (not started)** |

## 8. Next — Phase B (the real work)

1. Extract condition-level rows into `AIH2_WP1_extraction_sheet.xlsx`: tables manually, figure
   curves via WebPlotDigitizer (`extraction_method`). Enforce `absent=0` vs `unreported=NaN`;
   fill `h2_yield_pct` (Phase-1 target); complete provenance + A/B/C quality metadata.
2. After ~15–20 studies, measure real rows/study and rows/class.
3. Double-extract a 10–15% sample (extraction-error QC table).
4. At ≥150 rows: write `data/curated/`, point Hydra at it, rerun WP2–WP4 (the optimism gap, ~0
   on synthetic data, becomes meaningful).

## 9. Honest status

**Archive-ready ≠ paper-ready.** Acquisition is done; the dataset itself does not exist until
Phase B extraction produces QC'd rows. A submission-ready IJHE manuscript still requires:
Phase B extraction → Phase 1 results on real data → **core Phase 2** (SCM regime-switch +
SHAP↔physics consistency metric, which close H1). The access route remains **open-access-only**;
that limitation, plus the quality-tiering + high-quality-only sensitivity run, are the documented
defense against a "selection-artifact" reviewer objection.
