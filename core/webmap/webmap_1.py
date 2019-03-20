import folium

print(dir(folium))

map = folium.Map(location=[40.8979334, -73.885948], zoom_start=7)
print(map)


print(dir(folium.Map))
print(map.save('test.html'))

map2 = folium.Map(location=[40.8979334, -73.885948], zoom_start=15, tiles='Stamen Terrain')
print(map2)
print(map2.save('test2.html'))