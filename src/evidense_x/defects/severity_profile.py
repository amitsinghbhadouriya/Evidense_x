from dataclasses import dataclass

@dataclass
class DefectSeverityProfile:
    missing_rate: float
    duplicate_overlap_rate: float
    label_noise_rate: float = 0.0
