import pandas as pd
import random

d = {
    'aktie1': [0.1, 0.2, 0.15, 0.16, 0.3, 0.05, 0.1, 0.2],
    'aktie2': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie3': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie4': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie5': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie6': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie7': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie8': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie9': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
    'aktie10': [0.3, 0.1, 0.2, 0.13, 0.5, 0.01, 0.25, 0.11],
}
df = pd.DataFrame(data=d)

selected_stocks = {}
stocks = df.columns
used_stock = []

def get_random_stock():
    n = random.randint(0, df.columns.size-1)
    if n in used_stock:
        return get_random_stock()
    used_stock.append(n)
    return n

for i in range(1, 8):
    random_stock = stocks[get_random_stock()]
    random_stock_in_period = df[random_stock][i]
    selected_stocks[random_stock] = random_stock_in_period

print(selected_stocks)
