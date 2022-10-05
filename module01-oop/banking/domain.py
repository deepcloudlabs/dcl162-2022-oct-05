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

    # constructor
    def __init__(self, iban, balance=0.0, status=AccountStatus.ACTIVE):
        self._iban = iban
        self._balance = balance
        self._status = status

    @property  # getter method
    def balance(self):
        return self._balance

    @property  # getter method
    def iban(self):
        return self._iban

    @property  # getter method
    def status(self):
        return self._status

    @status.setter  # setter method
    def status(self, status):
        print("@status.setter status(self, status)")
        if self._status == AccountStatus.CLOSED:
            raise ValueError("Cannot change status for a CLOSED account.")
        self._status = status

    def deposit(self, amount=5.0):  # business method
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self._status != AccountStatus.ACTIVE:
            raise IllegalAccountStateError("Illegal account status to deposit.", self._status)
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, amount=5.0):  # business method
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.status != AccountStatus.ACTIVE:
            raise IllegalAccountStateError("Illegal account status to deposit.", self.status)
        if amount > self.balance:
            raise InsufficientBalanceError("Your balance does not cover your expenses.",
                                           amount - self.balance)
        self._balance = self.balance - amount
        return self.balance

    def __str__(self):
        return f"Account [iban: {self.iban}, balance: {self.balance}, status: {self.status}]"


"""
Account         -> base   /super/parent class
CheckingAccount -> derived/sub  /child   class   
"""


class CheckingAccount(Account):
    def __init__(self, iban, balance, status, overdraft_amount):
        super().__init__(iban, balance, status)
        self._overdraft_amount = overdraft_amount

    @property  # read-only property
    def overdraft_amount(self):
        return self._overdraft_amount

    def withdraw(self, amount=5.0):  # overriding
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.status != AccountStatus.ACTIVE:
            raise IllegalAccountStateError("Illegal account status to deposit.", self.status)
        if amount > self.balance + self.overdraft_amount:
            raise InsufficientBalanceError("Your balance does not cover your expenses.",
                                           amount - self.balance - self.overdraft_amount)
        self._balance = self.balance - amount
        return self.balance

    def __str__(self):  # overriding
        return f"CheckingAccount [iban: {self.iban}, balance: {self.balance}, status: {self.status}," \
               f" overdraft_amount: {self._overdraft_amount}]"
