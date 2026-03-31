from sqlalchemy.orm import Session
from models.user import User
from fastapi import HTTPException





def get_all_users(db: Session):
    return db.query(User).all()

def profile(db: Session, user_name: str):
    user =  db.query(User).filter(User.username == user_name).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user