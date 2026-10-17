def compute_relative_delta(val_leaked: float, val_ref: float) -> float:
    return (val_leaked - val_ref) / val_ref if val_ref != 0 else 0.0
