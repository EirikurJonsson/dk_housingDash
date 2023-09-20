import dash_leaflet as dl
def createMap(identity):
    return dl.Map(children = [
        dl.TileLayer(),
        dl.FeatureGroup(id = identity)
        ],
        center = [56,10],
        zoom = 6,
        style = {
            'height': '100vh',
            },
        )
