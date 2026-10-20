"""Empirical Bayes smoothed target encoder preventing categorical target leakage."""
import pandas as pd
import numpy as np
from typing import Dict, Any
from .base_transformer import BaseRobustTransformer

class RobustTargetEncoder(BaseRobustTransformer):
    """Smoothed target encoding using empirical Bayes shrinkage towards global prior."""
    
    def __init__(self, m_smoothing: float = 10.0) -> None:
        self.m = m_smoothing
        self.global_mean: float = 0.5
        self.mappings: Dict[str, Dict[Any, float]] = {}
        
    def fit(self, X: pd.DataFrame, y: np.ndarray) -> "RobustTargetEncoder":
        self.global_mean = float(np.mean(y))
        cat_cols = list(X.select_dtypes(include=["object", "category"]).columns)
        
        for col in cat_cols:
            counts = X.groupby(col).size()
            sums = pd.Series(y).groupby(X[col].values).sum()
            smoothed = (sums + self.m * self.global_mean) / (counts + self.m)
            self.mappings[col] = smoothed.to_dict()
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        for col, mapping in self.mappings.items():
            if col in out.columns:
                out[col] = out[col].map(mapping).fillna(self.global_mean)
        return out
