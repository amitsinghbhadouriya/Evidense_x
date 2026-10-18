"""Unit tests for newly added auditing modules."""
import pandas as pd
import numpy as np
from evidense_x.audit.exact_hash_auditor import ExactHashLeakageAuditor
from evidense_x.audit.nearest_neighbor_auditor import KDTreeLeakageAuditor

def test_exact_hash_auditor():
    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [2, 7, 8], "b": [5, 9, 10]})
    auditor = ExactHashLeakageAuditor()
    res = auditor.audit(df1, df2)
    assert res["exact_leakage_count"] == 1
    assert res["has_exact_leakage"] is True

def test_kdtree_auditor():
    df1 = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    df2 = pd.DataFrame({"a": [1.000001, 10.0], "b": [3.000001, 20.0]})
    auditor = KDTreeLeakageAuditor()
    res = auditor.audit(df1, df2, threshold=1e-3)
    assert res["near_leakage_count"] == 1
