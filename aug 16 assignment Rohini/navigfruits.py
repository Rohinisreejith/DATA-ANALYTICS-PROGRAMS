import pandas as pd
import plotly.express as px
import seaborn as sns
import sklearn
import streamlit as st

pg=st.navigation([st.Page("eda_fruits.py",title="Fruits Data Analysis"),
st.Page("model_fruits.py",title="Fruits Label prediction "),
st.Page("agglomerative_fruits.py",title="Agglomerative clustering in fruits data "),
st.Page("agglo_fruits_model.py",title="Agglomerative clustering prediction in fruits data "),
st.Page("divisive_fruits.py",title="Divisive clustering in fruits data ")])

pg.run()