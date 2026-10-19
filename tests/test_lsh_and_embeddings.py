"""Unit tests for MinHash LSH and Cosine Embedding similarity scanners."""
import numpy as np
import pandas as pd
from evidense_x.audit.embedding_leakage_scanner import EmbeddingCosineLeakageScanner
from evidense_x.audit.variance_auditor import ZeroVarianceFeatureAuditor

def test_embedding_scanner():
    train = np.array([[1.0, 0.0], [0.0, 1.0]])
    test = np.array([[1.0, 0.0001], [0.7, 0.7]])
    scanner = EmbeddingCosineLeakageScanner()
    res = scanner.scan_embeddings(train, test, threshold=0.99)
    assert res["flagged_semantic_duplicates"] == 1

def test_zero_variance_auditor():
    df = pd.DataFrame({"a": [5.0, 5.0, 5.0], "b": [1.0, 2.0, 3.0]})
    auditor = ZeroVarianceFeatureAuditor()
    res = auditor.audit(df)
    assert "a" in res["zero_variance_columns"]
    assert "b" not in res["zero_variance_columns"]
