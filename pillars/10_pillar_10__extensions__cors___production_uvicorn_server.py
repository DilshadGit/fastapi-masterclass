"""
Pillar 10: Extensions, CORS & Production Uvicorn Server
File: main.py & Uvicorn CLI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CLI: uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
