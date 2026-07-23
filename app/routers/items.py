from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import ItemService


router = APIRouter(
    prefix="/items",
    tags=["Items"],
)

service = ItemService()


@router.get("/", response_model=list[ItemResponse])
def list_items(
    db: Session = Depends(get_db),
):
    return service.get_all(db)


@router.post("/", response_model=ItemResponse)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
):
    return service.create(
        db,
        item_data,
    )


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    return service.get_by_id(
        db,
        item_id,
    )