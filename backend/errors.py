import os
from flask import Response, jsonify
from .app import create_app


app = create_app(os.getenv("FLASK_CONFIG") or "default")


class ErrorResponse:

    def __init__(self, message: str, http_status: int):
        self.playload = {
            "success":False,
            "message":message
        }
        self.http_status = http_status

    def to_response(self) -> Response:
        response = jsonify(self.playload)
        response.status_code = self.http_status
        return response


@app.errorhandler(404)
def not_found_error(err):
    return ErrorResponse(err.description, 404).to_response()


@app.errorhandler(400)
def bad_request_error(err):
    massages = err.data.get('messages', {}).get('json', {})
    return ErrorResponse(messages, 404).to_response()