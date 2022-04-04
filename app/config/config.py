import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    secret_key: str = Field(os.environ.get("SECRET_KEY"))
    redis_url: str = Field(os.environ.get("REDIS_URL"))
    host: str = Field(os.environ.get("HOST"))
    log_level: str = Field(os.environ.get("LOG_LEVEL"))

    postgres_db: str = Field(os.environ.get("POSTGRES_DB"))
    postgres_user: str = Field(os.environ.get("POSTGRES_USER"))
    postgres_password: str = Field(os.environ.get("POSTGRES_PASSWORD"))

    class Config:
        env_file = f"{os.getcwd()}/.env"
