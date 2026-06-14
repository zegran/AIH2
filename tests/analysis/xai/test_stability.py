from src.analysis.xai.stability import shap_rank_stability
from src.data_module.fixture import make_fixture


def test_rank_stability_in_unit_interval():
    df = make_fixture(n_studies=24, rows_per_study=8, seed=6)
    score = shap_rank_stability(df, n_splits=4, seed=0)
    assert -1.0 <= score <= 1.0
