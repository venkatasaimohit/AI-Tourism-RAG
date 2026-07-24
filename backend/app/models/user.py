from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database.database import Base
from app.models.base_model import TimestampMixin



class User(
    Base,
    TimestampMixin
):

    __tablename__ = "users"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    clerk_id = Column(
        String,
        unique=True,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        nullable=False
    )


    full_name = Column(
        String
    )