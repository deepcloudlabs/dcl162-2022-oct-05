import time

import requests


def get_sync_ticker(symbol):
    return requests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")


symbols = [
    "LTCBTC", "BNBBTC", "NEOBTC", "BTCUSDT", "ETHUSDT"
]


def sync_call():
    for symbol in symbols:
        ticker = get_sync_ticker(symbol)
        print(ticker.content)


start = time.perf_counter()
sync_call()
elapsed_time = time.perf_counter() - start
print(f"{elapsed_time:3.2f} seconds")
