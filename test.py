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
























       .Azure Virtual Network (VNet)
The foundation of Azure networking.
Similar to an on-premises network but in the cloud.
Lets you securely connect Azure resources (VMs, databases, apps).
Features:
Isolation: Each VNet is logically isolated.
Subnets: Divide VNet into smaller networks.
Private IPs for internal communication.
Peering → connect VNets across regions.
Integration with on-premises via VPN or ExpressRoute













       import pandas as pd
import sqlite3

class ETLError(Exception):
    pass

def run_etl(csv_file, db_file="bank.db"):
    try:
        # Extract
        df = pd.read_csv(csv_file)
        if df.empty:
            raise ETLError("CSV file is empty!")

        # Transform (basic validation)
        df['balance'] = df['balance'].apply(lambda x: float(x) if x >= 0 else 0)

        # Load
        conn = sqlite3.connect(db_file)
        df.to_sql("accounts", conn, if_exists="replace", index=False)
        conn.close()

        print("ETL Completed Successfully!")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except ETLError as e:
        print(f"ETL Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    run_etl("bank_data.csv")







            import redis

try:
    # Connect to Redis server
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Check connection
    if r.ping():
        print("✅ Connected to Redis!")

    # ---------------------------
    # Set and Get Operations
    # ---------------------------
    r.set('name', 'Alice')
    print("Name stored in Redis:", r.get('name').decode('utf-8'))

    # ---------------------------
    # Working with Numbers
    # ---------------------------
    r.set('count', 10)
    r.incr('count')   # Increment by 1
    print("Updated count:", r.get('count').decode('utf-8'))

    # ---------------------------
    # Storing a List
    # ---------------------------
    r.lpush('tasks', 'task1')
    r.lpush('tasks', 'task2')
    tasks = r.lrange('tasks', 0, -1)
    print("Tasks in Redis list:", [t.decode('utf-8') for t in tasks])

    # ---------------------------
    # Deleting a Key
    # ---------------------------
    r.delete('name')
    print("Deleted key 'name'? Exists:", r.exists('name'))

except redis.ConnectionError as e:
    print(" Redis connection failed:", e)




         from flask import Flask, jsonify
import redis
import logging

# ----------------------------
#  Flask and Redis Setup
# ----------------------------
app = Flask(__name__)

# Connect to Redis (adjust host/port if needed)
try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.ping()  # Test connection
    print(" Connected to Redis successfully!")
except redis.ConnectionError:
    print(" Failed to connect to Redis. Make sure the server is running.")


# ----------------------------
#  Logging Configuration
# ----------------------------
logging.basicConfig(
    filename="flask_redis_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ----------------------------
# Routes
# ----------------------------

@app.route('/')
def home():
    """Home route showing basic info."""
    return jsonify(message="Welcome to Flask + Redis Example!", endpoints=["/set/<key>/<value>", "/get/<key>", "/visits"])


@app.route('/set/<key>/<value>')
def set_value(key, value):
    """Set a key-value pair in Redis."""
    try:
        r.set(key, value)
        logging.info(f"Key set: {key} -> {value}")
        return jsonify(status="success", message=f"Stored {key} = {value} in Redis")
    except Exception as e:
        logging.error(f"Error setting value: {e}")
        return jsonify(status="error", message=str(e)), 500


@app.route('/get/<key>')
def get_value(key):
    """Get a value from Redis."""
    try:
        value = r.get(key)
        if value:
            value = value.decode('utf-8')
            logging.info(f"Key fetched: {key} -> {value}")
            return jsonify(status="success", key=key, value=value)
        else:
            return jsonify(status="error", message=f"Key '{key}' not found"), 404
    except Exception as e:
        logging.error(f"Error fetching value: {e}")
        return jsonify(status="error", message=str(e)), 500


@app.route('/visits')
def visit_counter():
    """Count how many times this endpoint was accessed."""
    try:
        visits = r.incr('visit_count')
        logging.info(f"Visit count updated: {visits}")
        return jsonify(message="Page visit counter", total_visits=visits)
    except Exception as e:
        logging.error(f"Error updating visit count: {e}")
        return jsonify(status="error", message=str(e)), 500


# ----------------------------
# Run the Flask App
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
 
