import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

# %matplotlib inline

days = 20
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Facebook": "META",
    "Google": "GOOGL",
    "Netflix": "NFLX",
    "Amazon": "AMZN"
}

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        print(tkr.info)
        hist = tkr.history(period=f"{days}d")
        # print(hist_aapl)

        # msft = yf.Ticker("MSFT")
        # hist_msft = msft.history(period=f"{days}d")
        # print(hist_msft)

        # print([hist_aapl, hist_msft], axix=1)

        hist.index = hist.index.strftime("%d %B %Y")
        # print(hist_aapl.head())

        hist = hist[["Close"]]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    return df

    # print(hist)
print(get_data(days, tickers))
companies = ["Apple", "Facebook"]
data = df.loc(companies)
print(data)

data.sort_index()
data = data.T.reset_index()
