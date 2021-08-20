import os
from flask import Response, jsonify

from .app import db
from .app import create_app
from flask_migrate import Migrate, upgrade


app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


class ErrorResponse:

    def __init__(self, message: str, http_status: int):
        self.playload = {
            "success": False,
            "message": message
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
    messages = err.data.get('messages', {}).get('json', {})
    return ErrorResponse(messages, 404).to_response()


@app.errorhandler(415)
def unsupported_media_type_error(err):
    return ErrorResponse(err.description, 415).to_response()


@app.errorhandler(500)
def internal_server_error(err):
    db.session.rollback()
    return ErrorResponse(err.description, 500).to_response()