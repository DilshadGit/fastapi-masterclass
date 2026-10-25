# Modern Async & Pydantic V2 Foundations

FastAPI relies on standard Python type annotations and Pydantic V2 for automatic parsing, validation, and serialization:

```python
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=120)
```
