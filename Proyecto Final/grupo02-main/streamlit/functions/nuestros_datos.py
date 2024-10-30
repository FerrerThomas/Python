import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go

def show_map_airports(df_airports):
    
    # Creo un mapa con folium (se le manda centro y el zoom)
    map_airports = folium.Map(location=[-34.8222, -58.5358], zoom_start=5)
    
    def add_marker_airports(row):
        """
        folium es un mapa, con .marker le agrego un marcador con los datos: location, popum, icon
        location: toma las cordenadas del aeropueo (longitud y latitud)
        popup: crea una mini ventana cuando pones el mouse arriba del marcador con el nombre del aeropuerto
        icon: crea el icono con el color segun elevation_name (fijarse en en la tupla colors xd)
        .add_to(m): agrega el marcador creado al mapa
        """
        # Colores según elevation_name
        colors_airports = { "bajo": "green", "medio": "orange", "altos": "red","Sin Datos": "pink"}
        folium.Marker(location=[row["latitude_deg"], row["longitude_deg"]], popup=row["name"], icon=folium.Icon(color=colors_airports[row["elevation_name"]])).add_to(map_airports)
        
    tamaños_aeropuertos = df_airports['elevation_name'].unique()

    tamaños_select_airport = st.multiselect("Seleccioné la/s elevacion/es de los aeropuertos a mostrar 🏞️", tamaños_aeropuertos)

    df_filtrado_airport = df_airports[df_airports["elevation_name"].isin(tamaños_select_airport)]
    # itera sobre los aeropuertos y para cada fila (cada aeropuerto) agrega un nuevo marcador segun sus datos
    df_filtrado_airport.apply(add_marker_airports, axis=1) 

    # Muestro el mapa en Streamlit
    st_folium(map_airports, width=700, height=500)

def show_chart_airports(df_airports):
    df_airports_grouped_elevation = df_airports.groupby('elevation_name').size().reset_index(name='count')
    fig = go.Figure(data=[go.Pie(labels=df_airports_grouped_elevation['elevation_name'], values=df_airports_grouped_elevation['count'])])
    fig.update_layout(title_text='Cantidad de aeropuertos por Elevation Name')
    st.plotly_chart(fig)
    
def show_board_airports(df_airports):
    st.write('Cantidad de aeropuertos de cada tipo')
    df_airports_grouped_type = df_airports.groupby('type').size().reset_index(name='Cantidad de este tipo')
    df_airports_grouped_type.columns = ['Tipo de Aropuerto','Cantidad de este tipo']
    st.dataframe(df_airports_grouped_type)

def show_map_lakes(df_lakes):
    
    def add_marker_lakes(row):
        folium.Marker(location=[row["Latitud"], row["Longitud"]], popup=f"{row['Nombre']} ({row['Sup Tamaño']})", icon=folium.Icon(color=colors_lakes[row["Sup Tamaño"]])).add_to(map_lakes)
    
    tamaños_lagos = df_lakes["Sup Tamaño"].unique()
    tamaños_seleccionados = st.multiselect("Che pa aca abajo elegi segun el tamaño que quieras filtrar 🏞️ ", tamaños_lagos)
    df_filtrado = df_lakes[df_lakes["Sup Tamaño"].isin(tamaños_seleccionados)]
    map_lakes = folium.Map(location=[-40, -70], zoom_start=5,max_bounds=True)
    # Limitar el área visible del mapa para excluir las Islas Malvinas
    colors_lakes = {
        "grande": "blue",
        "medio": "green",
        "chico": "yellow"
        }
    df_filtrado.apply(add_marker_lakes, axis=1)
    st_folium(map_lakes, width=700, height=500)
    
def show_chart_lakes(df_lakes):
    df_lakes_grouped_size = df_lakes.groupby('Sup Tamaño').size().reset_index(name='count')
    fig_lakes_size = go.Figure(data=[go.Pie(labels=df_lakes_grouped_size['Sup Tamaño'], values=df_lakes_grouped_size['count'])])
    fig_lakes_size.update_layout(title_text='Cantidad de lagos por el tamaño de la superficie')
    st.plotly_chart(fig_lakes_size)
    
def show_board_lakes(df_lakes):
    df_lakes_grouped_province = df_lakes.groupby('Ubicación').size().reset_index(name='Cantidad de lagos')
    st.write('Cantidad de lagos por ubicacion')
    st.dataframe(df_lakes_grouped_province)