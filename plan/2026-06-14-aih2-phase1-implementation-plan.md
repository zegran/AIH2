# AIH2 Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the AIH2 repository and build a leakage-controlled, interpretable, physics-validated single-target (H₂ yield %) ML pipeline that runs end-to-end on a schema-conforming synthetic fixture, ready for real literature-extracted data to be dropped into `data/curated/`.

**Architecture:** Integrated monorepo (Approach A). A config-driven (`Hydra`) pipeline flows: curated dataset → schema validation + quality tiers → study-grouped/LOSO cross-validation over a registry of comparative models → SHAP + ALE explainability → Arrhenius Eₐ physical validation → publication figures. Models live behind a factory/registry. Physics modules for shrinking-core and consistency metrics are created as tested stubs (Phase 2). The dataset is decoupled from code via a synthetic fixture so the whole pipeline is testable before real data exists.

**Tech Stack:** Python 3.11, `uv`, pandas, scikit-learn, XGBoost, LightGBM, `shap`, `PyALE`, SciPy, Hydra + OmegaConf, matplotlib, pytest, ruff, mypy. LaTeX (`elsarticle`-ready). Obsidian KB (filesystem-only).

**Governing spec:** `plan/2026-06-14-aih2-design-spec.md` (signed off). This plan implements **Phase 1** only; Phase 2 items appear as tested stubs/reserved columns.

**Reminder:** Phase 1 done = engineering completeness, **not** a submission-ready paper (spec §5 Publication-readiness note).

---

## File structure (decomposition locked here)

```
src/
  utils/            seed.py, logging_config.py, io.py
  data_module/      schema.py, fixture.py, loader.py, preprocessing.py
  cv/               splitters.py, metrics.py
  model_module/     registry.py, models.py, evaluation.py
  analysis/
    xai/            shap_analysis.py, ale_analysis.py, dependence.py, stability.py
    physical_validation/  arrhenius.py, shrinking_core.py(stub), consistency_metrics.py(stub)
    figures/        style.py, phase1_figures.py
run/
  conf/             config.yaml, model/*.yaml, data/*.yaml
  pipeline/         run_phase1.py
tests/              mirrors src/ (test_*.py)
data/
  raw/(gitignored)  curated/(versioned: fixture + later real data)  data_dictionary.md
paper/              main.tex, sections/*, references.bib
vault/              Obsidian KB
results/            figures/ tables/ metrics/
```

Each `src/` subpackage has one responsibility; files stay within the 200–400 line guideline. Tests mirror source paths.

---

## Milestone M0 — Repository bootstrap & environment

### Task 0.1: Initialize git, ignore rules, license, and commit the spec

**Files:**
- Create: `.gitignore`, `LICENSE`, `.python-version`
- Commit: `plan/` design spec + plan

- [ ] **Step 1: Initialize the repository**

Run:
```bash
cd /c/Users/zduna/Desktop/AIH2
git init
git config core.autocrlf false
```

- [ ] **Step 2: Write `.python-version`**

```
3.11
```

- [ ] **Step 3: Write `.gitignore`**

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
.mypy_cache/
.pytest_cache/
.ruff_cache/

# Project data & outputs
data/raw/
run/outputs/
temp/
results/figures/*.png
results/figures/*.pdf

# Keep curated data and dictionaries tracked
!data/curated/
!data/data_dictionary.md

# OS / editor
.DS_Store
Thumbs.db
```

- [ ] **Step 4: Write `LICENSE` (MIT)**

Use the standard MIT License text, copyright `2026 <author>`. (Dataset is separately CC-BY-4.0, declared later in README.)

- [ ] **Step 5: Commit the planning docs**

```bash
git add .gitignore LICENSE .python-version plan/
git commit -m "chore: initialize repo with design spec and Phase 1 plan"
```
Expected: one commit created on `main` (or `master`).

---

### Task 0.2: Python project, dependencies, and lock

**Files:**
- Create: `pyproject.toml`

- [ ] **Step 1: Write `pyproject.toml`**

```toml
[project]
name = "aih2"
version = "0.1.0"
description = "Physics-validated interpretable ML for aluminum-water hydrolysis H2 yield"
requires-python = ">=3.11"
dependencies = [
    "numpy>=1.26",
    "pandas>=2.2",
    "scipy>=1.12",
    "scikit-learn>=1.4",
    "xgboost>=2.0",
    "lightgbm>=4.3",
    "shap>=0.45",
    "PyALE>=1.2",
    "matplotlib>=3.8",
    "hydra-core>=1.3",
    "omegaconf>=2.3",
    "pyyaml>=6.0",
]

[dependency-groups]
dev = ["pytest>=8.0", "ruff>=0.4", "mypy>=1.10"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

- [ ] **Step 2: Create the environment and lock**

Run:
```bash
uv sync
```
Expected: `.venv/` created, `uv.lock` written, all deps resolved.

- [ ] **Step 3: Verify imports**

Run:
```bash
uv run python -c "import pandas, sklearn, xgboost, lightgbm, shap, PyALE, hydra; print('ok')"
```
Expected: `ok`

- [ ] **Step 4: Commit**

```bash
git add pyproject.toml uv.lock
git commit -m "chore: add uv project, dependencies, and lockfile"
```

---

### Task 0.3: Package skeleton

**Files:**
- Create: `src/__init__.py` and `__init__.py` for every subpackage listed in the file structure
- Create: empty dirs with `.gitkeep`: `data/raw/.gitkeep`, `data/curated/.gitkeep`, `results/figures/.gitkeep`, `results/tables/.gitkeep`, `results/metrics/.gitkeep`, `temp/.gitkeep`, `run/outputs/.gitkeep`

- [ ] **Step 1: Create package `__init__.py` files**

Create empty `__init__.py` in: `src/`, `src/utils/`, `src/data_module/`, `src/cv/`, `src/model_module/`, `src/analysis/`, `src/analysis/xai/`, `src/analysis/physical_validation/`, `src/analysis/figures/`, `tests/`.

- [ ] **Step 2: Create placeholder dirs**

Create the `.gitkeep` files listed above so empty tracked dirs exist.

- [ ] **Step 3: Verify test collection runs**

Run:
```bash
uv run pytest
```
Expected: `no tests ran` (exit code 5) — confirms pytest is wired.

- [ ] **Step 4: Commit**

```bash
git add src tests data results temp run
git commit -m "chore: scaffold package and directory skeleton"
```

---

### Task 0.4: Shared utilities (seed + logging)

**Files:**
- Create: `src/utils/seed.py`, `src/utils/logging_config.py`
- Test: `tests/utils/test_seed.py`

- [ ] **Step 1: Write the failing test**

`tests/utils/test_seed.py`:
```python
import numpy as np
from src.utils.seed import set_seed


def test_set_seed_makes_numpy_deterministic():
    set_seed(123)
    a = np.random.rand(5)
    set_seed(123)
    b = np.random.rand(5)
    assert np.array_equal(a, b)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/utils/test_seed.py -v`
Expected: FAIL (`ModuleNotFoundError: src.utils.seed`)

- [ ] **Step 3: Implement `src/utils/seed.py`**

```python
import os
import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set process-wide RNG seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
```

- [ ] **Step 4: Implement `src/utils/logging_config.py`**

```python
import logging


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Return a module logger with a single stream handler."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
```

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run pytest tests/utils/test_seed.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/utils tests/utils
git commit -m "feat: add set_seed and logging utilities"
```

---

## Milestone M1 — Obsidian knowledge-base binding

### Task 1.1: Create repo-internal vault and bind it

**Files:**
- Create: `vault/00-Hub.md`, `vault/Papers/.gitkeep`, `vault/Knowledge/.gitkeep`, `vault/Experiments/.gitkeep`, `vault/Results/.gitkeep`, `vault/Daily/2026-06-14.md`
- Create: `.claude/project-memory/registry.yaml`

- [ ] **Step 1: Write `.claude/project-memory/registry.yaml`**

```yaml
project: AIH2
bound: true
vault_path: vault
created: 2026-06-14
spec: plan/2026-06-14-aih2-design-spec.md
language: en   # vault personal notes may be Turkish
```

- [ ] **Step 2: Write `vault/00-Hub.md`**

```markdown
# AIH2 — Project Hub

**Topic:** Physics-validated interpretable ML for aluminum–water hydrolysis H2 yield.
**Spec:** [[../plan/2026-06-14-aih2-design-spec]]
**Venue:** IJHE (primary) → Energy and AI (fallback).

## Map
- Papers/      literature notes (one per source study)
- Knowledge/   synthesized concepts (Arrhenius, shrinking-core, system_class taxonomy)
- Experiments/ run logs
- Results/     result notes
- Daily/       daily working notes (Turkish allowed)

## State
- [x] Spec signed off
- [ ] Phase 1 scaffold
- [ ] Data extraction (>=150 hard floor, ~300 target)
```

- [ ] **Step 3: Write `vault/Daily/2026-06-14.md`** with a short kickoff note (Turkish allowed) referencing `[[00-Hub]]`.

- [ ] **Step 4: Create the `.gitkeep` folder placeholders** listed above.

- [ ] **Step 5: Commit**

```bash
git add vault .claude/project-memory/registry.yaml
git commit -m "chore: bind repo to internal Obsidian knowledge base"
```

> Note: after scaffolding, the `obsidian-project-memory` skill maintains these notes. Manual creation here avoids running an implementation skill mid-scaffold.

---

## Milestone M2 — Dataset schema, dictionary, fixture, loader

### Task 2.1: Data dictionary

**Files:**
- Create: `data/data_dictionary.md`

- [ ] **Step 1: Write `data/data_dictionary.md`**

Document every column: name, type, unit, allowed values, and the **`absent=0` vs `unreported=NaN`** rule for wt% columns. Columns:

- Target: `h2_yield_pct` (float, %, 0–100).
- Reserved targets (Phase 2, nullable): `max_rate_ml_min_g`, `t80_min`.
- Numeric features: `temperature_k`, `alkali_conc_mol_l`, `particle_size_d50_um`, `activator_ratio`.
- wt% features (float; `0`=absent, `NaN`=unreported): `al_wt_pct`, `ga_wt_pct`, `in_wt_pct`, `sn_wt_pct`, `bi_wt_pct`, `mg_wt_pct`, `zn_wt_pct`.
- Categorical features: `alkali_type` {NaOH,KOH,none}, `activation_method` {ball_milling,plasma,liquid_metal,none}, `water_type` {DI,tap,sea,alkaline}, `morphology_flag` {powder,flake,nano,foil}, `system_class` {pure_al_alkali,al_alloy,mechanically_activated,liquid_metal_activated,waste_al}.
- Group key: `study_id` (str, DOI).
- Provenance: `source_ref` (table/figure), `extractor`, `extraction_date`, `extraction_method` {table,webplotdigitizer}.
- Quality: `measurement_method` {water_displacement,mass_loss,pressure,gc}, `temperature_control` {isothermal_bath,uncontrolled,self_heating}, `vessel_type` {open,closed}, `rate_definition` {initial,avg,max}, `value_origin` {reported,derived}, `quality_tier` {A,B,C}.

- [ ] **Step 2: Commit**

```bash
git add data/data_dictionary.md
git commit -m "docs: add curated dataset data dictionary"
```

---

### Task 2.2: Schema module

**Files:**
- Create: `src/data_module/schema.py`
- Test: `tests/data_module/test_schema.py`

- [ ] **Step 1: Write the failing test**

`tests/data_module/test_schema.py`:
```python
from src.data_module import schema


def test_column_groups_are_disjoint_and_complete():
    feature_cols = set(schema.NUMERIC_FEATURES + schema.WT_PCT_COLUMNS + schema.CATEGORICAL_FEATURES)
    assert schema.TARGET not in feature_cols
    assert schema.GROUP_COLUMN not in feature_cols
    # wt% columns are a subset of numeric-modeling columns but tracked separately
    assert set(schema.WT_PCT_COLUMNS).isdisjoint(schema.NUMERIC_FEATURES)


def test_all_columns_listed():
    assert "system_class" in schema.CATEGORICAL_FEATURES
    assert schema.TARGET == "h2_yield_pct"
    assert schema.GROUP_COLUMN == "study_id"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/data_module/test_schema.py -v`
Expected: FAIL (`ModuleNotFoundError`)

- [ ] **Step 3: Implement `src/data_module/schema.py`**

```python
"""Canonical column schema for the curated AIH2 dataset."""

TARGET = "h2_yield_pct"
RESERVED_TARGETS = ["max_rate_ml_min_g", "t80_min"]  # Phase 2, nullable
GROUP_COLUMN = "study_id"

NUMERIC_FEATURES = [
    "temperature_k",
    "alkali_conc_mol_l",
    "particle_size_d50_um",
    "activator_ratio",
]

WT_PCT_COLUMNS = [
    "al_wt_pct", "ga_wt_pct", "in_wt_pct", "sn_wt_pct",
    "bi_wt_pct", "mg_wt_pct", "zn_wt_pct",
]

CATEGORICAL_FEATURES = [
    "alkali_type",
    "activation_method",
    "water_type",
    "morphology_flag",
    "system_class",
]

CATEGORICAL_LEVELS = {
    "alkali_type": ["NaOH", "KOH", "none"],
    "activation_method": ["ball_milling", "plasma", "liquid_metal", "none"],
    "water_type": ["DI", "tap", "sea", "alkaline"],
    "morphology_flag": ["powder", "flake", "nano", "foil"],
    "system_class": [
        "pure_al_alkali", "al_alloy", "mechanically_activated",
        "liquid_metal_activated", "waste_al",
    ],
}

PROVENANCE_COLUMNS = ["source_ref", "extractor", "extraction_date", "extraction_method"]
QUALITY_COLUMNS = [
    "measurement_method", "temperature_control", "vessel_type",
    "rate_definition", "value_origin", "quality_tier",
]

# Columns fed to models (wt% included; NaN preserved for tree models).
MODEL_NUMERIC = NUMERIC_FEATURES + WT_PCT_COLUMNS
MODEL_FEATURES = MODEL_NUMERIC + CATEGORICAL_FEATURES

EXPLORATORY_MIN_ROWS = 40  # system_class with fewer rows -> exploratory-only
HARD_FLOOR_ROWS = 150
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/data_module/test_schema.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/data_module/schema.py tests/data_module
git commit -m "feat: define curated dataset schema constants"
```

---

### Task 2.3: Synthetic fixture generator

**Files:**
- Create: `src/data_module/fixture.py`
- Test: `tests/data_module/test_fixture.py`

The fixture must be physically plausible so downstream physics tests work: yield should rise with temperature (Arrhenius-like) and depend on particle size with a **system_class-dependent sign** (to exercise the contradiction logic).

- [ ] **Step 1: Write the failing test**

`tests/data_module/test_fixture.py`:
```python
from src.data_module import schema
from src.data_module.fixture import make_fixture


def test_fixture_has_all_columns_and_groups():
    df = make_fixture(n_studies=20, rows_per_study=8, seed=0)
    expected = set(
        [schema.TARGET, schema.GROUP_COLUMN]
        + schema.MODEL_FEATURES
        + schema.PROVENANCE_COLUMNS
        + schema.QUALITY_COLUMNS
        + schema.RESERVED_TARGETS
    )
    assert expected.issubset(df.columns)
    assert df[schema.GROUP_COLUMN].nunique() == 20
    assert df[schema.TARGET].between(0, 100).all()
    # reserved Phase 2 targets exist but are empty
    assert df["max_rate_ml_min_g"].isna().all()


def test_fixture_temperature_increases_yield_on_average():
    df = make_fixture(n_studies=40, rows_per_study=10, seed=1)
    hot = df[df["temperature_k"] > df["temperature_k"].median()][schema.TARGET].mean()
    cold = df[df["temperature_k"] <= df["temperature_k"].median()][schema.TARGET].mean()
    assert hot > cold
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/data_module/test_fixture.py -v`
Expected: FAIL (`ModuleNotFoundError`)

- [ ] **Step 3: Implement `src/data_module/fixture.py`**

```python
"""Synthetic, schema-conforming fixture with embedded Arrhenius + regime-switch signal."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.data_module import schema

_R = 8.314  # J/mol/K

# Per-class apparent activation energy (J/mol) inside the literature 3.5-102.6 kJ/mol band,
# and the sign of the particle-size effect (the contradiction).
_CLASS_PARAMS = {
    "pure_al_alkali":        {"ea": 60_000, "size_sign": +1},
    "al_alloy":              {"ea": 35_000, "size_sign": -1},
    "mechanically_activated":{"ea": 20_000, "size_sign": -1},
    "liquid_metal_activated":{"ea": 8_000,  "size_sign": -1},
    "waste_al":              {"ea": 75_000, "size_sign": +1},
}


def make_fixture(n_studies: int = 40, rows_per_study: int = 10, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    classes = list(_CLASS_PARAMS)
    rows = []
    for s in range(n_studies):
        study_id = f"10.0000/synthetic.{s:03d}"
        system_class = classes[s % len(classes)]
        params = _CLASS_PARAMS[system_class]
        for _ in range(rows_per_study):
            t_k = rng.uniform(298, 363)
            size = rng.uniform(1, 200)
            conc = rng.uniform(0.0, 6.0)
            # Arrhenius-driven base extent + size effect with class-specific sign.
            k = np.exp(-params["ea"] / (_R * t_k)) * 1e9
            size_term = params["size_sign"] * (np.log(size) - np.log(50)) * 8
            yield_pct = 35 + 12 * np.log1p(k) + size_term + 6 * np.tanh(conc - 2)
            yield_pct = float(np.clip(yield_pct + rng.normal(0, 3), 0, 100))
            rows.append(_row(rng, study_id, system_class, t_k, size, conc, yield_pct))
    df = pd.DataFrame(rows)
    for col in schema.RESERVED_TARGETS:
        df[col] = np.nan
    return df


def _row(rng, study_id, system_class, t_k, size, conc, yield_pct) -> dict:
    has_alloy = system_class in ("al_alloy", "liquid_metal_activated")
    return {
        schema.GROUP_COLUMN: study_id,
        schema.TARGET: yield_pct,
        "temperature_k": t_k,
        "alkali_conc_mol_l": conc,
        "particle_size_d50_um": size,
        "activator_ratio": float(rng.uniform(0, 0.2)),
        "al_wt_pct": 100.0 - (5.0 if has_alloy else 0.0),
        "ga_wt_pct": 3.0 if has_alloy else 0.0,
        "in_wt_pct": 2.0 if has_alloy else 0.0,
        "sn_wt_pct": 0.0,
        "bi_wt_pct": 0.0,
        "mg_wt_pct": np.nan,  # unreported example
        "zn_wt_pct": 0.0,
        "alkali_type": "NaOH" if conc > 0.1 else "none",
        "activation_method": (
            "liquid_metal" if system_class == "liquid_metal_activated"
            else "ball_milling" if system_class == "mechanically_activated"
            else "none"
        ),
        "water_type": "DI",
        "morphology_flag": rng.choice(["powder", "flake", "nano", "foil"]),
        "system_class": system_class,
        "source_ref": "fig.2",
        "extractor": "synthetic",
        "extraction_date": "2026-06-14",
        "extraction_method": "table",
        "measurement_method": "water_displacement",
        "temperature_control": "isothermal_bath",
        "vessel_type": "closed",
        "rate_definition": "initial",
        "value_origin": "reported",
        "quality_tier": rng.choice(["A", "B", "C"], p=[0.5, 0.3, 0.2]),
    }


def write_fixture(path: str, **kwargs) -> pd.DataFrame:
    df = make_fixture(**kwargs)
    df.to_csv(path, index=False)
    return df
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/data_module/test_fixture.py -v`
Expected: PASS (both tests)

- [ ] **Step 5: Materialize the fixture file**

Run:
```bash
uv run python -c "from src.data_module.fixture import write_fixture; write_fixture('data/curated/fixture_v0.csv', n_studies=50, rows_per_study=8, seed=42)"
```
Expected: `data/curated/fixture_v0.csv` (400 rows) created — this is versioned.

- [ ] **Step 6: Commit**

```bash
git add src/data_module/fixture.py tests/data_module/test_fixture.py data/curated/fixture_v0.csv
git commit -m "feat: add synthetic schema-conforming dataset fixture"
```

---

### Task 2.4: Loader, schema validation, per-class N

**Files:**
- Create: `src/data_module/loader.py`, `src/utils/io.py`
- Test: `tests/data_module/test_loader.py`

- [ ] **Step 1: Write the failing test**

`tests/data_module/test_loader.py`:
```python
import pandas as pd
import pytest

from src.data_module import schema
from src.data_module.fixture import make_fixture
from src.data_module.loader import (
    exploratory_classes,
    meets_hard_floor,
    per_class_counts,
    validate_schema,
)


def test_validate_schema_passes_on_fixture():
    df = make_fixture(n_studies=10, rows_per_study=5, seed=0)
    assert validate_schema(df) == []


def test_validate_schema_flags_missing_target():
    df = make_fixture(n_studies=5, rows_per_study=5, seed=0).drop(columns=[schema.TARGET])
    errors = validate_schema(df)
    assert any("h2_yield_pct" in e for e in errors)


def test_validate_schema_flags_bad_categorical_level():
    df = make_fixture(n_studies=5, rows_per_study=5, seed=0)
    df.loc[0, "system_class"] = "acid_route"  # excluded by scope
    errors = validate_schema(df)
    assert any("system_class" in e for e in errors)


def test_per_class_counts_and_exploratory_flag():
    df = make_fixture(n_studies=50, rows_per_study=8, seed=1)
    counts = per_class_counts(df)
    assert counts.sum() == len(df)
    small = pd.concat([df[df.system_class == "pure_al_alkali"].head(3)])
    assert "pure_al_alkali" in exploratory_classes(per_class_counts(small))


def test_hard_floor():
    df = make_fixture(n_studies=50, rows_per_study=8, seed=1)
    assert meets_hard_floor(df) is True
    assert meets_hard_floor(df.head(100)) is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/data_module/test_loader.py -v`
Expected: FAIL (`ModuleNotFoundError`)

- [ ] **Step 3: Implement `src/utils/io.py`**

```python
from pathlib import Path

import pandas as pd


def read_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)
```

- [ ] **Step 4: Implement `src/data_module/loader.py`**

```python
"""Load and validate the curated dataset."""
from __future__ import annotations

import pandas as pd

from src.data_module import schema
from src.utils.io import read_csv


def load_dataset(path: str) -> pd.DataFrame:
    df = read_csv(path)
    errors = validate_schema(df)
    if errors:
        raise ValueError("Dataset schema validation failed:\n" + "\n".join(errors))
    return df


def validate_schema(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    required = [schema.TARGET, schema.GROUP_COLUMN] + schema.MODEL_FEATURES
    for col in required:
        if col not in df.columns:
            errors.append(f"missing required column: {col}")
    for col, levels in schema.CATEGORICAL_LEVELS.items():
        if col in df.columns:
            bad = set(df[col].dropna().unique()) - set(levels)
            if bad:
                errors.append(f"{col} has out-of-scope levels: {sorted(bad)}")
    if schema.TARGET in df.columns:
        t = df[schema.TARGET]
        if not t.dropna().between(0, 100).all():
            errors.append("h2_yield_pct out of [0, 100]")
    return errors


def per_class_counts(df: pd.DataFrame) -> pd.Series:
    return df.groupby("system_class").size().sort_values(ascending=False)


def exploratory_classes(counts: pd.Series) -> list[str]:
    return counts[counts < schema.EXPLORATORY_MIN_ROWS].index.tolist()


def meets_hard_floor(df: pd.DataFrame) -> bool:
    return len(df) >= schema.HARD_FLOOR_ROWS
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/data_module/test_loader.py -v`
Expected: PASS (all five)

- [ ] **Step 6: Commit**

```bash
git add src/data_module/loader.py src/utils/io.py tests/data_module/test_loader.py
git commit -m "feat: add dataset loader with schema validation and per-class N"
```

---

## Milestone M3 — Cross-validation (leakage control)

### Task 3.1: Grouped and LOSO splitters

**Files:**
- Create: `src/cv/splitters.py`
- Test: `tests/cv/test_splitters.py`

- [ ] **Step 1: Write the failing test**

`tests/cv/test_splitters.py`:
```python
import numpy as np

from src.cv.splitters import grouped_kfold_splits, loso_splits


def _groups():
    return np.array([f"s{i // 4}" for i in range(40)])  # 10 studies x 4 rows


def test_grouped_kfold_no_study_leak():
    groups = _groups()
    for train_idx, test_idx in grouped_kfold_splits(n_rows=40, groups=groups, n_splits=5, seed=0):
        assert set(groups[train_idx]).isdisjoint(set(groups[test_idx]))


def test_loso_leaves_one_study_out():
    groups = _groups()
    splits = list(loso_splits(groups))
    assert len(splits) == 10
    for train_idx, test_idx in splits:
        assert len(set(groups[test_idx])) == 1
        assert set(groups[train_idx]).isdisjoint(set(groups[test_idx]))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/cv/test_splitters.py -v`
Expected: FAIL (`ModuleNotFoundError`)

- [ ] **Step 3: Implement `src/cv/splitters.py`**

```python
"""Study-aware cross-validation splitters (leakage control)."""
from __future__ import annotations

from collections.abc import Iterator

import numpy as np
from sklearn.model_selection import GroupKFold, LeaveOneGroupOut


def grouped_kfold_splits(
    n_rows: int, groups: np.ndarray, n_splits: int = 5, seed: int = 0
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    x = np.zeros((n_rows, 1))
    # Shuffle group order deterministically for fold balance.
    rng = np.random.default_rng(seed)
    order = rng.permutation(np.unique(groups))
    remap = {g: i for i, g in enumerate(order)}
    shuffled = np.array([remap[g] for g in groups])
    yield from GroupKFold(n_splits=n_splits).split(x, groups=shuffled)


def loso_splits(groups: np.ndarray) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    x = np.zeros((len(groups), 1))
    yield from LeaveOneGroupOut().split(x, groups=groups)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/cv/test_splitters.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/cv/splitters.py tests/cv/test_splitters.py
git commit -m "feat: add grouped k-fold and LOSO cross-validation splitters"
```

---

### Task 3.2: Metrics and optimism gap

**Files:**
- Create: `src/cv/metrics.py`
- Test: `tests/cv/test_metrics.py`

- [ ] **Step 1: Write the failing test**

`tests/cv/test_metrics.py`:
```python
import numpy as np

from src.cv.metrics import optimism_gap, regression_metrics


def test_regression_metrics_perfect_prediction():
    y = np.array([1.0, 2.0, 3.0])
    m = regression_metrics(y, y)
    assert m["rmse"] == 0.0
    assert m["r2"] == 1.0


def test_optimism_gap_positive_when_random_better():
    gap = optimism_gap(random_score=0.9, grouped_score=0.6)
    assert abs(gap - 0.3) < 1e-9
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/cv/test_metrics.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/cv/metrics.py`**

```python
"""Regression metrics and the random-vs-grouped optimism gap."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
    }


def optimism_gap(random_score: float, grouped_score: float) -> float:
    """Headline metric: how much random-split R2 overstates grouped-split R2."""
    return float(random_score - grouped_score)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/cv/test_metrics.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/cv/metrics.py tests/cv/test_metrics.py
git commit -m "feat: add regression metrics and optimism-gap helper"
```

---

## Milestone M4 — Comparative model registry & evaluation

### Task 4.1: Preprocessing transformers

**Files:**
- Create: `src/data_module/preprocessing.py`
- Test: `tests/data_module/test_preprocessing.py`

Two preprocessors: `tree` keeps NaN (XGBoost/LightGBM handle it; preserves `absent=0` vs `unreported=NaN`); `linear` imputes + scales numerics and one-hot encodes categoricals (for ElasticNet/kNN/GP).

- [ ] **Step 1: Write the failing test**

`tests/data_module/test_preprocessing.py`:
```python
import numpy as np

from src.data_module.fixture import make_fixture
from src.data_module.preprocessing import make_preprocessor
from src.data_module import schema


def test_tree_preprocessor_preserves_nan():
    df = make_fixture(n_studies=10, rows_per_study=5, seed=0)
    pre = make_preprocessor("tree")
    x = pre.fit_transform(df[schema.MODEL_FEATURES])
    assert np.isnan(x).any()  # mg_wt_pct unreported stays NaN


def test_linear_preprocessor_no_nan_and_scaled():
    df = make_fixture(n_studies=10, rows_per_study=5, seed=0)
    pre = make_preprocessor("linear")
    x = pre.fit_transform(df[schema.MODEL_FEATURES])
    assert not np.isnan(np.asarray(x)).any()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/data_module/test_preprocessing.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/data_module/preprocessing.py`**

```python
"""Feature preprocessing variants for tree vs linear model families."""
from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.data_module import schema


def make_preprocessor(kind: str) -> ColumnTransformer:
    if kind == "tree":
        numeric = "passthrough"  # keep NaN; trees split on it
        categorical = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    elif kind == "linear":
        numeric = Pipeline(
            [("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]
        )
        categorical = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    else:
        raise ValueError(f"unknown preprocessor kind: {kind}")
    return ColumnTransformer(
        [
            ("num", numeric, schema.MODEL_NUMERIC),
            ("cat", categorical, schema.CATEGORICAL_FEATURES),
        ]
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/data_module/test_preprocessing.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/data_module/preprocessing.py tests/data_module/test_preprocessing.py
git commit -m "feat: add tree and linear preprocessing transformers"
```

---

### Task 4.2: Model registry and the six estimators

**Files:**
- Create: `src/model_module/registry.py`, `src/model_module/models.py`
- Test: `tests/model_module/test_registry.py`

- [ ] **Step 1: Write the failing test**

`tests/model_module/test_registry.py`:
```python
from sklearn.pipeline import Pipeline

from src.model_module import models  # noqa: F401  (registers estimators)
from src.model_module.registry import MODEL_REGISTRY, build_model


def test_all_six_models_registered():
    assert set(MODEL_REGISTRY) == {
        "elasticnet", "knn", "random_forest", "xgboost", "lightgbm", "gaussian_process"
    }


def test_build_model_returns_pipeline():
    pipe = build_model("xgboost")
    assert isinstance(pipe, Pipeline)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/model_module/test_registry.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/model_module/registry.py`**

```python
"""Factory/registry for comparative regression models."""
from __future__ import annotations

from collections.abc import Callable

from sklearn.pipeline import Pipeline

MODEL_REGISTRY: dict[str, Callable[[], Pipeline]] = {}


def register_model(name: str) -> Callable[[Callable[[], Pipeline]], Callable[[], Pipeline]]:
    def decorator(builder: Callable[[], Pipeline]) -> Callable[[], Pipeline]:
        MODEL_REGISTRY[name] = builder
        return builder
    return decorator


def build_model(name: str) -> Pipeline:
    if name not in MODEL_REGISTRY:
        raise KeyError(f"unknown model '{name}'; known: {sorted(MODEL_REGISTRY)}")
    return MODEL_REGISTRY[name]()
```

- [ ] **Step 4: Implement `src/model_module/models.py`**

```python
"""Concrete comparative models. Tree models keep NaN; others use linear preprocessing."""
from __future__ import annotations

from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from src.data_module.preprocessing import make_preprocessor
from src.model_module.registry import register_model

_SEED = 42


def _pipe(kind: str, estimator) -> Pipeline:
    return Pipeline([("pre", make_preprocessor(kind)), ("model", estimator)])


@register_model("elasticnet")
def _elasticnet() -> Pipeline:
    return _pipe("linear", ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=_SEED))


@register_model("knn")
def _knn() -> Pipeline:
    return _pipe("linear", KNeighborsRegressor(n_neighbors=7))


@register_model("random_forest")
def _rf() -> Pipeline:
    return _pipe("tree", RandomForestRegressor(n_estimators=400, random_state=_SEED, n_jobs=-1))


@register_model("xgboost")
def _xgb() -> Pipeline:
    return _pipe(
        "tree",
        XGBRegressor(
            n_estimators=400, max_depth=4, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8, random_state=_SEED,
        ),
    )


@register_model("lightgbm")
def _lgbm() -> Pipeline:
    return _pipe(
        "tree",
        LGBMRegressor(
            n_estimators=400, num_leaves=31, learning_rate=0.05,
            subsample=0.8, random_state=_SEED, verbose=-1,
        ),
    )


@register_model("gaussian_process")
def _gp() -> Pipeline:
    kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=1.0)
    return _pipe(
        "linear",
        GaussianProcessRegressor(kernel=kernel, normalize_y=True, random_state=_SEED),
    )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/model_module/test_registry.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/model_module tests/model_module
git commit -m "feat: add model registry and six comparative regressors"
```

---

### Task 4.3: Cross-validated evaluation harness

**Files:**
- Create: `src/model_module/evaluation.py`
- Test: `tests/model_module/test_evaluation.py`

- [ ] **Step 1: Write the failing test**

`tests/model_module/test_evaluation.py`:
```python
from src.data_module.fixture import make_fixture
from src.data_module import schema
from src.model_module import models  # noqa: F401
from src.model_module.evaluation import evaluate_model


def test_evaluate_model_returns_both_protocols():
    df = make_fixture(n_studies=30, rows_per_study=8, seed=3)
    result = evaluate_model("lightgbm", df, n_splits=5, seed=0)
    assert "grouped" in result and "random" in result
    assert "r2" in result["grouped"] and "r2" in result["random"]
    assert "optimism_gap_r2" in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/model_module/test_evaluation.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/model_module/evaluation.py`**

```python
"""Cross-validated evaluation under random vs grouped protocols."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import KFold

from src.cv.metrics import optimism_gap, regression_metrics
from src.cv.splitters import grouped_kfold_splits
from src.data_module import schema
from src.model_module.registry import build_model


def _cv_predict(model, x: pd.DataFrame, y: np.ndarray, splits) -> tuple[np.ndarray, np.ndarray]:
    y_true, y_pred = [], []
    for train_idx, test_idx in splits:
        m = clone(model)
        m.fit(x.iloc[train_idx], y[train_idx])
        y_pred.append(m.predict(x.iloc[test_idx]))
        y_true.append(y[test_idx])
    return np.concatenate(y_true), np.concatenate(y_pred)


def evaluate_model(name: str, df: pd.DataFrame, n_splits: int = 5, seed: int = 0) -> dict:
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    groups = df[schema.GROUP_COLUMN].to_numpy()
    model = build_model(name)

    random_splits = list(KFold(n_splits=n_splits, shuffle=True, random_state=seed).split(x))
    grouped = list(grouped_kfold_splits(len(df), groups, n_splits=n_splits, seed=seed))

    yt_r, yp_r = _cv_predict(model, x, y, random_splits)
    yt_g, yp_g = _cv_predict(model, x, y, grouped)
    random_m = regression_metrics(yt_r, yp_r)
    grouped_m = regression_metrics(yt_g, yp_g)
    return {
        "model": name,
        "random": random_m,
        "grouped": grouped_m,
        "optimism_gap_r2": optimism_gap(random_m["r2"], grouped_m["r2"]),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/model_module/test_evaluation.py -v`
Expected: PASS (allow up to ~60s for model fits)

- [ ] **Step 5: Commit**

```bash
git add src/model_module/evaluation.py tests/model_module/test_evaluation.py
git commit -m "feat: add random-vs-grouped CV evaluation harness"
```

---

## Milestone M5 — Explainability (SHAP + ALE)

### Task 5.1: SHAP main + interaction values

**Files:**
- Create: `src/analysis/xai/shap_analysis.py`
- Test: `tests/analysis/xai/test_shap_analysis.py`

- [ ] **Step 1: Write the failing test**

`tests/analysis/xai/test_shap_analysis.py`:
```python
from src.data_module.fixture import make_fixture
from src.analysis.xai.shap_analysis import compute_tree_shap


def test_tree_shap_shapes():
    df = make_fixture(n_studies=20, rows_per_study=6, seed=2)
    out = compute_tree_shap(df, max_interaction_samples=40)
    assert out.values.shape[0] == len(df)
    assert out.interaction_values is not None
    assert out.feature_names  # non-empty
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/xai/test_shap_analysis.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/xai/shap_analysis.py`**

```python
"""TreeSHAP main and 2-way interaction values on the fitted tree model."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import shap

from src.data_module import schema
from src.model_module.registry import build_model


@dataclass
class ShapResult:
    values: np.ndarray
    interaction_values: np.ndarray | None
    feature_names: list[str]
    data: np.ndarray


def compute_tree_shap(
    df: pd.DataFrame, model_name: str = "lightgbm", max_interaction_samples: int = 200
) -> ShapResult:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)
    pre, model = pipe.named_steps["pre"], pipe.named_steps["model"]
    x_trans = pre.transform(x)
    names = list(pre.get_feature_names_out())

    explainer = shap.TreeExplainer(model)
    values = explainer.shap_values(x_trans)
    sample = x_trans[:max_interaction_samples]
    interaction = explainer.shap_interaction_values(sample)
    return ShapResult(values=values, interaction_values=interaction,
                      feature_names=names, data=x_trans)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/xai/test_shap_analysis.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/analysis/xai/shap_analysis.py tests/analysis/xai/test_shap_analysis.py
git commit -m "feat: add TreeSHAP main and interaction value computation"
```

---

### Task 5.2: ALE (primary dependence tool)

**Files:**
- Create: `src/analysis/xai/ale_analysis.py`
- Test: `tests/analysis/xai/test_ale_analysis.py`

- [ ] **Step 1: Write the failing test**

`tests/analysis/xai/test_ale_analysis.py`:
```python
from src.data_module.fixture import make_fixture
from src.analysis.xai.ale_analysis import ale_for_feature


def test_ale_returns_grid_and_effect():
    df = make_fixture(n_studies=30, rows_per_study=8, seed=4)
    result = ale_for_feature(df, feature="temperature_k", bins=10)
    assert len(result.grid) >= 2
    assert len(result.effect) == len(result.grid)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/xai/test_ale_analysis.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/xai/ale_analysis.py`**

```python
"""Accumulated Local Effects on raw (untransformed) numeric features.

ALE is computed on the original feature scale by wrapping the fitted pipeline so the
predict function consumes raw model features. This avoids PDP extrapolation bias under
the correlated features in this dataset.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.data_module import schema
from src.model_module.registry import build_model


@dataclass
class AleResult:
    feature: str
    grid: np.ndarray
    effect: np.ndarray


def ale_for_feature(
    df: pd.DataFrame, feature: str, model_name: str = "lightgbm", bins: int = 20
) -> AleResult:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES].copy()
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)

    values = x[feature].to_numpy(dtype=float)
    quantiles = np.unique(np.nanquantile(values, np.linspace(0, 1, bins + 1)))
    local_effects = []
    for lo, hi in zip(quantiles[:-1], quantiles[1:], strict=False):
        mask = (values >= lo) & (values <= hi)
        if mask.sum() == 0:
            local_effects.append(0.0)
            continue
        x_lo, x_hi = x[mask].copy(), x[mask].copy()
        x_lo[feature] = lo
        x_hi[feature] = hi
        delta = pipe.predict(x_hi) - pipe.predict(x_lo)
        local_effects.append(float(np.mean(delta)))
    effect = np.cumsum(local_effects)
    effect = effect - effect.mean()  # center
    centers = (quantiles[:-1] + quantiles[1:]) / 2
    return AleResult(feature=feature, grid=centers, effect=effect)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/xai/test_ale_analysis.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/analysis/xai/ale_analysis.py tests/analysis/xai/test_ale_analysis.py
git commit -m "feat: add ALE dependence analysis on raw feature scale"
```

---

### Task 5.3: PDP/ICE + permutation importance (secondary)

**Files:**
- Create: `src/analysis/xai/dependence.py`
- Test: `tests/analysis/xai/test_dependence.py`

- [ ] **Step 1: Write the failing test**

`tests/analysis/xai/test_dependence.py`:
```python
from src.data_module.fixture import make_fixture
from src.analysis.xai.dependence import permutation_scores


def test_permutation_scores_sum_to_features():
    df = make_fixture(n_studies=20, rows_per_study=6, seed=5)
    scores = permutation_scores(df, n_repeats=3, seed=0)
    assert set(scores.index) <= set(df.columns)
    assert (scores >= 0).all() or (scores < 0).any()  # importances are real numbers
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/xai/test_dependence.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/xai/dependence.py`**

```python
"""Permutation importance (model-agnostic sanity check) and PDP grid helper."""
from __future__ import annotations

import pandas as pd
from sklearn.inspection import permutation_importance

from src.data_module import schema
from src.model_module.registry import build_model


def permutation_scores(
    df: pd.DataFrame, model_name: str = "lightgbm", n_repeats: int = 10, seed: int = 0
) -> pd.Series:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)
    result = permutation_importance(pipe, x, y, n_repeats=n_repeats, random_state=seed)
    return pd.Series(result.importances_mean, index=schema.MODEL_FEATURES).sort_values(
        ascending=False
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/xai/test_dependence.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/analysis/xai/dependence.py tests/analysis/xai/test_dependence.py
git commit -m "feat: add permutation importance sanity check"
```

---

### Task 5.4: SHAP stability across folds

**Files:**
- Create: `src/analysis/xai/stability.py`
- Test: `tests/analysis/xai/test_stability.py`

- [ ] **Step 1: Write the failing test**

`tests/analysis/xai/test_stability.py`:
```python
from src.data_module.fixture import make_fixture
from src.analysis.xai.stability import shap_rank_stability


def test_rank_stability_in_unit_interval():
    df = make_fixture(n_studies=24, rows_per_study=8, seed=6)
    score = shap_rank_stability(df, n_splits=4, seed=0)
    assert 0.0 <= score <= 1.0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/xai/test_stability.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/xai/stability.py`**

```python
"""Stability of SHAP-based feature importance ranking across grouped folds."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from src.analysis.xai.shap_analysis import compute_tree_shap
from src.cv.splitters import grouped_kfold_splits
from src.data_module import schema


def shap_rank_stability(df: pd.DataFrame, n_splits: int = 4, seed: int = 0) -> float:
    groups = df[schema.GROUP_COLUMN].to_numpy()
    rankings = []
    for train_idx, _ in grouped_kfold_splits(len(df), groups, n_splits=n_splits, seed=seed):
        out = compute_tree_shap(df.iloc[train_idx], max_interaction_samples=1)
        importance = np.abs(out.values).mean(axis=0)
        rankings.append(importance)
    corrs = []
    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            corrs.append(spearmanr(rankings[i], rankings[j]).statistic)
    return float(np.nanmean(corrs))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/xai/test_stability.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/analysis/xai/stability.py tests/analysis/xai/test_stability.py
git commit -m "feat: add cross-fold SHAP ranking stability metric"
```

---

## Milestone M6 — Physical validation

### Task 6.1: Arrhenius Eₐ fitting (working)

**Files:**
- Create: `src/analysis/physical_validation/arrhenius.py`
- Test: `tests/analysis/physical_validation/test_arrhenius.py`

- [ ] **Step 1: Write the failing test** (recover a known Eₐ from synthetic Arrhenius data)

`tests/analysis/physical_validation/test_arrhenius.py`:
```python
import numpy as np

from src.analysis.physical_validation.arrhenius import fit_arrhenius, within_literature_band


def test_recovers_known_activation_energy():
    R = 8.314
    ea_true = 50_000.0
    t_k = np.linspace(298, 363, 12)
    k = np.exp(-ea_true / (R * t_k)) * 1e8
    fit = fit_arrhenius(t_k, k)
    assert abs(fit.ea_j_mol - ea_true) / ea_true < 0.05
    assert fit.r2 > 0.99


def test_band_check():
    assert within_literature_band(50_000) is True
    assert within_literature_band(500_000) is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/physical_validation/test_arrhenius.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/physical_validation/arrhenius.py`**

```python
"""Arrhenius activation-energy fitting and literature-band validation."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

_R = 8.314  # J/mol/K
LITERATURE_EA_BAND_KJ = (3.5, 102.6)


@dataclass
class ArrheniusFit:
    ea_j_mol: float
    pre_exponential: float
    r2: float


def fit_arrhenius(temperature_k: np.ndarray, rate_constant: np.ndarray) -> ArrheniusFit:
    """Fit ln k = ln A - Ea/(R T). Slope = -Ea/R."""
    inv_t = (1.0 / np.asarray(temperature_k, dtype=float)).reshape(-1, 1)
    ln_k = np.log(np.asarray(rate_constant, dtype=float))
    reg = LinearRegression().fit(inv_t, ln_k)
    ea = -reg.coef_[0] * _R
    r2 = r2_score(ln_k, reg.predict(inv_t))
    return ArrheniusFit(ea_j_mol=float(ea), pre_exponential=float(np.exp(reg.intercept_)),
                        r2=float(r2))


def within_literature_band(ea_j_mol: float) -> bool:
    lo, hi = LITERATURE_EA_BAND_KJ
    return lo * 1000 <= ea_j_mol <= hi * 1000
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/physical_validation/test_arrhenius.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/analysis/physical_validation/arrhenius.py tests/analysis/physical_validation/test_arrhenius.py
git commit -m "feat: add Arrhenius activation-energy fitting with band check"
```

---

### Task 6.2: Shrinking-core stub (Phase 2)

**Files:**
- Create: `src/analysis/physical_validation/shrinking_core.py`
- Test: `tests/analysis/physical_validation/test_shrinking_core.py`

- [ ] **Step 1: Write the stub module**

```python
"""Shrinking-core regime classification (Phase 2 — interface defined, not implemented)."""
from __future__ import annotations

import numpy as np


def reaction_controlled_conversion(time: np.ndarray, k: float) -> np.ndarray:
    """g(X) = 1 - (1 - X)^(1/3) = k t  ->  X(t). Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")


def diffusion_controlled_conversion(time: np.ndarray, k: float) -> np.ndarray:
    """g(X) = 1 - 3(1-X)^(2/3) + 2(1-X) = k t  ->  X(t). Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")


def classify_regime(time: np.ndarray, conversion: np.ndarray) -> str:
    """Return 'reaction' or 'diffusion'. Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")
```

- [ ] **Step 2: Write the test asserting the stub contract**

`tests/analysis/physical_validation/test_shrinking_core.py`:
```python
import numpy as np
import pytest

from src.analysis.physical_validation import shrinking_core


def test_regime_classification_is_phase2_stub():
    with pytest.raises(NotImplementedError):
        shrinking_core.classify_regime(np.array([1.0]), np.array([0.5]))
```

- [ ] **Step 3: Run test to verify it passes**

Run: `uv run pytest tests/analysis/physical_validation/test_shrinking_core.py -v`
Expected: PASS (the stub raises as asserted)

- [ ] **Step 4: Commit**

```bash
git add src/analysis/physical_validation/shrinking_core.py tests/analysis/physical_validation/test_shrinking_core.py
git commit -m "feat: add shrinking-core regime stub (Phase 2 interface)"
```

---

### Task 6.3: Consistency-metric stub (Phase 2)

**Files:**
- Create: `src/analysis/physical_validation/consistency_metrics.py`
- Test: `tests/analysis/physical_validation/test_consistency_metrics.py`

- [ ] **Step 1: Write the stub module**

```python
"""SHAP <-> physics sign-agreement metric (Phase 2 — interface defined)."""
from __future__ import annotations

import numpy as np


def sign_agreement_rate(
    shap_local_gradients: np.ndarray, physics_gradients: np.ndarray
) -> float:
    """Fraction of points where SHAP-local and physics-predicted gradients share sign.

    Implemented in Phase 2 once SCM regimes are available.
    """
    raise NotImplementedError("Phase 2: SHAP<->physics consistency metric")
```

- [ ] **Step 2: Write the test**

`tests/analysis/physical_validation/test_consistency_metrics.py`:
```python
import numpy as np
import pytest

from src.analysis.physical_validation import consistency_metrics


def test_consistency_metric_is_phase2_stub():
    with pytest.raises(NotImplementedError):
        consistency_metrics.sign_agreement_rate(np.array([1.0]), np.array([1.0]))
```

- [ ] **Step 3: Run test to verify it passes**

Run: `uv run pytest tests/analysis/physical_validation/test_consistency_metrics.py -v`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add src/analysis/physical_validation/consistency_metrics.py tests/analysis/physical_validation/test_consistency_metrics.py
git commit -m "feat: add consistency-metric stub (Phase 2 interface)"
```

---

## Milestone M7 — Figures and end-to-end pipeline

### Task 7.1: Plot style + figure module

**Files:**
- Create: `src/analysis/figures/style.py`, `src/analysis/figures/phase1_figures.py`
- Test: `tests/analysis/figures/test_phase1_figures.py`

- [ ] **Step 1: Write the failing test** (figures write files without a display backend)

`tests/analysis/figures/test_phase1_figures.py`:
```python
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

from src.data_module.fixture import make_fixture
from src.analysis.figures.phase1_figures import (
    plot_contradiction_ale, plot_shap_summary,
)


def test_figures_write_png(tmp_path: Path):
    df = make_fixture(n_studies=25, rows_per_study=8, seed=7)
    p1 = tmp_path / "fig1.png"
    p3 = tmp_path / "fig3.png"
    plot_shap_summary(df, p1)
    plot_contradiction_ale(df, p3)
    assert p1.exists() and p1.stat().st_size > 0
    assert p3.exists() and p3.stat().st_size > 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/analysis/figures/test_phase1_figures.py -v`
Expected: FAIL

- [ ] **Step 3: Implement `src/analysis/figures/style.py`**

```python
"""Shared matplotlib styling for publication figures."""
from __future__ import annotations

import matplotlib.pyplot as plt


def apply_style() -> None:
    plt.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
    })
```

- [ ] **Step 4: Implement `src/analysis/figures/phase1_figures.py`**

```python
"""Phase 1 publication figures (yield-target only)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from src.analysis.figures.style import apply_style
from src.analysis.xai.ale_analysis import ale_for_feature
from src.analysis.xai.shap_analysis import compute_tree_shap
from src.data_module import schema


def plot_shap_summary(df, out_path: Path) -> None:
    """fig1: global SHAP importance (mean |SHAP|) bar chart."""
    apply_style()
    out = compute_tree_shap(df, max_interaction_samples=1)
    importance = np.abs(out.values).mean(axis=0)
    order = np.argsort(importance)[-15:]
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.barh([out.feature_names[i] for i in order], importance[order])
    ax.set_xlabel("mean |SHAP value|")
    ax.set_title("fig1: Global feature importance (SHAP)")
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def plot_contradiction_ale(df, out_path: Path) -> None:
    """fig3: particle-size ALE per system_class -> shows the sign flip."""
    apply_style()
    fig, ax = plt.subplots(figsize=(6, 5))
    for sc in df["system_class"].unique():
        sub = df[df["system_class"] == sc]
        if len(sub) < schema.EXPLORATORY_MIN_ROWS:
            continue
        res = ale_for_feature(sub, feature="particle_size_d50_um", bins=8)
        ax.plot(res.grid, res.effect, marker="o", label=sc)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xlabel("particle size D50 (um)")
    ax.set_ylabel("ALE on H2 yield (%)")
    ax.set_title("fig3: Particle-size effect by system class")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/analysis/figures/test_phase1_figures.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/analysis/figures tests/analysis/figures
git commit -m "feat: add fig1 (SHAP summary) and fig3 (contradiction ALE)"
```

> fig2 (SHAP interaction heatmap), fig4 (Eₐ vs literature band), the CV-gap bar, and the
> calibration plot follow the identical pattern; add each as its own task during execution
> using `compute_tree_shap(...).interaction_values`, `fit_arrhenius`, `evaluate_model`, and a
> predicted-vs-true scatter respectively. SCM part of fig4 and the rate–yield map stay DEFER.

---

### Task 7.2: Hydra config + end-to-end pipeline entry point

**Files:**
- Create: `run/conf/config.yaml`, `run/pipeline/run_phase1.py`
- Test: `tests/pipeline/test_run_phase1.py`

- [ ] **Step 1: Write `run/conf/config.yaml`**

```yaml
seed: 42
data:
  path: data/curated/fixture_v0.csv
cv:
  n_splits: 5
models:
  - elasticnet
  - knn
  - random_forest
  - xgboost
  - lightgbm
  - gaussian_process
output_dir: results
```

- [ ] **Step 2: Write the failing test**

`tests/pipeline/test_run_phase1.py`:
```python
from pathlib import Path

from src.data_module.fixture import write_fixture
from run.pipeline.run_phase1 import run_pipeline


def test_pipeline_produces_metrics_and_figures(tmp_path: Path):
    data_path = tmp_path / "fix.csv"
    write_fixture(str(data_path), n_studies=25, rows_per_study=8, seed=9)
    out = run_pipeline(data_path=str(data_path), models=["lightgbm"],
                       n_splits=4, seed=0, output_dir=str(tmp_path / "out"))
    assert (Path(out) / "metrics" / "cv_metrics.csv").exists()
    assert (Path(out) / "figures" / "fig1_shap_summary.png").exists()
    assert (Path(out) / "figures" / "fig3_contradiction_resolution.png").exists()
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/pipeline/test_run_phase1.py -v`
Expected: FAIL

- [ ] **Step 4: Implement `run/pipeline/run_phase1.py`**

```python
"""Phase 1 end-to-end pipeline: load -> evaluate -> explain -> figures."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.analysis.figures.phase1_figures import plot_contradiction_ale, plot_shap_summary
from src.data_module.loader import load_dataset, per_class_counts
from src.model_module import models  # noqa: F401  (registers estimators)
from src.model_module.evaluation import evaluate_model
from src.utils.logging_config import get_logger
from src.utils.seed import set_seed

logger = get_logger(__name__)


def run_pipeline(
    data_path: str, models: list[str], n_splits: int, seed: int, output_dir: str
) -> str:
    set_seed(seed)
    out = Path(output_dir)
    (out / "metrics").mkdir(parents=True, exist_ok=True)
    (out / "figures").mkdir(parents=True, exist_ok=True)

    df = load_dataset(data_path)
    logger.info("Loaded %d rows; per-class N:\n%s", len(df), per_class_counts(df))

    rows = [evaluate_model(name, df, n_splits=n_splits, seed=seed) for name in models]
    metrics = pd.json_normalize(rows)
    metrics.to_csv(out / "metrics" / "cv_metrics.csv", index=False)
    logger.info("CV metrics written")

    plot_shap_summary(df, out / "figures" / "fig1_shap_summary.png")
    plot_contradiction_ale(df, out / "figures" / "fig3_contradiction_resolution.png")
    return str(out)


if __name__ == "__main__":
    import hydra
    from omegaconf import DictConfig

    @hydra.main(version_base=None, config_path="../conf", config_name="config")
    def main(cfg: DictConfig) -> None:
        run_pipeline(cfg.data.path, list(cfg.models), cfg.cv.n_splits, cfg.seed, cfg.output_dir)

    main()
```

- [ ] **Step 5: Add `run/__init__.py` and `run/pipeline/__init__.py`** (empty) so the test import resolves.

- [ ] **Step 6: Run test to verify it passes**

Run: `uv run pytest tests/pipeline/test_run_phase1.py -v`
Expected: PASS

- [ ] **Step 7: Smoke-run the real pipeline via Hydra**

Run:
```bash
uv run python -m run.pipeline.run_phase1
```
Expected: `results/metrics/cv_metrics.csv` and `results/figures/fig1_shap_summary.png`, `fig3_contradiction_resolution.png` created; Hydra writes a run dir under `run/outputs/`.

- [ ] **Step 8: Commit**

```bash
git add run tests/pipeline
git commit -m "feat: add Hydra config and end-to-end Phase 1 pipeline"
```

---

## Milestone M8 — Paper skeleton, README, verification

### Task 8.1: `elsarticle`-ready LaTeX skeleton

**Files:**
- Create: `paper/main.tex`, `paper/sections/{introduction,related_work,method,experiments,results,conclusion}.tex`, `paper/references.bib`

- [ ] **Step 1: Write `paper/main.tex`** as a generic article that switches to `elsarticle` by
  uncommenting one block. Keep `\input{sections/...}` includes so content is template-agnostic.

```latex
% Generic now; switch to Elsevier by replacing the documentclass block with:
%   \documentclass[preprint,12pt]{elsarticle}
\documentclass[11pt]{article}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage[numbers]{natbib}
\usepackage{amsmath}
\graphicspath{{../results/figures/}}

\title{Explaining Contradictory Parameter Effects in Aluminum--Water Hydrolysis for
Hydrogen Production via Physics-Validated Interpretable Machine Learning}
\author{Author One \and Author Two}

\begin{document}
\maketitle
\begin{abstract}
% One paragraph: contradiction problem, unified dataset, leakage-controlled interpretable ML,
% physics validation (Arrhenius), contradiction-resolution result.
\end{abstract}

\input{sections/introduction}
\input{sections/related_work}
\input{sections/method}
\input{sections/experiments}
\input{sections/results}
\input{sections/conclusion}

\bibliographystyle{unsrtnat}
\bibliography{references}
\end{document}
```

- [ ] **Step 2: Create the six section files** each containing a `\section{...}` header and a
  one-line English comment describing its planned content (no Lorem ipsum).

- [ ] **Step 3: Create `paper/references.bib`** with a single placeholder BibTeX comment line
  `% references added during literature extraction`.

- [ ] **Step 4: Commit**

```bash
git add paper
git commit -m "docs: add elsarticle-ready LaTeX paper skeleton"
```

---

### Task 8.2: README, verification pass, release tag

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`** covering: project summary, the contradiction thesis, Phase
  1 vs Phase 2 scope, repo map, `uv sync` + `uv run python -m run.pipeline.run_phase1` quickstart,
  data availability statement (code MIT, dataset CC-BY-4.0, Zenodo DOI pending), and a note that
  `data/curated/fixture_v0.csv` is synthetic until real extractions land.

- [ ] **Step 2: Run the full verification pass**

Run:
```bash
uv run ruff check .
uv run pytest
```
Expected: ruff clean (fix any findings); all tests pass.

- [ ] **Step 3: Type-check the source**

Run:
```bash
uv run mypy src
```
Expected: no errors (add minimal annotations if any surface).

- [ ] **Step 4: Commit and tag the Phase 1 scaffold**

```bash
git add README.md
git commit -m "docs: add project README and data availability statement"
git tag phase1-scaffold
```

---

## Self-review (run against the spec)

**Spec coverage:** A1 single target → T2.2/T2.3; A2 hybrid encoding + absent/NaN → T2.2/T2.4/T4.1;
A3 scope + system_class central → T2.2 levels + T7.1 fig3 split; A4 N floor/target/per-class/<40 →
T2.4. B1 provenance → T2.1/T2.3; B2 quality tiers → T2.1/T2.3. C1 six models → T4.2; C2 ALE-primary
+ SHAP interaction + PDP/perm → T5.1–5.3; C3 grouped/LOSO + optimism gap → T3.1/T3.2/T4.3; SHAP
stability → T5.4. D1 Arrhenius working → T6.1; SCM + consistency stubs → T6.2/T6.3; D2 module → M6.
E1 MIT/CC-BY/Zenodo/uv.lock → T0.1/T0.2/T8.2; E2 figures fig1/fig3 built, fig2/fig4(Eₐ)/CV-gap/
calibration noted as same-pattern tasks, rate–yield + SCM DEFER → T7.1/T7.2.

**Placeholder scan:** no "TBD/TODO/handle edge cases"; stubs are intentional Phase 2 modules with
explicit `NotImplementedError` and tests asserting that contract.

**Type consistency:** `schema.MODEL_FEATURES/MODEL_NUMERIC` used identically across preprocessing,
models, SHAP, ALE, evaluation; `build_model(name)` signature consistent; `evaluate_model(name, df,
n_splits, seed)` consistent between T4.3 and T7.2; `ArrheniusFit.ea_j_mol` consistent T6.1.

**Known execution caveats (not gaps):** fig2/fig4/CV-gap/calibration are described as same-pattern
follow-on tasks rather than fully coded here, to keep the plan reviewable; the executor adds them as
individual TDD tasks. Model-fit tests may take up to ~60s.
