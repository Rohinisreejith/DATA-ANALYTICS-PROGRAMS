import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn import metrics as mat
from sklearn.preprocessing import LabelEncoder
import pickle

st.set_page_config(page_title="Obesity!!!",page_icon=":sandwich:",layout="wide")
st.title(":pizza: Obesity Data Analysis!!!")

df=pd.read_csv("obesity.csv")
st.subheader(":sandwich: Obesity data Analysis :pizza:")
df
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
 
df

c1, c2 = st.columns(2)
c1.header("Count of unique labels")
c1.table(df['Label'].value_counts())




x = df.iloc[:,1:6]  
y = df[[]]         

wcss = []
k    = []

for i in range(1, 11):
    k.append(i)
    kmeans = KMeans(n_clusters=i, init="k-means++", max_iter = 30, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
st.subheader("Values of K and wcss")

fig, ax = plt.subplots(figsize = (2,2))
ax.plot(k, wcss, c='g', marker='o', mfc='r')
st.pyplot(fig)

kdf = pd.DataFrame({'k':k, 'wcss':wcss })
fig1=px.line(kdf, x="k", y="wcss")
st.plotly_chart(fig1, use_container_width=True)




km_final =  KMeans(n_clusters = 4, init="k-means++", max_iter = 1000, random_state = 0, tol=0.001)
df['new_label'] = km_final.fit_predict(x)
st.table(df)


m1 = pickle.dump(km_final, open('obesity_kmeans.pkl', 'wb'))


st.header("Visualizing with new labels and clusters")
fig2=px.scatter(df,x='Age',y='Weight',size='BMI',color='Label')
st.plotly_chart(fig2,use_container_width=True)


fig3=px.scatter(df,x='Age',y='Weight',size='BMI',color='new_label')
st.plotly_chart(fig3,use_container_width=True)




st.divider()
st.header("Evaluation Scores")

dbs = mat.davies_bouldin_score(x, km_final.labels_)
sil = mat.silhouette_score(x, km_final.labels_)
cal = mat.calinski_harabasz_score(x, km_final.labels_)
ar = mat.adjusted_rand_score(df['Label'], km_final.labels_)
mu = mat.mutual_info_score(df['Label'], km_final.labels_)

c1, c2, c3  = st.columns(3)
c4, c5 = st.columns(2)

c1.subheader("davies bouldin score")
c1.write(dbs)
c2.subheader("silhouette score")
c2.write(sil)
c3.subheader("calinski harabasz score")
c3.write(cal)

c4.subheader("adjusted rand score")
c4.write(ar)
c5.subheader("mutual info score")
c5.write(mu)
st.divider()



    