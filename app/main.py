# app/main.py

from fastapi import FastAPI
from routers import auth, prompt, quiz, badges

app = FastAPI(
    title="KPSS AI Backend"
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(prompt.router, prefix="/prompt", tags=["Prompt"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(badges.router, prefix="/badges", tags=["Badges"])
