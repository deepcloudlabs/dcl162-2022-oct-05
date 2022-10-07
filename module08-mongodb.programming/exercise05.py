from pymongo import MongoClient
from pprint import pprint as pp

mongo_client = MongoClient("mongodb://localhost:27017")

bankingdb = mongo_client["banking"]

accounts = bankingdb.accounts

result = accounts.update_many(
    {"status": "CLOSED"},
    {"$set": {"balance": 0}}
)

print(f"{result.matched_count} document(s) are updated.")
