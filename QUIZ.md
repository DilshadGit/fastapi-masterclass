# 📝 Current Weekly Assessment — Edition #43

> **Subject / Focus Area**: FastAPI Microservices
> **7-Day Cycle Period**: 2026-10-22 to 2026-10-29 UTC
> **Total Questions**: 16
> **Location**: `docs/Quiz/`

---

## 📋 Assessment Overview
This examination comprises the 7-day rotating test bank for **FastAPI Microservices**.
Each question tests real-world systems architecture, cloud services, and production engineering practices.

---

## ❓ Questions & Verified Solutions

### Question 1: What decorator lifecycle pattern is used for modern FastAPI startup and shutdown events?

- [x] **`@asynccontextmanager` lifespan event handler passed to `FastAPI(lifespan=...)`** *(Correct Answer)*
- [ ] `@app.on_event("startup")` (deprecated)
- [ ] `__init__` constructor methods
- [ ] OS signal listeners

> **💡 Engineering Context & Rationale**:
> Modern FastAPI uses an <strong>asynccontextmanager lifespan handler</strong> to manage startup initialization and shutdown cleanup cleanly.

---

### Question 2: How does FastAPI automatically generate interactive API documentation endpoints?

- [x] **Inspects route parameter type hints and Pydantic schemas to dynamically host Swagger UI (`/docs`) and ReDoc (`/redoc`)** *(Correct Answer)*
- [ ] Requires writing OpenAPI YAML specs manually
- [ ] Scrapes documentation from external websites
- [ ] Compiles docstrings using Sphinx

> **💡 Engineering Context & Rationale**:
> FastAPI inspects route code type annotations to automatically output an <strong>OpenAPI schema</strong> rendered via interactive Swagger UI.

---

### Question 3: What is the purpose of `APIRouter` in FastAPI?

- [x] **Splits path operation routes into modular, reusable sub-routers that can be included in the main app instance** *(Correct Answer)*
- [ ] Configures network router IP tables
- [ ] Routes incoming TCP traffic across servers
- [ ] Manages DNS name lookups

> **💡 Engineering Context & Rationale**:
> <strong>APIRouter</strong> works similarly to Flask Blueprints, allowing modular organization of endpoint groups with shared prefixes and tags.

---

### Question 4: How do parameter type annotations control location in FastAPI route parameters?

- [x] **Parameters matching path placeholders become Path parameters; Pydantic models become Request Body; scalar types become Query parameters** *(Correct Answer)*
- [ ] All parameters are parsed from query strings
- [ ] Parameters must be explicitly marked with C types
- [ ] Location is determined by alphabetical name ordering

> **💡 Engineering Context & Rationale**:
> FastAPI intelligently infers parameter origins: path variables map to <strong>Path</strong>, Pydantic models map to <strong>Body</strong>, and scalar parameters map to <strong>Query</strong>.

---

### Question 5: What key performance advantage does FastAPI offer compared to traditional synchronous Python frameworks?

- [x] **Built natively on Starlette and ASGI, supporting asynchronous non-blocking concurrency via `async/await`** *(Correct Answer)*
- [ ] Compiles Python code into C binaries at runtime
- [ ] Disables garbage collection during requests
- [ ] Bypasses HTTP protocol handshakes

> **💡 Engineering Context & Rationale**:
> FastAPI achieves high performance by leveraging <strong>ASGI</strong> (Starlette) and native async execution for non-blocking I/O.

---

### Question 6: What is the role of `response_model` parameter in path operation decorators?

- [x] **Defines the Pydantic schema used to filter, format, and validate outgoing response data** *(Correct Answer)*
- [ ] Specifies HTTP status code integer
- [ ] Configures database table relationships
- [ ] Sets CORS origin headers

> **💡 Engineering Context & Rationale**:
> <strong>response_model</strong> filters outbound data, ensuring private fields (e.g., hashed passwords) are stripped before returning payloads.

---

### Question 7: How do you set a custom HTTP status code for successful responses in FastAPI?

- [x] **Pass `status_code=status.HTTP_201_CREATED` in path operation decorator** *(Correct Answer)*
- [ ] Modify system environment variables
- [ ] Return a tuple containing status integer
- [ ] Raise a 201 exception

> **💡 Engineering Context & Rationale**:
> Setting <strong>status_code</strong> on path operation decorators sets default HTTP response status codes.

---

### Question 8: What is Starlette in relation to FastAPI?

- [x] **The lightweight ASGI framework/toolkit upon which FastAPI builds routing, web requests, and WebSocket capabilities** *(Correct Answer)*
- [ ] A database migration engine
- [ ] A CSS styling framework
- [ ] An automated code linter

> **💡 Engineering Context & Rationale**:
> FastAPI is built directly on top of <strong>Starlette</strong> for web routing and <strong>Pydantic</strong> for data schemas.

---

### Question 9: How do you declare query parameter validation constraints (e.g., min length) in FastAPI?

- [x] **Use `Query(min_length=3, max_length=50)` constraint annotations** *(Correct Answer)*
- [ ] Write custom regex parsers inside function body
- [ ] Validate in HTML templates
- [ ] Configure database column limits

> **💡 Engineering Context & Rationale**:
> FastAPI's <strong>Query()</strong> function allows defining validation metadata, regex patterns, and documentation descriptions for query parameters.

---

### Question 10: What is WebSocket support in FastAPI?

- [x] **Supports real-time bi-directional communication endpoints via `@app.websocket("/ws")` decorator** *(Correct Answer)*
- [ ] Converts HTTP requests to gRPC
- [ ] Streams static video files
- [ ] Encrypts DNS queries

> **💡 Engineering Context & Rationale**:
> FastAPI provides first-class support for <strong>WebSockets</strong> via Starlette, allowing full-duplex real-time communication.

---

### Question 11: How does FastAPI support CORS (Cross-Origin Resource Sharing)?

- [x] **Adding `CORSMiddleware` using `app.add_middleware(CORSMiddleware, allow_origins=[...])`** *(Correct Answer)*
- [ ] Modifying system iptables
- [ ] Injecting script tags into client browsers
- [ ] Disabling HTTP OPTIONS method

> **💡 Engineering Context & Rationale**:
> FastAPI includes Starlette's <strong>CORSMiddleware</strong> to manage cross-origin headers and preflight handling.

---

### Question 12: How do you stream responses (e.g. large files or AI tokens) in FastAPI?

- [x] **Return a `StreamingResponse` object taking an async generator** *(Correct Answer)*
- [ ] Write responses to static files on disk
- [ ] Use standard `return` statements
- [ ] Send response via WebSocket only

> **💡 Engineering Context & Rationale**:
> <strong>StreamingResponse</strong> accepts python generators to stream data chunks incrementally to clients.

---

### Question 13: What is the difference between `def` and `async def` path operation functions in FastAPI?

- [x] **`async def` runs directly on the main event loop thread; `def` functions are offloaded to an external threadpool to prevent blocking** *(Correct Answer)*
- [ ] `def` is faster than `async def`
- [ ] `async def` cannot perform database queries
- [ ] `def` is deprecated in FastAPI

> **💡 Engineering Context & Rationale**:
> FastAPI handles synchronous <strong>def</strong> functions by running them in an internal threadpool, preventing blocking of the async event loop.

---

### Question 14: How does Pydantic `@field_validator` work in FastAPI data models?

- [x] **Applies custom validation functions to specific model attributes during payload instantiation** *(Correct Answer)*
- [ ] Validates SQL queries before execution
- [ ] Sanitizes HTML tags in templates
- [ ] Formats date strings into timestamps

> **💡 Engineering Context & Rationale**:
> <strong>@field_validator</strong> allows defining custom Python validation methods executed when instantiating Pydantic model attributes.

---

### Question 15: What is the role of Pydantic in FastAPI applications?

- [x] **Provides data validation, settings management, and automated JSON serialization based on Python type hints** *(Correct Answer)*
- [ ] Manages SQL database connections
- [ ] Renders Jinja HTML templates
- [ ] Handles OAuth2 password hashing

> **💡 Engineering Context & Rationale**:
> FastAPI utilizes <strong>Pydantic</strong> models to enforce request data schema validation and automatically serialize response data.

---

### Question 16: How do you configure OAuth2 password hashing security flow in FastAPI?

- [x] **Use `OAuth2PasswordBearer` security scheme combined with passlib/bcrypt hashing** *(Correct Answer)*
- [ ] Store passwords in plaintext cookies
- [ ] Use HTTP Basic Auth exclusively
- [ ] Disable authentication on POST endpoints

> **💡 Engineering Context & Rationale**:
> FastAPI provides built-in security utilities like <strong>OAuth2PasswordBearer</strong> to extract bearer tokens from request authorization headers.

---

## 🏆 End of Assessment
*TeachCloud Automated Quiz Engine — Edition #43 (Active Week).*
