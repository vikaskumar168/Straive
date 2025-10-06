import pytest
from banking import Account, InsufficientBalanceError, InvalidWithdrawlAmount


@pytest.fixture
def accounts():
    account1 = Account("Alice",1000)
    account2 = Account("Bob",500)
    return  account1, account2

def test_deposit_positive(accounts):
    account1, _ = accounts
    account1.deposit(200)
    assert account1.balance == 1200

def test_deposit_zero(accounts):
    account1, _ = accounts
    with pytest.raises(ValueError,match="Deposit must be positive"):
        account1.deposit(0)


def test_deposit_negative(accounts):
    account1, _ = accounts
    with pytest.raises(ValueError,match="Deposit must be positive"):
        account1.deposit(-100)


def test_withdraw_valid(accounts):
    account1, _ = accounts
    account1.withdraw(300)
    assert account1.balance == 700

def test_withdraw_zero(accounts):
    account1, _ = accounts
    with pytest.raises(InvalidWithdrawlAmount,match="Withdrawl amount must be positive"):
        account1.withdraw(0)


def test_withdraw_negative(accounts):
    account1, _ = accounts
    with pytest.raises(InvalidWithdrawlAmount,match="Withdrawl amount must be positive"):
        account1.withdraw(-100)

def test_withdraw_insufficient(accounts):
    account2 = accounts[1]
    with pytest.raises(InsufficientBalanceError) as exc_info:
        account2.withdraw(600)
    assert str(exc_info.value) == "Not enough balance"

def test_transfer_success(accounts):
    account1, account2 = accounts
    account1.transfer(account2, 200)
    assert account1.balance == 800
    assert account2.balance == 700

def test_transfer_insufficient(accounts):
    account1, account2 = accounts
    with pytest.raises(InsufficientBalanceError):
        account2.transfer(account1, 600)
    assert account2.balance == 500
    assert account1.balance == 1000


@pytest.mark.parametrize("amount", [100, 500, 1000])
def test_parametrized_withdrawals(accounts, amount):
    acc1, _ = accounts
    acc1.withdraw(amount)
    assert acc1.balance == 1000 - amount

def test_exception_message(accounts):
    acc2 = accounts[1]
    with pytest.raises(InsufficientBalanceError) as exc_info:
        acc2.withdraw(1000)
    assert str(exc_info.value) == "Not enough balance"

def test_full_balance_transfer(accounts):
    acc1, acc2 = accounts
    acc1.transfer(acc2, acc1.balance)
    assert acc1.balance == 0
    assert acc2.balance == 1500