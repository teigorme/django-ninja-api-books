from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    HOST: str
    LOG_LEVEL: str
    APP_KEY: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    CLIENT_ORIGIN: str = ""
    DEBUG: bool

    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")


env = Settings()
