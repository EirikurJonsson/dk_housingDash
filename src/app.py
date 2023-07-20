from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import json
from utils.getHousingData import getHousingData
from components import createHousingTable

dummypath = './assets/dummydata/response.json'

f = open(dummypath)
data = json.load(f)

df = pd.DataFrame.from_dict(data['results'])

test = getHousingData(asPandas = True, postCode = 5210)
print(len(test))
print(len(test.drop_duplicates(subset = ['guid'])))


app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.SLATE]
    )

app.layout = dbc.Container(
    createHousingTable(df = getHousingData(asPandas = True, postCode = 5210).sort_values('street'))
)

if __name__ == '__main__':
    app.run(debug = True, port = 8051)
