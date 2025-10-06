import pytest
# from ci import Account, InsufficientBalanceError
from banking import Account, InsufficientBalanceError
# @pytest.fixture
# def account():
#     return Account("Alice", 1000, 0.05)
#
# def test_deposit_valid(account):
#     account.deposit(500)
#     assert account.balance == 1500
#
# def test_deposit_zero(account):
#     with pytest.raises(ValueError, match="Deposit must be positive"):
#         account.deposit(0)
#
# def test_deposit_negative(account):
#     with pytest.raises(ValueError, match="Deposit must be positive"):
#         account.deposit(-100)
#
# def test_withdraw_valid(account):
#     account.withdraw(300)
#     assert account.balance == 700
#
# def test_withdraw_insufficient(account):
#     with pytest.raises(InsufficientBalanceError, match="Not enough balance"):
#         account.withdraw(2000)
#
# def test_withdraw_full_balance(account):
#     account.withdraw(1000)
#     assert account.balance == 0
#
# def test_calculate_annual_interest(account):
#     interest = account.calculate_annual_interest()
#     # assert interest == 30
#     assert interest == 50.0
#
# def test_calculate_compound_interest_default_frequency(account):
#     final_amount = account.calculate_compound_interest(2)
#     expected_amount = round(1000 * ((1 + 0.05) ** 2), 2)
#     assert final_amount == expected_amount
#
# def test_calculate_compound_interest_quarterly(account):
#     final_amount = account.calculate_compound_interest(2, 4)
#     expected_amount = round(1000 * ((1 + 0.05 / 4) ** (4 * 2)), 2)
#     assert final_amount == expected_amount
#
# def test_interest_on_zero_balance():
#     account1 = Account("Bob", balance=0)
#     assert account1.calculate_annual_interest() == 0.0
#     assert account1.calculate_compound_interest(years=3) == 0.0
#
# @pytest.mark.parametrize("years, expected", [
#     (1,round(1000 * ((1 + 0.05) ** 1), 2)),
#     (3,round(1000 * ((1 + 0.05) ** 3), 2)),
#     (5,round(1000 * ((1 + 0.05) ** 5), 2)),
# ])
# def test_multiple_years_compound_interest(account,years,expected):
#     assert account.calculate_compound_interest(years=years) == expected

@pytest.fixture
def accounts():
    ritesh = Account("ritesh", 0)
    vikash = Account("vikash", 0)
    return ritesh, vikash

def test_transaction_chain(accounts):
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

