"""Model interpretability, permutation importance, and attribution leakage auditing."""
from .base_explainer import BaseFeatureExplainer
from .permutation_importance import PermutationFeatureExplainer
from .kernel_shap import ApproximateKernelShapExplainer
from .attribution_leakage import AttributionLeakageAuditor
from .counterfactual_auditor import CounterfactualPerturbationAuditor
from .integrated_gradients import approximate_integrated_gradients
from .tree_stability import compute_ranking_stability

__all__ = [
    "BaseFeatureExplainer",
    "PermutationFeatureExplainer",
    "ApproximateKernelShapExplainer",
    "AttributionLeakageAuditor",
    "CounterfactualPerturbationAuditor",
    "approximate_integrated_gradients",
    "compute_ranking_stability",
]
