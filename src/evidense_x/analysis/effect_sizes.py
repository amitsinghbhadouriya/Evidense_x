import pandas as pd

def compute_eta_squared(anova_table: pd.DataFrame) -> pd.Series:
    ss_total = anova_table['sum_sq'].sum()
    return anova_table['sum_sq'] / ss_total
