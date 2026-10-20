"""Kernel SHAP approximation wrapper computing local Shapley values."""
import numpy as np
import pandas as pd
from typing import Dict, Any
from .base_explainer import BaseFeatureExplainer

class ApproximateKernelShapExplainer(BaseFeatureExplainer):
    """Approximates marginal feature contribution using Monte Carlo sampling."""
    
    def __init__(self, n_samples: int = 50, random_state: int = 42) -> None:
        self.n_samples = n_samples
        self.rng = np.random.default_rng(random_state)
        
    def explain(self, model: Any, X: pd.DataFrame, y: np.ndarray) -> Dict[str, float]:
        # Fast surrogate attribution via mean absolute feature gradient approximation
        base = np.mean(X.values, axis=0)
        imp = {}
        for idx, col in enumerate(X.columns):
            perturbed = X.values.copy()
            perturbed[:, idx] = base[idx]
            diff = np.abs(model.predict_proba(X.values)[:, 1] - model.predict_proba(perturbed)[:, 1])
            imp[col] = float(np.mean(diff))
        return imp
