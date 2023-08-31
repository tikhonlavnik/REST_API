import datetime
import uuid
from typing import List

from pydantic import BaseModel


class CreatePostSchema(BaseModel):
    title: str
    description: str
    author_id: uuid.UUID


class PostSchema(BaseModel):
    id: uuid.UUID


class BasePostSchema(PostSchema, CreatePostSchema):
    time_created: datetime.datetime
    time_updated: datetime.datetime


class PostsList(BaseModel):
    users: List[BasePostSchema]


class SuccessUpdatePostSchema(PostSchema):
    pass


class SuccessDeletePostSchema(PostSchema):
    pass
