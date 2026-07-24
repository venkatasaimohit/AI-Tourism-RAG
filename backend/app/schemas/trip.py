from pydantic import BaseModel
from uuid import UUID

class TripCreate(BaseModel):
    destination: str
    duration: int
    budget: int


class TripResponse(BaseModel):
    id: UUID
    destination: str
    duration: int
    budget: int

    class Config:
        from_attributes = True