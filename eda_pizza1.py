import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import seaborn as sns

st.set_page_config(page_title="Pizza Price", page_icon=":pizza:",layout="wide")
st.title(":pizza: Pizza Data Analysis :pizza:")

pdf=pd.read_csv('pizza_price-1.csv')
st.dataframe(pdf)

st.header("Data set")
st.dataframe(pdf.head())

st.header("Data visualization")
#fig1=sns.pairplot(pdf)
#st.pyplot(fig1)


pdf.drop(columns=['Restaurant'],inplace=True)

st.header("Correlation matrix of features")
corr=pdf.corr()

fig2=px.imshow(corr,text_auto=True)
st.plotly_chart(fig2)


x=pdf.drop(columns=['Price'])
y=pdf.Price

c1,c2=st.columns(2)

c1.subheader("Fetures are")
c1.dataframe(x)

c2.subheader("labels are")
c1.dataframe(y)

lmodel=LinearRegression()
lmodel.fit(x,y)

saved_model=pickle.dump(lmodel,open('pizza2.pk1','wb'))