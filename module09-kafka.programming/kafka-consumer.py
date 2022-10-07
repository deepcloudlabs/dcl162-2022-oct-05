import json

from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(
    "trades",
    bootstrap_servers=["localhost:9092"],
    group_id="algotrading",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
mongo_client = MongoClient("mongodb://localhost:27017")
algo_db = mongo_client["algodb"]  # use world

trades = algo_db.trades  # collection name : trades

for message in consumer:
    trade = json.loads(message.value)
    print(trade)
    trades.insert_one(trade)
