"""Unit tests for GroupStratifiedKFold, Temporal, and Purged cross-validators."""
import numpy as np
import pandas as pd
from evidense_x.splitters.group_stratified import GroupStratifiedKFold
from evidense_x.splitters.temporal_splitter import TemporalBlockSplitter
from evidense_x.splitters.purged_cv import PurgedWalkForwardCV

def test_group_stratified_kfold():
    X = pd.DataFrame({"feat": range(20)})
    y = np.array([0, 1] * 10)
    groups = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5] * 2)
    splitter = GroupStratifiedKFold(n_splits=3, random_state=42)
    splits = list(splitter.split(X, y, groups))
    assert len(splits) == 3
    for tr, ts in splits:
        assert len(set(groups[tr]).intersection(set(groups[ts]))) == 0

def test_temporal_block_splitter():
    df = pd.DataFrame({"val": range(100)})
    splitter = TemporalBlockSplitter(train_window_size=20, test_window_size=5, step_size=10)
    splits = list(splitter.split(df))
    assert len(splits) > 0
    tr, ts = splits[0]
    assert np.max(tr) < np.min(ts)
