from fastapi import APIRouter, Depends
from models.user import User
from schemas.user import UsersResponseModel, UserResponseModel
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from core.database import get_db
from crud.user import get_all_users, profile



router = APIRouter()


@router.get("/")
def read_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> list[UsersResponseModel]:
    return get_all_users(db)

@router.get("/aboutMe")
def about_me(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> UserResponseModel:
    return profile(db, user_name=current_user.username)