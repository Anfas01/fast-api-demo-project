from fastapi import APIRouter, Depends
from crud.authentication import register_user as crud_register_user, login_user, refresh
from schemas.authentication import UserRegister
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.authentication import UserLogin, UserLoginResponse






router = APIRouter()

@router.post("/register") 
def register(user: UserRegister, db: Session = Depends(get_db)):
    return crud_register_user(user, db)

@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)) -> UserLoginResponse:
    token = login_user(user_credentials, db)
    return token

@router.post("/refresh")
def refresh_token(token: str, db: Session = Depends(get_db)):
    return refresh(token, db)


