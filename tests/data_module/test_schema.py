from src.data_module import schema


def test_column_groups_are_disjoint_and_complete():
    feature_cols = set(
        schema.NUMERIC_FEATURES + schema.WT_PCT_COLUMNS + schema.CATEGORICAL_FEATURES
    )
    assert schema.TARGET not in feature_cols
    assert schema.GROUP_COLUMN not in feature_cols
    assert set(schema.WT_PCT_COLUMNS).isdisjoint(schema.NUMERIC_FEATURES)


def test_all_columns_listed():
    assert "system_class" in schema.CATEGORICAL_FEATURES
    assert schema.TARGET == "h2_yield_pct"
    assert schema.GROUP_COLUMN == "study_id"
