import logging
# External Imports
from flask import Flask
from flask_jwt_extended import JWTManager


# Setup JWT
jwt = JWTManager()

# Setup Logging


def initialize_blueprints(app: object) -> None:
    """Register Flask blueprints"""
    from system.api import system_api_bp
    app.register_blueprint(
        system_api_bp
    )


def create_app() -> Flask:
    # Define Flask Application as app.
    app = Flask(__name__)

    # Load all endpoints in to Application.
    initialize_blueprints(app)

    # Setup JWT
    jwt.init_app(app)

    return app
