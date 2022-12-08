"""
Pandas Series is the main Pandas data type.
It is a representation of a sequence of data, which
is an indexed data structure. The main advantage of
an indexed data structure is that you can access to any
element by position.

To access an item of a Pandas Series it can be done by index
or by location.
"""

import numpy as np
import pandas as pd

market_caps_list = [954.7, 514.4, 95.8, 76.3, 57.9, 45.7, 41.0, 38.7, 28.8, 25.8]
market_caps = pd.Series(market_caps_list)
market_caps.name = 'Market caps of top 10 cryptocurrencies in billions USD'
print(market_caps)

series_type = market_caps.dtype
series_values = market_caps.values
print(market_caps_list, type(market_caps_list))
print(series_values, type(series_values))

market_caps.index = ['BTC', 'ETH', 'BNB', 'USDT', 'SOL', 'ADA', 'USDC', 'XRP', 'DOT', 'LUNA']
print(market_caps)

# Access by index
bitcoin = market_caps['BTC']
ethereum = market_caps['ETH']


# Access by numerical index location
bnb1 = market_caps.iloc[2]
# Access by index location
bnb2 = market_caps.loc['BNB']
# Access by index location
bnb3 = market_caps['BNB']
print(bnb1, bnb2, bnb3)

slicing1 = market_caps[['BTC', 'ETH', 'BNB']]
slicing2 = market_caps[0:3]
slicing3 = market_caps[:'BNB']
print(slicing1, slicing2, slicing3)

