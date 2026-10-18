"""Unit tests for statistical testing and effect size modules."""
import numpy as np
from evidense_x.analysis.wilcoxon_test import run_paired_wilcoxon_test
from evidense_x.analysis.effect_size import compute_hedges_g

def test_wilcoxon_identical():
    a = np.array([0.8, 0.85, 0.9])
    res = run_paired_wilcoxon_test(a, a)
    assert res["significant"] is False

def test_hedges_g_computation():
    g1 = np.array([1.0, 2.0, 3.0, 4.0])
    g2 = np.array([5.0, 6.0, 7.0, 8.0])
    g = compute_hedges_g(g1, g2)
    assert g < 0.0
