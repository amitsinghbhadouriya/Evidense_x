import subprocess
import sys

def test_cli_version():
    cmd = [sys.executable, "-m", "evidense_x.cli", "--version"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert "Evidense-X" in res.stdout

def test_cli_info():
    cmd = [sys.executable, "-m", "evidense_x.cli", "info"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert "Research Framework" in res.stdout
