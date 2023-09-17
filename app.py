from dash import Dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import pandas as pd
import json


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

f = open('./tmp/data/housingMap.json')

data = json.load(f)

marker = []
for indx, dic in enumerate(data['results']):
    marker.append(dl.Marker(
        position = [dic['latitude'], dic['longitude']],
        children = [
            dl.Tooltip(
                content = f"""<ol>
                <li>Address: {dic['street']}</li>
                <li>Price: {dic['price']}</li>
                <li>Price Change: {dic['priceChangePercentTotal']}</li>
                <li>Energy Class: {dic['energyClass']}</li>
                </ol>"""
                )
            ]
        ))

app.layout = dbc.Container(
        dl.Map([
            dl.TileLayer(),
            dl.FeatureGroup(marker),
            ],
            center = [56,10],
            zoom = 6,
            style = {
                'height': '100vh',
                'width': '120vh'
                },
            )
        )

if __name__ == '__main__':
    app.run_server(debug = True)

