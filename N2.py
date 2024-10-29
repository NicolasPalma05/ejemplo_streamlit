import pandas as pd
import streamlit as st
def Suplentes():
  city = pd.read_csv('Seasons.csv')
  st.write(city)
