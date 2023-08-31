from faker import Faker

from config import Config

faker = Faker()
faker.seed_instance(4321)


class TestData:
    """ Class contains all necessary data for tests """
    url_path = "http://localhost:5000"

    # for users table

    user_get_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "username": {"type": "string"},
            "birthday": {"type": "string", "format": "date"},
            "time_created": {"type": "string", "format": "date-time"}
        },
        "required": ["id", "username", "birthday", "time_created"]
    }

    user_body = {
        "username": faker.name(),
        "password": faker.password(),
        "birthday": faker.date()
    }

    user_update_body = {
        "username": faker.name()
    }

    # for posts table

    post_get_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "title": {"type": "string"},
            "description": {"type": "string"},
            "author_id": {"type": "string"},
            "time_created": {"type": "string", "format": "date-time"},
            "time_updated": {"type": "string", "format": "date-time"}
        },
        "required": ["id", "title", "description", "author_id", "time_created", "time_updated"]
    }

    post_body = {
        "title": faker.name(),
        "description": faker.text(),
    }

    post_update_body = {
        "title": faker.name()
    }

