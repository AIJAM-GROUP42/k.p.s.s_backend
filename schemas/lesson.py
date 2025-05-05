from pydantic import BaseModel
from typing import Optional


class LessonBase(BaseModel):
    topic: str
    content: str
    memory_tip: Optional[str]


class LessonCreate(LessonBase):
    pass


class LessonResponse(LessonBase):
    id: int

    class Config:
        orm_mode = True
