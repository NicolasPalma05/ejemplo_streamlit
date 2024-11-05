import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Cargar el CSV
df = pd.read_csv('Seasons.csv')

# Mostrar los primeros registros del DataFrame (opcional)
st.write(df.head())

# Configuración del gráfico: Crear un gráfico de barras para visualizar la cantidad de equipos por temporada
option = {
    "tooltip": {
        "trigger": "item"
    },
    "legend": {
        "data": ['Count of Teams']
    },
    "xAxis": {
        "type": "category",
        "data": df['season'].tolist()  # Usar las temporadas (columna 'season') para el eje X
    },
    "yAxis": {
        "type": "value"
    },
    "series": [{
        "name": 'Count of Teams',
        "type": 'bar',
        "data": df['count_teams'].tolist()  # Usar la cantidad de equipos (columna 'count_teams') para los valores Y
    }]
}

# Usar Streamlit para mostrar el gráfico interactivo
st.title('Gráfico de Cantidad de Equipos por Temporada')
st_echarts(options=option, height="400px")
