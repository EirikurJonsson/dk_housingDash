from dash import Dash, html, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import json
from utils.getHousingData import getHousingData
from utils.getPlotData import getPlotData
from components.createGeoPlot import createGeoPlot
from components import createHousingTable
import dash_leaflet as dl
import dash_leaflet.express as dlx
import geopandas as gpd


dummypath = './assets/dummydata/response.json'

f = open(dummypath)
data = json.load(f)

df = pd.DataFrame.from_dict(data['results'])
geo = '.\geodata\dkPostnumbers.geojson'
geo = 'src\assets\geodata\dkPostnumbers.geojson'
geo = 'C:/Users/eirikur/projects/dk_housingDash/src/assets/geodata/dkPostnumbers.geojson'
file = open(geo)
test = gpd.read_file(file)

print(test)

#test = getHousingData(asPandas = True, postCode = 5210)

app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.SLATE]
    )

app.layout = html.Div(
    [
        dbc.Input(id = 'POSTNUMBER', placeholder = 'Please input a valid postnumber', type = 'text'),
        html.Div(
            id = 'PLOTHOLDER',
            children=[]
        )
    ]
)

@app.callback(Output('PLOTHOLDER', 'graph'), [Input('POSTNUMBER', 'value')])
def plot(value):
    return createGeoPlot(value)

if __name__ == '__main__':
    app.run(debug = True, port = 8051)
