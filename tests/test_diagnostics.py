import pytest
from evidense_x.metrics.diagnostic import compute_lsi, compute_eri, evaluate_performance

def test_lsi_calculation():
    lsi = compute_lsi(0.85, 0.70)
    assert pytest.approx(lsi, 0.001) == 0.15

def test_eri_calculation():
    # ref error = 0.40, leak error = 0.20 -> ERI = 0.50 (50%)
    eri = compute_eri(0.80, 0.60)
    assert pytest.approx(eri, 0.001) == 0.50

def test_evaluate_performance():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 0, 0]
    m = evaluate_performance(y_true, y_pred)
    assert 'f1' in m
    assert 'precision' in m
    assert 'recall' in m
