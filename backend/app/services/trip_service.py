from app.services.base_service import BaseService


class TripService(BaseService):

    def __init__(self, repository):
        super().__init__(repository)