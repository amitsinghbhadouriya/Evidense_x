"""Frequency category encoder mapping rare categorical values to common tail pool."""
import pandas as pd
from typing import Dict, Any
from .base_transformer import BaseRobustTransformer

class FrequencyCategoryEncoder(BaseRobustTransformer):
    """Replaces categorical labels with observed relative frequency in training partition."""
    
    def __init__(self, min_freq: float = 0.01) -> None:
        self.min_freq = min_freq
        self.freq_maps: Dict[str, Dict[Any, float]] = {}
        
    def fit(self, X: pd.DataFrame, y=None) -> "FrequencyCategoryEncoder":
        cat_cols = list(X.select_dtypes(include=["object", "category"]).columns)
        n = len(X)
        for col in cat_cols:
            freqs = (X[col].value_counts() / n).to_dict()
            self.freq_maps[col] = freqs
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        for col, fmap in self.freq_maps.items():
            if col in out.columns:
                out[col] = out[col].map(fmap).fillna(0.0)
        return out
