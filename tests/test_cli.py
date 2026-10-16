import os
import subprocess
import sys

def test_cli_version():
    env = os.environ.copy()
    src_path = os.path.abspath("src")
    env["PYTHONPATH"] = f"{src_path}{os.pathsep}{env.get('PYTHONPATH', '')}"
    cmd = [sys.executable, "-m", "evidense_x.cli", "--version"]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    assert res.returncode == 0
    assert "Evidense-X" in res.stdout

def test_cli_info():
    env = os.environ.copy()
    src_path = os.path.abspath("src")
    env["PYTHONPATH"] = f"{src_path}{os.pathsep}{env.get('PYTHONPATH', '')}"
    cmd = [sys.executable, "-m", "evidense_x.cli", "info"]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    assert res.returncode == 0
    assert "Research Framework" in res.stdout
