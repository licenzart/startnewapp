import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

df = pd.DataFrame([["Iris-setosa"], ["Iris-versicolor"],["Iris-virginica"]], columns=['Iris type'], index=['0', '1','2'])
st.header("Final Assignment for beginner")
st.info('Please becareful of the snowflakes!', icon="ℹ️")
st.table(df)
st.snow()


image = Image.open('food1.jpg')

st.image(image, caption='Food1')
