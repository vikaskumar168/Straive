from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
import logging

from models.account import Account

auth_bp = Blueprint("auth_bp", __name__)

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

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    name = data.get("name")
    adhaar_number = data.get("adhaar_number")
    password = data.get("password")

    logger.info(f"Login attempt for name={name}, adhaar={adhaar_number}")

    if not all([name, adhaar_number, password]):
        logger.warning("Missing login fields")
        return jsonify({"error": "Missing login fields"}), 400

    account = Account.fetch_by_credentials(name, adhaar_number)
    if not account or not check_password_hash(account.password, password):
        logger.warning("Invalid login credentials")
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(account.account_number))
    logger.info(f"Login successful for account {account.account_number}")
    return jsonify(access_token=access_token), 200
