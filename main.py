import pandas as pd
import random
import math

d = {
    0: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3
    },
    1: {
        'aktie1': 0.1,
        'aktie3': 0.2,
        'aktie4': 0.3,
        'aktie7': 0.4,
        'aktie9': 0.6,
        'aktie11': 0.7,
        'aktie12': 0.8
    },
    2: {
        'aktie4': 0.1,
        'aktie6': 0.2,
        'aktie7': 0.3,
        'aktie8': 0.4,
        'aktie9': 0.6,
        'aktie10': 0.7,
        'aktie15': 0.8
    }
}

df = pd.DataFrame(data=d)
used_stocks = []

def get_random_stock(period):
    n = random.randint(0, len(period.index.tolist())-1)
    stocks = period.index.tolist()
    stock_name = stocks[n]
    random_stock = period[stock_name]

    if math.isnan(random_stock) or stock_name in used_stocks:
        return get_random_stock(period)

    used_stocks.append(stock_name)

    return {
        'stock': stock_name,
        'value': random_stock
    }

for i in range(0, 3):
    print(get_random_stock(df[i]))
