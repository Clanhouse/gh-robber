from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api/v1.0")
users_api = Blueprint("users_api", __name__, url_prefix="/users")
api.register_blueprint(users_api)

from . import (
    users,
)  # Blueprints needs to be created before assigning api endpoint to them.
