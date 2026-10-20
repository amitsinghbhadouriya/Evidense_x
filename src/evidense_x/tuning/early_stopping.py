"""Early stopping callback tracker halting iteration when validation loss plateaus."""
from typing import Optional

class EarlyStoppingTracker:
    """Tracks validation objective improvement and signals stopping condition."""
    
    def __init__(self, patience: int = 5, min_delta: float = 1e-4) -> None:
        self.patience = patience
        self.min_delta = min_delta
        self.best_loss: float = float("inf")
        self.wait: int = 0
        
    def step(self, current_loss: float) -> bool:
        """Returns True if training should halt."""
        if current_loss < self.best_loss - self.min_delta:
            self.best_loss = current_loss
            self.wait = 0
            return False
        else:
            self.wait += 1
            return self.wait >= self.patience
