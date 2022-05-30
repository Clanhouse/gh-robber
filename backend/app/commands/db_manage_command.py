from app import db
from app import GH_API_handling
from app.models_helpers import create_fake_info
from app.commands import db_manage_bp
from ..models import GithubUserInfo
import json
import sys
import os
from datetime import datetime, timedelta


@db_manage_bp.cli.group()
def db_manage():
    """Database management command"""
    pass


@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        create_fake_info(count=10)
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def add_user_from_GH_API(username=None):
    """Add sample user to database"""
    try:
        GH_API_handling.add_user_to_database(username=username)
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def add_repo_from_GH_API(repo_name=None):
    """Add sample user to database"""
    try:
        GH_API_handling.add_repo_to_database(repo_name=repo_name)
        ## GH_API_handling.add_repo_to_database("orzeech/tasks")
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def remove_data():
    """Remove all data form database"""
    try:
        db.session.execute("DROP TABLE gh_repos_and_gh_users")
        db.session.execute("DROP TABLE github_users_info")
        db.session.execute("DROP TABLE github_repositories")
        db.session.commit()
        print("Data has been successfully removed from database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def update_single_repo(repo_name=None):
    try:
        GH_API_handling.update_repo(repo_name=repo_name)
        db.session.commit()
        print("Data has been successfully updated")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def update_single_user(username=None):
    try:
        GH_API_handling.update_user_info(usrname=username)
        db.session.commit()
        print("Data has been successfully updated")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def update_all_users(older_than=None):
    try:
        GH_API_handling.update_all_users(older_than=older_than)
        db.session.commit()
        print("Data has been successfully updated")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def update_all_repos(older_than=None):
    try:
        GH_API_handling.update_all_repos(older_than=None)
        db.session.commit()
        print("Data has been successfully updated")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def fill_repos_with_users():
    try:
        GH_API_handling.fill_repos_with_users()
        db.session.commit()
        print("Data has been successfully updated")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def auto_scraping():
    try:
        os.environ["AUTO_SCRAPING_RUNNING"] = "True"
        GH_API_handling.auto_scraping_GH()
    except Exception as exc:
        print(f"Unexpected error: {exc}")
