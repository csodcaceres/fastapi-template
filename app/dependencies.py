from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService


def get_item_service() -> ItemService:
    repository = ItemRepository()

    return ItemService(
        repository
    )