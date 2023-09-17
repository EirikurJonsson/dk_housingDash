import geopandas as gpd
from utils import makeHousingDataRequest

def getPlotData(postnumber: int):

    """
    This is very specific since it only returns a single thing - might need to add the gethousing data to this dataframe

    TODO: Add getHousingData to this dataframe
    """

    path = '../assets/geodata/dkPostnumbers.geojson'
    data = gpd.read_file(path)
    return data[data['POSTNR_TXT'] == str(postnumber)].to_json()

