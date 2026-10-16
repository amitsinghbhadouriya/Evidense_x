import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

def fit_interaction_ols(df: pd.DataFrame, formula: str = "f1 ~ overlap_rate * missing_rate"):
    """Fits an Ordinary Least Squares (OLS) interaction model."""
    model = ols(formula, data=df).fit()
    return model
