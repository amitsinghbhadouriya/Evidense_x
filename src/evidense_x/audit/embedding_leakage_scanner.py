"""Cosine embedding similarity scanner detecting semantic text/vector representation leakage."""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any

class EmbeddingCosineLeakageScanner:
    """Audits dense embedding vectors for cross-partition semantic near-duplicates."""
    
    def scan_embeddings(self, train_emb: np.ndarray, test_emb: np.ndarray, threshold: float = 0.95) -> Dict[str, Any]:
        sim_matrix = cosine_similarity(test_emb, train_emb)
        max_sims = np.max(sim_matrix, axis=1)
        flagged = int((max_sims >= threshold).sum())
        return {
            "flagged_semantic_duplicates": flagged,
            "semantic_leakage_rate": float(flagged / max(len(test_emb), 1)),
            "max_cosine_similarity": float(np.max(max_sims)),
            "mean_cosine_similarity": float(np.mean(max_sims))
        }
