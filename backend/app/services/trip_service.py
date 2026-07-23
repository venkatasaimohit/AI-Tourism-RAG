from app.repositories.trip_repository import (
    TripRepository
)



class TripService:


    def __init__(self):

        self.repository = TripRepository()



    def create_trip(
        self,
        trip
    ):

        return self.repository.create_trip(
            trip
        )