# routers/lesson.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models.lesson import Lesson
from services.llm_client import generate_lesson_content

router = APIRouter()

@router.post("/generate-lesson")
def create_lesson(topic: str, user_id: int, db: Session = Depends(get_db)):
    content, memory_tip = generate_lesson_content(topic)

    lesson = Lesson(
        topic=topic,
        content=content,
        memory_tip=memory_tip,
        user_id=user_id
    )

    db.add(lesson)
    db.commit()
    db.refresh(lesson)

    return {
        "message": "Konu başarıyla oluşturuldu",
        "lesson_id": lesson.id,
        "content": content,
        "memory_tip": memory_tip
    }
