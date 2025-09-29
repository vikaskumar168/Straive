import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 8), -8)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 1), 4)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 3), 1)
        self.assertEqual(self.calc.modulus(20, 7), 6)
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulus(10, 0)


if __name__ == "__main__":
    unittest.main()


















class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b
















import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(0, 5) == 15
    assert calc.add(-1, -1) == -2
    assert calc.add(-1, 1) == 0



def classify(num):
    if num % 2 == 0:
        return "even"
    elif num % 3 == 0:
        return "divisible by 3"
    else:
        return "other"



class InsufficientBalanceError(Exception):
    pass
 
 
class Account:
    def __init__(self, owner, balance=0, annual_rate=0.05):
        """
        :param owner: Account holder name
        :param balance: Initial balance
        :param annual_rate: Annual interest rate (default 5%)
        """
        self.owner = owner
        self.balance = balance
        self.annual_rate = annual_rate
 
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.balance -= amount
        return self.balance
 
    def calculate_annual_interest(self):
        """
        Formula: Interest = Balance * Rate
        """
        return round(self.balance * self.annual_rate, 2)
 
    def calculate_compound_interest(self, years, compounding_frequency=1):
        """
        Formula: A = P * (1 + r/n)^(n*t)
        Returns final amount after compounding.
        """
        P = self.balance
        r = self.annual_rate
        n = compounding_frequency
        t = years
        A = P * ((1 + r / n) ** (n * t))
        return round(A, 2)



Simple Interest Calculation (Balance * Rate).
 
Compound Interest (Yearly + Quarterly compounding).
 
Parameterized testing for multiple years.
 
Edge cases (zero years, zero balance).


                   Perform the following sequence in a test:
Alice deposits 2000.
Alice withdraws 500.
Alice transfers 1000 to Bob.
Write assertions for final balances of both accounts.
Add an extra check that Alice’s total debits = 1500 and credits = 2000.






                                            Write tests for multiple scenarios (e.g., 1-year loan vs 5-yer loan vs 30-year loan).
 
Assert that total paid = principal + interest is correct.
def calculate_emi(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return round(emi, 2)
 
 
Write tests to ensure: transaction history
 
Every deposit/withdraw updates the history correctly.
 
The last entry always reflects the final balance.
 
 
Integration Style Test
 
Simulate a full year of banking:
 
Start with 20,000.
 
Deposit 500 monthly.
 
Apply annual interest at 6%.
 
Withdraw 3000 at year-end.
 
Assert the final balance matches a manually calculated value.
 
 
Test that a zero interest rate means the balance never grows.
 
Test that a negative interest rate reduces the balance over time (like a penalty).
