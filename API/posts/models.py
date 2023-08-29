import uuid

from sqlalchemy.sql.functions import now
from sqlalchemy.dialects.postgresql import UUID
from API import db
from API.users.models import Users


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
