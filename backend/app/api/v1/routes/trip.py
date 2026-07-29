from fastapi import APIRouter, Depends

from app.dependencies.service import (
    get_trip_service,
)

from app.schemas.trip import TripCreate

from app.services.trip_service import (
    TripService,
)

router = APIRouter(
    prefix="/trips",
    tags=["Trips"],
)


@router.post("/")
def create_trip(
    trip: TripCreate,
    service: TripService = Depends(
        get_trip_service
    ),
):

    return service.create_trip(trip)


@router.get("/")
def get_trips(
    service: TripService = Depends(
        get_trip_service
    ),
):

    return service.get_all()