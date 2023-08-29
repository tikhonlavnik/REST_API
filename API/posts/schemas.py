import datetime
import uuid

from pydantic import BaseModel, Field


class BasePostSchema(BaseModel):
    title: str
    description: str
    author_id: int


class SuccessPostSchema(BaseModel):
    # id: uuid.UUID = Field(default_factory=uuid.uuid4)
    id: str

