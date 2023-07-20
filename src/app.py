from dash import Dash
import pandas as pd
import json

dummypath = './assets/dummydata/response.json'

f = open(dummypath)
data = json.load(f)

df = pd.DataFrame.from_dict(data['results'])
print(df)


