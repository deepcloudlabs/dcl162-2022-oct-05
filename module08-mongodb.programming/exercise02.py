from pymongo import MongoClient
from banking.domain import Account, AccountStatus

mongo_client = MongoClient("mongodb://localhost:27017")

accounts = [
    {"_id": "tr1", "balance": 10000, "status": AccountStatus.ACTIVE.name},
    {"_id": "tr2", "balance": 20000, "status": AccountStatus.CLOSED.name},
    {"_id": "tr3", "balance": 30000, "status": AccountStatus.ACTIVE.name},
    {"_id": "tr4", "balance": 40000, "status": AccountStatus.BLOCKED.name},
    {"_id": "tr5", "balance": 50000, "status": AccountStatus.ACTIVE.name}
]

acct = {"_id": "tr5", "balance": 6000, "status": AccountStatus.ACTIVE.name}

banking_db = mongo_client["banking"]  # use world

accts = banking_db.accounts  # collection name : accounts

# accts.insert_one(acct)
accts.insert_many(accounts)
