"""Post-hoc statistical power estimation for benchmark hypothesis testing."""
from statsmodels.stats.power import TTestIndPower

def compute_achieved_power(effect_size: float, n_obs: int, alpha: float = 0.05) -> float:
    """Computes achieved statistical power given effect size and sample size."""
    analysis = TTestIndPower()
    power = analysis.solve_power(effect_size=effect_size, nobs1=n_obs, alpha=alpha, alternative="two-sided")
    return float(power)
