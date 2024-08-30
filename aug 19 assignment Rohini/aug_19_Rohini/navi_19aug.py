import streamlit as st

pg=st.navigation([st.Page("association.py",title="Association rule mining"),


st.Page("kmeans_pca1.py",title="wine data analysis"),

st.Page("breast_can_pca.py",title="breast cancer data analysis "),
st.Page("airline_time_series.py",title="Airline data analysis ")])

pg.run()