"""Factory/registry for comparative regression models."""
from __future__ import annotations

from collections.abc import Callable

from sklearn.pipeline import Pipeline

MODEL_REGISTRY: dict[str, Callable[[], Pipeline]] = {}


def register_model(name: str) -> Callable[[Callable[[], Pipeline]], Callable[[], Pipeline]]:
    def decorator(builder: Callable[[], Pipeline]) -> Callable[[], Pipeline]:
        MODEL_REGISTRY[name] = builder
        return builder
    return decorator


def build_model(name: str) -> Pipeline:
    if name not in MODEL_REGISTRY:
        raise KeyError(f"unknown model '{name}'; known: {sorted(MODEL_REGISTRY)}")
    return MODEL_REGISTRY[name]()
