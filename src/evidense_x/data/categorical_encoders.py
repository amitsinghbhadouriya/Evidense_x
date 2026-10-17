import pandas as pd
from typing import List

def frequency_encode(df: pd.DataFrame, cat_cols: List[str]) -> pd.DataFrame:
    out = df.copy()
    for col in cat_cols:
        freq = out[col].value_counts() / len(out)
        out[col] = out[col].map(freq)
    return out
