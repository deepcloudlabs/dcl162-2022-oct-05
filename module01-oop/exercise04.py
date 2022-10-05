from random import random

from banking.domain import Account, AccountStatus, CheckingAccount

account = None

if random() < 0.5:  # head
    print("Head")
    account = Account("tr1", 1000, AccountStatus.ACTIVE)
else:  # tail
    print("Tail")
    account = CheckingAccount("tr1", 1000, AccountStatus.ACTIVE, 1000)

account.withdraw(500)
print(account)
