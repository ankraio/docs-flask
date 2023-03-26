# External Imports
from flask import Flask
from flask_jwt_extended import JWTManager

# Ankra Imports
from ankra import (
    Config,
    get_logger
)

# Setup JWT
jwt = JWTManager()

# Setup Logging
logging = get_logger()


def initialize_blueprints(app: object) -> None:
    """Register Flask blueprints"""
    from system.api import system_api_bp
    app.register_blueprint(
        system_api_bp
    )


def create_app() -> Flask:
    # Define Flask Application as app.
    app = Flask(__name__)

    # Fetch & setup config in Application.
    Config(
        app=app,
        fetch_common_secret=False
    )

    # Load all endpoints in to Application.
    initialize_blueprints(app)

    # Setup JWT
    jwt.init_app(app)

    logging.info(
        f"Application running in {app.config['ENV']} mode"
    )
    return app
