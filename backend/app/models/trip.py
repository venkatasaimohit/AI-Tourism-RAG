from sqlalchemy import Column, Integer, String

from app.database.base import Base

class Trip(Base):

    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)

    destination = Column(String)

    budget = Column(Integer)

    duration = Column(Integer)