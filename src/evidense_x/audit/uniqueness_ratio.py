import pandas as pd
from typing import List

def compute_uniqueness_ratio(df: pd.DataFrame, feature_cols: List[str]) -> float:
    return len(df.drop_duplicates(subset=feature_cols)) / len(df) if len(df) > 0 else 1.0
