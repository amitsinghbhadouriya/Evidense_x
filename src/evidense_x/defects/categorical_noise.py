import random
import pandas as pd
from typing import List

def perturb_categorical_casing(df: pd.DataFrame, cat_cols: List[str], rate: float = 0.1, seed: int = 42) -> pd.DataFrame:
    """Randomly alters casing in categorical values to simulate entity resolution noise."""
    random.seed(seed)
    out = df.copy()
    for col in cat_cols:
        def alter(val):
            if isinstance(val, str) and random.random() < rate:
                return val.lower() if val.isupper() else val.upper()
            return val
        out[col] = out[col].apply(alter)
    return out
