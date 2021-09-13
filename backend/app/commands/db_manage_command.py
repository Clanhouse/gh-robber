from app import db
from app import GH_API_handling
from app.models_helpers import create_fake_info
from app.commands import db_manage_bp


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
def add_data_from_GH_API():
    """Add sample data to database"""
    try:
        GH_API_handling.search_for_repositories('python', 3, '>20000') 
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        

@db_manage.command()
def add_single_user_from_GH_API():
    """Add sample user to database"""
    try:
        GH_API_handling.search_for_user('orzeech') 
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


@db_manage.command()
def remove_data():
    """Remove all data form database"""
    try:
        db.session.execute("DROP TABLE github_users_info")
        db.session.commit()
        print("Data has been successfully removed from database")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
