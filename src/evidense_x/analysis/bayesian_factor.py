"""Approximated Bayes Factor (BIC) for hypothesis evidence quantification."""
import numpy as np

def compute_bic_bayes_factor(bic_null: float, bic_alt: float) -> float:
    """Computes Kass & Raftery approximation of Bayes Factor from model BICs."""
    delta_bic = bic_null - bic_alt
    return float(np.exp(0.5 * delta_bic))
