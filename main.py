import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import geopy.distance
import random
import time

temp = pd.read_csv('schools.csv')
schools_df = temp[temp['regional_unit'] == 'ΠΕΡΙΦΕΡΕΙΑΚΗ Δ/ΝΣΗ Π/ΘΜΙΑΣ ΚΑΙ Δ/ΘΜΙΑΣ ΕΚΠ/ΣΗΣ ΑΤΤΙΚΗΣ'].copy()
# schools_df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lng, df.lat))
schools_df.reset_index(inplace=True, drop=True)
metro_2 = pd.read_csv('output/metro_line_2.csv')
# print(schools_df)

def metro_distance():
    school_records = schools_df.to_dict(orient='records')
    output = []
    for idx, school in schools_df.iterrows():
        t_row = school_records[idx]
        print(t_row)
        print(idx)
        school_coords = (school.lng, school.lat)
        for idj, station in metro_2.iterrows():
            station_coords = (station.lon, station.lat)
            try:
                dist = geopy.distance.distance(station_coords, school_coords).km
                print(station[1])
                t_row[station[1]] = dist
            except ValueError:
                pass
        output.append(t_row)
    return pd.DataFrame.from_records(output)


if __name__ == '__main__':
    # schools_line_2 = metro_distance()
    # schools_line_2.to_csv('output/schools_line_2.csv', index=False)
    df = pd.read_csv('output/schools_line_2.csv')
    temp = df.iloc[:, 18:].copy()
    print(temp.columns)
    print(type(temp))
    print(temp.min(axis='columns'))
    df['min_dist'] = temp.min(axis='columns')
    df.to_csv('output/schools_line_2.csv', index=False)





