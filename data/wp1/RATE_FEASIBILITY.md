# TEST 2 — Is the physics pillar (Arrhenius/SCM) recoverable from studies in hand?

Scan of all 31 archived studies' full text (8 parallel agents) for kinetic indicators: reported Eₐ,
rate constant k, max H₂ rate, t50/t80/time-to-completion, digitizable H₂(t) curves, and number of
distinct temperatures. No new literature. Analysis-only.

## VERDICT: **PILLAR RECOVERABLE** (strongly)
20/31 studies are ARRHENIUS-READY, spanning **all 5 system_classes**, with **≥3 ARRHENIUS-READY in 4
of 5 classes** (rule needed ≥3 in ≥2). **~15 studies report Eₐ directly** (≈10–70 kJ/mol, inside the
3.5–102.6 band), so a literature-Eₐ-per-`system_class` distribution can be built largely by direct
extraction, not digitization. → schedule a second, rate-focused extraction pass; keep the
"physics-validated" framing (IJHE).

## Per-class counts
| system_class | ARRHENIUS-READY | RATE-READY | YIELD-ONLY |
|---|---|---|---|
| pure_al_alkali | 6 | 3 | 0 |
| mechanically_activated | 4 | 2 | 0 |
| liquid_metal_activated | 4 | 0 | 1 |
| waste_al | 4 | 4 | 0 |
| al_alloy | 2 | 1 | 0 |
| **total** | **20** | **10** | **1** |

## Per-study classification
### ARRHENIUS-READY (reported Eₐ, or rate/k at ≥3 T)
| study | class | n_T | reported Eₐ (kJ/mol) | source |
|---|---|---|---|---|
| porciuncula2012 | pure_al_alkali | 4 | Eₐ tables 8–9 (J/mol) | Tab 8/9, Fig 13 |
| zhang2024 | pure_al_alkali | 5 | 45.46 (3µm) / 69.81 (25µm) | Tab 5 |
| wen2018 | pure_al_alkali | 4 | 56.6 / 58.3 / 73.5 / 164.9 | Tab 1, Fig 9 |
| wanghq2017 | pure_al_alkali | 4 | 45.92 | Fig 8 |
| yavor2013 | pure_al_alkali | ≥6 | 41 ± 5.3 | Eq 5, Fig 9/10 |
| rin2021 | pure_al_alkali | 5 | — (digitize Fig 8) | Fig 8 |
| guan2019 | mechanically | 5 | 20.08 | Tab 8, Fig 11 |
| xiao2020 | mechanically | 4 | 21.8–37.5 (6 comp.) | Tab 5 |
| xiao2018 | mechanically | 4 | 52.5 | Fig 7d |
| chen2020 | mechanically | 4 | 10.4 / 14.5 | Fig 2c/d |
| meng2022 | al_alloy | 3 | 39.2 (k at 50/70/90 °C) | Eq 8, Tab 3 |
| liuyh2017 | al_alloy | 3 | reported (SI S1/S2) | Fig 3 + SI |
| lu2017 | liquid_metal | 4 | 39.6 | Fig 3b |
| dudoladov2016 | liquid_metal | 4 | — (max-rate, sub-zero) | Tab 2 |
| jayaraman2015 | liquid_metal | 3 | — (rate at 30/50/90 °C) | Fig 2–6 |
| ilyukhina2012 | liquid_metal | 3 | — (rate at 21/40/60 °C) | Fig 6 |
| fadhilah2023 | waste_al | 6 | 47.4 | Sec 3.1 |
| urbonav2024 | waste_al | 4 | 32.30 (R²=0.9995) | Fig 4 |
| mezulis2023 | waste_al | ? | 48.1 | Sec 3.1 |
| ho2016 | waste_al | 4 | — (digitize Fig 4, fixed 0.25 M) | Fig 4 |

### RATE-READY (rate/V(t) at <3 T)
qiao2019 (al_alloy, 1T) · preez2018 (mech, 1T) · davies2022mat (mech, 1T) · trowell2022
(pure_al_alkali, 1T) · prabu2021 (pure_al_alkali, 1T) · deng2010 (pure_al_alkali, 1T, SCM k at 55 °C
across particle sizes) · buryakov2023met (waste_al, 1T) · martinezv2026 (waste_al, 1T) · knoks2025
(waste_al, 1T, SCM ks) · gupta2025 (waste_al, 3 T **confounded with [NaOH]** → not a clean Arrhenius set).

### YIELD-ONLY
fischman2020 (liquid_metal — mentions Arrhenius but reports no Eₐ/rate-vs-T; T tests are viscosity only).

## Notes
- **Directly-usable physics:** ~15 reported Eₐ values already span ~10–70 kJ/mol (all inside the
  3.5–102.6 kJ/mol band except wen2018's 164.9 outlier system) → H3's in-band check is largely
  answerable by direct extraction, and the ML-learned temperature sensitivity can be validated
  against these literature Eₐ per regime.
- **Rate-focused second pass** would: (i) harvest the ~15 reported Eₐ directly; (ii) digitize the
  5 rate-at-≥3-T studies without printed Eₐ (rin2021, jayaraman2015, dudoladov2016, ilyukhina2012,
  ho2016); (iii) optionally add single-T max-rate/t80 (Phase-2 columns) from the 10 RATE-READY studies.
- **Naming caveat (flagged by agents):** several `pure_al_alkali` studies (trowell2022, prabu2021,
  zhang2024, rin2021, yavor2013) use pure Al in *plain/sc water* (no alkali). This matches the class
  definition (pure unalloyed Al in alkaline **or** plain water) but the class *name* is a slight
  misnomer for the plain-water subset — consider renaming or a sub-flag. Does not affect any analysis.
