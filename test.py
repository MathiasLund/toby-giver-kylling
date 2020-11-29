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
        'aktie3': 0.3,
        'aktie4': 0.4,
        'aktie5': 0.5,
        'aktie6': 0.6,
        'aktie7': 0.7,
        'aktie8': 0.8
    },
    2: {
        'aktie1': 0.3,
        'aktie3': 0.2,
        'aktie4': 0.1,
        'aktie5': 0.3,
        'aktie6': 0.4,
        'aktie7': 0.3,
        'aktie8': 0.3
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

    return stock_name

stocks_test = {
    0: [],
    1: [],
    2: []
}

stocks_final = {}

for i in range(0, 3):
    random_stock = get_random_stock(df[i])
    stocks_test[i].append(random_stock)

stocks = []

for i in range(len(stocks_test)):
    stocks.append(stocks_test[i])

for i in range(len(stocks_test)):

    values = []
    for p in range(0, i+1):
        values.append(stocks_test[p])

    stocks_final[i] = values

for i in range(len(stocks_final)):
    stocks = stocks_final[i]
    #print("period",i)
    stock_returns = []

    for p in stocks:
        stock = p[0]
        stock_return_percent = d[i][stock]
        stock_return_value = (1+stock_return_percent) * 20000

        value = {
            'stock': stock,
            'percent': stock_return_percent,
            'value': stock_return_value
        }

        stock_returns.append(value)

    stocks_final[i] = stock_returns


for period in stocks_final:
    stocks_in_period = stocks_final[period]
    #print(period)
    for stock in stocks_in_period:
        stock_name = stock['stock']
        stock_percent = stock['percent']

        if period > 0:
            try:
                value = [i for i in stocks_final[period-1] if i['stock'] == stock_name][0]['value']
                final_value = value * (1 + stock_percent)

                [i for i in stocks_final[period] if i['stock'] == stock_name][0]['value'] = final_value

            except IndexError:
                print("")

print(stocks_final)
