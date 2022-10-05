"""
Class members:
 i. attribute/state/data/field -> static properties
    iban, balance, status
    property
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
        self._iban = iban
        self._balance = balance
        self._status = status

    @property
    def balance(self):
        return self._balance

    @property
    def iban(self):
        return self._iban

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        print("@status.setter status(self, status)")
        if self._status == AccountStatus.CLOSED:
            raise ValueError("Cannot change status for a CLOSED account.")
        self._status = status

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
