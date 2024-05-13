import streamlit as st
import pandas as pd
st.subheader("Files")

df=st.file_uploader("Upload your file ",type=["csv","xlsx"])
if df is not None:
    df = pd.read_csv(df)
    if df is not None:
        st.table(df.head())

st.subheader("Dealing with images")
st.image("img.png")


st.subheader("Dealing with images while uploading ")
img=st.file_uploader("Upload your image ",type=["jpg","png","jpeg"])
if img is not None:
    st.image(img)

st.subheader("Video Uploader")
vid=st.file_uploader("Upload your video ",type=["mp4","mkv"])
if vid is not None:
    st.video(vid,start_time=0)

#This is an "raw String" using which i don't have to modify th epth "\" to "/"
#As windows and unix based system handle path separators differently
st.subheader("Using raw string to upload file ")
st.video(Video_Test.mp4)

st.subheader("Audio Files")
audi=st.file_uploader("Upload your audio ",type=["wav","mp3"])
if audi is not None:
    st.audio(audi.read())



