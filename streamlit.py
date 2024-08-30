#2
import streamlit as st
import pandas as pd
st.set_page_config(page_title="my first page",page_icon=None,layout="centered",initial_sidebar_state="auto",menu_items=None)
st.write("Hello,*world!*:sunglasses:")
df1=pd.DataFrame({'column1':[1,2,3,4,5],'column2':[11,12,13,14,15]})
st.write("This is a dataframe",df1)
# Title

st.title("This is a title")
st.title("_Python_ is :blue[cool],:clown_face:")

#header

st.header("One",divider=True)
st.subheader("Two",divider=True)

#Mark down

st.markdown("#This is a markdown command")

# caption

st.caption(":copyright:,cdac Tvm")

# code

code='''
def hello():
    print("hello world") '''
    
st.code(code,language='python',line_numbers=True)
st.divider() 

# echo

with st.echo():
    st.write('This code will be printed')
    st.write(code)

# Latex

st.latex(r'''\frac{3}{4}''')

# Text

st.text("This is some text")

#Data elements

st.dataframe(df1.style.highlight_max(axis=0))

# table

st.table(df1)

# metric

st.metric(label="Temperature",value="35 degree celcius",delta="1.2 degree celcius")

# json

st.json({"1":"one","Numbers":[1,2,3,4,5]})


# Widgets

st.button("click me",type="primary")
st.button("click me",type="secondary")
if st.button("say hello"):
    st.write("hello dear")
else:
    st.write("good bye")

st.button("Reset",type="primary")


# download button

csv1=df1.to_csv().encode("utf-8")
st.download_button(label="dowmload as csv",data=csv1,file_name="funnel.csv",mime="text/csv")

# feed back button

fb1=st.feedback("stars")
if (fb1 is not None):
    st.write("Thanks for giving ",fb1+1, "stars")
    

## warning

name=st.text_input("Enter Name")
if not name:
    st.warning("input a name")
   # st.stop()
else:
    st.success("Thanks for inputting a name")
    
# link button

st.link_button("go to cdac site","http://www.cdac.in")

# page link

st.page_link("http://www.cdac.in",label="cdac")

# selections

agree=st.checkbox("I agree")
disagree=st.checkbox("I disagree")

if agree:
    st.write("GREAT")
elif disagree:
    st.write("Thank you visit again")
else:
    st.write("--------")
    
    
## colour picker

color=st.color_picker("pick a color","#00f900")
st.write("The selected color is ",color)

## multi selecte

options=st.multiselect("what are your favorite colors",["Green","Yellow","Red","Blue"],["Yellow","Red"])
st.write("New selected :",options)