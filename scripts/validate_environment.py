"""Pre-flight script verifying hardware resources and dependencies."""
import sys
import psutil
import platform

def verify_system():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    cpu_count = psutil.cpu_count(logical=True)
    print(f"System: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Python: {sys.version.split()[0]}")
    print(f"CPUs: {cpu_count} cores")
    print(f"RAM: {ram_gb:.1f} GB")
    assert ram_gb >= 2.0, "At least 2GB of RAM is required."
    print("Pre-flight environment validation: PASSED.")

if __name__ == "__main__":
    verify_system()
