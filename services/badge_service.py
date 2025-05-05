from sqlalchemy.orm import Session
from app.models.badge import Badge, UserBadge
from app.models.user import User
from datetime import datetime


def check_and_assign_badges(db: Session, user: User):
    badge_criteria = {
        1: "İlk Doğru",
        5: "Beş Doğru",
        10: "On Doğru"
    }

    for threshold, title in badge_criteria.items():
        if user.total_score >= threshold:
            badge = db.query(Badge).filter(Badge.title == title).first()
            if badge:
                already_has = db.query(UserBadge).filter_by(
                    user_id=user.id, badge_id=badge.id
                ).first()
                if not already_has:
                    new_user_badge = UserBadge(
                        user_id=user.id,
                        badge_id=badge.id,
                        earned_at=datetime.utcnow()
                    )
                    db.add(new_user_badge)

    db.commit()
