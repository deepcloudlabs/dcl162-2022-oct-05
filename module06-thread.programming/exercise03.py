import time

import grequests as grequests


def get_async_ticker():
    return (grequests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}") for symbol in symbols)


symbols = [
    "LTCBTC", "BNBBTC", "NEOBTC", "BTCUSDT", "ETHUSDT"
]

start = time.perf_counter()
for response in grequests.map(get_async_ticker()):
    print(response.content)
elapsed_time = time.perf_counter() - start
print(f"{elapsed_time:3.2f} seconds")
