import pandas as pd
from typing import List

def verify_group_containment(df: pd.DataFrame, train_idx: list, test_idx: list, group_col: str) -> bool:
    tr_groups = set(df.iloc[train_idx][group_col])
    te_groups = set(df.iloc[test_idx][group_col])
    return len(tr_groups.intersection(te_groups)) == 0
