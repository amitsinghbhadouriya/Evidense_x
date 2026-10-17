import pandas as pd

def check_pre_split_hygiene(df: pd.DataFrame) -> dict:
    return {
        "empty_rows": int(df.isna().all(axis=1).sum()),
        "constant_columns": [c for c in df.columns if df[c].nunique() <= 1]
    }
