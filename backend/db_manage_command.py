from pathlib import Path
import json

from . import app
from .app import db, app
from .app.models import User, GithubUser, GithubUserInfo, GithubUserInfoSchema
from .app.models_helpers import create_fake_info


@app.cli.group()
def db_manage():
    """Database management command"""
    pass


@db.manage.command()
def add_data():
    """Add sample data to database"""
    try:
        create_fake_info()
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db.manage.command()
def remove_data():
    """Remove all data form database"""
    try:
        db.session.execute("TRUNCATE TABLE user_info")
        db.session.cmmit()
        print("Data has been successfully removed from database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
