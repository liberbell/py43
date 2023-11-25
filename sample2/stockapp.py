import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf

st.title("US Stock Price Display Application")
st.sidebar.write("""
                 ## GAFA Stock price
                 ## Visualize tool
                 """)
st.sidebar.write("Select Display days")
days = st.sidebar.slider("Days", 1, 50, 20)

st.write(f"""
         ### GAFA Stock Price past **{days} days**
         """)

days = 20
tickers = {
    "Apple": "AAPL",
    "Facebook": "META",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Amazon": "AMZN"
}

def get_data(dats, tickers):
  df = pd.DataFrame()
  for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    hist = tkr.history(period=f"{days}d")
    hist.index = hist.index.strftime("%d %B %Y")
    hist = hist[["Close"]]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = "Name"
    df = pd.concat([df, hist])
  return df