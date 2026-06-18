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
