import datetime
import uuid
from typing import List

from pydantic import BaseModel, Field


class CreateUserSchema(BaseModel):
    username: str
    password: str
    birthday: datetime.date


class SuccessUserSchema(BaseModel):
    # id: uuid.UUID = Field(default_factory=uuid.uuid4)
    id: uuid.UUID


class BaseUserSchema(SuccessUserSchema, BaseModel):
    username: str
    birthday: datetime.date
    time_created: datetime.datetime


class UsersList(BaseModel):
    users: List[BaseUserSchema]
