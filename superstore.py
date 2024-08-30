import streamlit as st
import time
import pandas as pd
import numpy as np
import plotly.express as px
import warnings
from datetime import *



warnings.filterwarnings('ignore')


st.set_page_config(page_title="Superstore Analysis Dashboard!!!",page_icon=":shopping_trolley:",layout="wide")

st.title(":shopping_trolley: Superstore Analysis Dashboard!!!")

df=pd.read_excel("superstore.xlsx",sheet_name='Superstore')
col1,col2=st.columns(2)

d1=col1.date_input("start date",datetime(2000,7,6))
#st.write(d1)
d2=col2.date_input("End date",datetime(2000,7,6))
#st.write(d2)

#st.subheader("first 5 rows of superstore data")
#st.dataframe(df.head())


st.sidebar.header("Choose your filter: ")

Region=st.sidebar.multiselect("Pick your region",df["Region"].unique())
State=st.sidebar.multiselect("Pick your state",df["State"].unique())
City=st.sidebar.multiselect("Pick your city",df["City"].unique())

col1.subheader("Category wise sales")
table1=pd.pivot_table(df,values='Sales',index=['Category'],aggfunc=np.sum).reset_index()
fig1=px.bar(table1,x="Category",y="Sales")
col1.plotly_chart(fig1,use_container_width=True)

col2.subheader("Region wise sales")
if not Region:
    st.warning("select region")
else:
   
    table2=pd.pivot_table(df,values='Sales',index=['Region'],aggfunc=np.sum).reset_index()
    fig2=px.pie(table2,values="Sales",names="Region",hole=0.5)
    col2.plotly_chart(fig2,use_container_width=True)
    
    
col1.write(table1)
col2.write(table2)

col1.subheader("time series analysis")
table3=pd.pivot_table(df,values='Sales',index=['Order Date'],aggfunc=np.sum).reset_index()
fig3=px.line(table3,x="Order Date",y="Sales")
col1.plotly_chart(fig3,use_container_width=True)


col2.subheader("Hierarchical view of sales using tree map")
df.fillna("None")
fig=px.treemap(df,path=["Region","Category","Sub-Category"],values='Sales')
col2.plotly_chart(fig)
st.divider()



col1.subheader("Segment wise Sales")
table5=pd.pivot_table(df,values='Sales',index=['Segment'],aggfunc=np.sum).reset_index()
fig5=px.pie(table5,values="Sales",names="Segment",hole=0)
col1.plotly_chart(fig5,use_container_width=True)


col2.subheader("Category wise Sales")
table6=pd.pivot_table(df,values='Sales',index=['Category'],aggfunc=np.sum).reset_index()
fig6=px.pie(table6,values="Sales",names="Category",hole=0)
col2.plotly_chart(fig6,use_container_width=True)

