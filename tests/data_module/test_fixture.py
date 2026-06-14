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
    assert df["max_rate_ml_min_g"].isna().all()


def test_fixture_temperature_increases_yield_on_average():
    df = make_fixture(n_studies=40, rows_per_study=10, seed=1)
    hot = df[df["temperature_k"] > df["temperature_k"].median()][schema.TARGET].mean()
    cold = df[df["temperature_k"] <= df["temperature_k"].median()][schema.TARGET].mean()
    assert hot > cold
