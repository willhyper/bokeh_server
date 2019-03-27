
from os.path import dirname, join

import pandas as pd

DATA_DIR = join(dirname(__file__), 'daily')


def load_ticker(ticker):
    fname = join(DATA_DIR, 'table_%s.csv' % ticker.lower())
    data = pd.read_csv(fname, header=None, parse_dates=['date'],
                       names=['date', 'foo', 'o', 'h', 'l', 'c', 'v'])
    data = data.set_index('date')
    return pd.DataFrame({ticker: data.c})

def get_data():
    t1, t2 = 'AAPL', 'GOOG'
    df1 = load_ticker(t1)
    df2 = load_ticker(t2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['x'] = data[t1]
    data['y'] = data[t2]
    return data
