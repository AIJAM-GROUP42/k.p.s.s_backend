# app/routers/auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin
from services.auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/signup")
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            name=user_data.name,
            surname=user_data.surname,
            email=user_data.email,
            password=hash_password(user_data.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"message": "User created successfully!"}
    except Exception as e:
        print(f"❌ Signup error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}
