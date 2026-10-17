from statsmodels.stats.multicomp import pairwise_tukeyhsd

def run_tukey_hsd(data: list, groups: list, alpha: float = 0.05):
    return pairwise_tukeyhsd(endog=data, groups=groups, alpha=alpha)
