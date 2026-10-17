import pandas as pd
from typing import List
from .masking import apply_mcar_mask

class DefectPipeline:
    def __init__(self, mcar_rate: float = 0.0, seed: int = 42):
        self.mcar_rate = mcar_rate
        self.seed = seed

    def transform(self, df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
        return apply_mcar_mask(df, feature_cols, self.mcar_rate, self.seed)
