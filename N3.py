import streamlit as st
from streamlit_echarts import st_echarts
def grafico():
    pie_data = [
        {"name": row['Jugador'], "value": row['Goles']} 
        for _, row in df.iterrows()
    ]
    
    # Opciones del gráfico de pie
    options = {
        "title": {
            "text": "Goles por Jugador - Manchester City",
            "subtext": "Estadísticas de goles",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item",
            "formatter": "{a} <br/>{b}: {c} ({d}%)"
        },
        "legend": {
            "orient": "vertical",
            "left": "left",
            "data": df['Jugador'].tolist()
        },
        "series": [
            {
                "name": "Goles",
                "type": "pie",
                "radius": "50%",
                "data": pie_data,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
    
    # Mostrar el gráfico en Streamlit
    st_echarts(options=options, height="400px")
