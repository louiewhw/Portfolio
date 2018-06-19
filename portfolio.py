#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:37:25 2018

@author: louiewhw
"""

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import fix_yahoo_finance 
import matplotlib.pyplot as plt
fix_yahoo_finance.pdr_override

stocks = ['TSLA', 'AMZN', 'WMT', 'AAPL']
start_date = '01/01/2017'
end_date = '01/01/2018'

def get_data(stocks):
    
    df = pdr.DataReader(stocks,data_source = 'yahoo', start = start_date, end = end_date)['Adj Close']
    df.columns = stocks

    return df

df = get_data(stocks)

daily_returns = (df- df.shift(1))/df.shift(1) 
daily_returns2 = np.log(df/df.shift(1))


df.plot()
daily_returns.plot()
daily_returns2.plot()
plt.show()
