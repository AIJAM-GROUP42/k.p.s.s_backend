from sqlalchemy.orm import Session
from app.schemas.prompt import PromptRequest
from app.models.prompt import Prompt
from datetime import datetime


def save_prompt_to_db(db: Session, user_id: int, request: PromptRequest, content: str) -> Prompt:

    new_prompt = Prompt(
        user_id=user_id,
        topic=request.topic,
        mode=request.mode,
        content=content,
        created_at=datetime.utcnow()
    )
    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return new_prompt
