"""Missingness indicator transformer augmenting feature matrix with explicit boolean null flags."""
import pandas as pd
from .base_transformer import BaseRobustTransformer

class MissingnessIndicatorAugmenter(BaseRobustTransformer):
    """Appends binary indicator columns representing missing value locations."""
    
    def __init__(self, prefix: str = "missing_") -> None:
        self.prefix = prefix
        self.cols_with_missing = []
        
    def fit(self, X: pd.DataFrame, y=None) -> "MissingnessIndicatorAugmenter":
        self.cols_with_missing = [c for c in X.columns if X[c].isna().any()]
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        for col in self.cols_with_missing:
            out[f"{self.prefix}{col}"] = out[col].isna().astype(int)
        return out
