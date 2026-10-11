import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, roc_auc_score

warnings.filterwarnings('ignore')

# -------------------------------------------------------------
# 1. Dataset Loading and Preparation
# -------------------------------------------------------------
def load_red_wine():
    path = os.path.join('wine quality', 'winequality-red.csv')
    df = pd.read_csv(path, sep=';')
    feature_cols = [c for c in df.columns if c != 'quality']
    df['target'] = (df['quality'] >= 6).astype(int)
    num_cols = feature_cols
    cat_cols = []
    return df, num_cols, cat_cols, 'target'

def load_white_wine():
    path = os.path.join('wine quality', 'winequality-white.csv')
    df = pd.read_csv(path, sep=';')
    feature_cols = [c for c in df.columns if c != 'quality']
    df['target'] = (df['quality'] >= 6).astype(int)
    num_cols = feature_cols
    cat_cols = []
    return df, num_cols, cat_cols, 'target'

def load_adult(subsample_seed=26):
    path = os.path.join('Adult', 'adult.data')
    cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
            'hours-per-week', 'native-country', 'income']
    df = pd.read_csv(path, names=cols, sep=r',\s*', engine='python', na_values='?')
    df['target'] = (df['income'] == '>50K').astype(int)
    
    # 10,000 stratified subsample
    sub, _ = train_test_split(df, train_size=10000, random_state=subsample_seed, stratify=df['target'])
    sub = sub.reset_index(drop=True)
    
    num_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    cat_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    return sub, num_cols, cat_cols, 'target'

# -------------------------------------------------------------
# 2. Stratified Group Split (Duplicate-Aware Reference Split)
# -------------------------------------------------------------
def stratified_group_train_test_split(df, feature_cols, target_col, test_size=0.25, random_state=42):
    """
    Ensures identical feature-and-label rows stay strictly within either train or test,
    while maintaining overall stratified class balance.
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

# -------------------------------------------------------------
# 3. MCAR Masking Function
# -------------------------------------------------------------
def apply_mcar_mask(df, feature_cols, mask_rate, seed):
    """
    Applies MCAR masking to feature columns at given mask_rate.
    """
    if mask_rate == 0.0:
        return df.copy()
    
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    
    mask = rng.rand(len(df), len(feature_cols)) < mask_rate
    for j, col in enumerate(feature_cols):
        # preserve existing NaNs or replace with NaN
        col_series = df_masked[col].copy()
        col_series[mask[:, j]] = np.nan
        df_masked[col] = col_series
        
    return df_masked

# -------------------------------------------------------------
# 4. Pipeline Builder
# -------------------------------------------------------------
def get_pipeline(model_name, num_cols, cat_cols, seed):
    transformers = []
    if num_cols:
        num_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        transformers.append(('num', num_transformer, num_cols))
        
    if cat_cols:
        cat_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])
        transformers.append(('cat', cat_transformer, cat_cols))
        
    preprocessor = ColumnTransformer(transformers=transformers)
    
    if model_name == 'Logistic Regression':
        clf = LogisticRegression(max_iter=2000, random_state=seed)
    elif model_name == 'Decision Tree':
        clf = DecisionTreeClassifier(random_state=seed)
    elif model_name == 'Random Forest':
        clf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
    else:
        raise ValueError(f"Unknown model: {model_name}")
        
    return Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', clf)
    ])

print("Module experiment_runner helper functions defined successfully.")
