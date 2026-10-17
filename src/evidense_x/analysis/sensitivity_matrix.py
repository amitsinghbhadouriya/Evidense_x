import pandas as pd

def build_model_sensitivity_matrix(results_df: pd.DataFrame) -> pd.DataFrame:
    return results_df.groupby(['dataset', 'model'])['delta_f1'].mean().unstack()
