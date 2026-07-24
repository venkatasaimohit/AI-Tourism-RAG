import uuid

from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base
from app.models.base_model import TimestampMixin


class Conversation(Base, TimestampMixin):

    __tablename__ = "conversations"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    message = Column(
        Text,
        nullable=False
    )

    response = Column(
        Text,
        nullable=False
    )