"""
Class members:
 i. attribute/state/data/field -> static properties
    iban, balance, status
ii. behaviour/method           -> dynamic properties
"""
from enum import Enum


class AccountStatus(Enum):
    CLOSED = 100
    ACTIVE = 200
    BLOCKED = 300


class IllegalAccountStateError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status


class InsufficientBalanceError(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Account:

    def __init__(self, iban, balance=0.0, status=AccountStatus.ACTIVE):
        self.iban = iban
        self.balance = balance
        self.status = status

    def deposit(self, amount=5.0):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.status != AccountStatus.ACTIVE:
            raise IllegalAccountStateError("Illegal account status to deposit.", self.status)
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount=5.0):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.status != AccountStatus.ACTIVE:
            raise IllegalAccountStateError("Illegal account status to deposit.", self.status)
        if amount > self.balance:
            raise InsufficientBalanceError("Your balance does not cover your expenses.",
                                           amount - self.balance)
        self.balance = self.balance - amount
        return self.balance

try:
    account1 = Account("tr1")
    account2 = Account("tr2", 10000)
    account3 = Account("tr3", 20000, AccountStatus.ACTIVE)
    account1.deposit(100.0)
    account1.deposit(1.0)
    account1.withdraw(101.0)
    print(account1)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"{err.message}: {err.deficit}")
except IllegalAccountStateError as err:
    print(f"{err.message}: {err.status}")
