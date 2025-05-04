from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from models.base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    content = Column(Text, nullable=False)         # Konu anlatımı (LLM)
    memory_tip = Column(Text)                      # Hafıza tekniği (LLM)

    quiz_results = relationship("QuizResult", back_populates="lesson")

    def __repr__(self):
        return f"<Lesson(id={self.id}, topic='{self.topic}')>"
