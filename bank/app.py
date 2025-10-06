import logging

from flask_jwt_extended import JWTManager

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


from flask import Flask, jsonify
from controllers.accountcontroller import account_bp
from controllers.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(account_bp)

app.config["JWT_SECRET_KEY"] = "vashisoumyayuvikash"
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    logger.info("Starting Flask application...")
    app.run(debug=True)
