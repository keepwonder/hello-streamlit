import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('st.write')

#  样例 1 
st.write('hello, *World* :sunglasses:')

# 样例 2
st.write(1234)

# 样例 3
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write(df)

# 样例 4 
st.write('Below is a DataFrame', df, 'Above is a DataFrame')

# 样例 5 
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(x='a',y='b',size='c',color='c', tooltip=['a','b','c'])
st.write(c)


