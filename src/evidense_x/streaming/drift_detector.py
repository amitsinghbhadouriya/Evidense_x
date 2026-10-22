"""Adaptive window stream drift detector based on loss and residual shifts."""
import math
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from .base import BaseStreamMonitor, StreamAlert


class AdaptiveWindowDriftDetector(BaseStreamMonitor):
    """Monitors streaming prediction error rates using an adaptive window threshold."""

    def __init__(
        self,
        window_size: int = 200,
        confidence_delta: float = 0.05,
    ) -> None:
        super().__init__(name="AdaptiveWindowDriftDetector", window_size=window_size)
        self.confidence_delta = confidence_delta
        self.total_errors = 0
        self.total_ingested = 0
        self.min_mean_error: Optional[float] = None

    def ingest_record(self, record: Dict[str, Any]) -> Optional[StreamAlert]:
        """Ingest prediction loss / error indicator (e.g. 0 for correct, 1 for error)."""
        error = float(record.get("error", 0.0))
        self.total_ingested += 1
        if error > 0.5:
            self.total_errors += 1
        self.buffer.append(error)

        if len(self.buffer) >= 20:
            mean_error = sum(self.buffer) / len(self.buffer)
            if self.min_mean_error is None or self.total_ingested <= 50:
                self.min_mean_error = mean_error
            elif mean_error < self.min_mean_error:
                self.min_mean_error = mean_error

            epsilon = math.sqrt(math.log(2.0 / self.confidence_delta) / (2.0 * len(self.buffer)))
            
            # If current window error significantly exceeds historical baseline
            if (mean_error - (self.min_mean_error or 0.0)) > epsilon:
                return StreamAlert(
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    monitor_name=self.name,
                    metric_name="streaming_error_drift",
                    observed_value=float(mean_error),
                    threshold=float((self.min_mean_error or 0.0) + epsilon),
                    severity="WARNING",
                    details={
                        "mean_window_error": float(mean_error),
                        "baseline_min_error": float(self.min_mean_error or 0.0),
                        "hoeffding_bound": float(epsilon),
                    },
                )
        return None

    def get_window_summary(self) -> Dict[str, Any]:
        """Return streaming error summary."""
        return {
            "total_ingested": self.total_ingested,
            "window_size": len(self.buffer),
            "window_mean_error": float(sum(self.buffer) / max(1, len(self.buffer))),
            "cumulative_error_rate": float(self.total_errors / max(1, self.total_ingested)),
        }
