from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models.user import User
from core.security import hash_password, verify_password
from core.jwt import create_access_token



def register_user(user, db: Session):
    #existing_user = db.query(User).filter(User.email == user.email).first()
    existing_user = db.query(User).filter((User.email == user.email) | (User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists please login")

    hashed_password =  hash_password(user.password)

    db_user = User(username=user.username, email=user.email, password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created successfully"}


def login_user(user_credentials, db: Session):
    db_user = db.query(User).filter((User.email == user_credentials.username) | (User.username == user_credentials.username)).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    verified_password = verify_password(user_credentials.password, db_user.password)

    if not verified_password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    token = create_access_token(data={"sub": str(db_user.username)})

    return {"access_token": token, "token_type": "bearer"}