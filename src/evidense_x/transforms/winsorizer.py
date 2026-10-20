"""Tukey IQR and percentile Winsorization transformer clipping extreme distribution tails."""
import pandas as pd
import numpy as np
from typing import Dict, Tuple
from .base_transformer import BaseRobustTransformer

class OutlierWinsorizer(BaseRobustTransformer):
    """Clips extreme outliers exceeding empirical IQR thresholds."""
    
    def __init__(self, factor: float = 1.5) -> None:
        self.factor = factor
        self.bounds: Dict[str, Tuple[float, float]] = {}
        
    def fit(self, X: pd.DataFrame, y=None) -> "OutlierWinsorizer":
        num_cols = list(X.select_dtypes(include=[np.number]).columns)
        for col in num_cols:
            q25 = X[col].quantile(0.25)
            q75 = X[col].quantile(0.75)
            iqr = q75 - q25
            lower = q25 - self.factor * iqr
            upper = q75 + self.factor * iqr
            self.bounds[col] = (float(lower), float(upper))
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        for col, (lower, upper) in self.bounds.items():
            if col in out.columns:
                out[col] = np.clip(out[col], lower, upper)
        return out
