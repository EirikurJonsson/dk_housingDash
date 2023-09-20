import dash_leaflet as dl
def createMap():
    dl.Map(children = [
        dl.TileLayer()
        ],
        center = [56,10],
        zoom = 6,
        style = {
            'height': '100vh',
            },
        )
    )
