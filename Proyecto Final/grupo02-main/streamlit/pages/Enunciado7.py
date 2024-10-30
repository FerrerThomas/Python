import streamlit as st 
from streamlit_folium import st_folium
import os
file_path = os.path.join(os.getcwd(), '..', 'modified_datasets', 'lagos_arg_mod.csv')


import pandas as pd
lagos = pd.read_csv(file_path)
lagos['Latitud'] = lagos['Latitud'] * -1
lagos['Longitud'] = lagos['Longitud'] * -1

import folium
def generate_map():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
            location=(-33.457606, -65.346857),
            control_scale=True,
            zoom_start=5,
            name='es',
            tiles=tiles,
            attr=attr 
            )
    return m
def add_marker(row):
    colors_lakes = {"grande": "blue","medio": "green","chico": "yellow"}
    folium.Marker([row['Latitud'], row['Longitud']],popup=row['Nombre'],icon=folium.Icon(color=colors_lakes[row["Sup Tamaño"]])).add_to(mapa)

mapa = generate_map()
lagos.apply(add_marker, axis=1)
st_folium(mapa,width=700, height=800)