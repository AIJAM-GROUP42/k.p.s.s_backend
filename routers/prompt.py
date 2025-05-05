from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.prompt import PromptRequest, PromptResponse
from app.services.llm_client import generate_llm_content
from app.services.lesson_service import save_prompt_to_db
from app.database.session import get_db
from app.services.auth import get_current_user  # JWT doğrulama için
from app.models.user import User

router = APIRouter(prefix="/prompt", tags=["Prompt"])


@router.post("/", response_model=PromptResponse)
def create_prompt(
    request: PromptRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 1. LLM çağrısı
    content = generate_llm_content(request.topic, request.mode)

    # 2. DB’ye kaydet
    prompt = save_prompt_to_db(db, user_id=current_user.id, request=request, content=content)

    return prompt
