import uuid
from typing import Type, List

from sqlalchemy.sql.functions import now
from sqlalchemy.dialects.postgresql import UUID

from API import db
from API.users.schemas import CreateUserSchema
from utils.database_utils import DataBase


class Users(db.Model):
    """Model for users"""
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    time_created = db.Column(db.DateTime, default=now())

    @classmethod
    def create(cls, body: CreateUserSchema) -> Type["Users"] | bool:
        return DataBase.create(cls, body)

    @classmethod
    def get(cls, user_id: uuid) -> Type["Users"] | bool:
        return DataBase.get(cls, user_id)

    @classmethod
    def get_all(cls) -> List[Type["Users"]] | bool:
        return DataBase.get_all(cls)

    @classmethod
    def update(cls, body: dict, user_id: uuid) -> Type["Users"] | bool:
        return DataBase.update(cls, body, user_id)

    @classmethod
    def delete(cls, user_id: uuid) -> Type["Users"] | bool:
        return DataBase.delete(cls, user_id)
