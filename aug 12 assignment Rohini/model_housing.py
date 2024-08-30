import streamlit as st
import pickle

st.set_page_config(page_title="housing price analysis",page_icon=" :house_with_garden: ",layout="wide")
st.title(" :house_with_garden: housing price Data Analysis :house: ")


model_ridge      = pickle.load(open('rid11.pkl', 'rb'))
model_lasso      = pickle.load(open('lass11.pkl', 'rb'))
model_elasticnet = pickle.load(open('enet11.pkl', 'rb'))

st.header("Prediction")
n1 = int(st.number_input("Enter value for area : "))
n2 = int(st.number_input("Enter value for bedroom : "))
n3 = int(st.number_input("Enter value for bathroom : "))
n4 = int(st.number_input("Enter value for stories : "))
n5 = int(st.number_input("Enter value for mainroad : "))
n6 = int(st.number_input("Enter value for guestroom : "))
n7 = int(st.number_input("Enter value for basement: "))
n8 = int(st.number_input("Enter value for hotwaterheating : "))
n9 = int(st.number_input("Enter value for airconditioning: "))
n10 = int(st.number_input("Enter value for parking : "))
n11 = int(st.number_input("Enter value for prefarea : "))
n12 = int(st.number_input("Enter value for furnishingstatus: "))


sample1 = [[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]]

if st.button("Predict the price"):
    t1=model_ridge.predict(sample1)
    t2=model_lasso.predict(sample1)
    t3=model_elasticnet.predict(sample1)
    if (t1):
        st.write("Predicted price of house  is:")
        c1,c2,c3 = st.columns(3)
        c1.subheader("Ridge Regression")
        c2.subheader("LASSO Regression")
        c3.subheader("ElasticNet Regression")
        c1.write(t1)
        c2.write(t2)
        c3.write(t3)
    else:
        st.write("price cannot be determined")