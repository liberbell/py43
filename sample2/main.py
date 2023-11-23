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
                 ## GAFA Stock price
                 ## Visualize tool
                 """)

st.sidebar.write("Display days")


days = st.sidebar.slider("Days", 1, 50, 20)

st.write(f"""
         ### GAFA Stock Price past **{days} days**
         """)

@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{days}d")
        hist.index = hist.index.strftime("%d %D %Y")
        hist = hist[["Close"]]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    return df

st.sidebar.write("""
                 ## Stock Price Range
                 """)
ymin, ymax = st.sidebar.slider("Input Price Range", 0.0, 3500.0, (0.0, 3500.0))

df = get_data(days, tickers)
st.multiselect("Select company", list(df.index))