from typing import Dict, Callable

DATASET_REGISTRY: Dict[str, Callable] = {}

def register_dataset(name: str, loader_fn: Callable):
    DATASET_REGISTRY[name] = loader_fn

def list_available_datasets():
    return list(DATASET_REGISTRY.keys())
