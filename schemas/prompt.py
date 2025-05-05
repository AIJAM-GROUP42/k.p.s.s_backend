from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# POST /prompt için giriş verisi
class PromptRequest(BaseModel):
    topic: str
    mode: str  # "info" veya "memory_tip"


# DB'den dönecek veya response verisi
class PromptResponse(BaseModel):
    id: int
    topic: str
    mode: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True
