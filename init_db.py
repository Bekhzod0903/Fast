from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User

def init_db():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    db.commit()
    db.close()
