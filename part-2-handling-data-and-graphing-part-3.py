import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2000, 1, 1)
#end = dt.datetime(2016, 12, 31)
#df = web.DataReader('TSLA', 'yahoo', start, end)

# df.to_csv('tsla.csv')

# read in tsla.csv file as pandas data frame ...still don't all the way understand
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
print(df.head())  # prints first 5 rows of data frame
