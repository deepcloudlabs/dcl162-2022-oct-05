from banking.domain import Account, AccountStatus, InsufficientBalanceError, IllegalAccountStateError

try:
    account1 = Account("tr1")
    account2 = Account("tr2", 10000)
    account3 = Account("tr3", 20000, AccountStatus.CLOSED)
    account3.status = AccountStatus.BLOCKED
    account1.deposit(100.0)
    account1.deposit(1.0)
    print(account1.balance)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"{err.message}: {err.deficit}")
except IllegalAccountStateError as err:
    print(f"{err.message}: {err.status}")
