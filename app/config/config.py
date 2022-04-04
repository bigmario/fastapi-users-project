import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    secret_key: str = Field(os.environ.get("SECRET_KEY"))
    redis_url: str = Field(os.environ.get("REDIS_URL"))
    host: str = Field(os.environ.get("HOST"))
    log_level: str = Field(os.environ.get("LOG_LEVEL"))

    class Config:
        env_file = f"{os.getcwd()}/.env"
