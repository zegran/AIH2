from src.analysis.xai.ale_analysis import ale_for_feature
from src.data_module.fixture import make_fixture


def test_ale_returns_grid_and_effect():
    df = make_fixture(n_studies=30, rows_per_study=8, seed=4)
    result = ale_for_feature(df, feature="temperature_k", bins=10)
    assert len(result.grid) >= 2
    assert len(result.effect) == len(result.grid)
