"""Financial transaction stream generator with localized duplicate burst anomalies."""
import numpy as np
import pandas as pd
from typing import Optional

class FinancialTransactionStreamGenerator:
    """Generates streaming transaction telemetry with intermittent replay duplicates."""
    
    def __init__(self, n_transactions: int = 2000, duplicate_burst_prob: float = 0.05, random_state: Optional[int] = 42) -> None:
        self.n_tx = n_transactions
        self.burst_prob = duplicate_burst_prob
        self.rng = np.random.default_rng(random_state)
        
    def generate(self) -> pd.DataFrame:
        user_ids = [f"U{self.rng.integers(1, 100):03d}" for _ in range(self.n_tx)]
        amounts = np.round(self.rng.exponential(50.0, size=self.n_tx) + 5.0, 2)
        timestamps = np.sort(self.rng.uniform(0, 86400, size=self.n_tx))
        
        df = pd.DataFrame({
            "user_id": user_ids,
            "amount": amounts,
            "seconds_of_day": timestamps,
            "is_fraud": (amounts > 250).astype(int)
        })
        
        # Inject replay duplicate bursts
        n_burst = int(self.n_tx * self.burst_prob)
        if n_burst > 0:
            sample_dups = df.sample(n=n_burst, random_state=self.rng.integers(0, 10000)).copy()
            sample_dups["seconds_of_day"] += self.rng.uniform(0.1, 1.0, size=n_burst)
            df = pd.concat([df, sample_dups], ignore_index=True).sort_values("seconds_of_day").reset_index(drop=True)
        return df
