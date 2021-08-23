from flask import Blueprint

errors_bp = Blueprint("errors", __name__)

from backend.errors import errors