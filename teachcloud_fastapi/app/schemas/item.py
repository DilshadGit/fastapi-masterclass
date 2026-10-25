from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    description: str = Field(None, max_length=300)
    price: float = Field(..., gt=0)

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    is_active: bool = True
