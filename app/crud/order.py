from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.order import Order
from models.cart import Cart
from models.product import Product
from sqlalchemy import and_




def place_order(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.owner_id == user_id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty, please add products to your cart")

    processed_orders = []

    for item in cart_items:
        # create a new order record for the user
        order = Order(user_id=user_id, product_id=item.product_id, quantity=item.quantity)
        db.add(order)
        processed_orders.append(order)
        # After processing, mark the cart item for deletion
        db.delete(item)
    
    db.commit() # Commit all changes (adds, updates, deletes) in a single transaction
    
    for o in processed_orders:
        db.refresh(o)
        
    return {"message": f"order confirmed", "order": [{"product_name": o.product.name, "quantity": o.quantity} for o in processed_orders] }   



def view_order(db: Session, user_id: int):
    order = db.query(Order).filter(Order.user_id==user_id).order_by(Order.id.desc()).all()

    if not order:
        raise HTTPException(status_code=404, detail="You have no placed orders")
    
    # Return formatted data to match OrderResponseModel
    return [{"product_name": o.product.name, "quantity": o.quantity} for o in order]


def cancel_order(db: Session, product_name: str, user_id: int):
    product = db.query(Product).filter(Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    order = db.query(Order).filter(and_(Order.user_id==user_id, Order.product_id==product.id)).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()

    return {"message": f"Order for '{product_name}' has been cancelled"}