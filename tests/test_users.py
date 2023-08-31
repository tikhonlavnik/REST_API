import pytest
import requests

from jsonschema import validate
from tests.ustils_tests import TestData


class TestUsers:
    """ Test users module """
    @staticmethod
    @pytest.fixture
    def create_test_record():
        body = TestData.user_body
        response = requests.post(f"{TestData.url_path}/api/users", json=body).json()
        yield response.get('id')
        requests.delete(f"{TestData.url_path}/api/users/{response.get('id')}")

    @staticmethod
    def test_create_user():
        body = TestData.user_body
        response = requests.post(f"{TestData.url_path}/api/users", json=body)
        assert response.status_code == 201
        validate(instance=response.json(), schema=TestData.user_get_schema)
        requests.delete(f"http://localhost:5000/api/users/{response.json().get('id')}")

    @staticmethod
    def test_get_user(create_test_record):
        user_id = create_test_record
        response = requests.get(f"{TestData.url_path}/api/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        validate(instance=data, schema=TestData.user_get_schema)
        assert data["id"] == user_id

    @staticmethod
    def test_get_all_users(create_test_record):
        response = requests.get(f"{TestData.url_path}/api/users")
        assert response.status_code == 200
        assert type(response.json()) == list

    @staticmethod
    def test_update_user(create_test_record):
        user_id = create_test_record
        body = TestData.user_update_body
        response = requests.put(f"{TestData.url_path}/api/users/{user_id}", json=body)
        assert response.status_code == 200

    @staticmethod
    def test_delete_user():
        body = TestData.user_body
        user = requests.post(f"{TestData.url_path}/api/users", json=body).json()
        response = requests.delete(f"{TestData.url_path}/api/users/{user.get('id')}")
        assert response.status_code == 200
