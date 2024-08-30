import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics as mat
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np




import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans



st.set_page_config(page_title="Fruits Data Analysis", page_icon="🍒", layout="wide")
st.title("🍓 Fruits Data Analysis 🍓️")


df=pd.read_csv('fruits.csv')
st.header('🍎FRUITS DATA SET🍎')
st.table(df.head())

cl1,cl2=st.columns(2)

cl1.header("Count of unique labels")
cl1.table(df['fruit_label'].value_counts())

cl1.header("Count of unique names")
cl1.table(df['fruit_name'].value_counts())

x=df.iloc[:,3:7]
y=df[['fruit_label']]

wcss=[]
k=[]
for i in range(1,11):
    k.append(i)
    kmeans=KMeans(n_clusters=i,init='k-means++',max_iter=30,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

st.write("values of k and wcss")
fig,ax=plt.subplots(figsize=(2,2))
ax.plot(k,wcss,c='g',marker='o',mfc='r')
st.pyplot(fig)    

km_final=KMeans(n_clusters=4,init='k-means++',max_iter=30,random_state=0)
df['new_label']=km_final.fit_predict(x)

st.header('🍎FRUITS DATA SET WITH NEW LABELS🍎')
st.table(df)

st.header("Visualizing the new labels and clusters")

fig2=px.scatter(df,x='mass',y='width',size='color_score',color='new_label')
st.plotly_chart(fig2,use_container_width=True)

fig3=px.scatter(df,x='mass',y='width',size='color_score',color='fruit_label')
st.plotly_chart(fig3,use_container_width=True)


dbs=mat.davies_bouldin_score(x,km_final.labels_)
sil=mat.silhouette_score(x,km_final.labels_)
cal=mat.calinski_harabasz_score(x,km_final.labels_)

ars=mat.adjusted_rand_score(df['fruit_label'],km_final.labels_)
mu=mat.mutual_info_score(df['fruit_label'],km_final.labels_)

st.header("Evaluation score")

c1,c2,c3=st.columns(3)
c4,c5=st.columns(2)

c1.subheader('Davies_bouldin_score')
c1.subheader(dbs)
c2.subheader('silbouette_score')
c2.subheader(sil)
c3.subheader('calinski_harabasz_score')
c3.subheader(cal)
c4.subheader('adjusted_rand_score')
c4.subheader(ars)
c5.subheader('mutual_info_score')
c5.subheader(mu)

m1=pickle.dump(km_final,open('kmean.pkl','wb'))

