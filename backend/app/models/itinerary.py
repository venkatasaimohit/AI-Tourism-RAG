from sqlalchemy import Column, Integer, String

from app.database.base import Base

class Itinerary(Base):

    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True)

    day = Column(Integer)

    activity = Column(String)