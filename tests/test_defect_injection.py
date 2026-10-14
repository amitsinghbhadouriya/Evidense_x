import numpy as np
import pandas as pd
import pytest
from experiment_runner import apply_mcar_mask, stratified_group_train_test_split

def test_mcar_mask_zero_rate():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    masked = apply_mcar_mask(df, ['a', 'b'], 0.0, seed=42)
    assert df.equals(masked)

def test_mcar_mask_positive_rate():
    df = pd.DataFrame(np.random.randn(100, 4), columns=['f1', 'f2', 'f3', 'f4'])
    masked = apply_mcar_mask(df, ['f1', 'f2', 'f3', 'f4'], 0.25, seed=42)
    nan_count = masked.isna().sum().sum()
    total_entries = 100 * 4
    # Expected ~25%
    ratio = nan_count / total_entries
    assert 0.18 <= ratio <= 0.32

def test_stratified_group_train_test_split_no_leakage():
    # Construct data with intentional duplicates
    records = [
        {'f1': 1.0, 'f2': 2.0, 'target': 1},
        {'f1': 1.0, 'f2': 2.0, 'target': 1}, # duplicate
        {'f1': 3.0, 'f2': 4.0, 'target': 0},
        {'f1': 3.0, 'f2': 4.0, 'target': 0}, # duplicate
        {'f1': 5.0, 'f2': 6.0, 'target': 1},
        {'f1': 7.0, 'f2': 8.0, 'target': 0},
        {'f1': 9.0, 'f2': 10.0, 'target': 1},
        {'f1': 11.0, 'f2': 12.0, 'target': 0},
    ]
    df = pd.DataFrame(records)
    train_idx, test_idx = stratified_group_train_test_split(df, ['f1', 'f2'], 'target', test_size=0.25, random_state=42)
    
    # Verify no index overlaps
    assert len(set(train_idx).intersection(set(test_idx))) == 0
    assert len(train_idx) + len(test_idx) == len(df)
    
    # Check that identical records do not cross partitions
    train_df = df.iloc[train_idx]
    test_df = df.iloc[test_idx]
    
    train_tuples = set(tuple(x) for x in train_df[['f1', 'f2', 'target']].values)
    test_tuples = set(tuple(x) for x in test_df[['f1', 'f2', 'target']].values)
    assert len(train_tuples.intersection(test_tuples)) == 0
