import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def initialize_charts():
    if 'show_chart_gender' not in st.session_state:
        st.session_state.show_chart_gender = False
    if 'show_chart_points' not in st.session_state:
        st.session_state.show_chart_points = False
    if 'show_chart_day_week' not in st.session_state:
        st.session_state.show_chart_day_week = False  
    if 'show_chart_average_month' not in st.session_state:
        st.session_state.show_chart_average_month = False
    if 'show_chart_top_users' not in st.session_state:
        st.session_state.show_chart_top_users = False
    if 'show_chart_errors_theme' not in st.session_state:
        st.session_state.show_chart_errors_theme = False    
    if 'show_chart_two_users_comparison' not in st.session_state:
        st.session_state.show_chart_two_users_comparison = False
    if 'show_chart_theme_gender' not in st.session_state:
        st.session_state.show_chart_theme_gender = False    
    if 'show_chart_difficulty' not in st.session_state:
        st.session_state.show_chart_difficulty = False
    if 'show_chart_streak' not in st.session_state:
        st.session_state.show_chart_streak = False

def chart_glender(df):
    st.title("Cantidad de usuario por genero")
    # Boton para mostrar/ocultar el grafico de generos 
    if st.button('Mostrar/Ocultar Gráfico 1'):
        st.session_state.show_chart_gender = not st.session_state.show_chart_gender

    # Creo el gráfico de torta por género si el estado es true
    if st.session_state.show_chart_gender:
        # Filtrar usuarios únicos y contar por género
        users_gender = df[['usuario','mail', 'genero']].drop_duplicates()
        total_users = len(users_gender)
        # Contar usuarios por género
        gender_count = users_gender['genero'].value_counts().reset_index()
        gender_count.columns = ['genero', 'conteo'] # cambio index por genero y genero por conteo

        # creo el graficod e torta en plotly
        fig_gender = go.Figure(data=[go.Pie(labels=gender_count['genero'], values=gender_count['conteo'], hole=.3)])
        fig_gender.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=['#ff9999', '#66b3ff'], line=dict(color='#000000', width=2)))
        fig_gender.update_layout(title_text=f'Usuarios totales: {total_users}', title_x=0.1)
        # muestro el grafico en streamlit
        st.plotly_chart(fig_gender)
        
def chart_point(df):
    st.title("Puntuación Superior a la Media")
    # Boton para mostrar/ocultar el grafico de puntos
    if st.button('Mostrar/Ocultar Gráfico 2'):
        st.session_state.show_chart_points = not st.session_state.show_chart_points

    # Crear el gráfico de torta por puntuación si el estado es True
    if st.session_state.show_chart_points:
        # Calcular la puntuación media
        average_points = df['puntos'].mean()

        # Clasificar partidas según si la puntuación es superior a la media
        df['superior_media'] = df['puntos'] > average_points

        # Contar partidas por clasificación
        points_count = df['superior_media'].value_counts().reset_index()
        points_count.columns = ['superior_media', 'conteo']
        points_count['valores'] = points_count['superior_media'].map({True: 'Superior a la media', False: 'Inferior a la media'})

        # Crear gráfico de torta con Plotly
        fig_points = go.Figure(data=[go.Pie(labels=points_count['valores'], values=points_count['conteo'], hole=.3)])
        fig_points.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=['#ffcc99', '#99ccff'], line=dict(color='#000000', width=2)))
        fig_points.update_layout(title_text=f'Puntuacion Media: {average_points:.2f}', title_x=0.1)
        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig_points)
    
def chart_day_week(df):
    st.title('Partidas realizadas por cada dia de la semana')
    if st.button('Mostrar/Ocultar Gráfico 3'):
        st.session_state.show_chart_day_week = not st.session_state.show_chart_day_week

    # Crear el gráfico de barras por día de la semana si el estado es True
    if st.session_state.show_chart_day_week:
        # Agregar una columna con el día de la semana
        df['dia_semana'] = df['fecha'].dt.day_name()
        days_week_spanish = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miércoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'}
        df['dia_semana'] = df['dia_semana'].map(days_week_spanish)
        # Contar partidas por día de la semana
        day_week_count = df['dia_semana'].value_counts().reindex(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']).reset_index()
        day_week_count.columns = ['dia_semana', 'conteo']

        # Crear gráfico de barras con Plotly
        fig_day_week = px.bar(day_week_count, x='dia_semana', y='conteo', labels={'dia_semana': 'Día de la Semana', 'conteo': 'Cantidad de Partidas'}, title='Partidas por Día de la Semana')

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig_day_week)

def chart_average_month(df):
    st.title('Promedio de preguntas acertadas mensuales entre dos fechas')
    date_min = df['fecha'].min()
    date_max = df['fecha'].max()
    # Inputs para seleccionar el rango de fechas
    date_start = st.date_input("Fecha de inicio", min_value=date_min, max_value=date_max, value=date_min)
    date_end = st.date_input("Fecha de fin", min_value=date_min, max_value=date_max, value=date_max)

    # Convertir las fechas ingresadas por el usuario a tipo datetime64[ns]
    date_start = pd.to_datetime(date_start)
    date_end = pd.to_datetime(date_end)

    # Botón para mostrar/ocultar el gráfico de promedio mensual
    if st.button('Mostrar/Ocultar Gráfico 4'):
        st.session_state.show_chart_average_month = not st.session_state.show_chart_average_month

    # Crear el gráfico de barras por promedio de preguntas acertadas mensuales si el estado es True
    if st.session_state.show_chart_average_month:
        # Filtrar el DataFrame por el rango de fechas seleccionado
        df_date_filter = df[(df['fecha'].dt.date >= date_start.date()) & (df['fecha'].dt.date <= date_end.date())]

        # Agrupar por mes y calcular el promedio de preguntas acertadas
        average_month = df_date_filter.resample('M', on='fecha')['preguntas_acertadas'].mean()

        # Crear el gráfico de barras con Plotly
        fig_average_month = px.bar(x=average_month.index.strftime('%B'), y=average_month.values,
                                    labels={'x': 'Mes', 'y': 'Promedio de Preguntas Acertadas'},
                                    title='Promedio de Preguntas Acertadas Mensuales')
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_average_month)

def chart_top_users(df):
    # Calculo la fecha mínima y máxima en el DataFrame
    date_min = df['fecha'].min()
    date_max = df['fecha'].max()

    st.title('Top 10 de usuarios con más puntos acumulados')
    # Inputs para el rango de fechas
    date_start_top = st.date_input("Fecha de inicio para el Top 10 usuarios", value=date_min, min_value=date_min, max_value=date_max)
    date_end_top = st.date_input("Fecha de fin para el Top 10 usuarios", value=date_max, min_value=date_min, max_value=date_max)

    if st.button('Mostrar/Ocultar Gráfico 5'):
        st.session_state.show_chart_top_users = not st.session_state.show_chart_top_users

    if st.session_state.show_chart_top_users:

        # Filtrar datos por el rango de fechas
        df_top_users = df[(df['fecha'].dt.date >= pd.to_datetime(date_start_top).date()) & (df['fecha'].dt.date <= pd.to_datetime(date_end_top).date())]

        # Calcular los puntos acumulados por usuario
        accumulated_points = df_top_users.groupby('usuario')['puntos'].sum().reset_index()
        accumulated_points = accumulated_points[(accumulated_points['puntos'] > 0)]
        # Obtener el Top 10 de usuarios con más puntos
        top_10_users = accumulated_points.sort_values(by='puntos', ascending=False).head(10)

        # Crear el gráfico de barras
        fig_top_users = px.bar(top_10_users, x='usuario', y='puntos', labels={'usuario': 'Usuario', 'puntos': 'Puntos Acumulados'}, title='Top 10 Usuarios con más Puntos Acumulados')
        st.plotly_chart(fig_top_users)

def chart_errors_theme(df):
    st.title('Tematica por dificultad (errores en respuestas)')
    if st.button('Mostrar/Ocultar Gráfico 6'):
        st.session_state.show_chart_errors_theme = not st.session_state.show_chart_errors_theme
        
    if st.session_state.show_chart_errors_theme:
        # Calcular el número de errores por temática
        theme_errors = df.groupby('tematica')['preguntas_no_acertadas'].sum().reset_index()

        # Ordenar las temáticas por el número de errores en orden descendente
        theme_errors = theme_errors.sort_values(by='preguntas_no_acertadas', ascending=False)

        # Crear gráfico de barras con Plotly
        fig_theme_errors = px.bar(theme_errors, x='tematica', y='preguntas_no_acertadas',
                                    labels={'tematica': 'Temática', 'preguntas_no_acertadas': 'Número de Errores'},
                                    title='Temáticas Ordenadas por Número de Errores')
        st.plotly_chart(fig_theme_errors)

def chart_two_users_comparison(df):
    st.title('Comparación de evolución del puntaje de usuarios')

    users = df[['mail']].drop_duplicates()
    user_1 = st.selectbox('Selecciona el mail del primer user', users['mail'], key='usuario_1')
    user_2 = st.selectbox('Selecciona el mail del segundo usuario', users['mail'], key='usuario_2') 

    if st.button('Mostrar/Ocultar Gráfico 7'):
        st.session_state.show_chart_two_users_comparison = not st.session_state.show_chart_two_users_comparison
            
    if st.session_state.show_chart_two_users_comparison:
        if user_1 and user_2:
            df_users = df[df['mail'].isin([user_1, user_2])].copy()
            df_users = df_users.sort_values(by='fecha')
            
            fig_compare_users = px.line(df_users, x='fecha', y='puntos', color='usuario', markers=True,
                                    labels={'fecha': 'Fecha', 'puntos': 'Puntaje'},
                                    title='Evolución del Puntaje a lo Largo del Tiempo')
            st.plotly_chart(fig_compare_users)

def chart_theme_gender(df):
    st.title('Temática con mayor conocimiento por género')
    if st.button('Mostrar/Ocultar Gráfico 8'):
        st.session_state.show_chart_theme_gender = not st.session_state.show_chart_theme_gender

    if st.session_state.show_chart_theme_gender:
        theme_by_genero = df.groupby(['genero', 'tematica'])['preguntas_acertadas'].mean().reset_index()
        theme_max = theme_by_genero.loc[theme_by_genero.groupby('genero')['preguntas_acertadas'].idxmax()]
        fig_theme_by_genero = px.bar(theme_max, x='genero', y='preguntas_acertadas', color='tematica',
                                    labels={'genero': 'Género', 'preguntas_acertadas': 'Promedio de Preguntas Acertadas', 'tematica': 'Temática'},
                                    title='Temática con Mayor Conocimiento por Género')
        st.plotly_chart(fig_theme_by_genero)

def chart_difficulty(df):
    st.title('Dificultades y sus estadisticas')
    if st.button('Mostrar/Ocultar Gráfico 9'):
        st.session_state.show_chart_difficulty = not st.session_state.show_chart_difficulty

    if st.session_state.show_chart_difficulty:        
        difficulty_stats = df.groupby('dificultad').agg({'puntos': ['mean', 'count']}).reset_index()
        difficulty_stats.columns = ['dificultad', 'puntaje_promedio', 'cantidad'] 
        fig_difficulty = px.bar(difficulty_stats, x='dificultad', y='puntaje_promedio', text='cantidad', 
                                labels={'dificultad': 'Dificultad', 'puntaje_promedio': 'Puntaje Promedio'},
                                title='Puntaje Promedio y Cantidad de Elecciones por Dificultad')

        fig_difficulty.update_traces(texttemplate='%{text}', textposition='outside')  
        st.plotly_chart(fig_difficulty) 
    
def chart_streak(df):
    st.title('Usuarios en racha de los ultimos 7 dias')
    if st.button('Mostrar/Ocultar Gráfico 10'):
        st.session_state.show_chart_streak = not st.session_state.show_chart_streak

    if st.session_state.show_chart_streak:
        # Calcular la fecha de hace 7 días a partir de hoy
        date_today = pd.to_datetime('today')
        date_7_days_ago = date_today - pd.Timedelta(days=6)

        # Filtrar partidas de los últimos 7 días con puntaje mayor a cero
        df_7_days_ago = df[(df['fecha'].dt.date >= date_7_days_ago.date()) & (df['puntos'] > 0)]
        
        df_7_days_ago['dia_semana'] = df_7_days_ago['fecha'].dt.day_name()
        days_week_spanish = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miércoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'}
        df_7_days_ago['dia_semana'] = df_7_days_ago['dia_semana'].map(days_week_spanish)
        
        if not df_7_days_ago.empty:
            total_user_streaks = df_7_days_ago.groupby(['usuario', 'mail'])['fecha'].nunique().reset_index()
            total_user_streaks.columns = ['usuario', 'mail', 'dias_con_puntaje']
            st.dataframe(total_user_streaks)
            # Filtrar usuarios con puntaje mayor a cero en todos los últimos 7 días
            users_in_streak = total_user_streaks[total_user_streaks['dias_con_puntaje'] == 7]
            st.dataframe(users_in_streak)
            if not users_in_streak.empty:
                # Agregar la columna 'puntos' al DataFrame
                users_in_streak['puntos'] = df_7_days_ago.groupby(['usuario', 'mail'])['puntos'].sum().values
                
                # Agregar columnas para cada día de la semana con los puntos correspondientes
                for day in df_7_days_ago['dia_semana'].unique():
                    users_in_streak[day] = df_7_days_ago[df_7_days_ago['dia_semana'] == day].groupby(['usuario', 'mail'])['puntos'].sum().values
                
                # Renombrar las columnas
                users_in_streak.columns = ['Usuario', 'Mail', 'dias_con_puntaje', 'Puntos Acumulados'] + list(df_7_days_ago['dia_semana'].unique())
                st.success(f"{len(users_in_streak)} usuarios están en racha de los últimos 7 días.")
                st.dataframe(users_in_streak[['Usuario', 'Mail', 'Puntos Acumulados'] + list(df_7_days_ago['dia_semana'].unique())])
            else:
                st.info("No hay usuarios en racha de los últimos 7 días.")
        else:
            st.warning("No hay partidas con puntaje mayor a cero en los últimos 7 días.")
        