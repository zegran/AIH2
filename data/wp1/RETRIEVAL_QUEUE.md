# AIH2 — WP1 Priority Retrieval Queue (missing studies to fetch)

> The 36 IN-scope studies not yet in hand, ordered by priority. Focus: **contradiction-evidence
> studies** + **at-risk-class fillers** (al_alloy, liquid_metal_activated, waste_al need ≥40 rows).
> OA studies are downloadable now; paywalled (Elsevier IJHE/Fuel/etc.) need green-OA/Unpaywall or
> may be unobtainable under the open-access-only constraint. DOIs resolved via Crossref this session;
> "resolve on import" = Zotero/Unpaywall will fill the DOI + locate the OA PDF.

Legend — OA: 🟢 gold OA (free on publisher) · 🟡 likely green-OA (repository/author copy) · 🔴 paywalled.

---

## TIER 1 — Contradiction evidence (scientifically critical — get these first)

| citekey | system_class | why needed | OA | DOI / where |
|---|---|---|---|---|
| `martinezv2026` | waste_al | **H1 inverted-U** vs particle size + SCM R²≈0.999 | 🟢 | `10.3390/hydrogen7020055` (MDPI Hydrogen) |
| `davies2022mat` | mechanically_activated | **rate–yield trade-off** (Zn slows rate, keeps 99.5% yield) | 🟢 | `10.3390/ma15031197` (MDPI Materials) |
| `manilevich2020` | al_alloy | **rate–yield trade-off** (Bi lowers rate) | 🟡 | Materials Science (Springer) — resolve on import |

## TIER 2 — At-risk-class OA fillers (push al_alloy / waste_al toward ≥40 rows)

### waste_al (4/16 — biggest gap; most are OA)
| citekey | OA | DOI / where |
|---|---|---|
| `mezulis2023` | 🟢 | MDPI Energies — resolve on import (preprint exists; want journal DOI) |
| `fadhilah2023` | 🟢 | BCREC (open access) — resolve on import |
| `knoks2025` | 🟢 | MDPI Applied Sciences — resolve on import |
| `buryakov2024` | 🟢 | MDPI Molecules — resolve on import (preprint exists; want journal DOI) |
| `buryakov2023met` | 🟢 | MDPI Metals — resolve on import |
| `gupta2025` | 🟢 | SpringerOpen (Mater. Renew. Sustain. Energy) — resolve on import |
| `urbonav2024` | 🟢 | MDPI Materials — resolve on import |
| `singh2019` | 🟡 | resolve on import |
| `maulana2023` | 🔴 | Adv. Mater. Res. (Trans Tech) — paywalled |

### al_alloy (4/10)
| citekey | OA | DOI / where |
|---|---|---|
| `gaozeng2021` | 🟢 | `10.3390/en14051433` (MDPI Energies) |
| `zhu2021` | 🟢 | MDPI Materials — resolve on import |
| `manilevich2021b` | 🔴 | Springer book chapter — likely no clean DOI |

### mechanically_activated (9/15)
| citekey | OA | DOI / where |
|---|---|---|
| `davies2022eni` | 🟢 | `10.3390/en15072356` (MDPI Energies) |
| `manilevich2021a` | 🟡 | Powder Metall. Met. Ceram. (Springer) — resolve on import |
| `xuan2023` | 🔴 | J. Alloys Compd. (Elsevier) — preprint on SSRN only |

### liquid_metal_activated (3/4 — ⚠️ only missing one is paywalled)
| citekey | OA | DOI / where |
|---|---|---|
| `mohammed2025` | 🔴 | Fuel (Elsevier) — paywalled. **If unobtainable, this class stays exploratory-only (<40 rows).** |

## TIER 3 — pure_al_alkali OA fillers (class already 15/26 — lower priority, but easy OA wins)
| citekey | OA | DOI / where |
|---|---|---|
| `trowell2022` | 🟢 | RSC Advances — resolve on import |
| `zhang2024` | 🟢 | Frontiers in Energy Research — resolve on import |
| `li2019` | 🟢 | E3S Web of Conferences — resolve on import |
| `porciuncula2012` | 🟢 | Braz. J. Chem. Eng. (SciELO) — resolve on import |
| `saroukanian2020` | 🟡 | conference/report — resolve on import |
| `sykhyi2024` | 🟡 | Vopr. Khim. Khim. Tekhnol. — resolve on import |
| `wangyd2024`, `kandasamy2023`, `gao2023ijhe`, `gao2023jes` | 🔴 | Elsevier (IJHE / Renewable Energy / J. Energy Storage) — paywalled |

---

## How to use this
1. **Download the 🟢 gold-OA studies now** — free PDFs on the publisher site (mdpi.com, frontiersin.org, scielo, etc.). These alone substantially fill waste_al and al_alloy.
2. Drop the new PDFs/MDs into the same `downloads/aih2_wp1/` folders, then **re-run the CLI ingest command** — it will archive them and refresh the gap report.
3. For 🟡 studies, import this queue into Zotero (it resolves DOIs via Unpaywall and finds green-OA copies).
4. 🔴 paywalled (Elsevier) studies are likely unobtainable under open-access-only — accept that the affected classes (esp. `liquid_metal_activated`) may remain exploratory-only, per the end-to-end plan.

## DOIs resolved this session (add to master_dois.csv)
```
martinezv2026   10.3390/hydrogen7020055
davies2022mat   10.3390/ma15031197
davies2022eni   10.3390/en15072356
gaozeng2021     10.3390/en14051433
```
