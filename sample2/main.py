import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf


st.title("American Stock Price")

st.sidebar.write("""
                 GAFA Stock price

                 Visualize tool
                 """)

st.sidebar.write("Display days")