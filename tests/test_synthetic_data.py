from evidense_x.data.synthetic import generate_synthetic_benchmark

def test_synthetic():
    df = generate_synthetic_benchmark(n_samples=50, n_features=4)
    assert len(df) == 50
    assert "target" in df.columns
