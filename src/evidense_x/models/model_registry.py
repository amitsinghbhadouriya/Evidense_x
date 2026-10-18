"""Factory registry for instantiating model adapters by canonical name."""
from typing import Dict, Type, Any
from .model_protocol import TabularModelWrapper
from .rf_adapter import RandomForestAdapter
from .gradient_boosting_adapter import HistGradientBoostingAdapter
from .logistic_adapter import LogisticRegressionAdapter
from .mlp_adapter import MLPAdapter

MODEL_FACTORY: Dict[str, Type[TabularModelWrapper]] = {
    "rf": RandomForestAdapter,
    "random_forest": RandomForestAdapter,
    "hgb": HistGradientBoostingAdapter,
    "gradient_boosting": HistGradientBoostingAdapter,
    "lr": LogisticRegressionAdapter,
    "logistic_regression": LogisticRegressionAdapter,
    "mlp": MLPAdapter,
}

def create_model(name: str, **kwargs: Any) -> TabularModelWrapper:
    """Factory helper to instantiate a model adapter by key."""
    if name.lower() not in MODEL_FACTORY:
        raise KeyError(f"Unknown model adapter '{name}'. Choose from: {list(MODEL_FACTORY.keys())}")
    return MODEL_FACTORY[name.lower()](**kwargs)
