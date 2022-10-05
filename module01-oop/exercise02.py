from banking.domain import CheckingAccount, AccountStatus, InsufficientBalanceError, IllegalAccountStateError

try:
    account1 = CheckingAccount("tr1", 1000, AccountStatus.ACTIVE, 500)
    account1.withdraw(750)
    print(account1)
    account1.withdraw(500)
    print(account1)
    account1.withdraw(250)
    print(account1)
    account1.withdraw(0.1)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"{err.message}: {err.deficit}")
except IllegalAccountStateError as err:
    print(f"{err.message}: {err.status}")
