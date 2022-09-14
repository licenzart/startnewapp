import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame([["Iris-setosa"], ["Iris-versicolor"],["Iris-virginica"]], columns=['Iris type'], index=['0', '1','2'])
st.header("Final Assignment for beginner")
st.info('This is a purely informational message', icon="ℹ️")
st.table(df)
st.snow()
