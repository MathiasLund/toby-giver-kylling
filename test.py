import pandas as pd
import random
import math
import numpy as np

d = {
    0: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    1: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    2: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    3: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    4: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    5: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    6: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    },
    7: {
        'aktie1': 0.1,
        'aktie3': 0.3,
        'aktie4': 0.3,
        'aktie5': 0.3,
        'aktie6': 0.3,
        'aktie7': 0.3,
        'aktie8': 0.3,
        'aktie9': 0.1,
        'aktie10': 0.3,
        'aktie11': 0.3,
        'aktie12': 0.3,
        'aktie13': 0.3,
        'aktie14': 0.3,
        'aktie15': 0.3,
        'aktie16': 0.3,
        'aktie17': 0.3,
        'aktie18': 0.3,
        'aktie19': 0.3,
        'aktie20': 0.3,
        'aktie21': 0.3,
    }
}

irr_array = []
std_array = []
portfolio_array = []

for i in range(0,10):
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
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    stocks_final = {}

    for i in range(0, 8):
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

    stock_returns = {}
    for period in stocks_final:
        sum = 0
        for stock in stocks_final[period]:
            sum += stock['value']

        stock_returns[period] = sum

    stock_values = {}
    for i in stock_returns:
        val = stock_returns[i]
        #print("period", i)

        if i == 0:
            val = (val / 20000) - 1
        else:
            val = (val - 20000) / stock_returns[i-1] - 1

        stock_values[i] = val

    print("portfolio-returns", stock_values)
    print("portfolio-value", stock_returns)

    periods = []
    for period in stocks_final:
        periods.append(-20000)

    cashFlows = periods + [stock_returns[7]]

    irr = np.irr(cashFlows)
    print("irr", irr)

    irr_array.append(irr)

    stock_values_array = []
    for val in stock_values:
        stock_values_array.append(stock_values[val])

    # STD
    print("std")
    std = np.std(stock_values_array)
    print(std)
    std_array.append(std)

    portfolio_array.append(stock_returns[7])


print("irr_array", irr_array)
np_irr = np.array(irr_array)
print("irr_mean", np.mean(np_irr))

print("std_array", std_array)
np_std = np.array(std_array)
print("std_mean", np.mean(np_std))

print("portfolio_value", portfolio_array)
np_portifolio = np.array(portfolio_array)
print("portfolio_mean", np.mean(np_portifolio))
