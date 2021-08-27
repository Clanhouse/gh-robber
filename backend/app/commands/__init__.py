from flask import Blueprint

db_manage_bp = Blueprint("db_manage_cmd", __name__, cli_group=None)

from backend.app.commands import db_manage_command
