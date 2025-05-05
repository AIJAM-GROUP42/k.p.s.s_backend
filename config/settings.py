from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

# .env dosyasını yükle
load_dotenv(dotenv_path=Path(".") / ".env")

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"  # JWT için varsayılan algoritma
    GEMINI_API_KEY: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Bu nesne tüm projede kullanılabilir
settings = Settings()
