import pandas as pd
from keplergl import KeplerGl

data = pd.read_csv("output/schools_line_2.csv")

data.rename(columns={"lat": "Latitude", "lng": "Longitude"}, inplace=True)
print(data.columns)
w1 = data.to_dict(orient="records")
# map = KeplerGl(data=w1)
