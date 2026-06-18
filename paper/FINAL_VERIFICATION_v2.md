# Final Verification v2 — Post-Remediation

Date: 2026-06-18. Executed: CLI_EXECUTE_REMEDIATION_CLEANUP.md.

---

## Objective Evidence

### B1 — Corrected figures promoted to paper/figures/

| File | paper/figures/ | results/real_v1/figures/ | Match? |
|---|---|---|---|
| fig1_optimism_gap.pdf | 34460 B · Jun 18 22:08 | 34460 B · Jun 18 20:45 | ✅ same size |
| **fig2_variance_decomposition.pdf** | **39836 B · Jun 18 22:08** | **39836 B · Jun 18 20:46** | ✅ **corrected** |
| fig3_particle_size_consistency.pdf | 44266 B · Jun 18 22:08 | 44266 B · Jun 18 20:46 | ✅ same size |
| fig4_ea_spread.pdf | 55855 B · Jun 18 22:08 | 55855 B · Jun 18 20:46 | ✅ same size |
| fig5_dataset_composition.pdf | 35766 B · Jun 18 22:08 | 35766 B · Jun 18 20:46 | ✅ same size |
| fig6_within_study_surface.pdf | 53709 B · Jun 18 22:08 | 53709 B · Jun 18 20:46 | ✅ same size |

Pre-correction fig2 was 39848 B. Corrected fig2 is 39836 B. Size mismatch eliminated. ✅

### B2 — DOCX regenerated after fig2 update

`submission_package/manuscript/main_review.docx` mtime: **Jun 18 22:10**
fig2 copy mtime: **Jun 18 22:08**
DOCX mtime (22:10) > fig2 copy mtime (22:08) ✅

### B3 — figure-catalog.md and TB_method_variance.md updated

`grep "0.717\|0.425" results/real_v1/figures/figure-catalog.md` → present ✅
`grep "0.55.*method\|0.33.*TC\|jointly explain 0.5" results/real_v1/figures/figure-catalog.md` → 0 results ✅
`TB_method_variance.md` updated: old numbers in CORRECTED table; headline now 0.717/0.425/0.081 ✅

### B4 — Strict consistency gate PASS

New consistency_gate.py checks:
- Abstract block contains 72%, 43%
- results.tex contains R²=0.717, 0.425, 0.081, CI 0.443
- figure-catalog.md fig2 section contains 0.717, 0.425 and NOT stale 0.55x or 0.33
- No standalone 0.553 or 0.332 in any .tex
- R²~0.55 optimism-gap preserved in results.tex and main.tex (positive control)

Result: **PASS** ✅

### C — Deletions confirmed

| Path deleted | Verified |
|---|---|
| `submission_package/dataset/` | `ls: cannot access` → confirmed ✅ |
| `release/aih2_dataset_v1/` | `ls: cannot access` → confirmed ✅ |
| `release/aih2_dataset_v1.zip` | `ls: no such file` → confirmed ✅ |
| `release/ZENODO_METADATA.md` | deleted ✅ |
| `release/ZENODO_PREVIEW.md` | deleted ✅ |
| `submission_package/zenodo/ZENODO_METADATA.md` | deleted ✅ |
| `submission_package/zenodo/ZENODO_STEPS.md` | deleted ✅ |
| `paper/preview/` | deleted ✅ |
| `temp/` | deleted ✅ |

### Surviving corrected bundle == canonical CSV

`submission_package/zenodo/aih2_v1.csv` TC values: `{'self_heating', 'isothermal_bath'}` — 0 uncontrolled ✅

### Number presence in manuscript (grep evidence)

| Section | Pattern | Found? |
|---|---|---|
| Abstract (main.tex) | 72% | ✅ line 47 |
| Abstract (main.tex) | 43% | ✅ line 49 |
| Highlights (main.tex) | 72% | ✅ line 74 |
| Results (results.tex) | R²=0.717 | ✅ line 63 |
| Results (results.tex) | R²=0.425 | ✅ line 65 |
| Results (results.tex) | R²=0.081 | ✅ line 68 |
| Discussion | apparatus 43%, TC 8% | ✅ updated |
| Introduction | 72% / apparatus 43% | ✅ updated |

### Old method-share 0.55 absent from compiled source

Old method-share 0.55 absent from abstract ✅ (gate asserts abstract has no old value)
`grep "0.553" paper/sections/*.tex paper/main.tex` → 0 results ✅
`grep "0.332" paper/sections/*.tex paper/main.tex` → only historical transition contexts (discussion.tex method.tex) ✅

### fig1 optimism-gap R²≈0.55 intact (must preserve)

`grep "0.5[4-7]" paper/sections/results.tex` → R²≈0.55–0.57 lines present ✅

### All gates

| Gate | Result |
|---|---|
| `uv run python tools/lint_paper.py` | **PASS** (58/58 cites, 0 hard errors, consistency PASS) |
| `uv run python tools/compliance_gate.py` | **PASS** (250 words, 6 keywords, Energy and AI) |
| `uv run python tools/consistency_gate.py` | **PASS** (per-section + catalog checks) |

---

## Deletion log (complete)

| # | Path | Reason |
|---|---|---|
| 1 | `submission_package/dataset/` | Pre-correction data (TC=uncontrolled); replaced by `zenodo/` |
| 2 | `release/aih2_dataset_v1/` | Pre-correction bundle |
| 3 | `release/aih2_dataset_v1.zip` | Pre-correction zip |
| 4 | `release/ZENODO_METADATA.md` | Orphaned planning doc for deleted record 10.5281/zenodo.20750297 |
| 5 | `release/ZENODO_PREVIEW.md` | Same |
| 6 | `submission_package/zenodo/ZENODO_METADATA.md` | Same |
| 7 | `submission_package/zenodo/ZENODO_STEPS.md` | Same |
| 8 | `paper/preview/` (entire dir) | Stale pandoc snapshot; GitHub link, old DOI, pre-correction figs |
| 9 | `temp/` (entire dir) | IRR JSON task files, fig6 test crops, scratch scripts |

---

## Final submission_package/ tree

```
submission_package/
├── MANIFEST.md                         ← updated; JOURNAL/ZENODO tags; deletion log
├── README.md
├── manuscript/
│   ├── main.tex
│   ├── sections/ (7 .tex files)
│   ├── figures/ (6 PDF + 6 PNG — all Jun 18 corrected)
│   └── main_review.docx                ← 294 KB; built Jun 18 22:10 on corrected fig2
├── paperwork/
│   ├── cover_letter.md                 ← Energy and AI; Zenodo DOI; no GitHub link
│   ├── energy_and_ai_checklist.md      ← venue locked
│   ├── highlights.md / highlights.txt
│   ├── suggested_reviewers.md
│   ├── ai_disclosure.md
│   └── COMPLIANCE_REPORT.md
├── zenodo/                             ← ONE corrected bundle
│   ├── aih2_v1.csv (TC={iso,self_heating}; 0 uncontrolled)
│   ├── rate_extraction.csv
│   ├── data_dictionary.md
│   ├── README.md
│   ├── CITATION.cff (doi: 10.5281/zenodo.20751918)
│   ├── LICENSE_CC-BY-4.0.txt
│   └── aih2_dataset_v1.zip
└── upload_ready/
    ├── graphical_abstract.pdf          ← R² bar chart; 72%/43%/8%/2%; 3.35×3.35 in
    ├── graphical_abstract.png          ← 300 dpi
    └── declaration_of_interest.md      ← standalone; "no competing interests"
```

---

## Definition of done — SATISFIED

- [x] Corrected fig2 in paper/figures/ (39836 B) and submission_package/manuscript/figures/
- [x] DOCX rebuilt after fig2 update (Jun 18 22:10 > Jun 18 22:08)
- [x] Strict consistency gate: per-section abstract+results checks; catalog check; PASS
- [x] figure-catalog.md and TB_method_variance.md updated with corrected numbers
- [x] All stale/duplicate bundles deleted (dataset/, aih2_dataset_v1, preview/, temp/)
- [x] ONE corrected dataset bundle: submission_package/zenodo/ (0 uncontrolled rows)
- [x] upload_ready/: graphical abstract + declaration of interest
- [x] MANIFEST.md rewritten with JOURNAL/ZENODO tags + deletion log
- [x] All gates PASS (consistency + lint + compliance)
- [x] Old DOI fixed in release/aih2_code_v1/README.md
