import hashlib
import pandas as pd
from typing import List, Dict, Any

def compute_row_hashes(df: pd.DataFrame, feature_cols: List[str]) -> pd.Series:
    """Computes deterministic MD5 hashes for observation coordinate vectors."""
    def hash_row(row):
        rep = "|".join(str(val) for val in row)
        return hashlib.md5(rep.encode('utf-8')).hexdigest()
    return df[feature_cols].apply(hash_row, axis=1)

def detect_duplicate_clusters(df: pd.DataFrame, feature_cols: List[str], target_col: str = None) -> Dict[str, Any]:
    cols = feature_cols + ([target_col] if target_col else [])
    grouped = df.groupby(cols, sort=False, dropna=False)
    clusters = {k: v.tolist() for k, v in grouped.indices.items() if len(v) > 1}
    dup_rows = sum(len(v) for v in clusters.values())
    return {
        "cluster_count": len(clusters),
        "total_duplicate_rows": dup_rows,
        "duplicate_rate": dup_rows / len(df) if len(df) > 0 else 0.0,
        "clusters": clusters
    }
