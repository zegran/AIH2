# WP1 Ingest Gap Report

*Ingest of 35 downloaded MD files.*

- Archived (IN-scope): **35**
- Background (out-of-scope): **0**
- Unmatched (new candidates): **0**

## 1. Missing IN-scope studies (still to retrieve)

| system_class | obtained / pool | missing citekeys |
|---|---|---|
| `pure_al_alkali` | 15 / 26 | gao2023ijhe, gao2023jes, kandasamy2023, li2019, porciuncula2012, saroukanian2020, sykhyi2024, testa2024, trowell2022, wangyd2024, zhang2024 |
| `al_alloy` | 4 / 10 | an2022, gaozeng2021, manilevich2020, manilevich2021b, meng2023, zhu2021 |
| `mechanically_activated` | 9 / 15 | davies2022eni, davies2022mat, huang2023, manilevich2021a, wu2025, xuan2023 |
| `liquid_metal_activated` | 3 / 4 | mohammed2025 |
| `waste_al` | 4 / 16 | buryakov2023met, buryakov2024, deebika2023, fadhilah2023, gupta2025, kale2021, knoks2025, martinezv2026, maulana2023, mezulis2023, singh2019, urbonav2024 |

**Total missing IN-scope: 36 of 71.**

## 2. Out-of-scope downloads moved to background

None. No downloaded file was out of scope.

## 3. Unmatched downloads (new candidates to screen)

None.

## 4. Metadata gaps per archived item

| citekey | DOI | figure-only? | temp? | yield? |
|---|---|---|---|---|
| `chen2020` | yes | yes | yes | yes |
| `david2012` | yes | no | yes | yes |
| `deng2010` | yes | yes | yes | no |
| `dudoladov2016` | yes | no | yes | yes |
| `elitzur2014` | yes | yes | yes | yes |
| `godart2019` | yes | no | yes | yes |
| `guan2019` | yes | no | yes | yes |
| `ho2016` | yes | yes | yes | yes |
| `irankhah2018` | yes | no | yes | yes |
| `jayaraman2015` | yes | yes | yes | yes |
| `liuyh2017` | yes | no | yes | yes |
| `liuzh2021` | yes | no | yes | yes |
| `meng2022` | yes | no | yes | yes |
| `noland2020` | yes | no | yes | yes |
| `prabu2021` | yes | no | yes | yes |
| `preez2018` | yes | no | yes | yes |
| `preez2019` | yes | no | yes | yes |
| `qiao2019` | yes | no | yes | yes |
| `razavi2013` | yes | yes | yes | yes |
| `razavi2016` | yes | no | yes | yes |
| `rin2021` | yes | no | yes | yes |
| `shmelev2016` | yes | no | yes | yes |
| `tan2016` | yes | yes | yes | yes |
| `tekade2018a` | yes | no | yes | yes |
| `tekade2018k` | yes | no | yes | no |
| `tekade2018n` | yes | no | yes | no |
| `tekade2020` | yes | no | yes | yes |
| `wanghq2017` | yes | no | yes | yes |
| `wangxy2021` | yes | no | no | no |
| `wen2018` | yes | no | yes | yes |
| `xiao2018` | yes | no | yes | yes |
| `xiao2020` | yes | no | yes | yes |
| `yang2018` | yes | no | yes | yes |
| `yavor2013` | yes | no | yes | yes |
| `yolcular2020` | yes | no | yes | yes |

- Archived items missing a DOI: 0 (none).
- Archived items with likely figure-only data (WebPlotDigitizer needed): 7 (chen2020, deng2010, elitzur2014, ho2016, jayaraman2015, razavi2013, tan2016).

## 5. Per-system_class readiness vs row targets

| system_class | obtained studies | row target | at-risk for >=40 rows? |
|---|---|---|---|
| `pure_al_alkali` | 15 | 90-120 | ok |
| `al_alloy` | 4 | 50-70 | **AT-RISK / exploratory-only** |
| `mechanically_activated` | 9 | 60-80 | ok |
| `liquid_metal_activated` | 3 | 40-50 | **AT-RISK / exploratory-only** |
| `waste_al` | 4 | 60-80 | **AT-RISK / exploratory-only** |

> At-risk rule: fewer than 5 obtained studies is unlikely to yield >=40 condition rows (assuming ~8 rows/study). These classes stay exploratory-only until more studies are retrieved or extracted densely.

## Priority retrievals (contradiction-evidence studies still missing)
- `martinezv2026` (waste_al) — inverted-U size effect, SCM R²≈0.999 (H1).
- `davies2022mat` (mechanically_activated) — Zn rate/yield trade-off.
- `manilevich2020` (al_alloy) — Bi lowers rate (trade-off).

*See `ingest_manifest.csv` for the per-file record.*
