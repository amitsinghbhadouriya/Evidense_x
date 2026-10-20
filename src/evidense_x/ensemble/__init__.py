"""Ensembling, voting combiners, and Super Learner stacking classifiers."""
from .base_ensemble import BaseEnsembleCombiner
from .voting_ensemble import SoftVotingEnsemble
from .stacking_classifier import SuperLearnerStackingClassifier
from .diversity_blend import DiversityWeightedBlend
from .temperature_scaling import TemperatureScalingCalibrator
from .bayesian_averaging import BayesianModelAveragingCombiner

__all__ = [
    "BaseEnsembleCombiner",
    "SoftVotingEnsemble",
    "SuperLearnerStackingClassifier",
    "DiversityWeightedBlend",
    "TemperatureScalingCalibrator",
    "BayesianModelAveragingCombiner",
]
