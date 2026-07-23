from sqlalchemy.orm import Session

from app.database.models.item import Item
from app.exceptions.item import ItemNotFoundException
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate


class ItemService:

    def __init__(self):
        self.repository = ItemRepository()

    def get_all(
        self,
        db: Session,
    ) -> list[Item]:

        return self.repository.get_all(db)

    def create(
        self,
        db: Session,
        item_data: ItemCreate,
    ) -> Item:

        return self.repository.create(
            db,
            item_data,
        )

    def get_by_id(
        self,
        db: Session,
        item_id: int,
    ) -> Item:

        item = self.repository.get_by_id(
            db,
            item_id,
        )

        if item is None:
            raise ItemNotFoundException(
                f"Item with id {item_id} not found"
            )

        return item