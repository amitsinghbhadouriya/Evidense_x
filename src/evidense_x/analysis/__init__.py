"""Statistical testing, effect size, and meta-analytic evaluation routines."""
from .wilcoxon_test import run_paired_wilcoxon_test
from .friedman_ranking import compute_friedman_ranks
from .fdr_correction import benjamini_hochberg_correction
from .effect_size import compute_hedges_g
from .bootstrap_ci import compute_bootstrap_ci
from .shapiro_wilk import test_distribution_normality
from .two_way_anova import run_factorial_anova
from .robust_regression import fit_huber_regression
from .meta_analysis import random_effects_meta_analysis
from .bayesian_factor import compute_bic_bayes_factor
from .power_analysis import compute_achieved_power

__all__ = [
    "run_paired_wilcoxon_test",
    "compute_friedman_ranks",
    "benjamini_hochberg_correction",
    "compute_hedges_g",
    "compute_bootstrap_ci",
    "test_distribution_normality",
    "run_factorial_anova",
    "fit_huber_regression",
    "random_effects_meta_analysis",
    "compute_bic_bayes_factor",
    "compute_achieved_power",
]
