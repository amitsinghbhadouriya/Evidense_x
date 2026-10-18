"""Defect injection and corruption simulators for Evidense-X benchmark framework."""
from .mar_simulator import MARLogisticSimulator
from .censoring import ContinuousCensoringInjector
from .gaussian_jitter import GaussianJitterInjector
from .categorical_drift import CategoricalDriftInjector
from .label_noise import ClassificationLabelNoiseInjector
from .block_burst import BlockBurstMissingness
from .duplicate_burst import DuplicateBurstInjector
from .near_duplicate_cluster import NearDuplicateClusterGenerator
from .compound_pipeline import CompoundDefectPipeline
from .sparsity_mask import StructuredSparsityMask
from .outlier_injector import CauchyOutlierInjector

__all__ = [
    "MARLogisticSimulator",
    "ContinuousCensoringInjector",
    "GaussianJitterInjector",
    "CategoricalDriftInjector",
    "ClassificationLabelNoiseInjector",
    "BlockBurstMissingness",
    "DuplicateBurstInjector",
    "NearDuplicateClusterGenerator",
    "CompoundDefectPipeline",
    "StructuredSparsityMask",
    "CauchyOutlierInjector",
]
