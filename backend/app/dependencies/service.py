from fastapi import Depends

from app.dependencies.repository import get_trip_repository

from app.repositories.trip_repository import TripRepository

from app.services.trip_service import TripService


def get_trip_service(
    repository: TripRepository = Depends(get_trip_repository),
) -> TripService:

    return TripService(repository)