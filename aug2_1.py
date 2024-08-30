import streamlit as st
from datetime import *


# Radio button

genre=st.radio("what is your favorite movie genre?",["Comedy","Drama","Documentary"],captions=["Laugh out loud","Get the popcorn","Never stop learning"])
if genre=="Comedy":
    st.write("You have selected comedy")
else:
    st.write("You didnot selected comedy")
    


# select box

option=st.selectbox("How would you like to be contacted?",("Email","Home phone","Mobile phone","Whatsapp"))
st.write("You have selected",option)

# select slider

color=st.select_slider("select color of the rainbow",options=["Red","Orange","Yellow","Green","Blue","Indigo","Violet"])
st.write("The color you have selected is ",color)

# toggle bar

on=st.toggle("Activate your connection")
if on:
    st.write("Connected")


# Numeric

num=st.number_input("insert a number",value=None,placeholder="Type a number pls?")
st.write("The entered number is",num)

# slider

age=st.slider("How old are you?",0,100,25)
st.write("I am ",age," years old")

fvalue=st.slider("select a range of values",0.0,100.0,(25.0,75.0))
st.write("selected values",fvalue)

appointmenttime=st.slider("shedule an appointment:",value=(time(11,30),time(12,45)))
st.write("appointment is sheduled for",appointmenttime)


start_time=st.slider("When do you start?",value=datetime(2020,1,1,9,30),format="MM/DD/YY-hh:mm")
st.write("start time is",start_time)

# media elements

st.image("download.jpg",caption="cute cat")

video1=open("downloadvdo.mp4","rb")
video1_bytes=video1.read()
st.video(video1_bytes)

audio11=open("audio1.mp3","rb")
audio11_bytes=audio11.read()
st.audio(audio11_bytes,format="audio/mp3")

# layout &containers

col1,col2,col3=st.columns(3)
with col1:
    st.header("figure 1")
    st.image("1.jpg")
with col2:
    st.header("figure 2")
    st.image("2.jpg")
with col3:
    st.header("figure 3")
    st.image("3.jpg")
    
    
cont1=st.container(border=True)
cont1.write("this is a inside container")
st.write("This is  outside the container")

#expander

st.bar_chart(({"data":[1,5,2,6,2,1]}))
with st.expander("see explanation"):
    st.write("see the data")
    
 
#form

#form=st.form("my form")
##form.checkbox("form check box")
#form.slider("slider1")
#submit1=form.st.form_submit_button("submit form")
#if submit1:
 #   st.write("slider",slider_value,"checkbox",checkbox_val)
    

# side bar

with st.sidebar:
    with st.echo():
        st.write("This code will be printed on the side")