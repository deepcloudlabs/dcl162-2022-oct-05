from functools import reduce
from operator import add

from banking.domain import Account, AccountStatus, CheckingAccount

accounts = [  # heterogeneous list
    Account("tr1", 1000, AccountStatus.ACTIVE),
    CheckingAccount("tr2", 2000, AccountStatus.ACTIVE, 1000),
    Account("tr3", 3000, AccountStatus.ACTIVE),
    CheckingAccount("tr4", 4000, AccountStatus.ACTIVE, 2000),
    Account("tr5", 5000, AccountStatus.ACTIVE),
    CheckingAccount("tr6", 6000, AccountStatus.ACTIVE, 2000)
]

# outer loop
total_balance = 0
for account in accounts:
    if isinstance(account, CheckingAccount):
        total_balance += account.balance
print(f"total balance in CheckingAccount's is {total_balance}")

# hadoop: i) hdfs ii) filter-map-reduce

# inner loop
# functional programming
#  i. higher-order function: filter, map, reduce, ...
# ii. pure function        : lambda expression
if_checking_account = lambda acc: isinstance(acc, CheckingAccount)
to_balance = lambda acc: acc.balance
total_balance = reduce(add,
                       map(lambda acc: acc.balance, filter(lambda acc: isinstance(acc, CheckingAccount), accounts)), 0)
print(f"total balance in CheckingAccount's is {total_balance}")
