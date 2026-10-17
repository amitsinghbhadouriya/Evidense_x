import pandas as pd

def compute_imbalance_ratio(df: pd.DataFrame, target_col: str) -> float:
    counts = df[target_col].value_counts()
    return counts.max() / counts.min() if len(counts) > 1 else 1.0
