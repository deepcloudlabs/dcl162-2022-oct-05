from pymongo import MongoClient
from banking.domain import Account, AccountStatus

mongo_client = MongoClient("mongodb://localhost:27017")

accounts = [
    Account("tr1", 1000, AccountStatus.ACTIVE),
    Account("tr2", 2000, AccountStatus.ACTIVE),
    Account("tr3", 3000, AccountStatus.ACTIVE),
    Account("tr4", 4000, AccountStatus.ACTIVE),
    Account("tr5", 5000, AccountStatus.ACTIVE)
]

acct = {"_id": "tr5", "balance": 6000, "status": AccountStatus.ACTIVE.name}

banking_db = mongo_client["banking"]  # use world

accts = banking_db.accounts  # collection name : accounts

accts.insert_one(acct)
