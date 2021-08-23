from pathlib import Path
import json

from backend.app import db
from backend.app.models import GithubUserInfo, GithubUserInfoSchema
from backend.app.models_helpers import create_fake_info
from . import db_manage_bp


@db_manage_bp.cli.group()
def db_manage():
    """Database management command"""
    pass


@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        create_fake_info()
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def remove_data():
    """Remove all data form database"""
    try:
        db.session.execute("TRUNCATE TABLE user_info")
        db.session.cmmit()
        print("Data has been successfully removed from database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
