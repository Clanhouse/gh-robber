import pytest

from backend.app import create_app, db


@pytest.fixture()
def app():
    app = create_app("testing")

    with app.app_context():
        db.create_all()

    yield app

    app.config("DB_FILE_PATH").unlink(missing_ok=True)


