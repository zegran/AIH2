# CLI Command — Ingest downloaded WP1 articles into the AIH2 archive

> Paste this into Claude Code (running at the AIH2 repo root). It ingests the manually
> downloaded papers, screens them against the WP1 source pool + scope lock, archives the
> suitable ones, and reports what is still missing. Durable artifacts stay in English.

---

## Inputs

**SOURCE (downloaded files, outside the repo):**
```
C:\01_Laptop1_Aktif\Claude Projelerim\Ex Projeler\Atlas Inkbator\atlas_incubator\data\downloads\aih2_wp1\pdf\   (35 PDFs)
C:\01_Laptop1_Aktif\Claude Projelerim\Ex Projeler\Atlas Inkbator\atlas_incubator\data\downloads\aih2_wp1\md\    (35 MD files)
```

**CANONICAL LISTS (in this repo, the matching ground-truth):**
```
data/wp1/AIH2_WP1_source_pool.md          # 71 IN-scope studies (citekey, title, system_class)
data/wp1/AIH2_WP1_non_open_access.bib     # 49 paywalled entries (citekey, title, doi where known)
data/curated/data_dictionary.md           # schema + scope lock
```

---

## Task

### 1. Read every `*.md` in the SOURCE `md/` folder
For each MD file, extract: title, authors, year, journal, DOI (if present), abstract.

### 2. Match each file to a source-pool study
Match priority: (a) DOI exact match against the `.bib`; else (b) fuzzy title match (≥ ~0.85
similarity) against `AIH2_WP1_source_pool.md`. Record the matched **citekey**. If no match → mark
`UNMATCHED` (a new candidate to screen, not an error).

### 3. Apply the scope lock (concept-foundation precedence)
- **IN (archive as data source):** aqueous Al-water hydrolysis — pure_al_alkali, al_alloy,
  mechanically_activated, liquid_metal_activated, waste_al.
- **OUT → background (do NOT archive as data source):** acid hydrolysis, Al–NaBH₄ hybrids,
  non-aqueous, **Mg/other-metal-dominant**, reviews, pure simulation. Move these to a
  `background/` subfolder and flag them.

### 4. Archive the suitable (IN-scope, matched) files
Create these folders in the repo if absent, then **copy** (do not move from source) and
**rename to the citekey**:
```
data/raw/literature/pdf/<citekey>.pdf      # raw PDFs (data/raw is gitignored)
data/raw/literature/md/<citekey>.md        # extracted text / notes
vault/Papers/<citekey>.md                  # Obsidian reading-note stub (title, DOI, system_class, key conditions)
```
Background / out-of-scope items go to `data/raw/literature/background/` instead.

### 5. Write an ingest manifest
`data/wp1/ingest_manifest.csv` with columns:
`source_filename, matched_citekey, doi, in_scope(Y/N), system_class, action(archived|background|unmatched), title, notes`

### 6. Update study state (end-to-end plan)
For every archived citekey, set its state to **Accessible** (full text in hand). If the MD reveals
a DOI that was `pending` in the `.bib`, fill it in and note it. These archived studies become the
**Phase B extraction queue**.

### 7. Report the gaps — `data/wp1/INGEST_GAP_REPORT.md`
Must list, explicitly:
1. **Missing IN-scope studies** — the 71 pool citekeys NOT present in the download set (these still
   need retrieval). Group by `system_class` and show `obtained / pool` counts per class.
2. **Out-of-scope downloads** moved to background (with reason each).
3. **Unmatched downloads** — files that matched no pool study (new candidates to screen).
4. **Metadata gaps per archived item** — missing DOI, missing reported yield/temperature in the MD,
   figure-only data (needs WebPlotDigitizer), etc.
5. **Per-`system_class` readiness vs the row targets** (pure_al_alkali 90–120, al_alloy 50–70,
   mechanically_activated 60–80, liquid_metal_activated 40–50, waste_al 60–80); flag classes that
   cannot reach ≥40 rows from the obtained set as **at-risk / exploratory-only**.

---

## Rules
- **Copy, never move** from the SOURCE folder (leave the user's downloads intact).
- **Do not invent DOIs.** Use only DOIs found in the MD files or the `.bib`.
- Filenames in SOURCE may be titles, DOIs, or arbitrary — rely on MD content for matching, not the filename.
- Keep all archived identifiers, notes, and the report in **English**.
- Do not delete or overwrite existing archive files; if a citekey already exists, append `_v2` and note the duplicate.

## Definition of done
- Every SOURCE MD is classified (archived / background / unmatched) and appears in `ingest_manifest.csv`.
- `INGEST_GAP_REPORT.md` lists missing IN-scope studies per class + all gaps above.
- No out-of-scope (Mg/acid/non-aqueous/review) file is archived as a data source.
- Suggested commit: `chore(data): ingest WP1 downloaded literature (NN archived, MM background) + gap report`.
