"""
Pillar 08: Automatic OpenAPI & Interactive Swagger UI
File: app/main.py
"""

from fastapi import FastAPI

app = FastAPI(
    title="Enterprise FastAPI Gateway",
    description="Automated OpenAPI 3.0 Documentation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
