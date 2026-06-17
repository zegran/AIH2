# CLI Command — Terminal rate-based physics test, then write (senior brief)

> Paste into Claude Code at the AIH2 repo root. Decision: run the physics test **once, properly,
> on rate (not yield)** — this is completing a test that was previously run on the wrong variable,
> NOT an open-ended rescue. **Pre-commitment: this is the terminal physics attempt.** Whatever the
> verdict, the next step is writing — no further rescue rounds. Honest, pre-registered reporting.

Why this is legitimate (not p-hacking): the earlier A2 used yield as a proxy for rate; yield
saturates (~93% on pure_al) so that test was effectively invalid. Re-running A1/A2 on rate-derived
Arrhenius is the **first valid** physics test. The frozen success criteria from
`plan/analysis-protocol.md` stay unchanged; a second null is accepted and reported.

---

## Step 1 — Assemble rate-derived Arrhenius data (bounded)
1. Digitize the 5 curve-only studies (`rin2021`, `jayaraman2015`, `dudoladov2016`, `ilyukhina2012`,
   `ho2016`) → H₂ rate (or V(t)) vs temperature, via WebPlotDigitizer / render→vision. Same QC as
   before; **double-extract a 10–15% sample** and report error.
2. Extend `data/wp1/rate_extraction.csv` (keep it separate from `aih2_v1.csv`). For each study with
   ≥3 temperatures, **fit an Arrhenius Eₐ** (ln k vs 1/T); otherwise use the reported Eₐ. Record
   `fit_method` (reported | arrhenius_fit | derived), `r2_of_fit`, `temp_range_k`, `n_temperatures`,
   `rate_definition`, provenance, `quality_tier`.
3. Flag method heterogeneity; do NOT naively pool Eₐ across incompatible rate definitions —
   stratify or annotate.

**Gate:** rate-derived Eₐ table populated, QC'd, validated (`tools/validate_rate_rows.py`).

## Step 2 — A1: is the Eₐ spread regime-structured? (the realistic physics win)
- Test `Ea ~ system_class` (study as unit): between-class vs within-class variance, η²/ICC,
  cluster-bootstrap CI, frozen threshold. Report all 5 classes and the better-powered subset.
- **Success (frozen):** system_class explains a significant, non-trivial share of Eₐ variance →
  the 3.5–102.6 kJ/mol spread is regime-structured, not random (resolves contradiction #2 on
  **physical** grounds). Report effect size + CI, not just p.

## Step 3 — A2: proper rate-based consistency (honest, secondary)
- Where a study reports both rate-vs-T and an Eₐ: check **internal Arrhenius consistency**
  (fitted vs reported Eₐ) — validates the extraction and the physics.
- **Regime-rank agreement:** does the rate-fit Eₐ ranking across regimes match the reported-Eₐ
  ranking? (Spearman, CI.)
- Explicitly **downgrade** the "ML yield-temperature-sensitivity ↔ Eₐ" convergence to a secondary,
  acknowledged-weak check (yield is not a rate); do not hang the paper on it. Keep frozen criterion;
  accept null.

## Step 4 — Lock the verdict and framing, then STOP
Update `results/real_v1/GO_NOGO_SUMMARY.md` with the **final physics verdict** and the locked
decision:
- **If A1 is clean-significant** (and internally consistent in A2): framing = "leakage-controlled
  audit + **physics-validated regime structure of the Eₐ spread**"; venue target **IJHE**.
- **Else:** framing = "leakage-controlled methodology + cross-study non-poolability + curated open
  dataset; Eₐ regime structure reported as a weak/descriptive finding"; venue **Energy and AI**.
In both cases the physics section is now properly measured. **Do not start WP5 figures or paper
drafting** — stop for user sign-off on the final framing.

---

## Rules
- This is the terminal physics attempt; no further rescue analyses after this verdict.
- Frozen criteria binding; if A1/A2 are null/weak, say so plainly — write the honest result.
- Keep `aih2_v1.csv` (yield) and `rate_extraction.csv` (kinetic) separate; QC every new row.
- Effect sizes + CIs (cluster-bootstrap over studies) for every headline number.
- Durable artifacts English; Conventional Commits; commit Step-1 data and Step-2/3 results separately.

## Definition of done
- Rate-derived Eₐ table (digitized 5 + assembled) QC'd, validated, committed.
- `results/real_v1/H3_arrhenius.md` updated with rate-based A1 + A2 verdicts; `GO_NOGO_SUMMARY.md`
  locks final verdict + venue. Pipeline stopped for user sign-off before any figures/writing.
