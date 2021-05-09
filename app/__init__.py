from flask import Flask


def create_app():
    app = Flask(__name__)

    # fmt: off
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # fmt: on

    return app
