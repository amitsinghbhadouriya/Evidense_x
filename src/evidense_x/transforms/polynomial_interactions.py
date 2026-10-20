"""Sparse polynomial feature interaction generator filtering collinear cross-terms."""
import pandas as pd
import numpy as np
from .base_transformer import BaseRobustTransformer

class PolynomialInteractionGenerator(BaseRobustTransformer):
    """Generates pairwise multiplicative interaction terms for top numerical features."""
    
    def __init__(self, max_features: int = 5) -> None:
        self.max_features = max_features
        self.selected_cols = []
        
    def fit(self, X: pd.DataFrame, y=None) -> "PolynomialInteractionGenerator":
        num_cols = list(X.select_dtypes(include=[np.number]).columns)
        self.selected_cols = num_cols[:self.max_features]
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        n = len(self.selected_cols)
        for i in range(n):
            for j in range(i + 1, n):
                c1, c2 = self.selected_cols[i], self.selected_cols[j]
                out[f"{c1}_x_{c2}"] = out[c1] * out[c2]
        return out
