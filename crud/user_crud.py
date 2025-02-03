from sqlalchemy.orm import Session
from db_connect.connection import SessionLocal
from schemas.user_schemas import User

def get_users(db: Session):
    return db.query(User).all()