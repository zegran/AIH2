from src.analysis.xai.shap_analysis import compute_tree_shap
from src.data_module.fixture import make_fixture


def test_tree_shap_shapes():
    df = make_fixture(n_studies=20, rows_per_study=6, seed=2)
    out = compute_tree_shap(df, max_interaction_samples=40)
    assert out.values.shape[0] == len(df)
    assert out.interaction_values is not None
    assert out.feature_names  # non-empty
