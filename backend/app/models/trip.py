from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database.database import Base



class Trip(Base):

    __tablename__="trips"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )


    destination = Column(
        String
    )


    duration = Column(
        Integer
    )


    budget = Column(
        Integer
    )