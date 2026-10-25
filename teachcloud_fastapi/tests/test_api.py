import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

@pytest.mark.asyncio
async def test_create_and_get_item():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        res = await ac.post("/api/v1/items/", json={
            "title": "Cloud Server Node",
            "description": "High RAM Compute",
            "price": 99.99
        })
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == "Cloud Server Node"
        item_id = data["id"]

        get_res = await ac.get(f"/api/v1/items/{item_id}")
        assert get_res.status_code == 200
        assert get_res.json()["price"] == 99.99
