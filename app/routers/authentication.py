from fastapi import APIRouter, Depends
from crud.authentication import register_user as crud_register_user, login_user
from schemas.authentication import UserRegister, UserRegisterResponse
from sqlalchemy.orm import Session
from core.database import get_db
from fastapi.security import OAuth2PasswordRequestForm






router = APIRouter()

@router.post("/register") 
def register(user: UserRegister, db: Session = Depends(get_db)):
    return crud_register_user(user, db)

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = login_user(user_credentials, db)
    return token
