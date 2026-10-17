import pandas as pd

def validate_partition_sizes(train_df: pd.DataFrame, test_df: pd.DataFrame, expected_ratio: float = 0.25) -> bool:
    actual = len(test_df) / (len(train_df) + len(test_df))
    return abs(actual - expected_ratio) < 0.05
