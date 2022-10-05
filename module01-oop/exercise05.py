from banking.domain import Account, AccountStatus, CheckingAccount

accounts = [  # heterogeneous list
    Account("tr1", 1000, AccountStatus.ACTIVE),
    CheckingAccount("tr2", 2000, AccountStatus.ACTIVE, 1000),
    Account("tr3", 3000, AccountStatus.ACTIVE),
    CheckingAccount("tr4", 4000, AccountStatus.ACTIVE, 2000)
]

for account in accounts:
    print(account)
    if isinstance(account, CheckingAccount):
        account.withdraw(75)
    else:
        account.withdraw(50)
    print(type(account).__name__)
    print(account.__class__)
    print(account.__class__.__name__)
