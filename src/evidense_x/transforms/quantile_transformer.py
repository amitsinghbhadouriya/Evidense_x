"""Quantile rank transformer mapping arbitrary distributions to uniform or Gaussian margins."""
import pandas as pd
import numpy as np
from sklearn.preprocessing import QuantileTransformer
from .base_transformer import BaseRobustTransformer

class RobustQuantileTransformer(BaseRobustTransformer):
    """Maps non-normal continuous feature distributions to normal margins."""
    
    def __init__(self, output_distribution: str = "normal", random_state: int = 42) -> None:
        self.output_distribution = output_distribution
        self.transformer = QuantileTransformer(output_distribution=output_distribution, random_state=random_state)
        self.num_cols = []
        
    def fit(self, X: pd.DataFrame, y=None) -> "RobustQuantileTransformer":
        self.num_cols = list(X.select_dtypes(include=[np.number]).columns)
        if self.num_cols:
            self.transformer.fit(X[self.num_cols].fillna(0))
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        if self.num_cols:
            out[self.num_cols] = self.transformer.transform(out[self.num_cols].fillna(0))
        return out
