
import dash_leaflet as dl
import dash_leaflet.express as dlx
    

def createGeoPlot(data, style = None):
    return dl.Map(
        children = [
            dl.TileLayer(),
            dl.GeoJSON(
                data = data,
                format = ' geobuf',
                zoomToBounds = True,
                zoomToBoundsOnClick = True,
            )
        ],
        style = style
    )