from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.trip_repository import TripRepository
from app.schemas.trip import TripCreate
from app.services.trip_service import TripService

router = APIRouter()

@router.post("/")
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db)
):
    repository = TripRepository(db)
    service = TripService(repository)

    return service.create_trip(trip)


@router.get("/")
def get_trips(
    db: Session = Depends(get_db)
):
    repository = TripRepository(db)
    service = TripService(repository)

    return service.get_all_trips()