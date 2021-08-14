from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api/v1.0")
users_api = Blueprint("users_api", __name__, url_prefix="/users")
admin_api = Blueprint("admin_api", __name__, url_prefix="/admin")
api.register_blueprint(users_api)
api.register_blueprint(admin_api)

from . import (
    users,
    admin
)  # Blueprints needs to be created before assigning api endpoint to them.
