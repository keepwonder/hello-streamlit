import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('streamlit_pandas_profiling')

df = pd.read_csv('./book.csv', encoding='gbk')

pr = df.profile_report()
st_profile_report(pr)
