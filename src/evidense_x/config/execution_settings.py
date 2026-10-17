from dataclasses import dataclass

@dataclass
class ExecutionSettings:
    n_jobs: int = -1
    verbose: int = 1
    timeout_seconds: int = 3600
