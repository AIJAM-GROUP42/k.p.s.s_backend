from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.auth import get_current_user
from app.models.user import User
from app.schemas.quiz_result import QuizSubmitRequest, QuizResultResponse
from app.services.quiz_service import generate_quiz_questions, evaluate_quiz

router = APIRouter(prefix="/quiz", tags=["Quiz"])


@router.get("/", response_model=list[str])  # Dummy response (örnek sorular)
def get_daily_quiz(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    questions = generate_quiz_questions()  # bu dummy olabilir veya HF/OpenAI
    return questions


@router.post("/submit", response_model=QuizResultResponse)
def submit_quiz(
    submission: QuizSubmitRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = evaluate_quiz(db, current_user.id, submission)
    return result
