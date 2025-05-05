from pydantic import BaseModel
from datetime import datetime

class BadgeBase(BaseModel):
    name: str
    description: str

class BadgeCreate(BadgeBase):
    pass

class BadgeResponse(BadgeBase):
    id: int
    awarded_at: datetime

    class Config:
        from_attributes = True  
