from statsmodels.formula.api import ols
import pandas as pd

def fit_ols_with_robust_se(df: pd.DataFrame, formula: str = "f1 ~ overlap_rate * missing_rate", cov_type: str = "HC3"):
    model = ols(formula, data=df).fit(cov_type=cov_type)
    return model
