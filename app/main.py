# app/main.py

from fastapi import FastAPI
from routers import auth, prompt, quiz, badges
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

security = HTTPBearer()

app = FastAPI(
    title="KPSS AI Backend"
)

@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return {"token": credentials.credentials}


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(prompt.router, prefix="/prompt", tags=["Prompt"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(badges.router, prefix="/badges", tags=["Badges"])
