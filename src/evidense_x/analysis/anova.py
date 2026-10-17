import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

def run_two_way_anova(df: pd.DataFrame, dep_var: str = "f1", factor1: str = "overlap_rate", factor2: str = "missing_rate"):
    formula = f"{dep_var} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})"
    model = ols(formula, data=df).fit()
    return sm.stats.anova_lm(model, typ=2)
