from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

from flask_limiter import Limiter
from flask_login import LoginManager, current_user
from flask_redis import FlaskRedis
from flask_socketio import SocketIO
import base64
import hmac
import time
import logging

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins='*')
limiter = Limiter(key_func=lambda: current_user.id)
login_manager = LoginManager()
# mysql = Database(autocommit=True)
redis = FlaskRedis()
cors = CORS()


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.commands import db_manage_bp
    from app.errors import errors_bp
    from app.api.ver_1_0 import users_api
    from app.auth import auth_bp
    app.register_blueprint(db_manage_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(users_api)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # fmt: off
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api.ver_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint)
    # fmt: on

    return app
