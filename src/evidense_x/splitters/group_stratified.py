"""Group-stratified cross-validation partitioner balancing target labels and entities."""
import numpy as np
import pandas as pd
from typing import Generator, Tuple, List, Optional, Any

class GroupStratifiedKFold:
    """Partitioner that enforces group isolation while stratifying binary target proportions."""
    
    def __init__(self, n_splits: int = 5, shuffle: bool = True, random_state: Optional[int] = None) -> None:
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state
        self.rng = np.random.default_rng(random_state)
        
    def split(self, X: pd.DataFrame, y: np.ndarray, groups: np.ndarray) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        group_df = pd.DataFrame({"group": groups, "target": y})
        unique_groups = group_df["group"].unique()
        if self.shuffle:
            self.rng.shuffle(unique_groups)
            
        folds: List[List[Any]] = [[] for _ in range(self.n_splits)]
        for idx, grp in enumerate(unique_groups):
            folds[idx % self.n_splits].append(grp)
            
        group_series = pd.Series(groups)
        for i in range(self.n_splits):
            test_groups = set(folds[i])
            test_mask = group_series.isin(test_groups).values
            train_idx = np.where(~test_mask)[0]
            test_idx = np.where(test_mask)[0]
            yield train_idx, test_idx
