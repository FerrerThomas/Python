import streamlit as st
import csv
import pathlib
from datetime import datetime, timedelta

REGISTROS_PATH = pathlib.Path("log_records", "records.csv")
FIELDNAMES = ["Nombre de usuario", "Nombre Completo", "Email", "Fecha de nacimiento", "Genero"]

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

if "game_state" not in st.session_state:
        st.session_state['game_state'] = {
            "questions": False,
        }

# Creo la sesion del juego.
if "game_state" not in st.session_state:
    st.session_state["game_state"] = {
        "user": None,
        "email": None,
    }

def save_form ():
    # Lista para actualizar archivo de registros
    records = []

    # Formulario de registro
    if REGISTROS_PATH.exists():
        with open(REGISTROS_PATH, "r", newline="") as register_arch:
            reader = csv.DictReader(register_arch)
            records = list(reader)
    return records

def write_file (records):
    with open(REGISTROS_PATH, "w", newline="") as register_arch:
            writer = csv.DictWriter(register_arch, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)

# Titulo formulario
gif = pathlib.Path('gifs','formulario.gif')
st.image(str(gif))

with st.form ('questions'):
# Campos del formulario
    username = st.text_input("Nombre de usuario")
    full_name = st.text_input("Nombre Completo")
    email = st.text_input("Email")
    # Defino fecha hace 100 años y hot
    min_date = datetime.now() - timedelta(days=365*100)
    today = datetime.now()
    birth_date = st.date_input("Fecha de nacimiento", min_value=min_date ,max_value=today)

    gender = st.selectbox("Genero", ["Masculino", "Femenino", "Otro"])

# Botón "registrarse"
    if st.form_submit_button ("Registrarse"):
        records = save_form()

        registered_email = False
        
        # Caso en el que el email ya existe, solo se actualizan los campos
        for record in records:
            if record["Email"] == email:
                record.update({"Nombre de usuario": username, "Nombre Completo": full_name,
                                "Fecha de nacimiento": birth_date, "Genero": gender})
                registered_email = True
                write_file(records)
                st.success("¡Usuario actualizado correctamente!")
                break
        
        # Caso en el que el email no existe, se crea y se guarda en records.
        if not registered_email:
            new_record = {"Nombre de usuario": username, "Nombre Completo": full_name,
                            "Email": email, "Fecha de nacimiento": birth_date, "Genero": gender}
            records.append(new_record)
            write_file(records)

            st.success("¡Usuario registrado correctamente!")
        
        # Voy a la pagina de juego.
        st.switch_page('pages/02_Juego.py')
