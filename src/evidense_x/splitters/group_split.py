import numpy as np
import pandas as pd
from typing import Tuple, List

class DuplicateAwareGroupSplitter:
    @staticmethod
    def split(df: pd.DataFrame, feature_cols: List[str], target_col: str, test_size: float = 0.25, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray]:
        df_temp = df[feature_cols + [target_col]].copy()
        groups = df_temp.groupby(feature_cols + [target_col], sort=False, dropna=False).indices
        rng = np.random.RandomState(random_state)
        pos_groups = [idxs for g_key, idxs in groups.items() if g_key[-1] == 1]
        neg_groups = [idxs for g_key, idxs in groups.items() if g_key[-1] != 1]
        rng.shuffle(pos_groups)
        rng.shuffle(neg_groups)
        test_indices = []
        for grp_list in [pos_groups, neg_groups]:
            total_count = sum(len(idxs) for idxs in grp_list)
            target_test = int(round(test_size * total_count))
            curr = 0
            for idxs in grp_list:
                if curr + len(idxs) <= target_test or curr == 0:
                    test_indices.extend(idxs)
                    curr += len(idxs)
        test_set = set(test_indices)
        train_indices = [i for i in range(len(df)) if i not in test_set]
        return np.array(train_indices), np.array(test_indices)
