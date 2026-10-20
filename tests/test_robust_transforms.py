"""Unit tests for winsorizer, quantile transforms, and missing indicators."""
import pandas as pd
import numpy as np
from evidense_x.transforms.winsorizer import OutlierWinsorizer
from evidense_x.transforms.missing_indicator import MissingnessIndicatorAugmenter

def test_winsorizer():
    df = pd.DataFrame({"a": [1.0, 2.0, 2.5, 3.0, 100.0]})
    w = OutlierWinsorizer(factor=1.5)
    res = w.fit_transform(df)
    assert res["a"].max() < 100.0

def test_missing_indicator():
    df = pd.DataFrame({"a": [1.0, np.nan, 3.0], "b": [4.0, 5.0, 6.0]})
    aug = MissingnessIndicatorAugmenter()
    res = aug.fit_transform(df)
    assert "missing_a" in res.columns
    assert "missing_b" not in res.columns
