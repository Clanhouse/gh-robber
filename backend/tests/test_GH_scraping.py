import pytest
import requests


@pytest.fixture
def repo_test_input():
    return "username_test/reponame_test"


@pytest.fixture
def user_test_input():
    return "username_test"


def test_scrape_repo(repo_test_input):
    # test if api returns proper massage
    # this test to be tested
    response = requests.get(
        f"http://127.0.0.1:5000/api/v1.0/admin/scraping/GH-scrape-repo/{repo_test_input}"
    )
    # response_data = response.get_json()
    expected_result = {
        "message": "Request to scrape repo " "" + repo_test_input + " sent"
    }
    assert response.status_code == 200
    # assert response_data == expected_result


def test_scrape_user(user_test_input):
    # test if api returns proper massage
    # this test to be tested
    response = requests.get(
        f"http://127.0.0.1:5000/api/v1.0/admin/scraping/GH-scrape-user/{user_test_input}"
    )
    # response_data = response.get_json()
    expected_result = {
        "message": "Request to scrape user " "" + user_test_input + " sent"
    }
    assert response.status_code == 200
    # assert response_data == expected_result
