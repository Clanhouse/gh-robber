import pytest


def test_get_users_info_no_records(client):
    response = client.get("/api/v1.0/users/users")
    expected_result = {
        "data": [],
        "number_of_records": 0,
        "pagination": {
            "current_page": "/api/v1.0/users/users?page=1",
            "next_page": "/api/v1.0/users/users?page=2",
            "total_pages": 0,
            "total_records": 0,
        }
    }
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.get_json() == expected_result


def test_get_users_info(client, sample_data):
    response = client.get("/api/v1.0/users/users")
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json'
    assert response_data["number_of_records"] == 5
    assert len(response_data["data"]) == 10
    assert response_data["pagination"] == {
        "total_pages": 2,
        "total_records": 10,
        "current_page": "/api/v1.0/users/users?page=1",
        "next_page": "/api/v1.0/users/users?page=2"
    }

