from pymongo import MongoClient
from pprint import pprint as pp

mongo_client = MongoClient("mongodb://localhost:27017")

bankingdb = mongo_client["banking"]

accounts = bankingdb.accounts

result = accounts.delete_many({"balance": {"$gte": 3000}})

print(f"{result.deleted_count} document(s) are deleted.")
