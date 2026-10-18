"""Provenance and environment metadata recorder for reproducible research."""
import sys
import platform
import subprocess
from typing import Dict, Any

def get_system_provenance() -> Dict[str, Any]:
    """Capture operating system, Python runtime, and git commit provenance."""
    git_rev = "unknown"
    try:
        git_rev = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        pass
        
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": sys.version,
        "git_commit": git_rev
    }
