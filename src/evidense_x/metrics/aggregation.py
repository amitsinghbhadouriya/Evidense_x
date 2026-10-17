import pandas as pd

def aggregate_metric_runs(df: pd.DataFrame, metric_cols: list) -> pd.DataFrame:
    return df.groupby(['model', 'dataset', 'overlap_rate', 'missing_rate'])[metric_cols].agg(['mean', 'std']).reset_index()
