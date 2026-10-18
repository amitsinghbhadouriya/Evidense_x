"""Model adapters and registry for Evidense-X benchmark framework."""
from .model_protocol import TabularModelWrapper
from .rf_adapter import RandomForestAdapter
from .gradient_boosting_adapter import HistGradientBoostingAdapter
from .logistic_adapter import LogisticRegressionAdapter
from .mlp_adapter import MLPAdapter
from .model_registry import create_model, MODEL_FACTORY

__all__ = [
    "TabularModelWrapper",
    "RandomForestAdapter",
    "HistGradientBoostingAdapter",
    "LogisticRegressionAdapter",
    "MLPAdapter",
    "create_model",
    "MODEL_FACTORY",
]
