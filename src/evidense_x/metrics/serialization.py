import json

def save_metrics_to_json(metrics_dict: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metrics_dict, f, indent=2)
