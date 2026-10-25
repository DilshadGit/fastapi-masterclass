# 🎓 FastAPI Masterclass Quiz (24 Questions & Complete Answer Key)

1. **Which ASGI server standardly runs FastAPI applications?**
   - Answer: Uvicorn.
2. **What library powers request validation and serialization in FastAPI?**
   - Answer: Pydantic.
3. **Where does FastAPI automatically generate interactive documentation?**
   - Answer: `/docs` (Swagger UI) and `/redoc` (ReDoc).
4. **How do you define dependency injection in FastAPI?**
   - Answer: `Depends(dependency_function)`
5. **What is the purpose of 'async def' in path operations?**
   - Answer: Runs asynchronous non-blocking I/O operations directly on the event loop.
6. **How do you return HTTP status 201 Created from a route?**
   - Answer: `status_code=status.HTTP_201_CREATED`
7. **What does 'response_model' parameter do?**
   - Answer: Filters, validates, and serializes output data according to a Pydantic schema.
8. **How do you handle background tasks in FastAPI?**
   - Answer: Inject `BackgroundTasks` parameter and call `tasks.add_task(func)`.
9. **How do you validate query parameters with constraints?**
   - Answer: `Query(default, min_length=..., ge=...)`.
10. **How do you validate path parameters?**
    - Answer: `Path(..., title=..., ge=...)`.
11. **How do you raise HTTP errors with custom details?**
    - Answer: `raise HTTPException(status_code=404, detail="Item not found")`
12. **Which security scheme is standard for bearer tokens in FastAPI?**
    - Answer: `OAuth2PasswordBearer(tokenUrl="token")`
13. **How do you group related routes into modular files?**
    - Answer: `APIRouter()` and `app.include_router()`.
14. **What does 'lifespan' context manager replace in modern FastAPI?**
    - Answer: Replaces deprecated `@app.on_event("startup")` and `@app.on_event("shutdown")`.
15. **How do you handle file uploads in FastAPI?**
    - Answer: `UploadFile = File(...)`.
16. **What is the benefit of UploadFile over bytes?**
    - Answer: Streams file in memory up to a threshold, then spills to disk without exhausting RAM.
17. **How do you enable Cross-Origin Resource Sharing (CORS)?**
    - Answer: `CORSMiddleware`.
18. **What is SQLModel?**
    - Answer: A library by the creator of FastAPI combining Pydantic and SQLAlchemy.
19. **How to perform database dependency cleanup per request?**
    - Answer: Use `yield` inside a dependency generator function.
20. **How do you write unit tests for FastAPI?**
    - Answer: `from fastapi.testclient import TestClient` (backed by httpx).
21. **What is WebSocket support in FastAPI?**
    - Answer: `@app.websocket("/ws")` for real-time bidirectional streaming.
22. **What does Pydantic 'Field(..., gt=0)' specify?**
    - Answer: Greater-than-zero numeric constraint.
23. **How do you inject request headers?**
    - Answer: `Header(default=None)`.
24. **How do you run FastAPI with multiple worker processes in production?**
    - Answer: `uvicorn main:app --workers 4` or Gunicorn with Uvicorn worker class.
