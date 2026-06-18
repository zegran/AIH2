"""Phase 1 end-to-end pipeline: load -> evaluate -> XAI tables.

Figures are deferred to a later phase; this entry point produces numeric artifacts only
(CV metrics with the random-vs-grouped optimism gap, and permutation-importance ranking),
so the whole pipeline runs end-to-end on the synthetic fixture.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.analysis.xai.dependence import permutation_scores
from src.data_module.loader import load_dataset, per_class_counts
from src.model_module import models  # noqa: F401  (registers estimators)
from src.model_module.evaluation import evaluate_model
from src.utils.logging_config import get_logger
from src.utils.seed import set_seed

logger = get_logger(__name__)


def run_pipeline(
    data_path: str,
    model_names: list[str],
    n_splits: int,
    seed: int,
    output_dir: str,
    primary_model: str = "lightgbm",
) -> str:
    set_seed(seed)
    out = Path(output_dir)
    (out / "metrics").mkdir(parents=True, exist_ok=True)
    (out / "tables").mkdir(parents=True, exist_ok=True)

    df = load_dataset(data_path)
    logger.info("Loaded %d rows; per-class N:\n%s", len(df), per_class_counts(df).to_string())

    rows = [evaluate_model(name, df, n_splits=n_splits, seed=seed) for name in model_names]
    metrics = pd.json_normalize(rows)
    metrics.to_csv(out / "metrics" / "cv_metrics.csv", index=False)
    logger.info("CV metrics written to %s", out / "metrics" / "cv_metrics.csv")

    importance = permutation_scores(df, model_name=primary_model, n_repeats=10, seed=seed)
    importance.to_frame("permutation_importance").to_csv(
        out / "tables" / "permutation_importance.csv"
    )
    logger.info("Permutation importance written")
    return str(out)


if __name__ == "__main__":
    import hydra
    from omegaconf import DictConfig

    @hydra.main(version_base=None, config_path="../conf", config_name="config")
    def main(cfg: DictConfig) -> None:
        run_pipeline(
            cfg.data.path, list(cfg.models), cfg.cv.n_splits, cfg.seed,
            cfg.output_dir, cfg.primary_model,
        )

    main()
