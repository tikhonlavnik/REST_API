import uuid
from sqlalchemy.sql.functions import now
from sqlalchemy.dialects.postgresql import UUID

from API import db


# def create_id():
#     uuid_value = uuid.uuid4()
#     return str(uuid_value)


class Users(db.Model):
    """Model for users"""
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    time_created = db.Column(db.DateTime, default=now())


