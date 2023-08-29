from faker import Faker

faker = Faker()
faker.seed_instance(4321)


class TestData:
    url_path = "http://localhost:5000"

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

    body = {
        "username": faker.name(),
        "password": faker.password(),
        "birthday": faker.date()
    }

    update_body = {
        "username": faker.name()
    }

