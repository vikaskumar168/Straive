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

def deposit_amount(balance, amount):

    logger.info(f"Attempting deposit: balance={balance}, amount={amount}")
    if not isinstance(amount, (int, float)):
        logger.error("Deposit amount must be a number")
        raise ValueError("Deposit amount must be a number")
    if amount <= 0:
        logger.warning("Deposit amount must be positive")
        raise ValueError("Deposit amount must be positive")
    new_balance = balance + amount
    logger.info(f"Deposit successful: new_balance={new_balance}")
    return new_balance

def withdraw_amount(balance, amount):

    logger.info(f"Attempting withdrawal: balance={balance}, amount={amount}")
    if not isinstance(amount, (int, float)):
        logger.error("Withdrawal amount must be a number")
        raise ValueError("Amount must be a number")
    if amount <= 0:
        logger.warning("Withdrawal amount must be positive")
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        logger.warning("Insufficient balance for withdrawal")
        raise ValueError("Insufficient balance")
    new_balance = balance - amount
    logger.info(f"Withdrawal successful: new_balance={new_balance}")
    return new_balance

def calculate_interest(balance, account_type):

    logger.info(f"Calculating interest: balance={balance}, account_type={account_type}")
    if not isinstance(balance, (int, float)):
        logger.error("Balance must be a number")
        raise ValueError("Balance must be a number")
    if account_type.lower() == "savings":
        interest = round(balance * 0.04, 2)
        logger.info(f"Interest for savings account: {interest}")
        return interest, "Interest calculated at 4% for savings account."
    logger.info("No interest applicable for current account")
    return 0.0, "No interest applicable for current account."

def calculate_loan(balance, account_type, loan_type):

    logger.info(f"Calculating loan: balance={balance}, account_type={account_type}, loan_type={loan_type}")
    if not isinstance(balance, (int, float)):
        logger.error("Balance must be a number")
        raise ValueError("Balance must be a number")

    account_type = account_type.lower()
    loan_type = loan_type.lower()

    if account_type == "savings":
        if loan_type in ["car", "home", "education"]:
            loan_amount = round(balance * 0.8, 2)
            logger.info(f"Loan approved for savings account: {loan_amount}")
            return loan_amount
        else:
            logger.warning(f"Loan type '{loan_type}' not eligible for savings account")
    elif account_type == "current":
        if loan_type == "business":
            loan_amount = round(balance * 0.6, 2)
            logger.info(f"Loan approved for current account: {loan_amount}")
            return loan_amount
        else:
            logger.warning(f"Loan type '{loan_type}' not eligible for current account")
    else:
        logger.warning(f"Unknown account type: {account_type}")

    logger.info("Loan not approved")
    return None
