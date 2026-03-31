from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.product import Product


def product_create(product, db: Session, owner_name: str):
    existing_product = db.query(Product).filter(Product.name==product.name).first()

    if existing_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    db_product = Product(name=product.name, owner_name=owner_name)

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

def update_product(db: Session, old_product, new_product, owner_name: str):
    product = db.query(Product).filter(Product.name==new_product.product_name).first()
    
    existing_product = db.query(Product).filter(Product.name==old_product).first()

    if not existing_product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    if product:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    if existing_product.owner_name != owner_name:
        raise HTTPException(status_code=401, detail="You are not authorized to update this product")
    

    
    if new_product.product_name is not None:
        existing_product.name = new_product.product_name
    

    db.add(existing_product)
    db.commit()
    db.refresh(existing_product)

    return {"message": f"{old_product} has been updated to {existing_product.name} successfully"}



def delete_product(db: Session, product, owner_name):
    existing_product = db.query(Product).filter(Product.name==product).first()

    if not existing_product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    if existing_product.owner_name != owner_name:
        raise HTTPException(status_code=401, detail="You are not authorized to delete this product")
    
    db.delete(existing_product)
    db.commit()
    

    return {"message": f"{product} has been deleted successfully"}

    