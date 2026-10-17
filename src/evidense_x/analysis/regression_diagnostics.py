from scipy import stats

def test_residual_normality(residuals: list):
    return stats.shapiro(residuals)
