import pytest

from banking.domain import Account, AccountStatus, IllegalAccountStateError


@pytest.fixture
def an_active_account():
    """
    :return: creates an Account with iban TR1 and the balance 1000
    """
    return Account("tr1", 1000, AccountStatus.ACTIVE)


@pytest.fixture
def a_closed_account():
    """
    :return: creates an Account with iban TR1 and the balance 1000
    """
    return Account("tr1", 0, AccountStatus.CLOSED)


def test_create_account(an_active_account):
    """
    :param an_account: takes a fixture
    tests if an account is created successfully
    """
    assert an_active_account.iban == "tr1"
    assert an_active_account.balance == 1000
    assert an_active_account.status == AccountStatus.ACTIVE


def test_deposit_with_zero_amount_then_raise_ValueError(an_active_account):
    with pytest.raises(ValueError):
        an_active_account.deposit(0)  # 2. call exercise method
    assert an_active_account.balance == 1000


def test_deposit_with_positive_amount_closed_account_then_raise_error(a_closed_account):
    with pytest.raises(IllegalAccountStateError):
        a_closed_account.deposit(1)  # 2. call exercise method
    assert a_closed_account.balance == 0


def test_deposit_with_positive_amount_to_active_account_success(an_active_account):
    an_active_account.deposit(1)  # 2. call exercise method
    assert an_active_account.balance == 1001
