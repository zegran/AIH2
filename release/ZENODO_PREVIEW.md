# Zenodo upload preview — exactly what will be deposited

This is the review sheet for the **Route A dataset-only** deposit. Review it before uploading. The
manuscript, code, and internal files are **deliberately excluded** — the code lives in the GitHub
repo (linked from the metadata), and the paper is submitted to the journal separately.

## Bundle: `release/aih2_dataset_v1/` (zipped as `release/aih2_dataset_v1.zip`, 18.2 KB)

```
aih2_dataset_v1/
├── aih2_v1.csv              59,870 bytes   315 data rows + header (30 columns)
├── rate_extraction.csv      11,910 bytes    76 data rows + header (14 columns)
├── data_dictionary.md        2,931 bytes    full column definitions (both tables)
├── README.md                 3,345 bytes    dataset card (inlined below)
├── CITATION.cff              1,027 bytes    citation metadata
└── LICENSE_CC-BY-4.0.txt    18,657 bytes    verbatim CC-BY-4.0 legal code
```

**Sanity check:** no manuscript / `.tex` / `paper/` / `submission/` / code / CLI files in the bundle —
confirmed dataset-only.

## Metadata to enter on Zenodo

See `release/ZENODO_METADATA.md` for the full field-by-field block. Summary: **Dataset**, title
"AIH2: A Provenance-Tracked Open Dataset … Aluminum–Water Hydrolysis Hydrogen Production", v1.0.0,
**CC-BY-4.0**, creator **Unal, Dogukan** (ORCID 0009-0006-5102-8013, IPEC), linked to the GitHub
repo as `isSupplementTo`. (Mirrors `.zenodo.json`, so a GitHub→Zenodo release would pick it up
automatically.)

## README.md (inlined — the file shipped in the bundle)

---

<details open>
<summary>aih2_dataset_v1/README.md</summary>

See `release/aih2_dataset_v1/README.md`. Key facts: 315 condition-level yield rows (31 studies) +
76-row kinetic table; per-class composition pure_al_alkali 162/9, mechanically_activated 69/6,
al_alloy 45/3, waste_al 20/8, liquid_metal_activated 19/5; missing encoded as 0, unreported left
missing; QC = 52/52 double-extraction agreement, classification audit, ~1.5% digitization error,
Arrhenius fit gate (R²≥0.90, ≥3 T). Scope: aqueous Al–water/alkaline hydrolysis for H₂; out of scope
electrolysis/photocatalysis/non-aqueous. Author: Dogukan Unal (IPEC). License CC-BY-4.0.

</details>

---

## After the user deposits

1. Zenodo mints a DOI → paste it into `paper/sections/conclusion.tex` (`\todo{Zenodo DOI}`) and
   `release/aih2_dataset_v1/CITATION.cff`.
2. Re-zip if any bundle file changed (`release/aih2_dataset_v1.zip`).
