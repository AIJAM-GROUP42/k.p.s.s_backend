from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.quiz_result import QuizSubmitRequest
from app.models.quiz_result import QuizResult
from app.models.user import User
from app.services.badge_service import check_and_assign_badges
from app.services.llm_client import generate_quiz_with_gemini


def generate_quiz_questions(topic: str = "Genel Kültür") -> list[dict]:      #örnekleme için genel kültür
    return generate_quiz_with_gemini(topic)


def evaluate_quiz(db: Session, user_id: int, submission: QuizSubmitRequest) -> QuizResult:
    """
    Kullanıcının gönderdiği cevapları doğru cevaplarla karşılaştırarak quiz sonucunu hesaplar,
    skoru kaydeder ve gerekirse rozet verir.
    """
    correct = 0
    for user_ans, correct_ans in zip(submission.answers, submission.correct_answers):
        if user_ans.strip().lower() == correct_ans.strip().lower():
            correct += 1

    result = QuizResult(
        user_id=user_id,
        correct_count=correct,
        created_at=datetime.utcnow()
    )
    db.add(result)

    user = db.query(User).filter(User.id == user_id).first()
    user.total_score += correct

    db.commit()
    db.refresh(result)

    # Rozet kazanımı kontrolü
    check_and_assign_badges(db, user)

    return result
