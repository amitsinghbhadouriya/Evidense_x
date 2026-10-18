"""Two-way Factorial ANOVA testing missingness x leakage interaction effects."""
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
from typing import Dict, Any

def run_factorial_anova(df: pd.DataFrame, formula: str = "auc ~ C(missing_rate) * C(overlap_rate)") -> Dict[str, Any]:
    """Fits Ordinary Least Squares and returns ANOVA interaction table."""
    model = ols(formula, data=df).fit()
    table = sm.stats.anova_lm(model, typ=2)
    return {
        "f_statistic_interaction": float(table.loc["C(missing_rate):C(overlap_rate)", "F"]),
        "p_value_interaction": float(table.loc["C(missing_rate):C(overlap_rate)", "PR(>F)"]),
        "interaction_significant": table.loc["C(missing_rate):C(overlap_rate)", "PR(>F)"] < 0.05
    }
