from app.models.trip import Trip
from app.services.base_service import BaseService


class TripService(BaseService):

    def create_trip(
        self,
        data,
    ):

        if data.budget <= 0:
            raise ValueError(
                "Budget must be greater than zero."
            )

        if data.duration <= 0:
            raise ValueError(
                "Duration must be greater than zero."
            )

        trip = Trip(
            user_id=data.user_id,
            destination=data.destination,
            duration=data.duration,
            budget=data.budget,
        )

        return self.repository.create(trip)

    def search_destination(
        self,
        destination,
    ):
        return self.repository.search_destination(
            destination
        )