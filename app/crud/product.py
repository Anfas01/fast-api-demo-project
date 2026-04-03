from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.product import Product
from models.cart import Cart
from models.order import Order
from schemas.product import ProductCreate


def product_create(product: ProductCreate, db: Session, owner_id: int):
    existing_product = db.query(Product).filter(Product.name==product.name).first()

    if existing_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    db_product = Product(name=product.name, owner_id=owner_id)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return {"message": f"{product.name} has been created successfully"}


def get_all_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_name: str):
    product =  db.query(Product).filter(Product.name==product_name).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product


def delete_product(db: Session, product_name: str, owner_id: int):
    existing_product = db.query(Product).filter(Product.name==product_name).first()

    if not existing_product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    if existing_product.owner_id != owner_id:
        raise HTTPException(status_code=401, detail="You are not authorized to delete this product")
    
    # Safely remove product references in carts and orders to avoid Foreign Key constraint errors
    db.query(Cart).filter(Cart.product_id == existing_product.id).delete()
    db.query(Order).filter(Order.product_id == existing_product.id).delete()

    db.delete(existing_product)
    db.commit()
    

    return {"message": f"{product_name} has been deleted successfully"}

    