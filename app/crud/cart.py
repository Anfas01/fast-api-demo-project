from sqlalchemy.orm import Session
from schemas.cart import CartCreate
from models.cart import Cart
from fastapi import HTTPException
from models.product import Product
from sqlalchemy import and_





def create_cart(db: Session, cart: CartCreate, owner_name: str):
    product = db.query(Product).filter(Product.name==cart.product_name).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # A quantity of 0 or less is a bad request, not a "not found" error.
    if cart.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be a positive number")
    
    db_cart = db.query(Cart).filter(and_(Cart.owner_name == owner_name, Cart.product_name == cart.product_name)).first()

    if db_cart:
        # If the item is already in the cart, just update the quantity
        db_cart.quantity += cart.quantity
    else:
        # Otherwise, create a new cart item
        db_cart = Cart(owner_name=owner_name, product_name=cart.product_name, quantity=cart.quantity)
        db.add(db_cart)
        
    db.commit()
    db.refresh(db_cart)

    return {"message": f"Cart updated successfully. You now have {db_cart.quantity} of {db_cart.product_name}."}


def view_cart(db: Session, owner_name: str):
    cart = db.query(Cart).filter(Cart.owner_name==owner_name).all()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart is empty")
    
    return cart


def remove_from_cart(db: Session, product_name: str, owner_name: str):
    cart = db.query(Cart).filter(and_(Cart.owner_name == owner_name, Cart.product_name == product_name)).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Product not found in cart")
    
    db.delete(cart)
    db.commit()

    return {"message": f"{product_name} has been removed from cart successfully"}