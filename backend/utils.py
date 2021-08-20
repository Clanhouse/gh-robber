from flask import request
from werkzeug.exceptions import UnsupportedMediaType
from functools import wraps


def validate_json_content_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if data is None:
            raise UnsupportedMediaType("Content type must be application/json")
        return func(*args, **kwargs)

    return wrapper
