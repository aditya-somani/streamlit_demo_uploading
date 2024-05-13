import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#randn -> 20 rows and 3 columns
data=pd.DataFrame(np.random.rand(20,3),columns=["line1","line2","line3"])

st.subheader("Line Chart")
st.line_chart(data)

st.subheader("Area Chart")
st.area_chart(data)

st.subheader("bar chart")
st.bar_chart(data)

st.header("Plotting graph using matplotlib and seaborn")

st.subheader("Loading the DataFrame")
df=pd.read_csv(r"C:\Users\H.P\Desktop\Python\Learning\Libraries\Streamlit\Ref\iris.csv")
st.dataframe(df)

st.subheader("Bar Graph using Matplotlib")
fig = plt.figure(figsize=(15,8))
df["species"].value_counts().plot(kind="bar")
st.pyplot(fig)

st.subheader("Distribution graph using seaborn")
fig = plt.figure(figsize=(15,6))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

st.header("Multiple Graphs using seaborn")
col1, col2 = st.columns(2)
with col1:
    col1.header = "KDE=False"
    col1.write("KDE=False")
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df["sepal_length"],kde='False') #ye KDE ka matlab he vo blue colour ki line nahi ayegi
    st.pyplot(fig1)

with col2:
    col2.header = "hist=False"
    col2.write("hist=False")
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df["sepal_length"],kde=False)
    st.pyplot(fig2)

st.subheader("Changing the style")
col1, col2 = st.columns(2)
with col1:
    fig1=plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig1)

with col2:
    fig=plt.figure()
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig)

st.header("Exploring Different Graphs")
st.subheader("scatter PLot")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("count plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x="species")
st.pyplot(fig)

st.subheader("Box plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x="species",y="petal_length")
st.pyplot(fig)

st.subheader(("violin plot"))
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="species",y="petal_length")
st.pyplot(fig)
