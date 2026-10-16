import pytest
from evidense_x.data.loaders import DatasetLoader
from evidense_x.data.schemas import DatasetSchema

def test_schema_instantiation():
    schema = DatasetSchema(name="Test", target_column="target", numeric_features=["a", "b"])
    assert schema.name == "Test"
    assert len(schema.numeric_features) == 2

def test_red_wine_loader():
    df, schema = DatasetLoader.load_red_wine()
    assert len(df) == 1599
    assert schema.target_column == "target"
    assert "target" in df.columns
