import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import squarify

df2 = pd.read_csv('sample-treemap.csv')
st.write(df2)
#=================== 1 ===================================
st.subheader("(a) Treemap")

import streamlit as st
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
plt.rc('font', size=14)

squarify.plot(sizes=df2['D'], label=df2['B'], alpha=.8 )

plt.axis('off')
st.pyplot(fig)
plt.show()
#=================== Plotly sample code ===============================

import plotly.express as px
fig = px.treemap(
    names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
)
fig.update_traces(root_color="red")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()