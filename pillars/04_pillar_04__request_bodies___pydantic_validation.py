"""
Pillar 04: Request Bodies & Pydantic Validation
File: app/schemas.py
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: Optional[int] = Field(None, ge=18, le=120)

@app.post("/users/", status_code=201)
async def create_user(user: UserCreate):
    return {"status": "created", "user": user.dict()}
