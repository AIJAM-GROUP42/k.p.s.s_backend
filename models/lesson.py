from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.quiz_result import QuizResult
from models.base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    content = Column(Text, nullable=False)         # Konu anlatımı (LLM)
    memory_tip = Column(Text)                      # Hafıza tekniği (LLM)

    user_id = Column(Integer, ForeignKey("users.id"))  # FK eklendi


    def __repr__(self):
        return f"<Lesson(id={self.id}, topic='{self.topic}')>"
