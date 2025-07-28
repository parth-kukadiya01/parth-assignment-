from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # Database
    database_url: str = "ADD YOUR DB URL"

    # JWT
    secret_key: str = "your-super-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 24 hours

    # API
    api_title: str = "FastAPI JWT RBAC API"
    api_description: str = (
        "A RESTful API with JWT Authentication and Role-Based Access Control"
    )
    api_version: str = "1.0.0"

    # CORS
    allowed_origins: list[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
