from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from auth.dependencies import get_current_user
from models.user import User
from crud.order import place_order, view_order, cancel_order
from schemas.order import OrderResponseModel, OrderPlacementResponse



router = APIRouter()

@router.post("/")
def create_order(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> OrderPlacementResponse :
    return place_order(db, current_user.id)


@router.get("/", response_model=list[OrderResponseModel])
def order_view(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return view_order(db, current_user.id)


@router.delete("/{product_name}")
def order_cancel(product_name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return cancel_order(db, product_name, current_user.id)