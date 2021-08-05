from pathlib import Path
import json

from backend.app import db, app
from backend.app import GithubUserInfo


@app.cli.group()
def db_manage():
    """Database management command"""
    pass


@db.manage.command()
def add_data():
    """Add sample data to database"""
    try:
        user_info = Path(__file__).parent / "data_sample" / "user_info.json"
        with open(user_info) as file:
            data_json = json.load(file)
        for item in data_json:
            user_info = GithubUserInfo(**item)
            db.session.add(user_info)
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
