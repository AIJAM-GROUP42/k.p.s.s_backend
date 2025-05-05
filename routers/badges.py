from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from models.user import User

router = APIRouter()

@router.get("/badges/{user_id}")
def get_user_badges(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")

    badges = []

    if user.total_score >= 0:
        badges.append({"title": "👋 Hoş Geldin", "description": "Sisteme ilk giriş yaptın!"})
    if user.total_score >= 50:
        badges.append({"title": "🥉 Bronz Rozet", "description": "İlk başarını elde ettin!"})
    if user.total_score >= 100:
        badges.append({"title": "🥈 Gümüş Rozet", "description": "Gelişen bir yeteneksin!"})
    if user.total_score >= 200:
        badges.append({"title": "🥇 Altın Rozet", "description": "Üst düzey başarıya ulaştın!"})

    return {
        "user_id": user.id,
        "total_score": user.total_score,
        "badges": badges
    }
