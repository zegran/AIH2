# Zenodo deposit — exact fill guide (lock this down)

Account: dunal@ipec.com.tr · Form: https://zenodo.org/uploads/new
**Community:** skip ("Select a community" is optional — submit without one).

## 1. Files — drag these from `C:\Users\zduna\Desktop\AIH2\submission_package\zenodo\`
Upload these 6 (loose files, so reviewers can preview them):
- `aih2_v1.csv` · `rate_extraction.csv` · `data_dictionary.md` · `README.md` ·
  `CITATION.cff` · `LICENSE_CC-BY-4.0.txt`
(Do NOT also upload the `.zip` — avoids duplication. Visibility = **Public**.)

## 2. Digital Object Identifier
Select **"No, I need one"** → Zenodo mints the DOI on Publish. (Currently you have "Yes" selected — switch it.)

## 3. Resource type
**Dataset**

## 4. Title (paste verbatim)
`Aluminum–Water Hydrolysis Hydrogen-Yield and Kinetics Dataset (provenance-tracked, leakage-aware), v1.0`

## 5. Publication date
`2026-06-18` (today — leave as prefilled)

## 6. Authors/Creators → Add author
- Name: **Unal, Dogukan**
- ORCID: **0009-0006-5102-8013**
- Affiliation: **IPEC, Industrial Project Engineering Consulting, Çankaya, Ankara, Türkiye**

## 7. Description (paste verbatim)
> A curated, provenance-tracked dataset of hydrogen production via aluminum–water hydrolysis,
> compiled from 31 published studies: 315 condition-level hydrogen-yield rows and 76 kinetic
> (activation-energy / rate) rows, each with full provenance and A/B/C quality tiers. Scope is
> aqueous Al–water hydrolysis (pure-Al/alkali, Al-alloy, mechanically activated,
> liquid-metal-activated, and waste-Al systems). The dataset is released to enable
> leakage-controlled, reproducible machine-learning analysis of the literature and accompanies the
> manuscript "Apparent Contradictions in the Aluminum–Water Hydrolysis Literature are Predominantly
> Methodological: a Provenance-Tracked, Leakage-Controlled Analysis" (submitted to Energy and AI).
> See `data_dictionary.md` for the 30-column schema and the absent=0 vs unreported=NaN convention.

## 8. License
**Creative Commons Attribution 4.0 International** (already selected — keep it).

## 9. Recommended fields (fill these)
- **Keywords and subjects:** aluminum–water hydrolysis; hydrogen production; curated dataset;
  machine learning; data leakage; reproducibility; reaction kinetics; activation energy
- **Languages:** English (eng)
- **Version:** `1.0.0`
- **Publisher:** `Zenodo`
- **Related works:** Relation = **"is supplement to"**, Identifier = `https://github.com/zegran/AIH2`,
  Scheme = URL. (Later, after the paper gets a DOI, add a second "is supplement to" → the paper DOI.)
- Copyright (optional): `© 2026 Dogukan Unal`
- Funding: leave empty (none).

## 10. Publish → copy the DOI
Click **Publish** → Zenodo shows a DOI like `10.5281/zenodo.XXXXXXXX`.
**Send that DOI to me.** I prepare the command that inserts it into `conclusion.tex` (Data
Availability) + `CITATION.cff`, closing the last manuscript placeholder.

## Skip everything else
Funding, Alternate identifiers, References, Software, Publishing info, Conference, Thesis — all
optional, leave blank for a dataset record.
