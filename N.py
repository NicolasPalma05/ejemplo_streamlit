import streamlit as st

Plantilla = {
  'HOME': 'P1',
  'statistics': 'P2',
  'Grafico': 'P3'
}

select = st.sidebar.selectbox('Plantilla:',list(Plantilla.keys()))

if select == 'HOME':
  st.text('WINER UEFA CHAMPIONS LEAGUE 2022/2023')
  st.image('City.jpg')
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
  import N2
  N2.Suplentes()
elif select == 'Grafico':
  import N3
  N3.grafico()
