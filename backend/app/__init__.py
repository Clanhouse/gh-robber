from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)

    # fmt: off
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api.ver_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint)
    # fmt: on

    return app
