import pytest

from app import create_app, db
from app.commands.db_manage_command import add_data


@pytest.fixture
def app():
    app = create_app('testing')

    with app.app_context():
        db.create_all()

    yield app

    app.config['DB_FILE_PATH'].unlink(missing_ok=True)


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def user(client):
    user = {"username": "test", "password": "123456", "email": "test@gmail.com"}
    client.post("/auth/register", json=user)
    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        "/auth/login", json={"username": user["username"], "password": user["password"]}
    )
    return response.get_json()["token"]



@pytest.fixture
def sample_data(app):
    runner = app.test_cli_runner()
    runner.invoke(add_data)


@pytest.fixture
def github_user_info():
    return {
        "username": "test",
        "language": "language",
        "date": "10-10-2000",
        "stars": 10,
        "number_of_repositories": 30
    }

