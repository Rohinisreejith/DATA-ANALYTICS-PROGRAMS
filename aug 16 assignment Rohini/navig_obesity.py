import pandas as pd
import plotly.express as px
import seaborn as sns
import sklearn
import streamlit as st

pg=st.navigation([st.Page("eda_obesity.py",title="Obesity Data Analysis"),
st.Page("model_obesity.py",title="Obesity Label prediction "),
st.Page("agglomerative_obesity.py",title="Agglomerative clustering in obesity data "),
st.Page("divisive_obesity.py",title="Divisive clustering in obesity data ")])

pg.run()