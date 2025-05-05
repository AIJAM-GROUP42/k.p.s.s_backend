from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

# .env dosyasını yükle
load_dotenv(dotenv_path=Path(".") / ".env")

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Tüm projede kullanılmak üzere ayar nesnesi
settings = Settings()
