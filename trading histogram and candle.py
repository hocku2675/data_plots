# import requests
# import pandas as pd
# from datetime import datetime, timedelta
# import pandas_datareader as pdr
# import plotly.graph_objects as go
# import plotly.offline as py
import os
import requests
import pandas as pd
import mplfinance as mpf
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plt


def crypto_candles(start_time, base_currency, vs_currency, interval):
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload = {'interval': interval, 'baseTradingSymbol': base_currency,
               'quoteTradingSymbol': vs_currency, 'startTime': start_time}
    response = requests.get(url, params=payload)
    data = response.json()

    open_p, close_p, high_p, low_p, time_p = [], [],[],[],[]

    for candle in data:
        open_p.append(float(candle['open']))
        high_p.append(float(candle['high']))
        low_p.append(float(candle['low']))
        close_p.append(float(candle['close']))
        time_p.append(candle['time'])

    raw_data = {
        'Date': pd.DatetimeIndex(time_p),
        'Open': open_p,
        'High': high_p,
        'Low': low_p,
        'Close': close_p
    }

    df = pd.DataFrame(raw_data).set_index('Date')
    print(df)

    mpf.plot(df, type='candle', style='charles', title=base_currency)
    mpf.show()

    return df

crypto_candles(start_time='2023-05-14', base_currency='BTC',
                vs_currency='EUR', interval='1h')




#запрос для фигуры
# import requests
# import pandas as pd
# from datetime import datetime, timedelta
# import pandas_datareader as pdr
# import plotly.graph_objects as go
# import plotly.offline as py
# import mplfinance as mpf
#
# def crypto_histogram(start_time, base_currency, vs_currency, interval):
#     url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
#     payload = {'interval': interval, 'baseTradingSymbol': base_currency,
#                'quoteTradingSymbol': vs_currency, 'startTime': start_time}
#     response = requests.get(url, params=payload)
#     data = response.json()
#
#     open_p, close_p, high_p, low_p, time_p = [], [],[],[],[]
#
#     for candle in data:
#         open_p.append(float(candle['open']))
#         high_p.append(float(candle['high']))
#         low_p.append(float(candle['low']))
#         close_p.append(float(candle['close']))
#         time_p.append(candle['time'])
#
#     raw_data = {
#         'Date': pd.DatetimeIndex(time_p),
#         'Open': open_p,
#         'High': high_p,
#         'Low': low_p,
#         'Close': close_p
#     }
#
#     df = pd.DataFrame(raw_data).set_index('Date')
#     print(df)
#
#     mpf.plot(df, type='ohlc', style='charles', title=base_currency)
#     mpf.show()
#
#     return df
#
# crypto_histogram(start_time='2023-05-14', base_currency='BTC',
#                 vs_currency='EUR', interval='1h')
#

#запрос для изображения
def crypto_histogram(start_time, base_currency, vs_currency, interval):
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload = {'interval': interval, 'baseTradingSymbol': base_currency,
               'quoteTradingSymbol': vs_currency, 'startTime': start_time}
    response = requests.get(url, params=payload)
    data = response.json()

    open_p, close_p, high_p, low_p, time_p = [], [],[],[],[]

    for candle in data:
        open_p.append(float(candle['open']))
        high_p.append(float(candle['high']))
        low_p.append(float(candle['low']))
        close_p.append(float(candle['close']))
        time_p.append(candle['time'])

    raw_data = {
        'Date': pd.DatetimeIndex(time_p),
        'Open': open_p,
        'High': high_p,
        'Low': low_p,
        'Close': close_p
    }

    df = pd.DataFrame(raw_data).set_index('Date')
    print(df)

    fig, axlist = mpf.plot(df, type='ohlc', style='charles', title=base_currency, returnfig=True)
    fig.set_size_inches(8, 6)
    plt.savefig(os.path.join("C:\\temp\\", "chart.png"), dpi=120)  # сохраняем файл в директории "C:\temp\"

    with open(os.path.join("C:\\temp\\", "chart.png"), 'rb') as f:
        image = Image.open(BytesIO(f.read()))
        image.show()

    return df

crypto_histogram(start_time='2023-05-14', base_currency='BTC',
                vs_currency='EUR', interval='1h')