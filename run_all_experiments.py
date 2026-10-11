import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

def load_datasets():
    datasets = {}
    df_red = pd.read_csv(os.path.join('wine quality', 'winequality-red.csv'), sep=';')
    df_red['target'] = (df_red['quality'] >= 6).astype(int)
    red_features = [c for c in df_red.columns if c not in ['quality', 'target']]
    datasets['Wine Quality—Red'] = {
        'df': df_red,
        'feat_cols': red_features,
        'num_cols': red_features,
        'cat_cols': [],
        'target_col': 'target'
    }
    return datasets
