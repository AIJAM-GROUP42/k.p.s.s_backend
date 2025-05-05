from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.badge import BadgeResponse
from app.models.badge import UserBadge, Badge

router = APIRouter(prefix="/badges", tags=["Badges"])


@router.get("/{user_id}", response_model=list[BadgeResponse])
def get_user_badges(user_id: int, db: Session = Depends(get_db)):
    results = (
        db.query(UserBadge)
        .join(Badge)
        .filter(UserBadge.user_id == user_id)
        .all()
    )
    return [
        BadgeResponse(
            id=ub.badge.id,
            title=ub.badge.title,
            description=ub.badge.description,
            earned_at=ub.earned_at,
        )
        for ub in results
    ]
