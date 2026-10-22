"""Base protocol and audit logging for automated data defect remediation."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple
import pandas as pd


@dataclass
class RemediationActionLog:
    """Audit log recording specific actions taken during dataset remediation."""
    remediator_name: str
    action_type: str
    rows_affected: int
    columns_affected: List[str]
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    diagnostics: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert action log to dictionary."""
        return {
            "remediator_name": self.remediator_name,
            "action_type": self.action_type,
            "rows_affected": self.rows_affected,
            "columns_affected": self.columns_affected,
            "timestamp": self.timestamp,
            "diagnostics": self.diagnostics,
        }


class BaseRemediator(ABC):
    """Abstract interface for automated dataset defect repair operations."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def remediate(self, df: pd.DataFrame, **kwargs: Any) -> Tuple[pd.DataFrame, RemediationActionLog]:
        """Repair defects in dataset and return healed DataFrame along with audit action log."""
        pass
