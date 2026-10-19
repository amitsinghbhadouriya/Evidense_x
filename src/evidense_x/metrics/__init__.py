"""Evaluation metrics: calibration, memorization, fairness, and robustness indices."""
from .expected_calibration_error import compute_expected_calibration_error
from .brier_decomposition import decompose_brier_score
from .memorization_ratio import compute_memorization_ratio
from .cost_sensitive_evaluator import CostSensitiveEvaluator
from .fairness_demographic_parity import compute_demographic_parity_difference
from .fairness_equalized_odds import compute_equalized_odds_disparity
from .entropy_volatility import compute_prediction_entropy_volatility
from .pr_gain import compute_pr_gain_area

__all__ = [
    "compute_expected_calibration_error",
    "decompose_brier_score",
    "compute_memorization_ratio",
    "CostSensitiveEvaluator",
    "compute_demographic_parity_difference",
    "compute_equalized_odds_disparity",
    "compute_prediction_entropy_volatility",
    "compute_pr_gain_area",
]
