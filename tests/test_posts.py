import pytest
import requests

from jsonschema import validate
from tests.ustils_tests import TestData
from test_users import TestUsers

user_create = TestUsers.create_test_record


class TestPosts:
    """Test posts module"""

    @staticmethod
    @pytest.fixture
    def create_post_user():
        body = TestData.user_body
        response = requests.post(f"{TestData.url_path}/api/users", json=body).json()
        yield response.get("id")
        requests.delete(f"{TestData.url_path}/api/users/{response.get('id')}")

    @staticmethod
    @pytest.fixture
    def create_test_record():
        body = TestData.user_body
        response = requests.post(f"{TestData.url_path}/api/users", json=body).json()
        user_id = response.get("id")

        body = TestData.post_body
        body["author_id"] = user_id
        response = requests.post(f"{TestData.url_path}/api/posts", json=body).json()
        post_id = response.get("id")

        yield post_id

        requests.delete(f"{TestData.url_path}/api/posts/{post_id}")
        requests.delete(f"{TestData.url_path}/api/users/{user_id}")

    @staticmethod
    def test_create_post(create_post_user):
        body = TestData.post_body
        body["author_id"] = create_post_user
        response = requests.post(f"{TestData.url_path}/api/posts", json=body)
        assert response.status_code == 201
        validate(instance=response.json(), schema=TestData.post_get_schema)
        requests.delete(f"http://localhost:5000/api/posts/{response.json().get('id')}")

    @staticmethod
    def test_get_post(create_test_record):
        post_id = create_test_record
        response = requests.get(f"{TestData.url_path}/api/posts/{post_id}")
        data = response.json()
        assert response.status_code == 200
        validate(instance=data, schema=TestData.post_get_schema)
        assert data["id"] == post_id

    @staticmethod
    def test_get_all_posts(create_test_record):
        response = requests.get(f"{TestData.url_path}/api/posts")
        assert response.status_code == 200
        assert type(response.json()) == list

    @staticmethod
    def test_update_post(create_test_record):
        post_id = create_test_record
        body = TestData.post_update_body
        response = requests.put(f"{TestData.url_path}/api/posts/{post_id}", json=body)
        assert response.status_code == 200

    @staticmethod
    def test_delete_post(create_post_user):
        body = TestData.post_body
        body["author_id"] = create_post_user
        post = requests.post(f"{TestData.url_path}/api/posts", json=body)
        response = requests.delete(
            f"{TestData.url_path}/api/posts/{post.json().get('id')}"
        )
        assert response.status_code == 200
