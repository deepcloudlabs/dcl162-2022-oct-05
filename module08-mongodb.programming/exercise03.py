from pymongo import MongoClient
from pprint import pprint as pp

mongo_client = MongoClient("mongodb://localhost:27017")

bankingdb = mongo_client["banking"]

accounts = bankingdb.accounts

for acc in accounts.find({"$and": [ {"balance": {"$gt": 2000}} , {"status": "CLOSED"} ]}):
    pp(acc)
