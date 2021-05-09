from flask import Flask


def create_app():
    app = Flask(__name__)

    # fmt: off
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')
    # fmt: on

    return app
