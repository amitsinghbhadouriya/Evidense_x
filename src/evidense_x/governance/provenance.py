"""Cryptographic data lineage and partition fingerprint tracking."""
import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
import pandas as pd


class CryptographicProvenanceTracker:
    """Computes cryptographic hashes and lineage chains across data transformations."""

    def __init__(self, hash_algorithm: str = "sha256") -> None:
        self.hash_algorithm = hash_algorithm
        self.lineage_events: List[Dict[str, Any]] = []

    def compute_dataframe_fingerprint(self, df: pd.DataFrame) -> str:
        """Compute deterministic SHA256 checksum of DataFrame content."""
        hasher = hashlib.new(self.hash_algorithm)
        # Hash column names and shape
        header = f"cols:{list(df.columns)};shape:{df.shape}"
        hasher.update(header.encode("utf-8"))
        # Sample or hash representations
        csv_repr = df.head(1000).to_csv(index=False)
        hasher.update(csv_repr.encode("utf-8"))
        return hasher.hexdigest()

    def record_stage(
        self,
        stage_name: str,
        df: pd.DataFrame,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Record an immutable transformation stage in lineage chain."""
        fingerprint = self.compute_dataframe_fingerprint(df)
        event = {
            "stage_index": len(self.lineage_events),
            "stage_name": stage_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "row_count": len(df),
            "column_count": len(df.columns),
            "fingerprint": fingerprint,
            "parameters": parameters or {},
        }
        self.lineage_events.append(event)
        return event

    def verify_integrity(self, df: pd.DataFrame, expected_fingerprint: str) -> bool:
        """Verify whether dataframe matches recorded cryptographic checksum."""
        actual = self.compute_dataframe_fingerprint(df)
        return actual == expected_fingerprint

    def get_lineage_chain(self) -> List[Dict[str, Any]]:
        """Return complete transformation history chain."""
        return list(self.lineage_events)
