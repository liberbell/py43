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

print(hist_aapl.index)