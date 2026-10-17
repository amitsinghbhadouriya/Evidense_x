import hashlib
import pandas as pd

def compute_dataframe_checksum(df: pd.DataFrame) -> str:
    serialized = pd.util.hash_pandas_object(df).values
    return hashlib.sha256(serialized).hexdigest()
