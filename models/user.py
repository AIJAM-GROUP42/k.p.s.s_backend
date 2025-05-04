
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    total_score = Column(Integer, default=0)

    quiz_results = relationship("QuizResult", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
