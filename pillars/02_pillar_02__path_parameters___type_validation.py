"""
Pillar 02: Path Parameters & Type Validation
File: app/main.py
"""

from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., gt=0, description="The ID of the item to fetch")):
    if item_id == 99:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": f"FastAPI Component #{item_id}"}
