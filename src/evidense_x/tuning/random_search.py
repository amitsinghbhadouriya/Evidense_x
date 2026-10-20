"""Randomized search optimizer evaluating model candidates across CV folds."""
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from typing import Dict, Any, List
from .base_optimizer import BaseHyperparameterOptimizer

class RandomizedCVOptimizer(BaseHyperparameterOptimizer):
    """Randomized search evaluating parameter configurations under stratified cross-validation."""
    
    def __init__(self, model_cls, n_iter: int = 10, random_state: int = 42) -> None:
        self.model_cls = model_cls
        self.n_iter = n_iter
        self.rng = np.random.default_rng(random_state)
        
    def optimize(self, X: pd.DataFrame, y: np.ndarray, param_space: Dict[str, List[Any]]) -> Dict[str, Any]:
        best_score = -1.0
        best_params = {}
        skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
        
        for _ in range(self.n_iter):
            sampled_params = {k: self.rng.choice(v) for k, v in param_space.items()}
            scores = []
            for tr, ts in skf.split(X, y):
                m = self.model_cls(**sampled_params)
                m.fit(X.iloc[tr].values, y[tr])
                pred = m.predict_proba(X.iloc[ts].values)[:, 1]
                scores.append(roc_auc_score(y[ts], pred))
            mean_score = float(np.mean(scores))
            if mean_score > best_score:
                best_score = mean_score
                best_params = sampled_params
                
        return {"best_params": best_params, "best_cv_auc": best_score}
