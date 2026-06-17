# Citation-coverage matrix + target reference list

Generated from `tools/citation_coverage.py` (matches the 31 dataset `study_id` DOIs against
`references.bib`; per-study row counts from `aih2_v1.csv` / `rate_extraction.csv`; keys/DOIs from
`canonical_studies.csv`). **Rule:** BibTeX is never written from memory — each target entry's DOI is
verified (it is the extraction source, full text on hand: `has_md_text=Y`), and BibTeX will be
fetched from Crossref at execution time.

## Tier classification
- **Tier A — data-source (MUST cite):** 31 studies whose data is in the dataset. **3 cited, 28 missing.**
- **Tier B — domain-context (should cite):** 28 studies ingested with full text but not used as data
  sources → Related-Work / screening-funnel citations (optional, ~12 strongest recommended).
- **Tier C — method-precedent (already cited):** the 15 positioning references (data leakage,
  meta-analysis, catalysis-ML, field reviews). Keep.

## Tier A — data-source coverage matrix (31 studies)

| canonical key | system_class | yield rows | rate rows | cited? | DOI |
|---|---|---:|---:|---|---|
| wen2018 | pure_al_alkali | 8 | 5 | ✅ wen2018 | 10.1002/er.3955 |
| porciuncula2012 | pure_al_alkali | 120 | 7 | ✅ porciuncula2012 | 10.1590/s0104-66322012000200014 |
| urbonav2024 | waste_al | 2 | 1 | ✅ urbonav2024 | 10.3390/ma17112637 |
| prabu2021 | pure_al_alkali | 4 | 1 | ❌ | 10.1002/er.6478 |
| gupta2025 | waste_al | 1 | 4 | ❌ | 10.1007/s40243-024-00287-2 |
| wanghq2017 | pure_al_alkali | 2 | 3 | ❌ | 10.1016/j.energy.2017.05.031 |
| xiao2018 | mechanically_activated | 4 | 2 | ❌ | 10.1016/j.energy.2018.05.201 |
| guan2019 | mechanically_activated | 28 | 2 | ❌ | 10.1016/j.energy.2019.116107 |
| ilyukhina2012 | liquid_metal_activated | 5 | 2 | ❌ | 10.1016/j.ijhydene.2012.02.175 |
| yavor2013 | pure_al_alkali | 3 | 2 | ❌ | 10.1016/j.ijhydene.2013.09.070 |
| ho2016 | waste_al | 1 | 2 | ❌ | 10.1016/j.ijhydene.2015.11.083 |
| dudoladov2016 | liquid_metal_activated | 6 | 5 | ❌ | 10.1016/j.ijhydene.2015.11.122 |
| liuyh2017 | al_alloy | 16 | 1 | ❌ | 10.1016/j.ijhydene.2017.02.205 |
| preez2018 | mechanically_activated | 16 | 1 | ❌ | 10.1016/j.ijhydene.2018.09.133 |
| qiao2019 | al_alloy | 28 | 1 | ❌ | 10.1016/j.ijhydene.2018.12.124 |
| chen2020 | mechanically_activated | 4 | 3 | ❌ | 10.1016/j.ijhydene.2020.03.027 |
| fischman2020 | liquid_metal_activated | 1 | 0 | ❌ | 10.1016/j.ijhydene.2020.04.161 |
| rin2021 | pure_al_alkali | 9 | 2 | ❌ | 10.1016/j.ijhydene.2021.06.101 |
| meng2022 | al_alloy | 1 | 1 | ❌ | 10.1016/j.ijhydene.2022.09.127 |
| xiao2020 | mechanically_activated | 7 | 7 | ❌ | 10.1016/j.jallcom.2019.152800 |
| lu2017 | liquid_metal_activated | 1 | 1 | ❌ | 10.1039/c7ra01839h |
| trowell2022 | pure_al_alkali | 5 | 1 | ❌ | 10.1039/d2ra01231f |
| deng2010 | pure_al_alkali | 1 | 1 | ❌ | 10.1111/j.1551-2916.2010.03969.x |
| zhang2024 | pure_al_alkali | 10 | 4 | ❌ | 10.3389/fenrg.2024.1441155 |
| knoks2025 | waste_al | 4 | 4 | ❌ | 10.3390/app15052640 |
| mezulis2023 | waste_al | 1 | 2 | ❌ | 10.3390/en16145554 |
| martinezv2026 | waste_al | 3 | 4 | ❌ | 10.3390/hydrogen7020055 |
| davies2022mat | mechanically_activated | 10 | 1 | ❌ | 10.3390/ma15031197 |
| buryakov2023met | waste_al | 6 | 3 | ❌ | 10.3390/met13020185 |
| jayaraman2015 | liquid_metal_activated | 6 | 2 | ❌ | 10.4236/epe.2015.79041 |
| fadhilah2023 | waste_al | 2 | 1 | ❌ | 10.9767/bcrec.20041 |

**28 Tier-A studies to add** (the ❌ rows). All have verified DOIs + full text on hand. These will be
cited where their data is used: in the new **data-sources table**, and in Results/Discussion where
their specific conditions anchor a contradiction (e.g. the 5 particle-size studies, the liquid-metal
Eₐ spread studies).

## Tier B — domain-context pool (28 ingested, not data sources)
From `canonical_studies.csv`, the studies with full text on hand but no rows in the final dataset
(screened out, pool, or non-extractable): `razavi2016, tekade2018n, yang2018, tekade2018k, shmelev2016,
noland2020, tekade2018a, manilevich2020, gaozeng2021, zhu2021, elitzur2014, tan2016, godart2019,
razavi2013, irankhah2018, preez2019, davies2022eni, liuzh2021, david2012, yolcular2020, tekade2020,
changying2017, kravchenko2005, meroueh2020, nizovskii2017, parmuzina2009, slocum2020` (+1).
**Recommendation:** cite ~12 of the strongest in Related Work and the screening-funnel sentence
("we screened N studies and extracted from 31"), giving a verified provenance for the funnel and
~12 more references. DOIs are in `canonical_studies.csv`.

## Tier C — method-precedent (already cited; keep all 15)
`bernett2024, john2025, suvarna2024, bozalginesta2025, coelho2022, xue2024, noble2022, pomerantsev2021,
wulf2021, hoque2018` (methodology) + `das2023fuel, saceleanu2019, urbonavicius2023, musicco2025,
dupreez2021review` (Al-hydrolysis domain context / reviews).

## Projection
| stage | references |
|---|---|
| now | 18 (3 data-source + 15 positioning) |
| + 28 Tier-A data sources | **46** |
| + ~12 Tier-B domain-context | **~58** |

Lands in the Q1/IJHE range (40–80). The Tier-A backfill is the non-negotiable part (attribution);
Tier-B is the optional depth top-up.

## Preventive gate
`tools/citation_coverage.py --check` exits non-zero while any Tier-A study is uncited. Wire it into
`tools/lint_paper.py` / CI **after** the backfill so the regression cannot recur (see
`REMEDIATION_PLAN.md` § Preventive measures).
