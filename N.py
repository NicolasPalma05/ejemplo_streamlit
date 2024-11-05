import streamlit as st
from N2, N3 import Suplentes(), grafico()

Plantilla = {
  'HOME': 'P1',
  'statistics': 'P2',
  'Grafico': 'P3'
}

select = st.sidebar.selectbox('Plantilla:',list(Plantilla.keys()))

if select == 'HOME':
  st.title('WINER UEFA CHAMPIONS LEAGUE 2022/2023')
  st.image('city.jpg')
  st.sidebar.title('Ubicacion')
  st.sidebar.image('reino unido.jpg')
  st.sidebar.write('Manchester, Reino Unido')
  st.sidebar.title('Estadio')
  st.sidebar.text('Etihad Stadium')
  st.sidebar.image('city.jpg')
  st.sidebar.title('Entrenador')
  st.sidebar.image('guardiola.jpg')
  st.sidebar.text(' Pep Guardiola ')
elif select == 'statistics':
  N2.Suplentes()
elif select == 'Grafico':
  N3.grafico()
