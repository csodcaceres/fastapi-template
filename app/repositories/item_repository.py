from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemRepository:

    def get_all(
        self,
        db: Session,
    ) -> list[Item]:

        statement = select(Item)

        return list(db.scalars(statement).all())

    def create(
        self,
        db: Session,
        item_data: ItemCreate,
    ) -> Item:

        item = Item(
            name=item_data.name,
            description=item_data.description,
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item

    def get_by_id(
        self,
        db: Session,
        item_id: int,
    ) -> Item | None:

        statement = select(Item).where(Item.id == item_id)

        return db.scalar(statement)

    def update(
        self,
        db: Session,
        item_id: int,
        item_data: ItemUpdate,
    ) -> Item | None:

        item = self.get_by_id(
            db,
            item_id,
        )

        if item is None:
            return None

        update_data = item_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(item, field, value)

        db.commit()
        db.refresh(item)

        return item

    def delete(
        self,
        db: Session,
        item_id: int,
    ) -> bool:

        item = self.get_by_id(
            db,
            item_id,
        )

        if item is None:
            return False

        db.delete(item)
        db.commit()

        return True