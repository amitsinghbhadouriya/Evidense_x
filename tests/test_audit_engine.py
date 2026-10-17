import pandas as pd
from evidense_x.audit.exact_overlap import detect_exact_train_test_overlap

def test_overlap_audit():
    tr = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    te = pd.DataFrame({"a": [2, 5], "b": [4, 6]})
    common = detect_exact_train_test_overlap(tr, te, ["a", "b"])
    assert len(common) == 1
