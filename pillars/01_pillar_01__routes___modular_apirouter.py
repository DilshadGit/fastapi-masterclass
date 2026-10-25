"""
Pillar 01: Routes & Modular APIRouter
File: routers/users.py
"""

from fastapi import FastAPI, APIRouter

app = FastAPI(title="FastAPI Microservice")
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def list_users():
    return [{"id": 1, "username": "alice", "role": "admin"}]

app.include_router(router)
