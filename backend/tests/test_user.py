import pytest


def test_get_users_info_no_records(client):
    response = client.get("/api/v1.0/users/users")
    expected_result = {
        "data": [],
        "numbers_of_records": 0,
        "pagination": {
            "current_page": "/api/v1.0/users/users?page=1",
            "total_pages": 0,
            "total_records": 0,
        },
    }
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.get_json() == expected_result


def test_get_users_info(client, sample_data):
    response = client.get("/api/v1.0/users/users")
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_data["numbers_of_records"] == 5
    assert response_data["pagination"] == {
        "total_pages": 2,
        "total_records": 10,
        "current_page": "/api/v1.0/users/users?page=1",
        "next_page": "/api/v1.0/users/users?page=2",
    }


def test_get_users_info_with_params(client, sample_data):
    response = client.get("/api/v1.0/users/users?fields=username&sort=-id&page=2&limit=2")
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json'
    assert response_data["numbers_of_records"] == 2
    assert response_data["pagination"] == {
        "total_pages": 5,
        "total_records": 10,
        "current_page": "/api/v1.0/users/users?page=2&fields=username&sort=-id&limit=2",
        "next_page": "/api/v1.0/users/users?page=3&fields=username&sort=-id&limit=2",
        "previous_page": "/api/v1.0/users/users?page=1&fields=username&sort=-id&limit=2"
    }
    assert len(response_data["data"]) == 2
    assert response_data["data"][0]["username"] is not None
    assert isinstance(response_data["data"][0]["username"], str)


def test_single_github_user_info(client, sample_data):
    response = client.get("/api/v1.0/users/users/2")
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_data["data"]["username"] is not None
    assert response_data["data"]["date"] is not None
    assert response_data["data"]["language"] is not None
    assert response_data["data"]["stars"] is not None
    assert response_data["data"]["number_of_repositories"] is not None


def test_single_github_user_info_not_found(client, sample_data):
    response = client.get("/api/v1.0/users/users/9999")
    response_data = response.get_json()
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"
    assert "data" not in response_data


def test_create_github_user(client, token, github_user_info):
    response = client.post(
        "/api/v1.0/users/users",
        json=github_user_info,
        headers={"Authorization": f"Bearer {token}"},
    )
    response_data = response.get_json()
    expected_result = {"success": True, "data": {**github_user_info, "id": 1}}

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    assert response_data == expected_result

    response = client.get("/api/v1.0/users/users/1")
    response_data = response.get_json()
    expected_result = {"success": True, "data": {**github_user_info, "id": 1}}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_data == expected_result


@pytest.mark.parametrize(
    "data,missing_field",
    [
        (
            {
                "language": "language",
                "date": "10-10-2000",
                "stars": 10,
                "number_of_repositories": 30,
            },
            "username",
        ),
        (
            {
                "username": "test",
                "date": "10-10-2000",
                "stars": 10,
                "number_of_repositories": 30,
            },
            "language",
        ),
        (
            {
                "username": "test",
                "language": "language",
                "stars": 10,
                "number_of_repositories": 30,
            },
            "date",
        ),
        (
            {
                "username": "test",
                "language": "language",
                "date": "10-10-2000",
                "number_of_repositories": 30,
            },
            "stars",
        ),
        (
            {
                "username": "test",
                "language": "language",
                "date": "10-10-2000",
                "stars": 10,
            },
            "number_of_repositories",
        ),
    ],
)
def test_create_github_user_info_invalid_data(client, token, data, missing_field):
    response = client.post(
        "/api/v1.0/users/users", json=data, headers={"Authorization": f"Bearer {token}"}
    )
    response_data = response.get_json()
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert "token" not in response_data
    assert missing_field in response_data["message"]
    assert "Missing data for required field." in response_data["message"][missing_field]


def test_create_github_user_info_invalid_content_type(client, token, github_user_info):
    response = client.post(
        "/api/v1.0/users/users",
        data=github_user_info,
        headers={"Authorization": f"Bearer {token}"},
    )
    response_data = response.get_json()
    assert response.status_code == 415
    assert response.headers["Content-Type"] == "application/json"
    assert "data" not in response_data


def test_create_github_user_info_missing_token(client, github_user_info):
    response = client.post("/api/v1.0/users/users", json=github_user_info)
    response_data = response.get_json()
    assert response.headers["Content-Type"] == "application/json"
    assert "data" not in response_data
    assert response.status_code == 401
