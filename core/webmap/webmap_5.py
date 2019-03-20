import folium
import pandas as pd

map5 = folium.Map(location=[40.8979334, -73.885948], zoom_start=15, tiles='Stamen Terrain')
df = pd.read_csv('Volcano.txt')
#create a for loop to use file data to create markers
#we have 2 iterators in this for loop, and so put them in a zip function
#read as iterator, and then where is df to grab that iterators value

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

print(map5.save('test6.html'))
