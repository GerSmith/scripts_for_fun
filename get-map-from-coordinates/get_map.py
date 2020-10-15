#!C:\Python38\python.exe
# -*- coding: utf-8 -*-

# Как мгновенно получить любую карту по координатам с помощью Python

# pip install folium

import folium

place = folium.Map(location=[41.894802,12.4853384])

place.save('index.html')
