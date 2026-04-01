from fastapi import APIRouter, Depends
from models.user import User
from schemas.product import ProductCreate, ProductsResponseModel, ProductUpdate
from sqlalchemy.orm import Session
from crud.product import product_create, get_all_products, get_product, update_product, delete_product
from core.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return product_create(product, db, current_user.id)

@router.get("/")
def read_all_products(db: Session=Depends(get_db), current_user: User = Depends(get_current_user)) -> list[ProductsResponseModel]:
    return get_all_products(db)

@router.get("/{product_name}")
def get_product_by_id(product_name: str, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)) -> ProductsResponseModel:
    return get_product(db, product_name)


@router.put("/{old_product}")
def product_update(old_product: str, new_product: ProductUpdate, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_product(db, old_product, new_product, current_user.id)


@router.delete("/{product_name}")
def product_delete(product_name: str, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_product(db, product_name, current_user.id)