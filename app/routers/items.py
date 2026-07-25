from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services.item_service import ItemService
from app.api.dependencies import get_item_service

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)

# service = ItemService()

@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
def list_items(
    db: Session = Depends(get_db),
    service: ItemService = Depends(get_item_service),
):
    return service.get_all(db)

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED,)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
    service: ItemService = Depends(get_item_service),
):
    return service.create(
        db,
        item_data,
    )

@router.get("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    service: ItemService = Depends(get_item_service),
):
    return service.get_by_id(
        db,
        item_id,
    )

@router.put("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK,)
def update_item(
    item_id: int,
    item_data: ItemUpdate,
    db: Session = Depends(get_db),
    service: ItemService = Depends(get_item_service),
):
    return service.update(
        db,
        item_id,
        item_data,
    )

@router.delete("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    service: ItemService = Depends(get_item_service),
):
    return service.delete(
        db,
        item_id,
    )