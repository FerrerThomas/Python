import streamlit as st
import pandas as pd
import os
from functions import nuestros_datos as by

url_gifMapaAeropuertos = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2FrbDBpZjI3ang5MDlwYThkdHZkcm91ODZxOHhxbzhwZTluNXduaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AvfE26mAgn0g3eSdeJ/giphy.gif"
url_gifMapaLagos = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTduNjc4a2hsaGEyaGZ1Nm14dmJ2bDQ5N2MwM3J2cnNyMnF5cnJldyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SSWIUR4BPNkBfyXbk6/giphy.gif"

st.image(url_gifMapaAeropuertos, use_column_width=True)

#traigo lo de aeropuertos
file_path = os.path.join(os.getcwd(), '..', 'modified_datasets', 'ar-airports_mod.csv')
df_airports = pd.read_csv(file_path)

#traigo lo de lagos
lakes = os.path.join(os.getcwd(), '..', 'modified_datasets', 'lagos_arg_mod.csv')
df_lakes = pd.read_csv(lakes)

#muestro lo de aeropuertos       
by.show_map_airports(df_airports)
by.show_chart_airports(df_airports)
by.show_board_airports(df_airports)

st.write('')
st.write('')
st.write('-----------------------------------------------------------')
st.write('')
st.write('')

st.image(url_gifMapaLagos, use_column_width=True)

#pongo latitud y longitud en negativo porque quedo con un error (deberia ser negativo)
df_lakes['Latitud'] = df_lakes['Latitud'] * -1
df_lakes['Longitud'] = df_lakes['Longitud'] * -1

#muestro lo de lagos
by.show_map_lakes(df_lakes)
by.show_chart_lakes(df_lakes)
by.show_board_lakes(df_lakes)

st.write('Las Islas Malvinas son y siempre seran Argentinas 🩵🤍🩵')
