import streamlit as st
from sklearn.model_selection import train_test_split as tts
from series import train_test

st.set_page_config(page_title="Airline data forecasting", page_icon=":small_airplane:", layout="wide")
st.title(":small_airplane: Time series forecasting with arima for Airline Data :small_airplane:")

tr,ts=train_test()

c1,c2=st.columns(2)

c1.header("Training data")
c1.table(tr.head())

c2.header("Testing data")
c2.table(ts.head())




