"""Multi-objective Pareto optimizer balancing discrimination (AUC) and calibration error (ECE)."""
from typing import List, Dict, Any

class MultiObjectiveParetoFilter:
    """Filters non-dominated candidate parameter sets across multiple objective metrics."""
    
    def extract_pareto_front(self, candidates: List[Dict[str, Any]], auc_scores: List[float], ece_scores: List[float]) -> List[Dict[str, Any]]:
        pareto = []
        n = len(candidates)
        for i in range(n):
            dominated = False
            for j in range(n):
                if i != j:
                    if auc_scores[j] >= auc_scores[i] and ece_scores[j] <= ece_scores[i]:
                        if auc_scores[j] > auc_scores[i] or ece_scores[j] < ece_scores[i]:
                            dominated = True
                            break
            if not dominated:
                pareto.append(candidates[i])
        return pareto
