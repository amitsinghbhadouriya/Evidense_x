"""Non-parametric iterative Random Forest imputer (MissForest pattern)."""
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from .base_imputer import BaseTabularImputer

class MissForestRandomForestImputer(BaseTabularImputer):
    """MissForest style non-parametric missing value imputation using ensemble decision trees."""
    
    def __init__(self, max_iter: int = 5, random_state: int = 42) -> None:
        estimator = ExtraTreesRegressor(n_estimators=30, max_depth=6, random_state=random_state)
        self.imputer = IterativeImputer(estimator=estimator, max_iter=max_iter, random_state=random_state)
        
    def fit_transform(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        num_cols = list(df.select_dtypes(include=["number"]).columns)
        if not num_cols:
            return df.copy()
        out = df.copy()
        out[num_cols] = self.imputer.fit_transform(out[num_cols])
        return out
