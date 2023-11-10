import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# %matplotlib inline

aapl = yf.Ticker("AAPL")
days = 20
hist = aapl.history(period=f"{days}d")
print(hist)

msft = yf.Ticker("MSFT")
hist_msft = msft.history(period=f"{days}d")
print(hist_msft)