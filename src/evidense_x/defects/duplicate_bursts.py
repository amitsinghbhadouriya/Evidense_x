import pandas as pd
import numpy as np

def simulate_duplicate_bursts(df: pd.DataFrame, burst_indices: list, copies_per_burst: int = 3) -> pd.DataFrame:
    """Replicates specific observations multiple times to simulate sensor burst duplicates."""
    burst_rows = df.loc[burst_indices]
    repeated = pd.concat([burst_rows] * copies_per_burst, axis=0)
    return pd.concat([df, repeated], axis=0, ignore_index=True)
