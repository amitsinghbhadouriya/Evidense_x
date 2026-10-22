"""Base interfaces and sliding window buffers for online stream monitoring."""
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import pandas as pd


@dataclass
class StreamAlert:
    """Alert event emitted when streaming defects or drift exceed threshold."""
    timestamp: str
    monitor_name: str
    metric_name: str
    observed_value: float
    threshold: float
    severity: str  # 'INFO', 'WARNING', 'CRITICAL'
    details: Dict[str, Any]


class BaseStreamMonitor(ABC):
    """Abstract interface for real-time streaming data quality monitoring."""

    def __init__(self, name: str, window_size: int = 500) -> None:
        self.name = name
        self.window_size = window_size
        self.buffer = deque(maxlen=window_size)

    @abstractmethod
    def ingest_record(self, record: Dict[str, Any]) -> Optional[StreamAlert]:
        """Ingest single incoming record into window and evaluate defect alerts."""
        pass

    @abstractmethod
    def get_window_summary(self) -> Dict[str, Any]:
        """Return diagnostic metrics across current active window."""
        pass
