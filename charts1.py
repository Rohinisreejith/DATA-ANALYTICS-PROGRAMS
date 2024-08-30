import streamlit as st
import pandas as pd
import numpy as np


chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.subheader("area chart")
st.area_chart(chart_data)

st.subheader("bar chart")
st.bar_chart(chart_data)

st.subheader("line chart")
st.line_chart(chart_data)

st.subheader("scatter chart")
st.scatter_chart(chart_data)

df2=pd.DataFrame({"Latitude":np.random.randn(1000)/50+37.76,"Longitude":np.random.randn(1000)/50+-122.4,"sizes":np.random.randn(1000)*100,"colors":np.random.rand(1000,4).tolist()})
st.map(df2,latitude='Latitude',longitude="Longitude",size='sizes',color='colors')