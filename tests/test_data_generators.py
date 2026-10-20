"""Unit tests for synthetic dataset generators and preflight sanitizers."""
from evidense_x.data.synthetic_generator import SyntheticDefectDatasetGenerator
from evidense_x.data.multimodal_generator import MultiModalTabularGenerator
from evidense_x.data.sanitizer import DatasetPreflightSanitizer

def test_synthetic_generator():
    gen = SyntheticDefectDatasetGenerator(n_samples=50, n_features=5, random_state=42)
    X, y = gen.generate()
    assert len(X) == 50
    assert X.shape[1] == 5
    assert len(y) == 50

def test_multimodal_generator():
    gen = MultiModalTabularGenerator(n_samples=40, random_state=42)
    df = gen.generate()
    assert len(df) == 40
    assert "annual_income" in df.columns
    assert "education" in df.columns

def test_sanitizer():
    sanitizer = DatasetPreflightSanitizer()
    df, log = sanitizer.sanitize(SyntheticDefectDatasetGenerator(n_samples=20).generate()[0])
    assert len(df) == 20
