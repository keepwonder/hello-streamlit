import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader('choose a file')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='gbk')
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

