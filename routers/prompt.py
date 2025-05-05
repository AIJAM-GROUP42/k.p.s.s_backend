from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.prompt import PromptRequest, PromptResponse
from services.llm_client import generate_llm_content
from services.lesson_service import save_prompt_to_db
from database.session import get_db
from services.auth import get_current_user  # JWT doğrulama için
from models.user import User

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
