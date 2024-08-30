import streamlit as st

pg=st.navigation([st.Page("airline_arima.py",title="Airline data analysis"),

st.Page("airline_arima_prediction.py",title="Airline data prediction")])




pg.run()