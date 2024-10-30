import streamlit as st
from pathlib import Path

st.title("Bienvenido a PYTRIVIA")
url_gif = "https://images-ext-1.discordapp.net/external/WY6ztGuMrqQLXIgQXtI6a1Ct6W-Z4tpUwnF5asb2268/https/i.pinimg.com/originals/5d/2d/f2/5d2df2d7c05e7457d63a6e630d1cd469.gif?width=600&height=414"
st.image(url_gif, use_column_width=True)


button1, button2, button3, button4= st.columns(4)

# Botón de descripción
with button1:
    desc = st.button("Descripcion")
# Botón de datos sobre la aplicación
with button2:
    info = st.button("Datos")   
# Botón  de instrucciones para jugar
with button3:
    inst = st.button("Instrucciones")
with button4:
    dif = st.button("Dificultades")
    

if desc:
    st.header("Descripcion Del Juego")
    st.write("""
        PyTrivia es un juego de preguntas y respuestas diseñado principalmente en el lenguaje de programación Python. Su nombre refleja tanto su implementación técnica como su formato de trivia basado en cuatro temáticas clave.    
        Las categorías que componen esta trivia son:
        \n- Aeropuertos de Argentina
        \n- Lagos de Argentina
        \n- Conectividades en Argentina
        \n- Censo Poblacional en Argentina
    \nCada temática ofrece una oportunidad para aprender y divertirse mientras se exploran diferentes aspectos de Argentina.
    """)

if info:
    st.header("Datos Requeridos")
    st.write("""
    Para comenzar a jugar, el usuario debe registrarse proporcionando los siguientes datos:
        \n- Nombre de Usuario
        \n- Nombre Completo
        \n- Género
        \n- Email
        \n- Fecha de Nacimiento
    """)     

if inst:
    st.header("Instrucciones Básicas")
    st.write("""
    Una vez registrado, el usuario puede comenzar a jugar haciendo clic en el apartado del menú llamado "Juego". A continuación, se le pedirá que seleccione:
        \n- Su Usuario (Si no dispone de uno podrá presionar REGISTRARSE)
        \n- Una Temática
        \n- Una Dificultad
    \nDespués de realizar todas las selecciones, el usuario puede presionar el botón "Jugar". Esto lo llevará a una nueva página donde podrá ver y responder las preguntas de la trivia. 
    Una vez que haya respondido todas las preguntas, se le mostraran los resultados y podra ver el ranking y la posición en la que quedó.
    """)

if dif:
    st.header("Dificultades Del Juego")
    st.write("""
             El juego cuenta con tres dificultades:
             \n- **Fácil:** Se proporciona como ayuda la primer y última letra de cada palabra de la respuesta a la pregunta dada, cada respuesta correcta suma 1 punto.
             \n- **Medio:** Se proporciona como ayuda la cantidad de palabras que contiene la respuesta a la pregunta dada, cada respuesta correcta suma 1.5 puntos.
             \n- **Difícil:** No se proporcionan ayudas, cada respuesta correcta suma 2 puntos.
             \nEl jugador podrá seleccionar la dificultad deseada antes de iniciar el juego.
             """)
st.markdown("<hr>",unsafe_allow_html=True)

st.header("Integrantes")
int1,int2,int3,int4 = st.columns(4)
with int1:
        st.write("**Facundo Peri**")
with int2:
        st.write("**Martin Stampone**")
with int3:
        st.write("**Tomás Ferrer**")
with int4:
        st.write("**Aixa Charif**")

st.markdown("<hr>",unsafe_allow_html=True)

st.header("Páginas")
pag1, pag2, pag3, pag4, pag5= st.columns(5)
with pag1:
    our_data = st.button("Datos",key="buttonData")
with pag2:
    game = st.button("Juego")
with pag3:
    form = st.button("Formulario")
with pag4:
    rank = st.button("Ranking")
with pag5:
    stats = st.button("Estadisticas")

if our_data:
    st.switch_page('pages/01_NuestrosDatos.py')
if game:
    st.switch_page('pages/02_Juego.py')
if form:
    st.switch_page('pages/03_Formulario.py')
if rank:
    st.switch_page('pages/04_Ranking.py')
if stats:
    st.switch_page('pages/05_Estadisticas.py')
    
st.markdown("""
    <style>
    .centered, img, h1, h2, h3{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stButton > button {
        display: block;
        margin: auto;
        background-color: #75C0CB; /* Fondo del botón */
        color: white;
        padding: 10px 20px;
        width:95%;
        font-size: 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: transform 0.2s, background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #A9B6BD; /* Efecto hover */
        color: white; /* Cambiar el color del texto a negro */
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)
