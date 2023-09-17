import pandas as pd
import dash_bootstrap_components as dbc

def createHousingTable(df: pd.DataFrame(), cols = None):
    for i in df.columns:
        if i == 'images':
            df.drop('images', axis = 1, inplace = True)

    if cols:
        return dbc.Table.from_dataframe(df.drop(cols, inplace = True))
    elif not cols:
        return dbc.Table.from_dataframe(df)
    else:
        print('No cols selected to be filtered')
        return dbc.Table.from_dataframe(df)
