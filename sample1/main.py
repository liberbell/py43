import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit introduction")

st.write("DataFrame")

df = pd.DataFrame({
    "First row": [1, 2, 3, 4],
    "Second row": [10, 20, 30, 40]
})

st.write(df)