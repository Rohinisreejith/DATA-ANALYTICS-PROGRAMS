import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

from mlxtend.frequent_patterns import association_rules,apriori


st.set_page_config(page_title="Association Rule Mining!!!",page_icon=":sandwich:",layout="wide")
st.title(":pizza: Association Rule Mining!!!")
st.divider()

df=pd.read_csv("bread.csv")
st.subheader(":sandwich: Sample transaction data set :pizza:")
st.table(df.head())

st.header("Finding count of each item in transaction")

tran_df=df.groupby(['Transaction','Item'])['Item'].count().reset_index(name='count')
st.table(tran_df.head(15))
st.divider()

st.header("Convert into format of apriori function")

my_basket=tran_df.pivot_table(index='Transaction',columns='Item',values='count').fillna(0)

st.table(my_basket.head(15))

def encode1(x):
    if x<=0:
        return 0
    else:
        return 1
my_basket=my_basket.map(encode1)


st.header("Data after encoding")
st.table(my_basket.head())

# ===== APRIORI     
large_items = apriori(my_basket, min_support = 0.01, use_colnames=True)
st.header("Large Itemsets")
st.table(large_items.head(15))

# ===== Association Rules
st.header("Association Rules")
rules = association_rules(large_items, min_threshold = 0.1, metric = "lift")
st.table(rules) 


