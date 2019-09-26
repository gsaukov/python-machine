import folium
import pandas as pd

def getMap():
    df = pd.read_csv('Volcano.txt')
    latmean = df['LAT'].mean()
    lonmean = df.LON.mean()

    map5 = folium.Map(location=[latmean, lonmean], zoom_start=5, tiles='Stamen Terrain')

    def color(elev):
        if elev in range(0, 1000):
            col='green'
        elif elev in range(1001, 1999):
            col='blue'
        elif elev in range(2000, 2999):
            col='orange'
        else:
            col = 'red'
        return col

    for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df.ELEV):
            folium.Marker(location = [lat, lon], popup=name, icon=folium.Icon(color=color(elev))).add_to(map5)

    return map5.get_root().render()

