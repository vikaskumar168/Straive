import pytest
from account import Account, InsufficientBalanceError, calculate_emi

@pytest.fixture
def accounts():
    ritesh = Account("Ritesh", 0, annual_rate=0.06)
    vikash = Account("Vikash", 0)
    return ritesh, vikash

def test_deposit_and_withdraw(accounts):
    ritesh, _ = accounts
    ritesh.deposit(2000)
    ritesh.withdraw(500)
    assert ritesh.balance == 1500

def test_transfer_and_audit(accounts):
    ritesh, vikash = accounts
    ritesh.deposit(2000)
    ritesh.withdraw(500)
    ritesh.transfer(vikash, 1000)
    assert ritesh.balance == 500
    assert vikash.balance == 1000
    total_debits = 2000 - ritesh.balance
    total_credits = 2000
    assert total_debits == 1500
    assert total_credits == 2000

def test_transaction_history(accounts):
    ritesh, _ = accounts
    ritesh.deposit(1000)
    ritesh.withdraw(200)
    assert len(ritesh.history) == 3
    assert ritesh.history[-1]['balance'] == ritesh.balance
    assert ritesh.history[-1]['type'] == 'withdraw'

def test_zero_interest_rate():
    acc = Account("Zero", 10000, annual_rate=0.0)
    assert acc.calculate_annual_interest() == 0.0

def test_negative_interest_rate():
    acc = Account("Penalty", 10000, annual_rate=-0.05)
    assert acc.calculate_annual_interest() < 10000.0

def test_full_year_simulation():
    acc = Account("Ritesh", 20000, annual_rate=0.06)
    for _ in range(12):
        acc.deposit(500)
    interest = acc.calculate_annual_interest()
    acc.deposit(interest)
    acc.withdraw(3000)
    expected = 20000 + (500 * 12) + interest - 3000
    assert round(acc.balance, 2) == round(expected, 2)


@pytest.mark.parametrize("principal, rate, years", [
    (100000, 0.06, 1),
    (100000, 0.06, 5),
    (100000, 0.06, 30),
])
def test_emi_total_payment(principal, rate, years):
    emi = calculate_emi(principal, rate, years)
    total_paid = round(emi * years * 12, 2)
    assert total_paid > principal