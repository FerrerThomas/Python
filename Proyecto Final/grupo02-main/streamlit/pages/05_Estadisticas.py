import json
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from functions import estadisticas as est

reader = Path('archivos','games.json')
# seteo titulo e icono de la pagina del navegador
st.set_page_config(page_title="Estadísticas de Partidas", page_icon="📊")

gif = Path('gifs','estadisticas.gif')
st.image(str(gif))


try:
    with reader.open(mode='r', encoding='utf-8') as f:
        games = json.load(f)

    # creo el dataframe de partidas
    df = pd.DataFrame(games)

    # Convertir la columna de fechas
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    est.initialize_charts()
    est.chart_glender(df)
    est.chart_point(df)
    est.chart_day_week(df)
    est.chart_average_month(df)
    est.chart_top_users(df)
    est.chart_errors_theme(df)
    est.chart_two_users_comparison(df)
    est.chart_theme_gender(df)
    est.chart_difficulty(df)
    est.chart_streak(df)
        
except FileNotFoundError:
    st.warning("No se jugaron partidas")
