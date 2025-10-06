import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token
from controllers.accountcontroller import account_bp

class AccountControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["JWT_SECRET_KEY"] = "test-secret"
        JWTManager(self.app)
        self.app.register_blueprint(account_bp)
        self.client = self.app.test_client()
        self.token = create_access_token(identity=1)
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @patch("models.account.Account.fetch_all")
    def test_get_accounts(self, mock_fetch_all):
        mock_account = MagicMock()
        mock_account.account_number = 1
        mock_account.name = "Alice"
        mock_account.email = "alice@example.com"
        mock_account.balance = 1000.0
        mock_account.account_type = "savings"
        mock_fetch_all.return_value = [mock_account]

        response = self.client.get("/accounts", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alice", response.get_data(as_text=True))

    @patch("models.account.Account.save")
    @patch("models.account.Account.get_next_account_number", return_value=101)
    def test_create_account_success(self, mock_next_number, mock_save):
        payload = {
            "name": "Bob",
            "balance": 5000,
            "account_type": "savings",
            "adhaar_number": "123456789012",
            "email": "bob@example.com",
            "password": "securepass123"
        }
        response = self.client.post("/add_account", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Account created", response.get_data(as_text=True))

    def test_create_account_missing_fields(self):
        payload = {"name": "Bob"}
        response = self.client.post("/add_account", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing required fields", response.get_data(as_text=True))

    @patch("models.account.Account.fetch_by_number")
    @patch("utils.helper.calculate_interest", return_value=(120.0, "Interest calculated"))
    def test_calculate_interest(self, mock_calc_interest, mock_fetch):
        mock_account = MagicMock()
        mock_account.account_number = 1
        mock_account.name = "Alice"
        mock_account.account_type = "savings"
        mock_account.balance = 1000.0
        mock_fetch.return_value = mock_account

        response = self.client.get("/calculate_interest", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Interest calculated", response.get_data(as_text=True))

    @patch("models.account.Account.fetch_by_number")
    def test_delete_account(self, mock_fetch):
        mock_account = MagicMock()
        mock_fetch.return_value = mock_account
        response = self.client.delete("/delete_account", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted", response.get_data(as_text=True))
        mock_account.delete.assert_called_once()

    @patch("models.account.Account.fetch_by_number")
    def test_transaction_deposit(self, mock_fetch):
        mock_account = MagicMock(account_number=1, balance=1000)
        mock_fetch.return_value = mock_account
        payload = {"amount": 500, "is_deposit": True}
        response = self.client.put("/transaction", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Deposit successful", response.get_data(as_text=True))

    @patch("models.account.Account.fetch_by_number")
    def test_transaction_withdrawal(self, mock_fetch):
        mock_account = MagicMock(account_number=1, balance=1000)
        mock_fetch.return_value = mock_account
        payload = {"amount": 200, "is_deposit": False}
        response = self.client.put("/transaction", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Withdrawal successful", response.get_data(as_text=True))

    @patch("models.account.Account.fetch_by_number")
    def test_get_my_account(self, mock_fetch):
        mock_account = MagicMock()
        mock_account.account_number = 1
        mock_account.name = "Alice"
        mock_account.email = "alice@example.com"
        mock_account.balance = 1000.0
        mock_account.account_type = "savings"
        mock_fetch.return_value = mock_account

        response = self.client.get("/my_account", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alice", response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()

