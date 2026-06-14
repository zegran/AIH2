import numpy as np

from src.data_module import schema
from src.data_module.fixture import make_fixture
from src.data_module.preprocessing import make_preprocessor


def test_tree_preprocessor_preserves_nan():
    df = make_fixture(n_studies=10, rows_per_study=5, seed=0)
    pre = make_preprocessor("tree")
    x = pre.fit_transform(df[schema.MODEL_FEATURES])
    assert np.isnan(np.asarray(x, dtype=float)).any()  # mg_wt_pct unreported stays NaN


def test_linear_preprocessor_no_nan_and_scaled():
    df = make_fixture(n_studies=10, rows_per_study=5, seed=0)
    pre = make_preprocessor("linear")
    x = pre.fit_transform(df[schema.MODEL_FEATURES])
    assert not np.isnan(np.asarray(x, dtype=float)).any()
