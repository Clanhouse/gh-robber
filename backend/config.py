import os
from dotenv import load_dotenv
from pathlib import Path

# basedir = os.path.abspath(os.path.dirname(__file__))

basedir = Path(__file__).resolve().parent


class Config:
    PER_PAGE = 5
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = ""

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DB_FILE_PATH = basedir / "tests" / "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     "TEST_DATABASE_URL"
    # ) or "sqlite:///" + os.path.join(basedir, "data-testing.sqlite")
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
