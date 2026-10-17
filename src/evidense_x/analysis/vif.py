import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

def compute_vif_scores(df: pd.DataFrame, num_cols: list) -> pd.Series:
    X = df[num_cols].dropna()
    vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return pd.Series(vifs, index=num_cols)
