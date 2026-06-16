# AIH2 — Project Hub

**Topic:** Physics-validated interpretable ML for the aluminum–water reaction (H2 yield).
**Concept foundation (immutable core):** [[concept-foundation]] →
`../plan/2026-06-14-aih2-concept-foundation.md`
**Design spec:** `../plan/2026-06-14-aih2-design-spec.md`
**Venue:** IJHE (primary) → Energy and AI (fallback).

## Central thesis (one line)
The Al–water hydrolysis literature contradicts itself about parameter effects on H2 yield;
this is an unsolved scientific problem, resolved here with leakage-controlled, physics-validated
interpretable ML on a unified open dataset. See [[concept-foundation]].

## Map
- [[concept-foundation]]  immutable scientific core (start here)
- [[wp1-source-pool]]  WP1 literature source pool + contradiction evidence
- Papers/      literature notes (one per source study)
- Knowledge/   synthesized concepts (Arrhenius, shrinking-core, system_class taxonomy)
- Experiments/ run logs
- Results/     result notes
- Daily/       daily working notes (Turkish allowed)

## State
- [x] Concept foundation · spec · implementation plan signed off
- [x] Phase 1 scaffold (tested end-to-end on synthetic fixture; GitHub zegran/AIH2, tag phase1-scaffold)
- [x] **WP1 archive assembled** ([[wp1-source-pool]]; 59-study pool, all in hand)
- [x] **WP1 Phase B extraction COMPLETE** — 315 condition-level rows, validator PASS (floor 150 met).
  Per class: pure_al_alkali 162 · mechanically_activated 69 · al_alloy 45 · waste_al 20 (exploratory)
  · liquid_metal_activated 19 (exploratory). Both contradiction signals captured (H1 size, rate–yield).
- [x] **Data QC** — double-extraction (52 rows, **0% value error**) + classification audit
  (31/31 studies; 1 fix: dudoladov2016 → liquid_metal_activated). `system_class` axis verified.
- [ ] **WP2–WP4 real-data run** ← next critical stage: write `data/curated/`, repoint Hydra, run
  GroupKFold + group-weighting + porciuncula-out + SHAP/ALE + Arrhenius Eₐ on the 315 rows.
- [ ] Phase 2 physics (shrinking-core SCM + consistency metrics) — required to complete the
  "physics-validated" claim before submission.
- [ ] Paper writing (IJHE) → self-review → submission.

## Lifecycle position (governance, 2026-06-16)
| stage | status | primary skill/agent |
|---|---|---|
| Ideation | ✅ done (concept-foundation locked) | research-ideation, brainstorming |
| ML development (Phase 1) | ✅ scaffold tested on synthetic | architecture-design, TDD, code-review |
| Data curation (WP1) | ✅ 315 rows, QC'd, class-verified | literature-reviewer, consensus-evidence-search, citation-verification |
| **Experiment analysis (WP2–WP4)** | ⏭️ **NEXT** (run on real data) | **results-analysis** |
| Phase 2 physics (SCM) | ⬜ stubs only — pre-submission dependency | results-analysis |
| Paper writing | ⬜ `paper/` stub only | ml-paper-writing, writing-anti-ai, citation-verification |
| Self-review | ⬜ | paper-self-review |
| Submission / rebuttal | ⬜ | review-response, rebuttal-writer |
| Post-acceptance | ⬜ | post-acceptance |

Pipeline confirmed correct. We are at the **ML-development → experiment-analysis boundary**: the
Phase 1 pipeline is built+tested, the real dataset is curated+QC'd, so the next action is the first
real WP2–WP4 run. The headline "physics-validated" claim additionally needs Phase 2 SCM before the
paper is complete (Arrhenius Eₐ validation already exists in Phase 1).
