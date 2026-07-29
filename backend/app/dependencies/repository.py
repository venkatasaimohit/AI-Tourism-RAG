from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.trip_repository import (
    TripRepository,
)


def get_trip_repository(
    db: Session = Depends(get_db),
):

    return TripRepository(db)