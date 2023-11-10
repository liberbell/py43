import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# %matplotlib inline

aapl = yf.Ticker("AAPL")
days = 20
hist_aapl = aapl.history(period=f"{days}d")
# print(hist_aapl)

# msft = yf.Ticker("MSFT")
# hist_msft = msft.history(period=f"{days}d")
# print(hist_msft)

# print([hist_aapl, hist_msft], axix=1)

hist_aapl.index = hist_aapl.index.strftime("%d %B %Y")
# print(hist_aapl.head())

hist_aapl = hist_aapl[["Close"]]
hist_aapl.columns = ["Apple"]
print(hist_aapl)
