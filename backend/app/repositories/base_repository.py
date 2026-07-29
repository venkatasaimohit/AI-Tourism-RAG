from typing import Generic, Type, TypeVar, Optional, List

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        model: Type[ModelType],
        db: Session,
    ):
        self.model = model
        self.db = db

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()

    def get_by_id(
        self,
        obj_id,
    ) -> Optional[ModelType]:
        return (
            self.db.query(self.model)
            .filter(self.model.id == obj_id)
            .first()
        )

    def update(self):
        self.db.commit()

    def delete(
        self,
        obj: ModelType,
    ):
        self.db.delete(obj)
        self.db.commit()

    def exists(
        self,
        obj_id,
    ) -> bool:
        return self.get_by_id(obj_id) is not None

    def count(self):
        return self.db.query(self.model).count()