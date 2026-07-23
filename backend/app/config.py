from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str
    ENVIRONMENT: str

    DATABASE_URL: str

    OPENAI_API_KEY: str

    QDRANT_URL: str

    CLERK_SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
