import uuid
from typing import Type, List

from sqlalchemy.sql.functions import now
from sqlalchemy.dialects.postgresql import UUID
from API import db
from API.posts.schemas import CreatePostSchema
from API.users.models import Users
from utils.database_utils import DataBase


class Posts(db.Model):
    """Model for posts"""
    __tablename__ = "posts"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("Users")
    time_created = db.Column(db.DateTime, default=now())
    time_updated = db.Column(db.DateTime, default=now())

    @classmethod
    def create(cls, body: CreatePostSchema) -> Type["Posts"] | bool:
        return DataBase.create(cls, body)

    @classmethod
    def get(cls, post_id: uuid) -> Type["Posts"] | bool:
        return DataBase.get(cls, post_id)

    @classmethod
    def get_all(cls) -> List[Type["Posts"]] | bool:
        return DataBase.get_all(cls)

    @classmethod
    def update(cls, body: dict, post_id: uuid) -> Type["Posts"] | bool:
        return DataBase.update(cls, body, post_id)

    @classmethod
    def delete(cls, post_id: uuid) -> Type["Posts"] | bool:
        return DataBase.delete(cls, post_id)

    