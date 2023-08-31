import datetime
import uuid
from typing import List

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    password: str
    birthday: datetime.date


class UserSchema(BaseModel):
    id: uuid.UUID


class BaseUserSchema(UserSchema, BaseModel):
    username: str
    birthday: datetime.date
    time_created: datetime.datetime


class UsersList(BaseModel):
    users: List[BaseUserSchema]


class SuccessUpdateUserSchema(UserSchema):
    pass


class SuccessDeleteUserSchema(UserSchema):
    pass
