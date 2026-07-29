from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.repositories.base_repository import BaseRepository


class TripRepository(BaseRepository[Trip]):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(Trip, db)

    def get_by_user(
        self,
        user_id,
    ):
        return (
            self.db.query(Trip)
            .filter(Trip.user_id == user_id)
            .all()
        )

    def search_destination(
        self,
        destination: str,
    ):
        return (
            self.db.query(Trip)
            .filter(
                Trip.destination.ilike(
                    f"%{destination}%"
                )
            )
            .all()
        )