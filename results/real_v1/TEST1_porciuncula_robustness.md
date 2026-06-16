# TEST 1 — Is the flagship within-pure_al_alkali signal real or porciuncula-driven?

random_forest · study = CV group · 5 seeds (0,1,2,7,42), mean ± sd · analysis-only (no data rows touched).
Prior single-seed claim: within-pure_al_alkali grouped R² = +0.58. porciuncula2012 = 120/162 = **74%**
of this class.

## VERDICT: **FAILS**
The +0.58 is **not** a genuine per-study cross-study signal — it is porciuncula-weighted. The
SURVIVES bar requires study-macro skill > 0; it is **−0.311**. The headline must be reframed/killed,
not salvaged.

## Item 1–2 · within-class 5-fold grouped CV
| data | n | studies | R² | MAE | skill vs mean |
|---|---|---|---|---|---|
| FULL pure_al_alkali | 162 | 9 | +0.596 ± 0.009 | 9.29 ± 0.28 | +0.829 ± 0.004 |
| porciuncula-OUT | 42 | 8 | +0.452 ± 0.008 | **17.22 ± 0.19** | +0.590 ± 0.006 |

porc-out R² stays positive (>0.2), but MAE nearly **doubles** (9.3 → 17.2% yield). The positive
R²/skill here is driven by the high variance of the 8-study remainder (yield sd 30 vs porciuncula 6.8) —
a mediocre model still beats the mean when the spread is large. So R² alone is misleading at this n.

## Item 3–4 · LOSO within pure_al_alkali (per study, mean over 5 seeds)
| study | n_rows | yield_mean | LOSO MAE | LOSO skill |
|---|---|---|---|---|
| porciuncula2012 | 120 | 93.0 | 6.64 | **+0.926** |
| zhang2024 | 10 | 72.1 | 12.10 | +0.569 |
| rin2021 | 9 | 26.1 | 17.87 | +0.902 |
| wen2018 | 8 | 94.0 | 18.31 | **−3.278** |
| trowell2022 | 5 | 55.8 | 18.53 | +0.624 |
| prabu2021 | 4 | 83.8 | 15.83 | −0.287 |
| yavor2013 | 3 | 55.0 | 38.89 | −0.098 |
| wanghq2017 | 2 | 83.2 | 4.91 | −2.387 |
| deng2010 | 1 | 87.4 | 1.29 | +0.228 |

- **row-weighted LOSO skill = +0.825** (pooled rows; porciuncula = 74% of them)
- **study-macro LOSO skill = −0.311** (each study weight 1)
- **porciuncula LOSO skill = +0.926** (predicted very well when trained on the other 8)
- **8 small studies: 4/8 skill > 0, median +0.065** (≈ no better than the class mean)

The ~1.14 gap between row-weighted (+0.83) and study-macro (−0.31) is the decisive evidence: the
headline number is porciuncula-weighted, not a per-study replication signal. Cross-study transfer to
the *other* studies is weak and inconsistent (half the studies are worse than guessing the mean, with
large negatives: wen −3.3, wanghq −2.4).

## Item 5 · distribution check
| group | n | yield mean | yield sd | range | T cov | conc cov | psize cov |
|---|---|---|---|---|---|---|---|
| porciuncula | 120 | 93.0 | 6.8 | [65,100] | 100% | 100% | **0%** |
| rest (8 studies) | 42 | 65.3 | 30.1 | [6,100] | 100% | 64% | 95% |

porciuncula is an **easy, narrow, high-yield cluster** (sd 6.8, all 65–100%) with a clean T×conc grid
and **no particle_size variation** — exactly the kind of dominant block that inflates a pooled,
rows-weighted score while contributing nothing to the particle-size question.

## What survives, stated plainly
- The **global leakage result** (random-vs-grouped optimism gap) is unaffected by this and remains robust.
- A **weak, inconsistent** within-regime signal exists (4/9 studies predicted with positive skill),
  but it does **not** support the "regime-conditioning resolves the contradiction (R²=0.58)" headline.
- H2 as previously evidenced is **not robustly supported**; the headline needs reframing. Whether the
  paper has a positive mechanism contribution now hinges on TEST 2 (physics pillar recoverability).
