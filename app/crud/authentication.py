from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.user import User
from core.security import hash_password, verify_password
from core.jwt import create_access_token, create_refresh_token, SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from schemas.authentication import UserRegister
from schemas.authentication import UserLogin


def register_user(user: UserRegister, db: Session):
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


def login_user(user_credentials: UserLogin, db: Session):
    db_user = db.query(User).filter((User.email == user_credentials.username) | (User.username == user_credentials.username)).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    verified_password = verify_password(user_credentials.password, db_user.password)

    if not verified_password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(db_user.username)})
    refresh_token = create_refresh_token(data={"sub": str(db_user.username)})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


def refresh(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        new_access_token = create_access_token(data={"sub": str(username)})

        return {"access_token": new_access_token}
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    
 