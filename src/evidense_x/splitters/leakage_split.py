import numpy as np
import pandas as pd
from typing import Tuple

class ControlledLeakageInjector:
    @staticmethod
    def inject(train_df: pd.DataFrame, test_df: pd.DataFrame, overlap_rate: float, random_state: int = 42) -> pd.DataFrame:
        if overlap_rate <= 0.0:
            return train_df.copy()
        rng = np.random.RandomState(random_state)
        n_leak = int(round(len(test_df) * overlap_rate))
        leak_indices = rng.choice(test_df.index, size=n_leak, replace=False)
        leak_records = test_df.loc[leak_indices].copy()
        augmented_train = pd.concat([train_df, leak_records], axis=0, ignore_index=True)
        return augmented_train
