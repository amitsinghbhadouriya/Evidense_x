def calculate_leakage_risk_score(exact_overlap_ratio: float, fuzzy_overlap_ratio: float) -> str:
    combined = 0.7 * exact_overlap_ratio + 0.3 * fuzzy_overlap_ratio
    if combined > 0.2:
        return "CRITICAL"
    elif combined > 0.05:
        return "HIGH"
    elif combined > 0.0:
        return "MODERATE"
    return "LOW"
