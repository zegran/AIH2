# Zenodo deposit — click-path

Upload the **dataset only** (no manuscript). All files are in this `zenodo/` folder.

## Pre-deposit checklist
- [ ] You have a Zenodo account (zenodo.org)
- [ ] You have the Zenodo DOI to insert into `conclusion.tex` after deposit

## Step-by-step

### 1. Log in to Zenodo
Go to https://zenodo.org and sign in.

### 2. Start a new upload
Click **"+ New Upload"** (top menu, green button).

### 3. Set upload type
Select **Dataset**.

### 4. Upload files (one-shot: use the zip)
Upload **`aih2_dataset_v1.zip`** — this contains all dataset files in one bundle.
Optionally also upload the individual CSVs and support files for in-browser preview:
- `aih2_v1.csv`
- `rate_extraction.csv`
- `data_dictionary.md`
- `README.md`
- `CITATION.cff`
- `LICENSE_CC-BY-4.0.txt`

### 5. Fill in metadata
Copy-paste from `ZENODO_METADATA.md`:

| Field | Value |
|---|---|
| **Title** | AIH2: A Provenance-Tracked Open Dataset and Reproducible Analysis for Aluminum–Water Hydrolysis Hydrogen Production |
| **Version** | 1.0.0 |
| **Access** | Open |
| **License** | Creative Commons Attribution 4.0 International |
| **Creator** | Unal, Dogukan — ORCID 0009-0006-5102-8013 |
| **Affiliation** | IPEC, Industrial Project Engineering Consulting, Ankara, Türkiye |
| **Keywords** | aluminum-water hydrolysis; hydrogen production; open dataset; reproducibility; data leakage; meta-analysis; activation energy; methodological heterogeneity |
| **Related identifier** | isSupplementTo → https://github.com/zegran/AIH2 |

Paste the **Description** from `ZENODO_METADATA.md` into the Zenodo description field.

### 6. Publish
Click **Save**, then **Publish**. Zenodo mints a DOI immediately.

### 7. After deposit — update the manuscript
Replace the DOI placeholder in **two places**:

1. `paper/sections/conclusion.tex` — find `\todo{Zenodo DOI}` (line 17) and replace with:
   ```latex
   \href{https://doi.org/10.5281/zenodo.XXXXXXX}{https://doi.org/10.5281/zenodo.XXXXXXX}
   ```
2. `submission_package/zenodo/CITATION.cff` — update the `doi:` field.

Then commit and push so CI rebuilds the PDF with the live DOI.
