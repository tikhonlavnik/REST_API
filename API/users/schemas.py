import datetime
import uuid
from typing import List

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    password: str
    birthday: datetime.date


class SuccessUserSchema(BaseModel):
    id: uuid.UUID


class BaseUserSchema(SuccessUserSchema, BaseModel):
    username: str
    birthday: datetime.date
    time_created: datetime.datetime


class UsersList(BaseModel):
    users: List[BaseUserSchema]


class SuccessUpdateUserSchema(SuccessUserSchema):
    pass


class SuccessDeleteUserSchema(SuccessUserSchema):
    pass
