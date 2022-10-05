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


class Account:

    def __init__(self, iban, balance, status):
        self.iban = iban
        self.balance = balance
        self.status = status

    def deposit(self, amount):
        if amount <= 0:
            return False
        if self.status == AccountStatus.ACTIVE:
            self.balance = self.balance + amount
            return True

        return False
