import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf

st.title("US Stock Price Display Application")
st.sidebar.write("""
                 ## GAFA Stock price
                 ## Visualize tool
                 """)
st.sidebar.write("Display days")