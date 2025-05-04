from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import settings


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Engine ve Session oluştur
engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency fonksiyonu
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()