"""Unit tests for soft-voting ensemble and super learner stacking classifier."""
import numpy as np
from evidense_x.models.rf_adapter import RandomForestAdapter
from evidense_x.models.logistic_adapter import LogisticRegressionAdapter
from evidense_x.ensemble.voting_ensemble import SoftVotingEnsemble

def test_soft_voting_ensemble():
    X = np.random.randn(50, 4)
    y = np.random.choice([0, 1], size=50)
    m1 = RandomForestAdapter(n_estimators=10)
    m2 = LogisticRegressionAdapter()
    ens = SoftVotingEnsemble()
    ens.fit([m1, m2], X, y)
    probs = ens.predict_proba(X)
    assert probs.shape == (50, 2)
    assert np.allclose(probs.sum(axis=1), 1.0)
