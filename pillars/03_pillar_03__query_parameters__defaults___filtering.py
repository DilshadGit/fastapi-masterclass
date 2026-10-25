"""
Pillar 03: Query Parameters, Defaults & Filtering
File: app/main.py
"""

from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/search/")
async def search_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"query": q, "skip": skip, "limit": limit, "results": ["item1", "item2"]}
