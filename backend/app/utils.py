import jwt
from flask import request, url_for, current_app, abort
from werkzeug.exceptions import UnsupportedMediaType
from functools import wraps


def validate_json_content_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if data is None:
            raise UnsupportedMediaType('Content type must be application/json')
        return func(*args, **kwargs)
    return wrapper


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        auth = request.headers.get('Authorization')
        if auth:
            token = auth.split(' ')[1]
        if token is None:
            abort(401, description='Missing token. Please login or register')

        try:
            payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            abort(401, description='Expired token. Please login to get new token')
        except jwt.InvalidTokenError:
            abort(401, description='Invalid token. Please login or register')
        else:
            return func(payload['user_id'], *args, **kwargs)
    return wrapper
