"""Unit tests for MICE, KNN, and MissForest tabular imputers."""
import numpy as np
import pandas as pd
from evidense_x.imputation.knn_imputer import KNNNeighborImputer
from evidense_x.imputation.mice_imputer import IterativeChainedEquationsImputer

def test_knn_imputer():
    df = pd.DataFrame({"a": [1.0, np.nan, 3.0, 4.0], "b": [2.0, 3.0, 4.0, np.nan]})
    imputer = KNNNeighborImputer(n_neighbors=2)
    res = imputer.fit_transform(df)
    assert res.isna().sum().sum() == 0

def test_mice_imputer():
    df = pd.DataFrame({"x": [10.0, 20.0, np.nan, 40.0], "y": [1.0, np.nan, 3.0, 4.0]})
    imputer = IterativeChainedEquationsImputer(max_iter=3)
    res = imputer.fit_transform(df)
    assert res.isna().sum().sum() == 0
