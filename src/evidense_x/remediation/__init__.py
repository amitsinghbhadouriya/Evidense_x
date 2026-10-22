"""Automated defect remediation, self-healing datasets, and auto-cleaning pipelines."""
from .base import BaseRemediator, RemediationActionLog
from .deduplicator import DeduplicationAutoResolver
from .imputation_router import IntelligentImputationRouter
from .outlier_clipper import AdaptiveOutlierClipperRemediator
from .label_noise_cleaner import ConfidentLabelNoiseRemediator
from .pipeline import AutoCleanPipeline

__all__ = [
    "BaseRemediator",
    "RemediationActionLog",
    "DeduplicationAutoResolver",
    "IntelligentImputationRouter",
    "AdaptiveOutlierClipperRemediator",
    "ConfidentLabelNoiseRemediator",
    "AutoCleanPipeline",
]
