"""
Pillar 07: Async Endpoints & Non-blocking I/O
File: app/main.py
"""

import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/async-data")
async def fetch_external_data():
    await asyncio.sleep(0.05)  # Non-blocking async sleep
    return {"status": "async completion", "duration_ms": 50}
