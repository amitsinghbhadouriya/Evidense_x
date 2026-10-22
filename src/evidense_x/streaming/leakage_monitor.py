"""Sliding window duplicate and train-set contamination stream monitor."""
import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, Any, Set, Optional, List
from .base import BaseStreamMonitor, StreamAlert


class SlidingWindowLeakageMonitor(BaseStreamMonitor):
    """Tracks duplicate contamination in real time against known training hashes and window."""

    def __init__(
        self,
        reference_hashes: Optional[Set[str]] = None,
        window_size: int = 500,
        leakage_alert_rate: float = 0.05,
    ) -> None:
        super().__init__(name="SlidingWindowLeakageMonitor", window_size=window_size)
        self.reference_hashes: Set[str] = reference_hashes or set()
        self.window_hashes: List[str] = []
        self.leakage_alert_rate = leakage_alert_rate
        self.contamination_events = 0
        self.total_ingested = 0

    def compute_hash(self, record: Dict[str, Any]) -> str:
        """Compute SHA-256 hash of sorted key-value pairs."""
        payload = json.dumps(record, sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def ingest_record(self, record: Dict[str, Any]) -> Optional[StreamAlert]:
        """Ingest record and alert if duplicate contamination rate in window spikes."""
        self.total_ingested += 1
        rec_hash = self.compute_hash(record)
        is_leakage = rec_hash in self.reference_hashes

        if is_leakage:
            self.contamination_events += 1

        self.buffer.append(is_leakage)
        self.window_hashes.append(rec_hash)
        if len(self.window_hashes) > self.window_size:
            self.window_hashes.pop(0)

        current_window_rate = sum(self.buffer) / len(self.buffer)
        if len(self.buffer) >= 20 and current_window_rate >= self.leakage_alert_rate:
            return StreamAlert(
                timestamp=datetime.now(timezone.utc).isoformat(),
                monitor_name=self.name,
                metric_name="window_leakage_rate",
                observed_value=float(current_window_rate),
                threshold=self.leakage_alert_rate,
                severity="WARNING" if current_window_rate < 0.15 else "CRITICAL",
                details={
                    "total_ingested": self.total_ingested,
                    "window_size": len(self.buffer),
                    "duplicate_count_in_window": sum(self.buffer),
                },
            )
        return None

    def get_window_summary(self) -> Dict[str, Any]:
        """Return window leakage statistics."""
        rate = sum(self.buffer) / max(1, len(self.buffer))
        return {
            "total_ingested": self.total_ingested,
            "window_size": len(self.buffer),
            "window_contamination_rate": float(rate),
            "total_contamination_events": self.contamination_events,
        }
