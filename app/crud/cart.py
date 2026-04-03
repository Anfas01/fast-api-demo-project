from sqlalchemy.orm import Session
from schemas.cart import CartCreate
from models.cart import Cart
from fastapi import HTTPException
from models.product import Product
from sqlalchemy import and_





def create_cart(db: Session, cart: CartCreate, owner_id: int):
    product = db.query(Product).filter(Product.name==cart.product_name).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # A quantity of 0 or less is a bad request, not a "not found" error.
    if cart.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be a positive number")
    
    db_cart = db.query(Cart).filter(and_(Cart.owner_id == owner_id, Cart.product_id == product.id)).first()

    if db_cart:
        # If the item is already in the cart, just update the quantity
        db_cart.quantity += cart.quantity
    else:
        # Otherwise, create a new cart item
        db_cart = Cart(owner_id=owner_id, product_id=product.id, quantity=cart.quantity)
        db.add(db_cart)
        
    db.commit()
    db.refresh(db_cart)

    return {"message": f"Cart updated successfully. You now have {db_cart.quantity} of '{product.name}'."}


def view_cart(db: Session, owner_id: int):
    cart = db.query(Cart).filter(Cart.owner_id==owner_id).all()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart is empty")
    
    # Extract the product name from the relationship for the response
    return [{"product_name": item.product.name, "quantity": item.quantity} for item in cart]


def remove_from_cart(db: Session, product_name: str, owner_id: int):
    product = db.query(Product).filter(Product.name==product_name).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    cart = db.query(Cart).filter(and_(Cart.owner_id == owner_id, Cart.product_id == product.id)).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Product not found in cart")
    
    db.delete(cart)
    db.commit()

    return {"message": f"{product_name} has been removed from your cart"}