import sqlite3
import logging
from config import DB_FILE
from werkzeug.security import generate_password_hash, check_password_hash

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(levelname)s,%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Account:
    def __init__(self, account_number=None, name=None, email=None, balance=0.0,
                 account_type=None, adhaar_number=None, password=None):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.balance = balance
        self.account_type = account_type
        self.adhaar_number = adhaar_number
        self.password = password
    @staticmethod
    def create_table():
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT,
                balance REAL NOT NULL,
                account_type TEXT NOT NULL,
                adhaar_number TEXT NOT NULL,
                password TEXT NOT NULL
            )
            """)
            conn.commit()
            conn.close()
            logger.info("Accounts table created or already exists.")
        except sqlite3.Error as e:
            logger.error(f"Error creating accounts table: {e}")

    @staticmethod
    def fetch_all():
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts")
            rows = cursor.fetchall()
            conn.close()
            logger.info(f"Fetched {len(rows)} accounts from database.")
            return [Account(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error fetching accounts: {e}")
            return []

    @staticmethod
    def fetch_by_number(account_number):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            conn.close()
            if row:
                logger.info(f"Account {account_number} fetched successfully.")
                return Account(*row)
            else:
                logger.warning(f"Account {account_number} not found.")
                return None
        except sqlite3.Error as e:
            logger.error(f"Database error while fetching account {account_number}: {e}")
            return None

    @staticmethod
    def get_next_account_number():
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(account_number) FROM accounts")
            last_number = cursor.fetchone()[0]
            conn.close()
            next_number = last_number + 1 if last_number else 1006
            logger.info(f"Next account number generated: {next_number}")
            return next_number
        except sqlite3.Error as e:
            logger.error(f"Error generating next account number: {e}")
            return 1006

    def save(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            hashed_password = generate_password_hash(self.password)
            cursor.execute("""
            INSERT INTO accounts (account_number, name, email, balance, account_type, adhaar_number, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (self.account_number, self.name, self.email, self.balance,
                  self.account_type, self.adhaar_number, hashed_password))
            conn.commit()
            conn.close()
            logger.info(f"Account {self.account_number} saved successfully.")
        except sqlite3.Error as e:
            logger.error(f"Error saving account {self.account_number}: {e}")

    def update_balance(self, new_balance):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                           (new_balance, self.account_number))
            conn.commit()
            conn.close()
            self.balance = new_balance
            logger.info(f"Account {self.account_number} balance updated to ₹{new_balance}.")
        except sqlite3.Error as e:
            logger.error(f"Error updating balance for account {self.account_number}: {e}")

    def delete(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
            conn.commit()
            conn.close()
            logger.info(f"Account {self.account_number} deleted successfully.")
        except sqlite3.Error as e:
            logger.error(f"Error deleting account {self.account_number}: {e}")

    @staticmethod
    def fetch_by_credentials(name, adhaar_number):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts WHERE name = ? AND adhaar_number = ?", (name, adhaar_number))
            row = cursor.fetchone()
            conn.close()
            return Account(*row) if row else None
        except sqlite3.Error as e:
            logger.error(f"Error fetching credentials: {e}")
            return None

    def verify_password(self, input_password):
        try:
            return check_password_hash(self.password, input_password)
        except Exception as e:
            logger.error(f"Error verifying password for account {self.account_number}: {e}")
            return False
