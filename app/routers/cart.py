from fastapi import APIRouter, Depends
from models.user import User
from schemas.cart import CartCreate, CartResponseModel
from schemas.product import ProductName
from sqlalchemy.orm import Session
from core.database import get_db
from auth.dependencies import get_current_user
from crud.cart import create_cart, view_cart, remove_from_cart


router = APIRouter()

@router.post("/")
def add_to_cart(cart: CartCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_cart(db, cart, current_user.username)


@router.get("/")
def cart_view(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> list[CartResponseModel]:
    return view_cart(db, current_user.username)


@router.delete("/{product_name}")
def remove_cart(product_name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return remove_from_cart(db, product_name, current_user.username)