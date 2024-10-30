import streamlit as st
import pandas as pd
import pathlib
from unidecode import unidecode
import json

GAME_PATH = pathlib.Path("archivos", "games.json")

if "game_state" not in st.session_state:
        st.session_state['game_state'] = {
            "questions": False,
            "state": None,
            "i":0,
            "user_inp":[],
            "user": None,
            "email": None,
            "state" : None,
        }

if st.session_state.game_state['questions']: 

    if st.session_state.game_state['data'] != None:
        
        st.header ("Finalizó su partida")

        correct = 0
        score = 0
        for i in range(5):
            st.header(f"Pregunta {i+1}")
            for clave, valor in st.session_state.game_state['data'][i].items():
                st.write (f"{clave}: {valor}")
            if unidecode(st.session_state.game_state['user_inp'][i].lower()) == unidecode(st.session_state.game_state['data'][i][clave].lower()):
                correct += 1
                st.subheader ("Tu respuesta fue:")
                st.success(st.session_state.game_state['user_inp'][i])
                st.markdown("<hr>",unsafe_allow_html=True)
            else:
                st.subheader ("Tu respuesta fue:")
                st.error(st.session_state.game_state['user_inp'][i])
                st.subheader ("La respuesta correcta era:")
                st.success(st.session_state.game_state['data'][i][clave])
                st.markdown("<hr>",unsafe_allow_html=True)

        if st.session_state.game_state['difficulty'] == "Facil":
            score = correct
        elif st.session_state.game_state['difficulty'] == "Media":
            score = correct * 1.5
        else: 
            score = correct * 2
        
        st.header ('Información de la partida')
        st.write (f"Finalizó: * {st.session_state.game_state['now']}")
        st.write (f"Obtuvo: * {correct} respuestas correctas")
        st.write (f"Obtuvo: * {score} puntos")
        st.markdown("<hr>",unsafe_allow_html=True)

        game = {"usuario": st.session_state.game_state['user'], 
                    "mail": st.session_state.game_state['email'],
                    "genero": st.session_state.game_state['gender'],
                    "fecha": st.session_state.game_state['now'],
                    "dificultad": str(st.session_state.game_state['difficulty']).lower(),
                    "tematica": str(st.session_state.game_state['theme']).lower(),
                    "preguntas_acertadas": correct,
                    "preguntas_no_acertadas": 5 - correct,
                    "puntos": score}

        if GAME_PATH.exists():
            with open(GAME_PATH, 'r') as file:
                games = json.load(file)
                games.append(game) 
        else:
            games = []
            games.append(game)
        try:
            with open(GAME_PATH, "w") as file:
                json.dump(games, file, indent=4)
        except Exception as e: 
            st.write (e)
    st.session_state.game_state['questions'] = False
    st.session_state.game_state['user_inp'] = []
    
try:
    df_ranking = pd.read_json(GAME_PATH)
    gif = pathlib.Path('gifs','ranking.gif')
    st.image(str(gif))
    if len(df_ranking) == 0:
        st.write ("No hay partidas todavia, juega tu primer partida y se el primero en ser reconocido en el top 15!!!.")
    else:
        df_ranking['Puesto'] = df_ranking['puntos'].rank(ascending=False, method="first")
        # Seleccionar las columnas a mostrar
        columns_to_show = ["Puesto","usuario", "puntos", "mail"]
        # Mostrar la tabla
        st.dataframe(df_ranking[columns_to_show].sort_values(by="Puesto").head(15))
except FileNotFoundError:
    st.warning ("No se encontro el archivo de partidas.")