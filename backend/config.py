import os
from dotenv import load_dotenv
from pathlib import Path


basedir = Path(__file__).resolve().parent
env_file = basedir / "env.txt"
load_dotenv(env_file)


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = ""
    PER_PAGE = 5
    JWT_EXPIRED_MINUTES = 30


class TestingConfig(Config):
    DB_FILE_PATH = basedir / "tests" / "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI=f'mysql+pymysql://root:plyta123@localhost/github_user_info?charset=utf8mb4'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # DB_USERNAME = os.environ.get('root')
    # DB_PASSWORD = os.environ.get('plyta123')
    # DB_HOST = os.environ.get('localhost')
    # DB_NAME = os.environ.get('github_user_info')
    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'


class ProductionConfig(Config):
    DB_HOST = os.environ.get('DB_HOST')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
