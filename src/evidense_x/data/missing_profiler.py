import pandas as pd

def profile_missing_rates(df: pd.DataFrame) -> pd.Series:
    return df.isna().mean()
