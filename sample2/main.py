import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf


tickers = {
    "Apple": "AAPL",
    "Facebook": "META",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Netflix": "NTLX",
    "Amazon": "AMZN"
}

st.title("American Stock Price")

st.sidebar.write("""
                 # GAFA Stock price
                 # Visualize tool
                 """)

st.sidebar.write("Display days")


days = st.sidebar.slider("Days", 1, 50, 20)

st.write(f"""
         ### GAFA Stock Price past **{days} days**
         """)

def get_data(days, tickers)