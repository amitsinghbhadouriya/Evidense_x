import os
import subprocess
import sys
import pandas as pd


def test_cli_govern(tmp_path):
    csv_file = tmp_path / "sample.csv"
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df.to_csv(csv_file, index=False)
    
    out_file = tmp_path / "report.md"
    
    env = os.environ.copy()
    src_path = os.path.abspath("src")
    env["PYTHONPATH"] = f"{src_path}{os.pathsep}{env.get('PYTHONPATH', '')}"
    
    cmd = [
        sys.executable,
        "-m",
        "evidense_x.cli",
        "govern",
        "--data",
        str(csv_file),
        "--name",
        "TestModel",
        "--output",
        str(out_file),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    assert res.returncode == 0
    assert "Governance report written to" in res.stdout
    assert os.path.exists(out_file)


def test_cli_stream_audit(tmp_path):
    csv_file = tmp_path / "stream.csv"
    df = pd.DataFrame({"x": [10.0, 20.0, 30.0], "y": [1.0, None, 3.0]})
    df.to_csv(csv_file, index=False)
    
    env = os.environ.copy()
    src_path = os.path.abspath("src")
    env["PYTHONPATH"] = f"{src_path}{os.pathsep}{env.get('PYTHONPATH', '')}"
    
    cmd = [
        sys.executable,
        "-m",
        "evidense_x.cli",
        "stream-audit",
        "--data",
        str(csv_file),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    assert res.returncode == 0
    assert "Stream audit completed" in res.stdout


def test_cli_remediate(tmp_path):
    csv_file = tmp_path / "raw.csv"
    cleaned_file = tmp_path / "cleaned.csv"
    df = pd.DataFrame({"x": [1, 1, 2], "y": [10.0, 10.0, 20.0]})
    df.to_csv(csv_file, index=False)
    
    env = os.environ.copy()
    src_path = os.path.abspath("src")
    env["PYTHONPATH"] = f"{src_path}{os.pathsep}{env.get('PYTHONPATH', '')}"
    
    cmd = [
        sys.executable,
        "-m",
        "evidense_x.cli",
        "remediate",
        "--input-file",
        str(csv_file),
        "--output-file",
        str(cleaned_file),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    assert res.returncode == 0
    assert "Dataset successfully remediated" in res.stdout
    assert os.path.exists(cleaned_file)
