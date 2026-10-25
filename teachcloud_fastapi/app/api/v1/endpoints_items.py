from fastapi import APIRouter, HTTPException, status
from typing import List
from ...schemas.item import ItemCreate, ItemResponse

router = APIRouter()
fake_db = {}
next_id = 1

@router.get("/", response_model=List[ItemResponse])
async def list_items():
    return list(fake_db.values())

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    global next_id
    new_item = ItemResponse(id=next_id, **item.model_dump())
    fake_db[next_id] = new_item
    next_id += 1
    return new_item

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]
