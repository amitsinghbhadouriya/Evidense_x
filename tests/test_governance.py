import pandas as pd
from evidense_x.governance import (
    ModelCardGenerator,
    CryptographicProvenanceTracker,
    EUAIActRiskClassifier,
    GovernanceExportSuite,
)


def test_model_card_generator():
    generator = ModelCardGenerator(model_name="DefectAuditedXGB")
    generator.set_metrics({"auc_roc": 0.88, "ece": 0.03})
    generator.set_defects(["DuplicateLeakage", "MARMissingness"])
    
    card_dict = generator.generate_dict()
    assert card_dict["model_details"]["name"] == "DefectAuditedXGB"
    assert card_dict["evaluated_metrics"]["auc_roc"] == 0.88
    
    md = generator.generate_markdown()
    assert "# Model Card: DefectAuditedXGB" in md
    assert "DuplicateLeakage" in md


def test_cryptographic_provenance_tracker():
    df = pd.DataFrame({"feat1": [1.0, 2.0, 3.0], "feat2": [4, 5, 6]})
    tracker = CryptographicProvenanceTracker()
    event = tracker.record_stage("initial_ingestion", df)
    
    assert event["stage_name"] == "initial_ingestion"
    assert tracker.verify_integrity(df, event["fingerprint"])
    
    modified_df = df.copy()
    modified_df.iloc[0, 0] = 99.0
    assert not tracker.verify_integrity(modified_df, event["fingerprint"])


def test_eu_ai_act_risk_classifier():
    # Clean dataset
    df_clean = pd.DataFrame({"a": range(100), "b": range(100)})
    classifier = EUAIActRiskClassifier()
    rec_clean = classifier.evaluate_compliance(df_clean)
    assert rec_clean.risk_tier == "Low"
    
    # Contaminated with duplicates
    df_dup = pd.DataFrame({"a": [1] * 50 + list(range(50)), "b": [2] * 50 + list(range(50))})
    rec_dup = classifier.evaluate_compliance(df_dup)
    assert rec_dup.risk_tier in ["Moderate", "High"]
    assert len(rec_dup.identified_defects) > 0
    
    # Exporters test
    json_ld = GovernanceExportSuite.to_json_ld(rec_dup)
    assert "https://schema.org" in json_ld
    html = GovernanceExportSuite.to_html(rec_dup)
    assert "Governance Certificate" in html
