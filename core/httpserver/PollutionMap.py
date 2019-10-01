import folium
from folium.plugins import HeatMap
import pandas as pd

def getMap():
    df = pd.read_csv('us_national_parks.txt')
    latmean = df['LAT'].mean()
    lonmean = df.LON.mean()
    max_val = float(df.VAL.max())

    map = folium.Map(location=[latmean, lonmean], zoom_start=5, tiles='stamentoner')



    heat = HeatMap( list(zip(df.LAT.values, df.LON.values, df.VAL.values)),
                       min_opacity=0.2,
                       max_val=max_val,
                       radius=17, blur=15,
                       max_zoom=1,
                       )

    map.add_child(heat)

    return map.get_root().render()
