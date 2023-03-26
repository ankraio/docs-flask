# External Imports
import logging
from flask import (
    current_app as app,
    Blueprint,
    jsonify,
    request
)
from flask_jwt_extended import (
    jwt_required
)

# Local Imports
from utils.system import (
    status
)

# Blueprint Setup
system_api_bp = Blueprint(
    "system_api_bp",
    __name__,
    url_prefix='/api/v1.0/system'
)

@system_api_bp.route("/status", methods=["POST"])
@jwt_required()
def unseal():
    """
    System status
    
        Returns:
            Flask Response: Flask Response Object
    """
    # Get system data
    data=status(app)
    # Check if data is empty
    if not data:
        return jsonify(
            status="error",
            message="No system data found"
        ), 404
    # Return data
    return jsonify(
        status="ok",
        data=data
    ), 200
