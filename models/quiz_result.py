from sqlalchemy import Column, Integer, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime

class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    generated_questions = Column(JSON, nullable=False)  # LLM oluşturur
    user_answers = Column(JSON, nullable=False)         # Kullanıcının verdiği cevaplar
    correct_count = Column(Integer)
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="quiz_results")
    lesson = relationship("Lesson", back_populates="quiz_results")

    def __repr__(self):
        return f"<QuizResult(id={self.id}, user_id={self.user_id}, lesson_id={self.lesson_id})>"

from models.user import User
from models.lesson import Lesson

QuizResult.user = relationship("User", back_populates="quiz_results")
QuizResult.lesson = relationship("Lesson", back_populates="quiz_results")
