import streamlit as st


pg=st.navigation([
st.Page("weather_eda.py",title="Weather EDA - Exploratory Data Analysis"),
st.Page("weather_prediction.py",title="Prediction"),
])

pg.run()