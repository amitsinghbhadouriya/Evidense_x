import pandas as pd
from typing import List

def create_missing_indicators(df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    """Generates binary 0/1 missing indicator columns."""
    out = pd.DataFrame(index=df.index)
    for col in feature_cols:
        out[f"{col}_isnan"] = df[col].isna().astype(int)
    return out
