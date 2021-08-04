from pathlib import Path
import json

from . import db, app
from .models import GithubUserInfo


@db.manage.command()
def add_data():
    """Add sample data to database"""
    user_info = Path(__file__).parent / "data_sample"/ "user_info.json"
    with open(user_info) as file:
        data_json = json.load(file)
    for item in data_json:
        pass
