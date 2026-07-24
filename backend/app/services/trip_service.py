from app.models.trip import Trip
from app.repositories.trip_repository import TripRepository

class TripService:

    def __init__(self, repository: TripRepository):
        self.repository = repository

    def create_trip(self, data):
        trip = Trip(
            destination=data.destination,
            duration=data.duration,
            budget=data.budget
        )

        return self.repository.create(trip)

    def get_all_trips(self):
        return self.repository.get_all()

    def get_trip(self, trip_id):
        return self.repository.get_by_id(trip_id)

    def delete_trip(self, trip):
        self.repository.delete(trip)