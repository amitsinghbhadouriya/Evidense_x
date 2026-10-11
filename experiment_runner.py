import os
import numpy as np
import pandas as pd

def apply_mcar_mask(df, feature_cols, mask_rate, seed):
    if mask_rate == 0.0:
        return df.copy()
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    mask = rng.rand(len(df), len(feature_cols)) < mask_rate
    for j, col in enumerate(feature_cols):
        col_series = df_masked[col].copy()
        col_series[mask[:, j]] = np.nan
        df_masked[col] = col_series
    return df_masked

def stratified_group_train_test_split(df, feature_cols, target_col, test_size=0.25, random_state=42):
    """
    Ensures identical feature-and-label rows stay strictly within either train or test,
    preventing natural duplicate leakage while maintaining stratified class balance.
    """
    df_temp = df[feature_cols + [target_col]].copy()
    groups = df_temp.groupby(feature_cols + [target_col], sort=False, dropna=False).indices
    rng = np.random.RandomState(random_state)
    
    pos_groups = []
    neg_groups = []
    for g_key, idxs in groups.items():
        target_val = g_key[-1]
        if target_val == 1:
            pos_groups.append(idxs)
        else:
            neg_groups.append(idxs)
            
    rng.shuffle(pos_groups)
    rng.shuffle(neg_groups)
    
    test_indices = []
    for grp_list in [pos_groups, neg_groups]:
        total_class_count = sum(len(idxs) for idxs in grp_list)
        target_test_count = int(round(test_size * total_class_count))
        curr_count = 0
        for idxs in grp_list:
            if curr_count + len(idxs) <= target_test_count or curr_count == 0:
                test_indices.extend(idxs)
                curr_count += len(idxs)
                
    test_set = set(test_indices)
    train_indices = [i for i in range(len(df)) if i not in test_set]
    return np.array(train_indices), np.array(test_indices)
