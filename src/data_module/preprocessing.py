"""Feature preprocessing variants for tree vs linear model families."""
from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.data_module import schema


def make_preprocessor(kind: str) -> ColumnTransformer:
    if kind == "tree":
        numeric = "passthrough"  # keep NaN; trees split on it (absent=0 vs unreported=NaN)
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
