from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import json
from utils.getHousingData import getHousingData
from components import createHousingTable
import dash_leaflet as dl
import dash_leaflet.express as dlx

dummypath = './assets/dummydata/response.json'

f = open(dummypath)
data = json.load(f)

df = pd.DataFrame.from_dict(data['results'])
geo = dlx.dicts_to_geojson('./geodata/dkPostnumbers.geojson')
geo_json = dl.GeoJSON(data = geo)

#test = getHousingData(asPandas = True, postCode = 5210)

app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.SLATE]
    )

app.layout = dbc.html(
    [
        dbc.Container(
            createHousingTable(df)
    ),
    dl.Map(
        [
            dl.TileLayer(), geo_json
        ]
    )
    ]
) 

if __name__ == '__main__':
    app.run(debug = True, port = 8051)
