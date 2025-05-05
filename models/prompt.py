from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    mode = Column(String, nullable=False)  # "info" veya "memory_tip"
    content = Column(String, nullable=False)  # LLM'den alınan yanıt
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="prompts")
