from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Tourism RAG"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str

    OPENAI_API_KEY: str | None = None

    QDRANT_URL: str | None = None

    CLERK_SECRET_KEY: str | None = None
    CLERK_PUBLISHABLE_KEY: str | None = None
    CLERK_JWT_ISSUER: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()