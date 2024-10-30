import streamlit as st
import random
import string
import os
import pandas as pd
import pathlib



data_info = {
    'Aeropuertos': {
        'file_name': 'ar-airports_mod.csv',
        'columns': ['type', 'name', 'country_name', 'region_name', 'municipality']
    },
    'Lagos': {
        'file_name': 'lagos_arg_mod.csv',
        'columns': ['Nombre', 'Ubicación' ,'Superficie (km²)', 'Sup Tamaño']
    },
    'Conectividad': {
        'file_name': 'conectividad_internet_modificado.csv',
        'columns': ['Provincia', 'Partido', 'Localidad', 'Poblacion', 'posee_conectividad']
    },
    'Censo': {
        'file_name': 'censo_poblacion_2022.csv',
        'columns': ['Jurisdicción', 'Total de población', 'Población en viviendas particulares', 'Población en viviendas colectivas (¹)', 'Población en situación de calle(²)', 'Varones Total de población', 'Mujeres Total de población']
    }
}

def filter (theme):
    """
    Usando pandas filtra un csv dependiendo la temática; Genera 5 preguntas eligiendo de forma random 5 filas y 3 columnas del csv.

    Recibe: 
    theme: Cadena de texto que representa la temática elegida por el usuario.

    Retorna: Un DataFrame de pandas que contiene las 5 preguntas aleatorias.
    """
    # Traigo la información del tema seleccionado
    theme_info = data_info[theme]

    # Guardo path
    file_path = os.path.join(os.getcwd(), '..', 'modified_datasets', theme_info['file_name'])

    # Leo archivo csv
    df = pd.read_csv(file_path)

    # Filtro para quedarme con 4 columnas random
    df_filtered = df[random.sample(theme_info['columns'], 4)]

    # Devuelvo 5 filas random del dataframe filtrado de 4 columnas
    return df_filtered.sample(n=5)


def generate_questions_easy(df):
    data = []
    for i in range(len(df)):
        row = df.iloc[i]
        columns = list(df.columns)
        st.subheader(f"Pregunta {i+1}")
        column_random = random.choice(columns)  # Elige una columna al azar
        columns.remove(column_random)  # Elimina la columna elegida de la lista
        pregunta_respuesta_dict = {}
        for column in columns:
            st.markdown(f"**{column}:** {row[column]}")
            pregunta_respuesta_dict[column] = row[column]
        # Convierte el valor a cadena antes de procesarlo
        original_answer = str(row[column_random])
            
        pregunta_respuesta_dict[column_random] = original_answer
        # Agregar el diccionario a la lista en el estado de la sesión
        data.append(pregunta_respuesta_dict)
    return data

# Genero preguntas para dificultad Media
def generate_questions_medium(df):
    data = []
    for i in range(len(df)):
        row = df.iloc[i]
        columns = list(df.columns)
        st.subheader(f"Pregunta {i+1}")
        column_random = random.choice(columns)  # Elige una columna al azar
        original_answer = str(row[column_random])
        columns.remove(column_random)  # Elimina la columna elegida de la lista
        pregunta_respuesta_dict = {}
        for column in columns:
            st.markdown(f"**{column}:** {row[column]}")
            pregunta_respuesta_dict[column] = row[column]

        pregunta_respuesta_dict[column_random] = original_answer

        # Agregar el diccionario a la lista en el estado de la sesión
        data.append(pregunta_respuesta_dict)
    return data

def generate_questions_hard(df):
    data = []
    for i in range(5):
        row = df.iloc[i]
        columns = list(df.columns)
        column_random = random.choice(columns)  # Elige una columna al azar
        columns.remove(column_random)  # Elimina la columna elegida de la lista
        pregunta_respuesta_dict = {}
        
        for column in columns:
            st.markdown(f"**{column}:** {row[column]}")
            pregunta_respuesta_dict[column] = row[column]

        original_answer = str(row[column_random])
        
        # Agregar la respuesta correcta y la entrada del usuario al diccionario
        pregunta_respuesta_dict[column_random] = original_answer

        # Agregar el diccionario a la lista en el estado de la sesión
        data.append(pregunta_respuesta_dict)
    return data

def mostrar_facil (data,index):
    ix = 0
    for clave, valor in data[index].items():
        if ix < 3:
            st.write (f"{clave}: {valor}")
            ix += 1
        else: 
            hidden_answer = ' '.join(['_'*len(word) if len(word) <= 2 else word[0] + '_ '*(len(word)-2) + word[-1] for word in valor.split()])
            return st.text_input(f"{clave}:{hidden_answer}")

def mostrar_medio (data,index):
    ix = 0
    for clave, valor in data[index].items():
        if ix < 3:
            st.write (f"{clave}: {valor}")
            ix += 1
        else: 
            number_of_words = len(valor.split())
            # Informa al usuario la cantidad de palabras
            st.info(f"La respuesta tiene {number_of_words} palabras.")
            return st.text_input(f"{clave}:")
    
def mostrar_dificil (data,index):
    ix = 0
    for clave, valor in data[index].items():
        if ix < 3:
            st.write (f"{clave}: {valor}")
            ix += 1
        else: 
            return st.text_input(f"{clave}:")
    
