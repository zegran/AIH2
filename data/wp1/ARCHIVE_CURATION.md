# WP1 — Archive Curation & Q1-Sufficiency Analysis

*2026-06-15. Decision doc for curating the in-hand archive toward a Q1 (IJHE) submission.
Inputs: `master_dois.csv` (52 in hand), `archive_quality_52.csv` (Crossref citations/venue/year).
Citation counts are Crossref `is-referenced-by-count` (a consistent proxy; undercounts vs Scholar).*

## 0. TL;DR

- **19 unreachable studies deleted** from the active pool → `WP1_EXCLUDED.md` (do-not-resuggest).
- The remaining **52 are bibliometrically strong**: 100% peer-reviewed journal articles; ~46 are
  clearly Q1/Q2 reference-grade (IJHE, Energy, Fuel, RSC, J. Hazard. Mater., J. Alloys Compd.,
  MDPI). **Quality is not the problem.**
- **Only 2 weak studies recommended for removal** (`li2019`, `sykhyi2024`). `jayaraman2015` is a
  weak venue but **scientifically essential** (H1 evidence) → keep with a venue caveat.
- The **binding constraint is sample, not quality**: `liquid_metal_activated` has just **3**
  studies (can't reliably reach ≥40 rows). This — not Q1 hygiene — is what the Consensus
  re-search must fix.
- ⚠️ **Over-curating toward "Q1/recent/high-cite/OA" would introduce selection bias** — the very
  artifact-vs-real objection this paper exists to defeat. Defense = quality-tiering + sensitivity
  run (already designed), **not** deletion.

## 1. Quality tiers (52 in hand)

Tier A = Q1 reference-grade (Elsevier IJHE/Energy/Fuel, RSC, Wiley high-impact, well-cited).
Tier B = solid peer-reviewed Q2/OA (MDPI, Frontiers, Springer, SciELO, BCREC, T&F).
Tier C = weak venue / low value. ★ = carries primary contradiction evidence.

### `pure_al_alkali` (20)
| citekey | venue | cites | yr | tier |
|---|---|---|---|---|
| yavor2013 | IJHE | 134 | 2013 | A |
| shmelev2016 | IJHE | 76 | 2016 | A |
| dudoladov2016 | IJHE | 66 | 2016 | A |
| wangxy2021 | IJHE | 64 | 2021 | A |
| wanghq2017 | Energy | 51 | 2017 | A |
| razavi2016 | IJHE | 44 | 2016 | A |
| trowell2022 | RSC Advances | 38 | 2022 | A |
| deng2010 | J. Am. Ceram. Soc. | 32 | 2010 | A ★(size) |
| porciuncula2012 | Braz. J. Chem. Eng. | 88 | 2012 | B |
| yang2018 | Int. J. Energy Res. | 66 | 2018 | B ⚠️partial |
| wen2018 | Int. J. Energy Res. | 26 | 2017 | B |
| rin2021 | IJHE | 25 | 2021 | B |
| prabu2021 | Int. J. Energy Res. | 24 | 2021 | B |
| noland2020 | IJHE | 17 | 2020 | B |
| zhang2024 | Frontiers Energy Res. | 13 | 2024 | B |
| tekade2018n | IJCRE (De Gruyter) | 7 | 2018 | C (SCM data) |
| tekade2018a | IJCRE | 4 | 2018 | C (SCM data) |
| tekade2018k | IJCRE | 3 | 2018 | C (SCM data) |
| **li2019** | **E3S Web of Conf.** | **1** | 2019 | **C → ELIMINATE** (conf. proceedings; NaF medium, off-axis) |
| **sykhyi2024** | **Voprosy Khimii** | **0** | 2024 | **C → ELIMINATE** (obscure venue; partial/electrochemical scope) |

### `al_alloy` (7) — borderline supply
| elitzur2014 | IJHE | 113 | A | · liuyh2017 | IJHE | 92 | A | · qiao2019 | IJHE | 89 | A |
| meng2022 | IJHE | 28 | A ★(Ga/In/Sn) | · zhu2021 | Materials | 18 | B | · manilevich2020 | Mater. Sci. (Springer) | 11 | B ★(rate–yield) | · gaozeng2021 | Energies | 10 | B |

### `liquid_metal_activated` (3) — ⚠️ UNDER-SUPPLIED (the real gap)
| godart2019 | IJHE | 93 | A | · tan2016 | IJHE | 58 | A | · **jayaraman2015** | Energy & Power Eng. (SCIRP) | 20 | **C-venue but KEEP ★(H1 size inverted-U)** |

### `mechanically_activated` (11) — strong
| razavi2013 | IJHE | 108 | A | xiao2018 | Energy | 108 | A | irankhah2018 | IJHE | 98 | A | guan2019 | Energy | 63 | A | preez2018 | IJHE | 56 | A | preez2019 | IJHE | 50 | A | chen2020 | IJHE | 47 | A ★(Eₐ low end) | xiao2020 | J. Alloys Compd. | 38 | A | davies2022mat | Materials | 31 | B ★(rate–yield) | davies2022eni | Energies | 25 | B | liuzh2021 | IJHE | 23 | B |

### `waste_al` (11) — strong
| david2012 | J. Hazard. Mater. | 129 | A | ho2016 | IJHE | 76 | A | tekade2020 | IJHE | 41 | A | mezulis2023 | Energies | 16 | B | gupta2025 | Mater. Renew. Sustain. Energy (Springer) | 13 | B | buryakov2023met | Metals | 11 | B | urbonav2024 | Materials | 11 | B | fadhilah2023 | BCREC | 9 | B | yolcular2020 | Energy Sources A | 8 | B | knoks2025 | Applied Sciences | 4 | B | martinezv2026 | Hydrogen (MDPI) | 0 | B ★(H1; 2026 → 0 cites expected) |

## 2. Recommended eliminations (minimal — 2 of 52)

| citekey | why | cost |
|---|---|---|
| `li2019` | E3S Web of Conferences (conference proceedings, not a journal); 1 citation; NaF medium sits off the main alkali axis | none — `pure_al_alkali` has 18 others |
| `sykhyi2024` | Voprosy Khimii (obscure regional journal); 0 citations; "dissolvable anode" is partly electrochemical → borderline scope | none |

**Keep everything else**, including: the three `tekade` IJCRE papers (peer-reviewed, carry SCM
condition data → tier C, valid data source) and **`jayaraman2015`** (weak venue but a *primary*
H1 contradiction source — removing it would amputate the thesis; keep, tier its rows C, note the
venue in the limitations).

> **Why not a deeper purge?** A Q1 reviewer does not require every *data source* to be Q1 — they
> require transparent inclusion/exclusion criteria, source quality-tiering, and a sensitivity
> analysis. All three are already in the design (A/B/C tiers + high-quality-only run, spec §B2/§D).
> Deleting peer-reviewed sources to look "cleaner" shrinks the sample and biases it.

## 3. Per-class status after deletion + recommended elimination → **50 studies**

| system_class | studies | ≥40-row feasibility | action |
|---|---|---|---|
| pure_al_alkali | 18 | ✅ ample | none |
| mechanically_activated | 11 | ✅ | none |
| waste_al | 11 | ✅ | none |
| al_alloy | 7 | 🟡 borderline (~6 rows/study) | +2–3 as insurance |
| **liquid_metal_activated** | **3** | **❌ needs ~13 rows/study** | **+5–7 OA studies (priority)** |

**Row feasibility (global):** 50 studies × ~5–10 condition rows ≈ 250–500 rows → clears the
≥150 floor / ~300 target. The shortfall is **per-class**, concentrated in `liquid_metal_activated`.

## 4. Target & Consensus OA search plan

**Goal:** add ~**8–11 open-access, peer-reviewed** studies, focused on the thin classes — to
reach ~**58–60 studies** with every class feasible for ≥40 rows.

Search via Consensus (`exclude_preprints=true`; **no `year_min`** — avoid recency bias and keep
older foundational work; resolve OA per-DOI via OpenAlex→Unpaywall). Precise domain terms, avoid
neighbor-field hijackers ("splitting"/"electrolysis"). Proposed queries:

1. `gallium indium tin eutectic activated aluminum hydrolysis hydrogen generation`
2. `liquid metal Galinstan activated aluminum water reaction hydrogen`
3. `EGaIn aluminum composite hydrogen production hydrolysis`
4. `aluminum-rich alloy hydrolysis hydrogen low-melting-point metals` (al_alloy top-up)

Each candidate must pass the **access+richness gate** (OA full text + table/figure data) before
it enters the pool — per `WP1_END_TO_END_PLAN.md`. We do not grow the Discovered pile.

## 5. Selection-bias caveat (Q1 defense — read before searching)

Filtering the dataset toward *OA + recent + high-citation + Q1* systematically biases the sample.
A sharp reviewer will say: *"your contradiction resolution may be an artifact of selecting recent
OA MDPI papers."* That is the **same artifact-vs-real objection the paper is built to defeat.**
Mitigations (do all):
- Keep the **era/venue spread** (foundational 2010–2016 studies stay in).
- Lean on **quality-tiering (A/B/C) + the high-quality-only sensitivity run**, not deletion, to
  prove the contradiction is physical not artifactual.
- **Document the open-access-only access route as an explicit limitation** in the paper — honest
  scope reporting is itself a Q1 strength.

## 6. Decisions needing the author's OK
1. Eliminate the 2 weak studies (`li2019`, `sykhyi2024`)? (recommended) — or keep all 52.
2. Greenlight the **focused Consensus OA search** (target `liquid_metal_activated` + `al_alloy`,
   ~8–11 new studies)? — or a broader re-search.
3. Confirm: **keep `jayaraman2015`** despite venue (recommended, it anchors H1).
