import pandas as pd
from typing import List

def deduplicate_clusters(df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    """Retains exactly one observation per identical feature vector."""
    return df.drop_duplicates(subset=feature_cols).reset_index(drop=True)
