from flask import abort
from webargs.flaskparser import use_args

from backend.auth import auth
from backend.app.models import User, user_schema
from backend.utils import validate_json_content_type



@auth_bp.route('/register', methods=['POST'])
@validate_json_content_type
@use_args(user_schema, error_status_code=400)
def register(args: dict):
    if User.query.filter(User.username == args["username"]).first():
        abort(409, description=f"User with username {args['username']} already exists")
    if User.query.filter(User.email == args["email"]).first():
        abort(409, description=f"User with email {args['email']} already exists")