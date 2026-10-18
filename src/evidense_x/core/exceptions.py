"""Domain-specific exception hierarchy for data leakage and defect simulation."""

class EvidenseXError(Exception):
    """Base exception class for all Evidense-X errors."""
    pass

class DataDefectError(EvidenseXError):
    """Raised when defect injection fails or violates boundary conditions."""
    pass

class LeakageAuditViolation(EvidenseXError):
    """Raised when leakage rate exceeds acceptable auditing thresholds."""
    pass

class PartitionInconsistencyError(EvidenseXError):
    """Raised when train/test partition schemas do not match."""
    pass
