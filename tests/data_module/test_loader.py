import pandas as pd

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
