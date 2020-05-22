import folium
import pandas as pd

def getMap():
    df = pd.read_csv('./us_capital.txt')
    latmean = df['LAT'].mean()
    lonmean = df.LON.mean()


# http://leaflet-extras.github.io/leaflet-providers/preview/

    map = folium.Map(location=[latmean, lonmean], zoom_start=5,
                     tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                     attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')


    for lat,lon,name,val in zip(df['LAT'], df['LON'], df['CITY'] + ' ' + df['STATE'], df.VAL):
        folium.Circle(
            location=[lat, lon],
            popup=name,
            radius=val*100,
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(map)

    return map.get_root().render()

