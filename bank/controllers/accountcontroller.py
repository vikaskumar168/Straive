from flask import Blueprint, request, jsonify
from models.account import Account
from utils.helper import *
from flask_jwt_extended import jwt_required, get_jwt_identity

import logging

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

class AccountNotFoundError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

account_bp = Blueprint("account_bp", __name__)
Account.create_table()

@account_bp.route("/accounts", methods=["GET"])
@jwt_required()
def get_accounts():
    logger.info("Fetching all accounts")
    try:
        accounts = Account.fetch_all()
        logger.info(f"Fetched {len(accounts)} accounts")
        return jsonify([{
            "account_number": acc.account_number,
            "name": acc.name,
            "email": acc.email,
            "balance": acc.balance,
            "account_type": acc.account_type
            # "password":acc.password
        } for acc in accounts])
    except Exception as e:
        logger.error(f"Error fetching accounts: {e}")
        return jsonify({"error": "Failed to fetch accounts"}), 500

@account_bp.route("/add_account", methods=["POST"])
def create_account():
    data = request.get_json()
    logger.info(f"Received account creation request: {data}")
    required_fields = {"name", "balance", "account_type", "adhaar_number", "password"}
    if not required_fields.issubset(data.keys()):
        logger.warning("Missing required fields in account creation")
        return jsonify({"error": "Missing required fields"}), 400

    if not data["adhaar_number"]:
        logger.warning("Adhaar number missing in account creation")
        return jsonify({"error": "Adhaar Number is required for opening an account"}), 400

    try:
        account_number = Account.get_next_account_number()
        new_account = Account(
            account_number=account_number,
            name=data["name"],
            email=data.get("email", ""),
            balance=float(data["balance"]),
            account_type=data["account_type"],
            adhaar_number=data["adhaar_number"],
            password=data["password"]
        )
        new_account.save()
        logger.info(f"Account created successfully: {account_number}")
        return jsonify({"message": "Account created", "account_number": account_number}), 201
    except Exception as ex:
        logger.error(f"Error creating account: {ex}")
        return jsonify({"error": str(ex)}), 500

@account_bp.route("/calculate_interest", methods=["GET"])
@jwt_required()
def get_interest():
    account_number = get_jwt_identity()
    logger.info(f"Calculating interest for account: {account_number}")
    try:
        account = Account.fetch_by_number(account_number)
        if not account:
            raise AccountNotFoundError("Account not found")
        interest, message = calculate_interest(account.balance, account.account_type)
        logger.info(f"Interest calculated for account {account_number}: {interest}")
        return jsonify({
            "account_number": account.account_number,
            "name": account.name,
            "account_type": account.account_type,
            "annual_interest": interest,
            "message": message
        })
    except AccountNotFoundError as e:
        logger.warning(f"Interest calculation failed: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unexpected error during interest calculation: {e}")
        return jsonify({"error": str(e)}), 500

@account_bp.route("/loan", methods=["GET"])
@jwt_required()
def get_loan():
    account_number = get_jwt_identity()
    loan_type = request.args.get("loan_type")
    tan_number = request.args.get("tan_number")
    pancard_number = request.args.get("pancard_number")

    logger.info(f"Loan request for account {account_number}")
    logger.info(f"Params: loan_type={loan_type}, tan_number={tan_number}, pancard_number={pancard_number}")

    try:
        account = Account.fetch_by_number(account_number)
        if not account:
            raise AccountNotFoundError("Account not found")

        if not pancard_number or pancard_number.strip() == "":
            logger.warning("Missing PAN card number")
            return jsonify({"error": "PAN card number is required for all accounts"}), 400

        if not loan_type:
            logger.warning("Missing loan_type")
            return jsonify({"error": "Missing loan_type"}), 400

        if account.account_type.lower() == "current" and not tan_number:
            logger.warning("Missing TAN number for current account")
            return jsonify({"error": "TAN number is required for current accounts"}), 400

        if account.account_type.lower() == "savings" and loan_type.lower() not in ["car", "home", "education"]:
            logger.warning(f"Invalid loan type for savings account: {loan_type}")
            return jsonify({"error": f"{loan_type} loan not available for savings"}), 400

        if account.account_type.lower() == "current" and loan_type.lower() != "business":
            logger.warning(f"Invalid loan type for current account: {loan_type}")
            return jsonify({"error": f"{loan_type} loan not available for current"}), 400

        loan_amount = calculate_loan(account.balance, account.account_type, loan_type)
        if loan_amount is None:
            logger.warning("Loan type not eligible")
            return jsonify({"error": "Loan type not eligible"}), 400

        logger.info(f"Loan approved for account {account_number}: {loan_amount}")
        return jsonify({
            "account_number": account.account_number,
            "name": account.name,
            "account_type": account.account_type,
            "loan_type": loan_type,
            "eligible_loan": loan_amount,
            "pancard_number": pancard_number
        })
    except AccountNotFoundError as e:
        logger.warning(f"Loan request failed: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unexpected error during loan processing: {e}")
        return jsonify({"error": str(e)}), 500

@account_bp.route("/delete_account", methods=["DELETE"])
@jwt_required()
def delete_account_route():
    account_number = get_jwt_identity()
    logger.info(f"Delete request for account {account_number}")
    try:
        account = Account.fetch_by_number(account_number)
        if not account:
            raise AccountNotFoundError("Account not found")
        account.delete()
        logger.info(f"Account {account_number} deleted successfully")
        return jsonify({"message": f"Account {account_number} deleted"}), 200
    except AccountNotFoundError as e:
        logger.warning(f"Delete failed: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unexpected error during account deletion: {e}")
        return jsonify({"error": str(e)}), 500

@account_bp.route("/transaction", methods=["PUT"])
@jwt_required()
def process_transaction():
    data = request.get_json()
    logger.info(f"Transaction request: {data}")
    required_fields = {"amount", "is_deposit"}
    if not required_fields.issubset(data.keys()):
        logger.warning("Missing required fields in transaction")
        return jsonify({"error": "Missing required fields"}), 400
    try:
        account_number = get_jwt_identity()
        amount = float(data["amount"])
        is_deposit = bool(data["is_deposit"])

        account = Account.fetch_by_number(account_number)
        if not account:
            raise AccountNotFoundError("Account not found")

        if is_deposit:
            new_balance = deposit_amount(account.balance, amount)
            action = "Deposit"
        else:
            new_balance = withdraw_amount(account.balance, amount)
            action = "Withdrawal"

        account.update_balance(new_balance)
        logger.info(f"{action} of ₹{amount} successful for account {account_number}")
        return jsonify({
            "message": f"{action} successful",
            "account_number": account.account_number,
            "new_balance": round(new_balance, 2)
        }), 200
    except AccountNotFoundError as e:
        logger.warning(f"Transaction failed: {e}")
        return jsonify({"error": str(e)}), 404
    except ValueError as ve:
        logger.error(f"Value error during transaction: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logger.error(f"Unexpected error during transaction: {e}")
        return jsonify({"error": str(e)}), 500

@account_bp.route("/my_account", methods=["GET"])
@jwt_required()
def get_my_account():
    account_number = int(get_jwt_identity())
    logger.info(f"Fetching account details for JWT identity: {account_number}")
    account = Account.fetch_by_number(account_number)
    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "account_number": account.account_number,
        "name": account.name,
        "email": account.email,
        "balance": account.balance,
        "account_type": account.account_type
    })

