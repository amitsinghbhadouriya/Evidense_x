import statsmodels.api as sm
from statsmodels.formula.api import mixedlm
import pandas as pd

def fit_mixed_effects(df: pd.DataFrame, formula: str = "f1 ~ overlap_rate + missing_rate", group_col: str = "dataset"):
    model = mixedlm(formula, df, groups=df[group_col]).fit()
    return model
