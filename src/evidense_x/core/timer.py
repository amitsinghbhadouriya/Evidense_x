"""High-precision execution timing context manager for benchmarking."""
import time
from typing import Optional

class BenchmarkTimer:
    """Context manager for tracking wall-clock execution time with nanosecond accuracy."""
    
    def __init__(self, description: Optional[str] = None) -> None:
        self.description = description
        self.elapsed_sec: float = 0.0
        self._start: float = 0.0
        
    def __enter__(self) -> "BenchmarkTimer":
        self._start = time.perf_counter()
        return self
        
    def __exit__(self, *args) -> None:
        self.elapsed_sec = time.perf_counter() - self._start
