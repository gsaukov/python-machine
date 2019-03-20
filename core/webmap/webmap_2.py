import folium
map3 = folium.Map(location=[40.8979334, -73.885948], zoom_start=15, tiles='Stamen Terrain')
location=[40.8979334, -73.885948]
folium.Marker([40.8979334, -73.885948], 'I am so lost', icon=folium.Icon(icon='cloud')).add_to(map3)

folium.Marker(location = [40.8895439, -73.9015249], popup='But i can see you', icon=folium.Icon(color='green')).add_to(map3)

print(map3.save('test3.html'))
