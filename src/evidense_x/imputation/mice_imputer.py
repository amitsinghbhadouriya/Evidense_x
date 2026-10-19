"""Multivariate Imputation by Chained Equations (MICE) using Bayesian ridge regressions."""
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from .base_imputer import BaseTabularImputer

class IterativeChainedEquationsImputer(BaseTabularImputer):
    """MICE algorithm iteratively predicting missing features using Bayesian linear models."""
    
    def __init__(self, max_iter: int = 10, random_state: int = 42) -> None:
        self.imputer = IterativeImputer(max_iter=max_iter, random_state=random_state)
        
    def fit_transform(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        num_cols = list(df.select_dtypes(include=["number"]).columns)
        if not num_cols:
            return df.copy()
        out = df.copy()
        imputed_vals = self.imputer.fit_transform(out[num_cols])
        out[num_cols] = imputed_vals
        return out
