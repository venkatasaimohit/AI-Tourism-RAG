from sqlalchemy import Column, Integer, String

from app.database.base import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    clerk_user_id = Column(String, unique=True)

    email = Column(String)

    full_name = Column(String)