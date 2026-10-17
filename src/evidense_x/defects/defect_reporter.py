import pandas as pd
from typing import Dict

def summarize_defect_rates(df: pd.DataFrame) -> Dict[str, float]:
    return {
        "missing_rate": float(df.isna().sum().sum() / df.size),
        "row_count": float(len(df))
    }
