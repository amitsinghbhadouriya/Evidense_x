import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_red_wine():
    path = os.path.join('wine quality', 'winequality-red.csv')
    df = pd.read_csv(path, sep=';')
    feature_cols = [c for c in df.columns if c != 'quality']
    df['target'] = (df['quality'] >= 6).astype(int)
    return df, feature_cols, [], 'target'

def load_white_wine():
    path = os.path.join('wine quality', 'winequality-white.csv')
    df = pd.read_csv(path, sep=';')
    feature_cols = [c for c in df.columns if c != 'quality']
    df['target'] = (df['quality'] >= 6).astype(int)
    return df, feature_cols, [], 'target'

def load_adult(subsample_seed=26):
    path = os.path.join('Adult', 'adult.data')
    cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
            'hours-per-week', 'native-country', 'income']
    df = pd.read_csv(path, names=cols, sep=r',\s*', engine='python', na_values='?')
    df['target'] = (df['income'] == '>50K').astype(int)
    sub, _ = train_test_split(df, train_size=10000, random_state=subsample_seed, stratify=df['target'])
    sub = sub.reset_index(drop=True)
    num_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    cat_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    return sub, num_cols, cat_cols, 'target'

def stratified_group_train_test_split(df, feature_cols, target_col, test_size=0.25, random_state=42):
    df_temp = df[feature_cols + [target_col]].copy()
    groups = df_temp.groupby(feature_cols + [target_col], sort=False, dropna=False).indices
    rng = np.random.RandomState(random_state)
    pos_groups = [idxs for g_key, idxs in groups.items() if g_key[-1] == 1]
    neg_groups = [idxs for g_key, idxs in groups.items() if g_key[-1] != 1]
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
