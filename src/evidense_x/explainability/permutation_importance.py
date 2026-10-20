"""Permutation feature importance evaluator measuring AUC degradation under column shuffling."""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from typing import Dict, Any
from .base_explainer import BaseFeatureExplainer

class PermutationFeatureExplainer(BaseFeatureExplainer):
    """Computes decrease in ROC-AUC when individual features are permuted."""
    
    def __init__(self, n_repeats: int = 5, random_state: int = 42) -> None:
        self.n_repeats = n_repeats
        self.rng = np.random.default_rng(random_state)
        
    def explain(self, model: Any, X: pd.DataFrame, y: np.ndarray) -> Dict[str, float]:
        baseline_pred = model.predict_proba(X.values)[:, 1]
        baseline_auc = roc_auc_score(y, baseline_pred)
        
        scores: Dict[str, float] = {}
        X_vals = X.values.copy()
        
        for c_idx, col in enumerate(X.columns):
            drop_sum = 0.0
            for _ in range(self.n_repeats):
                X_shuffled = X_vals.copy()
                X_shuffled[:, c_idx] = self.rng.permutation(X_shuffled[:, c_idx])
                pred = model.predict_proba(X_shuffled)[:, 1]
                drop_sum += max(0.0, baseline_auc - roc_auc_score(y, pred))
            scores[col] = float(drop_sum / self.n_repeats)
        return scores
