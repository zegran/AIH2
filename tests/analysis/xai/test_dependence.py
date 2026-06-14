from src.analysis.xai.dependence import permutation_scores
from src.data_module.fixture import make_fixture


def test_permutation_scores_cover_model_features():
    df = make_fixture(n_studies=20, rows_per_study=6, seed=5)
    scores = permutation_scores(df, n_repeats=3, seed=0)
    assert len(scores) > 0
    assert set(scores.index) <= set(df.columns)
