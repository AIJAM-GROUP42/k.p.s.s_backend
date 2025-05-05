# app/main.py
from fastapi import FastAPI
from routers import auth,lesson
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from routers import quiz


app = FastAPI()
security = HTTPBearer()

@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return {"token": credentials.credentials}

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(lesson.router)


app.include_router(quiz.router)
