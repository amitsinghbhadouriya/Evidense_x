import pandas as pd

def format_retention_table(results_df: pd.DataFrame) -> pd.DataFrame:
    return results_df[results_df['missing_rate'] == 0.30].groupby(['dataset', 'model'])['delta_f1'].mean().reset_index()
