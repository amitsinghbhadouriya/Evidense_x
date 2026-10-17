import pandas as pd

def extract_metadata(df: pd.DataFrame) -> dict:
    return {
        "n_rows": len(df),
        "n_cols": len(df.columns),
        "memory_mb": round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)
    }
