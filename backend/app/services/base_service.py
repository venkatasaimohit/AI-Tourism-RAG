class BaseService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def create(
        self,
        obj,
    ):
        return self.repository.create(obj)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(
        self,
        obj_id,
    ):
        return self.repository.get_by_id(obj_id)

    def delete(
        self,
        obj,
    ):
        return self.repository.delete(obj)