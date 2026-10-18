"""Core interfaces, registries, exceptions, and protocols for Evidense-X."""
from .interfaces import BaseDefectSimulator
from .audit_interface import BaseLeakageAuditor
from .registry import register_injector, get_injector
from .exceptions import EvidenseXError, DataDefectError, LeakageAuditViolation
from .timer import BenchmarkTimer
from .serialization import to_audit_json
from .provenance import get_system_provenance

__all__ = [
    "BaseDefectSimulator",
    "BaseLeakageAuditor",
    "register_injector",
    "get_injector",
    "EvidenseXError",
    "DataDefectError",
    "LeakageAuditViolation",
    "BenchmarkTimer",
    "to_audit_json",
    "get_system_provenance",
]
