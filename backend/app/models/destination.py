from sqlalchemy import Column, String, Text

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database.database import Base


class Destination(Base):

    __tablename__ = "destinations"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    name = Column(
        String,
        nullable=False
    )


    country = Column(
        String
    )


    description = Column(
        Text
    )