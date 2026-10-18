"""Registry pattern implementation for dynamically discovering injectors and auditors."""
from typing import Dict, Type, Any, Callable

_INJECTOR_REGISTRY: Dict[str, Type[Any]] = {}
_AUDITOR_REGISTRY: Dict[str, Type[Any]] = {}

def register_injector(name: str) -> Callable[[Type[Any]], Type[Any]]:
    """Decorator to register a defect injector class by identifier."""
    def decorator(cls: Type[Any]) -> Type[Any]:
        _INJECTOR_REGISTRY[name.lower()] = cls
        return cls
    return decorator

def get_injector(name: str) -> Type[Any]:
    """Retrieve registered injector class by name."""
    if name.lower() not in _INJECTOR_REGISTRY:
        raise KeyError(f"Injector '{name}' is not registered. Available: {list(_INJECTOR_REGISTRY.keys())}")
    return _INJECTOR_REGISTRY[name.lower()]
