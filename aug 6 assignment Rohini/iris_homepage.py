import streamlit as st

pg=st.navigation([

st.Page("iris_webapp.py",title="Iris Data Analysis"),
st.Page("iris_webapp_eda.py",title="Iris Data EDA"),
st.Page("iris_webapp_prediction.py",title="Prediction"),

])

pg.run()