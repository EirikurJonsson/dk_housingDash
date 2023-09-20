import pandas as pd


def getNumericalStats(df: pd.DataFrame, col: str) -> dict:
    return {
            'mean': round(df[col].mean(), 2),
            'std': round(df[col].std(), 2),
            'median': round(df[col].median(), 2)
            }

def getObjectStats(df: pd.DataFrame, col:str) -> dict:
    return df.groupBy(col).count().to_json()
