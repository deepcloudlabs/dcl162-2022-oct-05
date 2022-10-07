import websockets
import asyncio
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=lambda m: json.dumps(m).encode('utf-8'))


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        print(trade)
        producer.send("trades", value=frame)


async def connect_to_binance():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


asyncio.run(connect_to_binance())
