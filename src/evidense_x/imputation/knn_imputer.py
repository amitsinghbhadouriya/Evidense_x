"""K-Nearest Neighbors distance-weighted tabular missing value imputer."""
import pandas as pd
from sklearn.impute import KNNImputer
from .base_imputer import BaseTabularImputer

class KNNNeighborImputer(BaseTabularImputer):
    """Imputes missing attributes using distance-weighted average of nearest neighbors."""
    
    def __init__(self, n_neighbors: int = 5, weights: str = "distance") -> None:
        self.imputer = KNNImputer(n_neighbors=n_neighbors, weights=weights)
        
    def fit_transform(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        num_cols = list(df.select_dtypes(include=["number"]).columns)
        if not num_cols:
            return df.copy()
        out = df.copy()
        out[num_cols] = self.imputer.fit_transform(out[num_cols])
        return out
