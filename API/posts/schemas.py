import datetime
import uuid
from typing import List

from pydantic import BaseModel


class CreatePostSchema(BaseModel):
    title: str
    description: str
    author_id: uuid.UUID


class SuccessPostSchema(BaseModel):
    id: uuid.UUID


class BasePostSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    author_id: uuid.UUID
    time_created: datetime.datetime
    time_updated: datetime.datetime


class PostsList(BaseModel):
    users: List[BasePostSchema]


class SuccessUpdatePostSchema(SuccessPostSchema):
    pass


class SuccessDeletePostSchema(SuccessPostSchema):
    pass
