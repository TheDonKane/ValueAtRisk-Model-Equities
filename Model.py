#Data manipulation
import numpy as np
import pandas as pd

#Plotting
import matplotlib.pyplot as plt
import seaborn

#Data fetching
import yfinance as yf

#Calculate daily returns
df = yf.download('GOOG')
df = yf.download('MSFT')
df = yf.download('AAPL')
df['returns'] = df.Close.pct_change()
df = df.dropna()
plt.hist(df.returns, bins=40)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
