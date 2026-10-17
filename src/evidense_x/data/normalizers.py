import pandas as pd
from typing import List

def minmax_scale(df: pd.DataFrame, num_cols: List[str]) -> pd.DataFrame:
    out = df.copy()
    for c in num_cols:
        denom = out[c].max() - out[c].min()
        out[c] = (out[c] - out[c].min()) / (denom if denom != 0 else 1.0)
    return out
