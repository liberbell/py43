import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# %matplotlib inline

days = 20
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Facebook": "META",
}
# company = "Facebook"
df = pd.DataFrame()
for comp in tickers.keys():
    tkr = yf.Ticker(tickers[company])
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
    pd.concat([df, hist])

    # print(hist)
