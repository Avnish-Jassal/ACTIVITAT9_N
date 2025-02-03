from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_connect.connection import SessionLocal, engine
from schemas.user_schemas import User
from crud.user_crud import get_users

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users