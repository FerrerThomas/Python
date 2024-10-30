import streamlit as st
import os
import pathlib
from datetime import datetime 
from functions import juego as j
import pandas as pd

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

REGISTROS_PATH = os.path.join(os.getcwd(), 'log_records', 'records.csv')
REGISTROS = pathlib.Path("log_records", "records.csv")
CANT_PREG = 5
game = os.path.join(os.getcwd(), '..', 'games', 'game.py')



# Insertar el estilo CSS personalizado para el botón
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
    }
    .stButton > button {
        display: block;
        margin: auto;
        background-color: #75C0CB; /* Fondo del botón */
        color: white;
        padding: 10px 20px;
        font-size: 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: transform 0.2s, background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #A9B6BD; /* Efecto hover */
        color: black; /* Cambiar el color del texto a negro */
        transform: scale(1.1);
    }
    .stButton > button:active {
    color: black; /* Color del texto en negro cuando se hace clic */
    }
    </style>
    """, unsafe_allow_html=True)
# Crear una fila centrada para el botón
st.markdown('<div class="centered">', unsafe_allow_html=True)





# Cargo y muestro el gif del titulo del juego
url_gif_title = "https://text.media.giphy.com/v1/media/giphy.gif?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJwcm9kLTIwMjAtMDQtMjIiLCJzdHlsZSI6ImZsb2F0aWUiLCJ0ZXh0IjoiQmllbnZlbmlkbyUyMGElMjBQeXRyaXZpYSIsImlhdCI6MTcxNjQxNzY2Mn0.lFl7S8Xo8Kdnah_tCXK9KK6LMGL6hMoJKEytRjY5-BM"
st.image(url_gif_title, use_column_width=True)
if st.session_state.game_state['state'] == None:
    try:
        
        df = pd.read_csv(REGISTROS_PATH)
        st.subheader("Seleccion de usuario ya existente")
        # Si hay usuarios registrados
        if  len(df) != 0:
            # Traigo columnas de emails y nombres de usuario
            user_info = df[['Email', 'Nombre de usuario','Genero']]
            # Crea el desplegable de user y los guardo en session_state 
            selected_index = st.selectbox('Selecciona un Usuario', range(len(user_info)), format_func=lambda x: f"Nombre: {user_info.iloc[x]['Nombre de usuario']} - Email: {user_info.iloc[x]['Email']}")
            st.write ('Si no tiene usuario:')
            # Guarda la información seleccionada en session_state.game_state
            st.session_state.game_state["user"] = user_info.iloc[selected_index]['Nombre de usuario']
            st.session_state.game_state["email"] = user_info.iloc[selected_index]['Email']
            st.session_state.game_state["gender"] = user_info.iloc[selected_index]['Genero']
        else:
            st.warning("No hay usuarios registrados, por favor, regístrese.")
            st.write ('Si no tiene usuario:')

    except FileNotFoundError:
        st.warning("No hay usuarios registrados, por favor, regístrese.")
        
    if st.button ('Registrarse'):
        st.switch_page ('pages/03_Formulario.py')

if REGISTROS.exists() and st.session_state.game_state['state'] == None:
# Desplegable temática
    st.session_state.game_state["theme"] = st.selectbox ('Selecciona una temática',['Aeropuertos','Lagos','Conectividad','Censo'])

    # Desplegable dificultad
    st.session_state.game_state["difficulty"] = st.selectbox ('Seleccione la dificultad',['Facil', 'Media', 'Dificil'])
    if st.button('Jugar'):
        st.session_state.game_state["state"] = "GENERAR_PREGUNTA"
        st.rerun()
elif st.session_state.game_state["state"] == "GENERAR_PREGUNTA":
    st.session_state.game_state["state"] = "NUEVO"
    questions = j.filter(st.session_state.game_state["theme"])
    if st.session_state.game_state["difficulty"] == 'Facil':
        st.session_state.game_state['data'] = j.generate_questions_easy(questions)
    elif st.session_state.game_state["difficulty"] == "Media":
        st.session_state.game_state['data'] = j.generate_questions_medium(questions)
    else:
        st.session_state.game_state['data'] = j.generate_questions_hard(questions)
    st.rerun()
elif st.session_state.game_state["state"] == "NUEVO":
    preg = st.session_state.game_state["i"]
    st.header(f"Pregunta {preg+1}")
    with st.form("preguntando"):
        if st.session_state.game_state["difficulty"] == 'Facil':
            respuesta = j.mostrar_facil(st.session_state.game_state['data'],st.session_state.game_state["i"])
            responder = st.form_submit_button("Submit")
        elif st.session_state.game_state["difficulty"] == "Media":
            respuesta = j.mostrar_medio(st.session_state.game_state['data'],st.session_state.game_state["i"])
            responder = st.form_submit_button("Submit")
        else:
            respuesta = j.mostrar_dificil(st.session_state.game_state['data'],st.session_state.game_state["i"])
            responder = st.form_submit_button("Submit")
    if responder:
        if st.session_state.game_state["i"] < CANT_PREG-1:
            st.session_state.game_state["i"]+=1
            st.session_state.game_state["user_inp"].append(respuesta)
            st.session_state.game_state["state"] = "NUEVO"
            st.rerun()
        elif st.session_state.game_state["i"] == CANT_PREG-1:
            st.session_state.game_state["user_inp"].append(respuesta)
            st.session_state.game_state["state"] = "TERMINE"
            st.rerun()
elif st.session_state.game_state["state"] == "TERMINE":
    st.write (st.session_state.game_state["user_inp"])
    st.session_state.game_state['questions'] = True
    st.session_state.game_state['now'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.game_state['state'] = None
    st.session_state.game_state['i'] = 0
    st.switch_page('pages/04_Ranking.py')
