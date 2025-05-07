import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna()
    df = df.sort_values(by='trade_date')
    return df.reset_index(drop=True)