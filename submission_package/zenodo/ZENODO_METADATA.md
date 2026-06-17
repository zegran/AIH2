# Zenodo deposit metadata — aih2_dataset_v1

The exact metadata to enter on Zenodo (mirrors `.zenodo.json` at the repo root). Route A:
**dataset-only** deposit (the manuscript is NOT included).

| Field | Value |
|---|---|
| **Upload type** | Dataset |
| **Title** | AIH2: A Provenance-Tracked Open Dataset and Reproducible Analysis for Aluminum–Water Hydrolysis Hydrogen Production |
| **Version** | 1.0.0 |
| **Access right** | Open |
| **License** | Creative Commons Attribution 4.0 International (CC-BY-4.0) |
| **Creator** | Unal, Dogukan — ORCID 0009-0006-5102-8013 — IPEC, Industrial Project Engineering Consulting, Ankara, Türkiye |
| **Keywords** | aluminum-water hydrolysis; hydrogen production; open dataset; reproducibility; data leakage; meta-analysis; activation energy; methodological heterogeneity |
| **Related identifier** | isSupplementTo → https://github.com/zegran/AIH2 (URL) |
| **Notes** | Data licensed CC-BY-4.0; analysis/figure code licensed MIT (in the repository). |

**Description (paste into Zenodo):**

> Curated, provenance-tracked dataset and reproducible analysis pipeline for hydrogen production by
> aluminum–water hydrolysis. Includes a condition-level yield table (315 rows from 31 studies) and a
> separate kinetic table (76 rows: activation energies, peak rates, rate constants, t80). Each row
> carries full provenance (study DOI, table/figure source, extractor, extraction method) and
> quality/methodology metadata. The accompanying analysis demonstrates that the literature's apparent
> parameter-effect contradictions are predominantly methodological rather than physico-chemical. Data
> are released under CC-BY-4.0; the accompanying analysis code is released under MIT (see the linked
> repository).

**After deposit:** copy the minted DOI into the manuscript Data availability statement
(`paper/sections/conclusion.tex`, replacing `\todo{Zenodo DOI}`) and into `CITATION.cff`.
