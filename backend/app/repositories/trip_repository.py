from sqlalchemy.orm import Session
from app.models.trip import Trip

class TripRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, trip: Trip):
        self.db.add(trip)
        self.db.commit()
        self.db.refresh(trip)
        return trip

    def get_all(self):
        return self.db.query(Trip).all()

    def get_by_id(self, trip_id):
        return (
            self.db.query(Trip)
            .filter(Trip.id == trip_id)
            .first()
        )

    def delete(self, trip):
        self.db.delete(trip)
        self.db.commit()