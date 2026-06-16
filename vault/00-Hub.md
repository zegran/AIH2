# AIH2 — Project Hub

**Topic:** Why the aluminum–water hydrolysis literature contradicts itself — a leakage-controlled,
provenance-tracked analysis. (Pivoted from the original "physics-validated ML" framing; see below.)
**Concept foundation (original framing, now historical):** [[concept-foundation]] →
`../plan/2026-06-14-aih2-concept-foundation.md`
**Frozen analysis protocol (the pivot):** `../plan/analysis-protocol.md`
**Venue:** **Energy and AI** (methodology + open dataset); IJHE if the physics pillar is later strengthened.

## Central finding (one line, pivoted)
The literature's apparent contradictions are **predominantly methodological, not physico-chemical**:
methodological covariates explain ~55% of between-study yield variance vs ~2% for physical regime
(temperature-control method ~33%). H1/H2/H3 (the original "real-physics" hypotheses) were **refuted**
under pre-registered testing; the methodological-artifact answer (T_B) is supported. See
`../results/real_v1/GO_NOGO_SUMMARY.md`.

## Map
- [[concept-foundation]]  immutable scientific core (start here)
- [[wp1-source-pool]]  WP1 literature source pool + contradiction evidence
- Papers/      literature notes (one per source study)
- Knowledge/   synthesized concepts (Arrhenius, shrinking-core, system_class taxonomy)
- Experiments/ run logs
- Results/     result notes
- Daily/       daily working notes (Turkish allowed)

## State (analysis campaign COMPLETE; paper in draft)
- [x] WP0 scaffold · WP1 dataset (315 yield rows / 31 studies + 76-row kinetic table; QC 0% error)
- [x] **WP2 leakage-controlled CV** — optimism gap 0.62–0.85, robust to dropping the dominant study
- [x] **Stress tests** — TEST1: the within-regime ML headline was porciuncula-driven → FAILS;
  TEST2: physics (Arrhenius) data recoverable
- [x] **H2 mixed-effects** → NULL (regime does not moderate the contradiction)
- [x] **H3 Arrhenius** (incl. rate digitization + QC) → NULL (Eₐ does not organize by regime)
- [x] **T_A / T_B** (methodological pivot, pre-registered) — T_A partial/null; **T_B SUPPORTED**
  (method R²=0.55 vs regime 0.02; temperature_control 0.33; survives confound check)
- [x] **WP5 figures** (5, reproducible) · **WP6 first draft** (`../paper/`, bibliography complete)
- [ ] Remaining (user-gated): TeX compile · elsarticle frontmatter (author info) · Zenodo DOI ·
  submission prep — see `../paper/SUBMISSION_PLAN.md`.

## Lifecycle position (governance, 2026-06-17)
| stage | status |
|---|---|
| Ideation | ✅ done |
| ML development (Phase 1) | ✅ done |
| Data curation (WP1) | ✅ done (yield + kinetic tables, QC'd) |
| Experiment analysis (WP2–WP4 + stress tests + T_A/T_B) | ✅ **done** — H1/H2/H3 refuted, T_B supported |
| Figures (WP5) | ✅ done |
| Paper writing (WP6) | 🟡 first draft + bibliography done; polish/compile/frontmatter pending |
| Self-review | ✅ first pass done (`../paper/SELF_REVIEW.md`) |
| Submission / rebuttal | ⬜ user-gated (compile, author info, Zenodo, venue) |
| Post-acceptance | ⬜ |

The analysis is complete. The disciplined, pre-registered campaign refuted the original physics
hypotheses and landed an honest positive answer (T_B: methodology, not physical regime, drives the
contradictions). Next is paper finalization, blocked only on user inputs (author/affiliation + a TeX
build path) — everything else can proceed now.
