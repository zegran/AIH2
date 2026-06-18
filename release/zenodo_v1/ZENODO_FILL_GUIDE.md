# Zenodo Upload Field Guide — AIH2 Dataset v1.0

Fresh upload (old record was deleted). Fill every field exactly as shown below.

---

## Step 1 — Upload files

Drag the **6 loose files** into the file upload area (NOT the zip):

```
aih2_v1.csv
rate_extraction.csv
data_dictionary.md
README.md
CITATION.cff
LICENSE_CC-BY-4.0.txt
```

You may optionally also upload `aih2_dataset_v1.zip` as a convenience archive.

**Visibility:** Public  
**Community:** Skip (leave blank)

---

## Step 2 — DOI

Select: **"No, I need one."**

Zenodo will mint a new DOI. Record it — you will need it for Stage 2 of the manuscript finalization.

---

## Step 3 — Resource type

**Dataset**

---

## Step 4 — Title

```
Aluminum–Water Hydrolysis Hydrogen-Yield and Kinetics Dataset (provenance-tracked, leakage-aware), v1.0
```

(Copy exactly, including the em-dash and parenthetical.)

---

## Step 5 — Publication date

```
2026-06-18
```

---

## Step 6 — Author

| Field | Value |
|---|---|
| Family name | Unal |
| Given name | Dogukan |
| ORCID | 0009-0006-5102-8013 |
| Affiliation | IPEC, Industrial Project Engineering Consulting, Çankaya, Ankara, Türkiye |

---

## Step 7 — Description

Paste this verbatim into the description box:

```
A provenance-tracked, quality-tiered dataset for hydrogen production by aluminum–water hydrolysis, assembled from 31 independent published studies (315 yield rows; 76 kinetic rows). Each row traces to a study DOI and a table/figure source reference. Methodology covariates (temperature-control method, hydrogen measurement apparatus, vessel type, activation method) and quality tier are recorded per row and verified by blind independent-agent inter-rater reliability (post-adjudication Cohen's κ = 1.00 for temperature_control and measurement_method; κ = 0.826 for system_class).

The dataset accompanies the paper "Apparent Contradictions in the Aluminum–Water Hydrolysis Literature are Predominantly Methodological: a Provenance-Tracked, Leakage-Controlled Analysis" (D. Unal, Energy and AI).

Files:
- aih2_v1.csv — 315 experimental yield rows × 30 columns (target: h2_yield_pct; features: alloy composition, temperature, alkali, activation method, methodology covariates; provenance).
- rate_extraction.csv — 76 kinetic rows (activation energy, peak rate, rate constant, t₈₀).
- data_dictionary.md — full column definitions for both tables.
- CITATION.cff — citation metadata.
- LICENSE_CC-BY-4.0.txt — license text.

Scope: aqueous aluminum–water/alkaline hydrolysis for H₂ production only. Out of scope: electrolysis, photocatalysis, non-aqueous routes. Dataset is observational; all reported analyses are associational.
```

---

## Step 8 — License

**Creative Commons Attribution 4.0 International (CC-BY-4.0)**

---

## Step 9 — Keywords

Enter each on a separate line (Zenodo accepts up to 6):

```
aluminum-water hydrolysis
hydrogen production
machine learning
meta-analysis
provenance tracking
inter-rater reliability
```

---

## Step 10 — Additional fields

| Field | Value |
|---|---|
| Language | English |
| Version | 1.0.0 |
| Publisher | Zenodo |

---

## Step 11 — Related works / GitHub

**Leave blank.** The code repository is private; do not add a GitHub related-works link.

---

## Step 12 — Publish

Click **Publish**. Zenodo will assign a DOI of the form `10.5281/zenodo.XXXXXXX`.

**Send that DOI to Claude Code** to trigger Stage 2 (insert DOI everywhere + final manuscript finalization).

---

## Checklist before clicking Publish

- [ ] 6 loose files uploaded (aih2_v1.csv, rate_extraction.csv, data_dictionary.md, README.md, CITATION.cff, LICENSE_CC-BY-4.0.txt)
- [ ] DOI: "No, I need one."
- [ ] Resource type: Dataset
- [ ] Title copied exactly
- [ ] Author: Unal, Dogukan — ORCID 0009-0006-5102-8013
- [ ] Description pasted
- [ ] License: CC-BY-4.0
- [ ] 6 keywords entered
- [ ] Version: 1.0.0
- [ ] No GitHub related-works link
- [ ] Visibility: Public
