import folium
import pandas as pd


map4 = folium.Map(location=[40.8979334, -73.885948], zoom_start=15, tiles='Stamen Terrain')
df = pd.read_csv('Volcano.txt')
#create a for loop to use file data to create markers
#we have 2 iterators in this for loop, and so put them in a zip function
#read as iterator, and then where is df to grab that iterators value


for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker(location = [lat, lon], popup=name, icon=folium.Icon(color='cloud')).add_to(map4)

print(map4.save('test4.html'))
