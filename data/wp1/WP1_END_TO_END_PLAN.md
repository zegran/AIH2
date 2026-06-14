# AIH2 — WP1 End-to-End Plan: Access-Gated Dataset Construction

> **Governing principle.** A study has **zero value until its dataset is in our hands and
> extracted**. The only metric that counts is **extracted, QC'd rows** — never "papers found".
> Growing the count of discovered-but-inaccessible papers *increases risk, not value*: it
> creates false confidence and a backlog we cannot convert. Therefore discovery is **gated**
> by access. We never expand the pool faster than we can extract it.

---

## 0. The three states of a study (and the one that matters)

Every study lives in exactly one state. Movement is one-directional and gated.

| State | Meaning | Counts toward target? |
|-------|---------|------------------------|
| **Discovered** | Found via search; abstract read; in-scope | ❌ No |
| **Accessible** | Full text obtained **and** data is in extractable form (table or digitizable figure) | ❌ No |
| **Extracted** | Condition rows in the sheet, provenance + quality filled, QC-eligible | ✅ **Yes — the only real metric** |

**Rule:** a study may not enter "Accessible" until we have verified *both* (a) we hold the full
text and (b) the data exists as a table or a figure we can digitize (not a single text
sentence). It may not be claimed as progress until "Extracted".

**Anti-goal:** a large Discovered pile with a small Extracted count. We actively keep
`Discovered − Extracted` small.

---

## 1. Value function (how we decide which study is worth the effort)

```
study_value = in_scope  ×  access  ×  data_richness  ×  class_need
```

- `in_scope` (0/1): aqueous Al hydrolysis only (scope lock). 0 ⇒ drop.
- `access` (0/1): full text obtainable now (OA, repository, or institutional).
- `data_richness` (0–3): 0 = single text number · 1 = small table · 2 = multi-condition table ·
  3 = parametric study (many conditions) or digitizable figure series.
- `class_need` (0–2): how much its `system_class` still needs rows (2 = starving class).

We extract **high-value first**. A paywalled study reporting one number in prose
(`access`×`richness` ≈ low) is **deprioritized or dropped**, no matter how relevant it sounds.

---

## 2. Row accounting — the real target

| system_class | studies in pool | row target | status |
|---|---|---|---|
| pure_al_alkali | 26 | 90–120 | supply OK |
| waste_al | 16 | 60–80 | supply OK |
| mechanically_activated | 15 | 60–80 | supply OK |
| al_alloy | 10 | 50–70 | supply OK (borderline) |
| **liquid_metal_activated** | **4** | **40–50** | **UNDER-SUPPLIED — must expand** |
| **Total** | **71** | **~300 (floor 150)** | |

- Headline-claim threshold: **≥ 40 rows per class**. Below that → **exploratory-only**, declared
  honestly (never faked).
- We do **not** know real row yield until PDFs are open. Phase B *measures* it; everything
  downstream is sized from the measurement, not a guess.

---

## 3. The end-to-end pipeline (phases, gates, definition-of-done)

### Phase A — Access triage of the existing 71 (do this BEFORE any expansion)
**Goal:** convert "do we command the datasets?" from a feeling into a number.
1. Add three columns to the pool tracker: `access_status` (open / institutional / paywalled /
   unobtainable), `data_form` (table / figure / text-only), `data_richness` (0–3).
2. For each of the 71, check the source: open-access publishers (RSC, MDPI, Frontiers,
   Hydrogen, many conf.) are reachable now; Elsevier/Springer need institutional or author copy.
3. Output: a **prioritized extraction queue** + a hard count of how many of the 71 are
   *actually* extractable.
**Gate / DoD:** we know `N_accessible` and `N_unobtainable`. If a class's accessible studies
can't reach its row target, it is flagged **at-risk now**, not after wasted effort.

### Phase B — Extract the accessible core & measure real yield
**Goal:** get real rows from the highest-value accessible studies; learn the true row-per-study rate.
1. Retrieve PDFs (Zotero). Confirm **DOI** → replace citekey in `study_id`.
2. Extract: tables manually; figure curves via WebPlotDigitizer (`extraction_method`).
3. Enforce schema rules: `absent=0` vs `unreported=NaN`; fill `h2_yield_pct`; leave Phase-2
   columns blank; complete provenance + quality metadata; assign A/B/C tier.
4. After ~15–20 studies, compute **rows/study** and **rows/class**.
**Gate / DoD:** projected total and per-class rows are now *evidence-based*. Decide if/where
expansion is needed.

### Phase C — Targeted, access-gated expansion (only to fill measured gaps)
**Goal:** close *specific* row gaps — not grow the pile.
1. Priority 1: `liquid_metal_activated` → add studies until ≥ ~8–10 *accessible* ones
   (Ga-In-Sn / EGaIn / Galinstan-activated Al). Reference-mine the reviews
   (`kumar2020`, `musicco2025`, `cao2024`, `rafi2023`, `preez2021`) for primary sources.
2. Every new study must pass the **access+richness gate** before it is added — if we can't get
   its data, it does not enter the pool. We do not accumulate inaccessible studies.
3. Stop when each class meets its row target **or** is honestly declared exploratory-only.
**Gate / DoD:** no class is under target *for a reason we could have fixed*; remaining gaps are
documented as genuine literature limits.

### Phase D — Quality control (the credibility layer)
1. **Double-extract a 10–15% random sample** independently; report extraction error as a
   separate table (pre-empts "the contradiction is an extraction artifact" objection).
2. Verify A/B/C tiers are applied consistently.
3. Per-`system_class` N report; set exploratory-only flags.
**Gate / DoD:** extraction-error table exists; ≥ 150 rows total; provenance complete on every row.

### Phase E — Integration & modeling handoff
1. Write curated file to `data/curated/`; update `data/data_dictionary.md`.
2. Point Hydra `data.path` at the real dataset; rerun pipeline (WP2–WP4).
3. Confirm the **optimism gap** now surfaces (it was ~0 on synthetic data by construction).
**Gate / DoD:** pipeline produces real metrics + SHAP + Arrhenius check on real data.

---

## 4. Risk controls (the "don't endanger the work" layer)

- **Access gate** (Phase A/C): inaccessible studies never enter the pool. `Discovered −
  Extracted` is monitored and kept small.
- **Richness gate:** text-only single-number studies are deprioritized; we don't spend effort
  on low-yield sources.
- **High-quality-only sensitivity run** (A-tier subset): the decisive test of whether a
  contradiction is real physics or study noise.
- **Double-extraction:** quantifies *our own* reading error before we blame the literature.
- **Honest exploratory-only flag:** a starving class is labelled, never padded with weak rows.
- **DOI as group key:** prevents study-level leakage in CV (GroupKFold / LOSO).

---

## 5. Critical dependency — access route (CONFIRMED: open-access only)

**Decision locked (2026-06):** no institutional/library access. We work **open-access only**
(author copies and repository deposits included). Consequences:

- The **paywalled subset — chiefly Int. J. Hydrogen Energy (Elsevier) and Springer — is largely
  unreachable** and must be treated as such during Phase A triage, not assumed available.
- **Expansion (Phase C) is re-scoped toward open-access venues**: RSC Advances, MDPI (Materials,
  Energies, Molecules, Metals, Applied Sciences, Sustainability, Hydrogen), Frontiers, and
  conference proceedings — these dominate our reachable core.
- This makes Phase A triage **decisive**: it tells us how thin the OA core really is, and whether
  any `system_class` (especially `liquid_metal_activated`) can hit its row floor from OA sources
  alone. Classes that cannot are declared exploratory-only honestly.

**Tooling note — no Zotero connector.** A dedicated Zotero MCP connector does not exist in this
environment, so reference-manager automation is not available as a connector. Substitutes for the
actual underlying need (obtain OA full text + manage DOIs):
- **PubMed connector** (`get_full_text_article`, `get_copyright_status`) — works for the
  PMC-deposited OA subset (much of MDPI, some RSC); not for Elsevier.
- **Unpaywall-by-DOI** resolution and **Claude-in-Chrome** to fetch OA PDFs from publisher pages.
- DOIs/BibTeX maintained directly in the pool tracker (no Zotero round-trip required).

---

## 6. One-line summary of the discipline

> Discover cheaply, **gate on access**, extract relentlessly, and count only what is in the sheet.
> Never let the number of papers we *can't* use grow.

*Durable artifacts are English per project convention.*
