import os
from dotenv import load_dotenv
from pathlib import Path


basedir = Path(__file__).resolve().parent
env_file = basedir / ".env"
load_dotenv(env_file)


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = ""
    PER_PAGE = 5
    JWT_EXPIRED_MINUTES = 30


class TestingConfig(Config):
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DB_FILE_PATH = basedir / "tests" / "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class ProductionConfig(Config):
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
