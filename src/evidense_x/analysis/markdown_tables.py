import pandas as pd

def dataframe_to_markdown(df: pd.DataFrame) -> str:
    return df.to_markdown(index=False)
