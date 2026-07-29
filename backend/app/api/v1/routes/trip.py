from fastapi import APIRouter, Depends

from app.dependencies.service import get_trip_service

from app.services.trip_service import TripService

router = APIRouter()


@router.get("/")
def get_trips(

    service: TripService = Depends(get_trip_service),

):

    return service.get_all()