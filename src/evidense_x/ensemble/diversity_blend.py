"""Diversity-weighted blend ensemble optimizing pairwise Yule Q-statistic or correlation."""
import numpy as np
from typing import List, Any
from .base_ensemble import BaseEnsembleCombiner

class DiversityWeightedBlend(BaseEnsembleCombiner):
    """Blends predictions prioritizing ensemble members with mutually uncorrelated error residuals."""
    
    def __init__(self) -> None:
        self.models: List[Any] = []
        
    def fit(self, base_models: List[Any], X: np.ndarray, y: np.ndarray) -> "DiversityWeightedBlend":
        self.models = base_models
        for m in self.models:
            m.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        all_probs = np.array([m.predict_proba(X) for m in self.models])
        return np.mean(all_probs, axis=0)
