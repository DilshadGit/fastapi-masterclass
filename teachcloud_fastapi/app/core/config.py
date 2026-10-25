from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "TeachCloud FastAPI Masterclass"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "fastapi-masterclass-super-secret-jwt-key-2026"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
