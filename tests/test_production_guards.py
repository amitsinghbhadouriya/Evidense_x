"""Unit tests for deployment gatekeepers and schema integrity guards."""
import pandas as pd
from evidense_x.production.leakage_guard import DeploymentLeakageGatekeeper
from evidense_x.production.schema_guard import SchemaIntegrityGuard

def test_deployment_gatekeeper():
    gate = DeploymentLeakageGatekeeper(max_allowed_leakage_rate=0.01)
    pass_report = {"exact_leakage_rate": 0.005}
    fail_report = {"exact_leakage_rate": 0.05}
    assert gate.evaluate_gate(pass_report)["gate_passed"] is True
    assert gate.evaluate_gate(fail_report)["gate_passed"] is False

def test_schema_integrity_guard():
    guard = SchemaIntegrityGuard(expected_dtypes={"a": "int64", "b": "float64"})
    df = pd.DataFrame({"a": [1, 2], "b": [3.0, 4.0]})
    res = guard.validate(df)
    assert res["valid"] is True
