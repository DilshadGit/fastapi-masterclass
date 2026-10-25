from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="FastAPI Masterclass API",
    version="1.0.0",
    description="High-performance async API with Pydantic validation by DilshadGit"
)

class ItemSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    is_available: bool = True

items_db: List[ItemSchema] = [
    ItemSchema(id=1, title="Cloud Server", price=49.99, is_available=True),
    ItemSchema(id=2, title="Load Balancer", price=29.99, is_available=True)
]

@app.get("/", tags=["Health"])
async def root():
    return {"status": "online", "framework": "FastAPI", "author": "DilshadGit"}

@app.get("/api/items", response_model=List[ItemSchema], tags=["Items"])
async def list_items():
    return items_db

@app.post("/api/items", response_model=ItemSchema, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: ItemSchema):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item
