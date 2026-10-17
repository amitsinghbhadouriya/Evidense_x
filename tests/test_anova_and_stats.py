from evidense_x.analysis.significance import bonferroni_correct

def test_bonferroni():
    res = bonferroni_correct([0.001, 0.04, 0.5], alpha=0.05)
    assert res[0] is True
