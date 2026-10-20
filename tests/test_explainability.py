"""Unit tests for attribution leakage auditor and ranking stability."""
from evidense_x.explainability.attribution_leakage import AttributionLeakageAuditor
from evidense_x.explainability.tree_stability import compute_ranking_stability

def test_attribution_leakage():
    auditor = AttributionLeakageAuditor(dominance_threshold=0.6)
    leaked = {"f1": 90.0, "f2": 5.0, "f3": 5.0}
    clean = {"f1": 35.0, "f2": 35.0, "f3": 30.0}
    assert auditor.audit_importance(leaked)["concentration_leakage"] is True
    assert auditor.audit_importance(clean)["concentration_leakage"] is False

def test_ranking_stability():
    c = ["f1", "f2", "f3", "f4"]
    p = ["f1", "f2", "f3", "f4"]
    score = compute_ranking_stability(c, p)
    assert score == 1.0
