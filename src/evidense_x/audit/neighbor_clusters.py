import pandas as pd
from typing import List, Dict

def find_exact_neighbor_clusters(df: pd.DataFrame, feature_cols: List[str]) -> Dict[int, List[int]]:
    grouped = df.groupby(feature_cols, sort=False).indices
    return {i: idxs.tolist() for i, idxs in enumerate(grouped.values()) if len(idxs) > 1}
