"""Soft-voting probability ensemble with configurable model weights."""
import numpy as np
from typing import List, Optional, Any
from .base_ensemble import BaseEnsembleCombiner

class SoftVotingEnsemble(BaseEnsembleCombiner):
    """Computes weighted average of predicted probability distributions."""
    
    def __init__(self, weights: Optional[List[float]] = None) -> None:
        self.weights = weights
        self.models: List[Any] = []
        
    def fit(self, base_models: List[Any], X: np.ndarray, y: np.ndarray) -> "SoftVotingEnsemble":
        self.models = base_models
        for m in self.models:
            m.fit(X, y)
        if self.weights is None:
            self.weights = [1.0 / len(self.models)] * len(self.models)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        probs = [m.predict_proba(X) * w for m, w in zip(self.models, self.weights)]
        total = sum(probs) / sum(self.weights)
        return total
