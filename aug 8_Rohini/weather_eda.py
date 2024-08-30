import pandas as pd
import plotly.express as px
import seaborn as sns
import sklearn
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Weather WEBAPP", page_icon=":umbrella:",layout="wide")
st.title(":umbrella: Weather Data Analysis")

# loading weather dataset
wdf=pd.read_csv('weather.csv')
st.header("Weather Dataset")
st.dataframe(wdf.head())

# Setting numerical Labels
st.subheader("Converting Data to Numerical Labels")
le = LabelEncoder()
wdf['outlook'] = le.fit_transform(wdf['outlook'])
wdf['temperature'] = le.fit_transform(wdf['temperature'])
wdf['humidity'] = le.fit_transform(wdf['humidity'])
wdf['windy'] = le.fit_transform(wdf['windy'])
wdf['play'] = le.fit_transform(wdf['play'])
st.dataframe(wdf.head())


weather=wdf

st.title("Weather Data Analysis")
st.subheader("Weather Dataset")
st.dataframe(weather)
st.subheader("Summary statistics")
st.write(weather.describe())
st.subheader("Pairplot")
pairplot=sns.pairplot(weather,hue='play')
st.pyplot(pairplot)
plt.figure(figsize=(10,6))
heatmap=sns.heatmap(weather.corr(),annot=True,cmap='coolwarm')
st.pyplot(heatmap.figure)

