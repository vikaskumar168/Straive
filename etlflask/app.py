from flask import Flask, jsonify, request
import sqlite3
import  pandas as pd


app = Flask(__name__)


DB_FILE="bank.db"


def fetch_accounts():
    try:
        conn = sqlite3.connect(DB_FILE)
        df = pd.read_sql("SELECT * FROM accounts",conn)
        conn.close()
        return df
    except Exception as ex:
        return pd.DataFrame({"Error",[str(ex)]})

def deposit_amount(balance, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    return balance + amount

def withdraw_amount(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount



def calculate_interest(balance, account_type):
    if account_type.lower() == "savings":
        return round(balance * 0.04, 2), "Interest calculated at 4% for savings account."
    return 0.0, "No interest applicable for current account."

#
# def calculate_loan(balance, account_type):
#     if account_type.lower() == "savings":
#         return round(balance * 2, 2)
#     elif account_type.lower() == "current":
#         return round(balance * 1.5, 2)
#     return 0.0

def calculate_loan(balance, account_type, loan_type):
    if account_type.lower() == "savings":
        if loan_type.lower() in ["car", "home", "education"]:
            return balance * 0.8
        else:
            return None
    elif account_type.lower() == "current":
        if loan_type.lower() == "business":
            return balance * 0.6
        else:
            return None
    return None



@app.route("/accounts", methods=['GET'])
def get_accounts():
    df = fetch_accounts()
    return jsonify(df.to_dict(orient="records"))


def generate_account_number(cursor):
    pass


@app.route("/add_account", methods=['POST'])
def create_account():
    data = request.get_json()
    required_fields = {"name", "balance", "account_type"}
    if not required_fields.issubset(data.keys()):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(account_number) FROM accounts")
        last_number = cursor.fetchone()[0]
        next_account_number = last_number + 1 if last_number else 1006

        cursor.execute("""
            INSERT INTO accounts (account_number, name, balance, account_type)
            VALUES (?, ?, ?, ?)
        """, (next_account_number, data['name'], data['balance'], data['account_type']))
        conn.commit()
        conn.close()

        return jsonify({
            "message": "Account created successfully",
            "account_number": next_account_number
        }), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500



@app.route("/calculate_interest/<int:account_number>", methods=['GET'])
def get_interest(account_number):
    try:
        conn = sqlite3.connect(DB_FILE)
        df = pd.read_sql("SELECT * FROM accounts WHERE account_number = ?", conn, params=(account_number,))
        conn.close()

        if df.empty:
            return jsonify({"error": "Account not found"}), 404

        row = df.iloc[0]
        interest, message = calculate_interest(row["balance"], row["account_type"])
        return jsonify({
            "account_number": account_number,
            "name": row["name"],
            "account_type": row["account_type"],
            "annual_interest": interest,
            "message": message
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route("/loan/<int:account_number>", methods=["GET"])
# def get_loan(account_number):
#     try:
#         conn = sqlite3.connect(DB_FILE)
#         df = pd.read_sql("SELECT * FROM accounts WHERE account_number = ?", conn, params=(account_number,))
#         conn.close()
#
#         if df.empty:
#             return jsonify({"error": "Account not found"}), 404
#
#         row = df.iloc[0]
#         loan = calculate_loan(row["balance"], row["account_type"])
#         return jsonify({
#             "account_number": account_number,
#             "name": row["name"],
#             "eligible_loan": loan
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route("/loan/<int:account_number>", methods=["GET"])
def get_loan(account_number):
    loan_type = request.args.get("loan_type")
    tan_number = request.args.get("tan_number")

    try:
        conn = sqlite3.connect(DB_FILE)
        df = pd.read_sql("SELECT * FROM accounts WHERE account_number = ?", conn, params=(account_number,))
        conn.close()

        if df.empty:
            return jsonify({"error": "Account not found"}), 404

        row = df.iloc[0]
        account_type = row["account_type"].lower()


        if not loan_type:
            return jsonify({"error": "Missing loan_type parameter"}), 400

        if account_type == "current" and not tan_number:
            return jsonify({"error": "TAN number is required for current accounts"}), 400

        if account_type == "savings" and loan_type not in ["car", "home", "education"]:
            return jsonify({"error": f"{loan_type} loan is not available for savings accounts"}), 400
        if account_type == "current" and loan_type != "business":
            return jsonify({"error": f"{loan_type} loan is not available for current accounts"}), 400

        loan_amount = calculate_loan(row["balance"], account_type, loan_type)
        if loan_amount is None:
            return jsonify({"error": "Loan type not eligible"}), 400

        return jsonify({
            "account_number": account_number,
            "name": row["name"],
            "account_type": account_type,
            "loan_type": loan_type,
            "eligible_loan": loan_amount
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/delete_account/<int:account_number>", methods=["DELETE"])
def delete_account(account_number):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({"error": "Account not found"}), 404

        return jsonify({"message": f"Account {account_number} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/transaction", methods=["PUT"])
def process_transaction():
    data = request.get_json()
    required_fields = {"account_number", "amount", "is_deposit"}
    if not required_fields.issubset(data.keys()):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        account_number = data["account_number"]
        amount = float(data["amount"])
        is_deposit = bool(data["is_deposit"])

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            return jsonify({"error": "Account not found"}), 404

        current_balance = result[0]

        if is_deposit:
            new_balance = deposit_amount(current_balance, amount)
            action = "Deposit"
        else:
            new_balance = withdraw_amount(current_balance, amount)
            action = "Withdrawal"

        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
        conn.commit()
        conn.close()

        return jsonify({
            "message": f"{action} successful",
            "account_number": account_number,
            "new_balance": round(new_balance, 2)
        }), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)