from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class QuizSubmitRequest(BaseModel):
    answers: List[str]  # frontend cevabı string olarak yollar
    correct_answers: List[str]  # backend doğru cevapları kontrol etmek için


class QuizResultResponse(BaseModel):
    id: int
    correct_count: int
    created_at: datetime

    class Config:
        orm_mode = True

class QuizItem(BaseModel):
    question: str
    options: List[str]
    answer: str  
