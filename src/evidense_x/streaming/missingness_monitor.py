"""Exponential Moving Average (EMA) missingness rate streaming monitor."""
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from .base import BaseStreamMonitor, StreamAlert


class ExponentialMovingAverageMissingnessAuditor(BaseStreamMonitor):
    """Monitors real-time missing value ratios using smoothed exponential moving averages."""

    def __init__(
        self,
        alpha: float = 0.05,
        missingness_alert_rate: float = 0.20,
    ) -> None:
        super().__init__(name="ExponentialMovingAverageMissingnessAuditor", window_size=100)
        self.alpha = alpha
        self.missingness_alert_rate = missingness_alert_rate
        self.smoothed_missing_rate: Optional[float] = None
        self.total_records = 0

    def ingest_record(self, record: Dict[str, Any]) -> Optional[StreamAlert]:
        """Ingest single incoming record dictionary, calculate null ratio, and update EMA."""
        self.total_records += 1
        num_fields = len(record)
        if num_fields == 0:
            return None

        null_count = sum(1 for v in record.values() if v is None or (isinstance(v, float) and v != v))
        current_rate = null_count / float(num_fields)
        self.buffer.append(current_rate)

        if self.smoothed_missing_rate is None:
            self.smoothed_missing_rate = current_rate
        else:
            self.smoothed_missing_rate = (self.alpha * current_rate) + ((1.0 - self.alpha) * self.smoothed_missing_rate)

        if self.total_records >= 15 and self.smoothed_missing_rate >= self.missingness_alert_rate:
            return StreamAlert(
                timestamp=datetime.now(timezone.utc).isoformat(),
                monitor_name=self.name,
                metric_name="smoothed_missingness_rate",
                observed_value=float(self.smoothed_missing_rate),
                threshold=self.missingness_alert_rate,
                severity="WARNING" if self.smoothed_missing_rate < 0.40 else "CRITICAL",
                details={
                    "current_record_null_ratio": float(current_rate),
                    "smoothed_ema_rate": float(self.smoothed_missing_rate),
                    "total_records_processed": self.total_records,
                },
            )
        return None

    def get_window_summary(self) -> Dict[str, Any]:
        """Return missingness EMA summary."""
        return {
            "total_records_processed": self.total_records,
            "smoothed_missing_rate": float(self.smoothed_missing_rate or 0.0),
            "alert_threshold": self.missingness_alert_rate,
        }
