# ⚡ FastAPI High-Performance Asynchronous Masterclass

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

> Complete zero-to-hero curriculum in modern high-performance asynchronous API architecture with FastAPI, Starlette event loops, Pydantic V2 validation, Dependency Injection (`Depends`), WebSockets, BackgroundTasks, and automated `httpx.AsyncClient` test suites.

---

## 🏛️ The 10 Pillars of Modern FastAPI Architecture

Every pillar is fully implemented with runnable code in the [`pillars/`](pillars/) folder:

1. **[`Pillar 01`](pillars/)**: ASGI Starlette Foundation & Uvicorn Event Loop
2. **[`Pillar 02`](pillars/)**: Pydantic V2 Data Models, Schemas & Declarative Constraints
3. **[`Pillar 03`](pillars/)**: Advanced Dependency Injection System (`Depends`)
4. **[`Pillar 04`](pillars/)**: Asynchronous Database Integration & Async Sessions
5. **[`Pillar 05`](pillars/)**: OAuth2 Password Flow & JWT Security Tokens
6. **[`Pillar 06`](pillars/)**: High-Throughput Concurrency & Async Non-Blocking Endpoints
7. **[`Pillar 07`](pillars/)**: Background Tasks & Worker Offloading
8. **[`Pillar 08`](pillars/)**: Bidirectional Real-Time WebSockets
9. **[`Pillar 09`](pillars/)**: Pytest Async Testing with `httpx.AsyncClient`
10. **[`Pillar 10`](pillars/)**: Production Containerization & Multi-Worker Uvicorn Deployment

---

## 🛠️ Complete Runnable FastAPI Application Included

Located in [`teachcloud_fastapi/`](teachcloud_fastapi/):
- **Core Async API**: Modular APIRouter structure with Pydantic V2 schemas.
- **Real-Time WebSockets**: Echo broadcast handler at `/ws/echo`.
- **Automated Async Testing**: Pytest-asyncio suite testing live endpoints.
- **Production Containerization**: Lightweight [`Dockerfile`](Dockerfile).

### Quickstart:
```bash
cd teachcloud_fastapi
pip install -r ../requirements.txt
uvicorn main:app --reload
```

---

## 🧪 Masterclass Examination

Complete your FastAPI mastery evaluation in [`QUIZ.md`](QUIZ.md), testing your knowledge of ASGI event loops, `Depends()` caching, Pydantic V2 validators, and WebSocket disconnect handling.
