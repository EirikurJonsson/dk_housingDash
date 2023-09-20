from dash import Dash, Input, Output, html
import folium
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import pandas as pd
import json

# component imports

from src.components.createMap import createMap
from src.utils.getHousingData import getHousingData
from src.utils.getStats import getNumericalStats, getObjectStats

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
        id = 'mainContainer',
        children = [
            dbc.Row(
                id = 'inputRow',
                children = [
                    html.H1('Tool for Real Estate Buying In Denmark'),
                    dbc.Input(
                        id = 'zipCodeInput',
                        placeholder = 'Enter A Valid Danish Zip Code And Press Enter',
                        debounce = True
                        )
                    ]
                ),
            dbc.Row(
                id = 'toolContainer',
                children = [
                    dbc.Container(
                        id = 'mapContainer',
                        children = [
                            createMap(identity = 'propertyMap')
                            ]
                        )
                    ]
                )
            ]
        )

@app.callback(Output('propertyMap', 'children'), Input('zipCodeInput', 'value'))
def updateMap(input_value):
    df = getHousingData(input_value)
    df = df.dropna(subset = ['images'])
    meanPriceInfo = getNumericalStats(df = df, col = 'price')
    print(meanPriceInfo)

    belowMean = "./assets/belowMean.png"
    belowMedian = './assets/belowMedian.png'
    belowStd = './assets/belowStd.png'
    standardPrice = './assets/standardPrice.png'

    df['priceInfo'] = [belowStd if row['price'] < meanPriceInfo['mean'] - meanPriceInfo['std'] else belowMedian if row['price'] < meanPriceInfo['median'] else belowMean if row['price'] < meanPriceInfo['mean'] else standardPrice  for _, row in df.iterrows()]
    print(df)
    return [
            dl.Marker(
            position = [row['latitude'], row['longitude']],
            children = [
                dl.Tooltip(
                    content = f"""
                    <ol>
                    <li>Street Name : {row['street']}</li>
                    <li>Price : {row['price']}</li>
                    <li>Price Change in % : {row['priceChangePercentTotal']}</li>
                    <li>Energy Class : {row['energyClass']}</li>
                    <li>Rooms : {row['rooms']}</li>
                    <li>Size : {row['size']}</li>
                    <li>Property Size : {row['lotSize']}</li>
                    </ol>
                    """
                    )
                ],
            icon = {
                'iconUrl': row['priceInfo'],
                'iconSize': [20, 20]
                }
            )
            for _, row in df.iterrows()]


if __name__ == '__main__':
    app.run_server(debug = True)

