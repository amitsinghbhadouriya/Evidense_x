import pandas as pd
from typing import List, Set

def detect_exact_train_test_overlap(train_df: pd.DataFrame, test_df: pd.DataFrame, feature_cols: List[str]) -> Set[tuple]:
    train_tuples = set(tuple(x) for x in train_df[feature_cols].values)
    test_tuples = set(tuple(x) for x in test_df[feature_cols].values)
    return train_tuples.intersection(test_tuples)
