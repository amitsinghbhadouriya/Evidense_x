import pandas as pd

def iterate_chunks(csv_path: str, chunksize: int = 5000):
    for chunk in pd.read_csv(csv_path, chunksize=chunksize):
        yield chunk
