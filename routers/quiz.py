from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.session import get_db
from models.quiz_result import QuizResult
from models.user import User  # Import the User model

# Import or define the generate_quiz function
from services.llm_client import generate_quiz  # Example import

router = APIRouter()

class QuizSubmission(BaseModel):
    user_id: int
    correct_count: int
    score: int = 0  # opsiyonel, frontend gönderirse kaydedilir



@router.get("/quiz/generate")
def get_quiz(topic: str):
    quiz = generate_quiz(topic)
    return {"topic": topic, "quiz": quiz}


@router.post("/quiz/submit")
def submit_quiz(quiz_data: QuizSubmission, db: Session = Depends(get_db)):
    result = QuizResult(
        user_id=quiz_data.user_id,
        correct_count=quiz_data.correct_count,
        score=quiz_data.score
    )
    db.add(result)

    
    # 2. Kullanıcının toplam skorunu güncelle
    user = db.query(User).filter(User.id == quiz_data.user_id).first()
    if user:
        user.total_score = (user.total_score or 0) + quiz_data.score
        db.add(user)  # Güncellenmiş user'ı tekrar DB'ye ekliyoruz

    db.commit()
    db.refresh(result)

    return {
        "message": "Quiz sonucu başarıyla kaydedildi.",
        "quiz_result_id": result.id,
        "correct_count": result.correct_count,
        "score": result.score
    }
