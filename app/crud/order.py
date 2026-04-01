from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.order import Order
from models.cart import Cart
from sqlalchemy import and_




def place_order(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.owner_id == user_id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty, please add products to your cart")

    processed_orders = []

    for item in cart_items:
        # Correctly find an existing order for this specific user and product
        existing_order = db.query(Order).filter(and_(Order.user_id == user_id, Order.product_id == item.product_id)).first()

        if existing_order:
            # If it exists, just update the quantity
            existing_order.quantity += item.quantity
            db.add(existing_order)
            processed_orders.append(existing_order)
        else:
            # Otherwise, create a new order record for the user
            order = Order(user_id=user_id, product_id=item.product_id, quantity=item.quantity)
            db.add(order)
            processed_orders.append(order)
        
        # After processing, mark the cart item for deletion
        db.delete(item)
    
    db.commit() # Commit all changes (adds, updates, deletes) in a single transaction
    
    for o in processed_orders:
        db.refresh(o)
        
    return {"message": f"User {user_id} order placed", "order": processed_orders}



def view_order(db: Session, user_id: int):
    order = db.query(Order).filter(Order.user_id==user_id).all()

    if not order:
        raise HTTPException(status_code=404, detail="You have no placed orders")
    
    return order


def cancel_order(db: Session, product_id: int, user_id: int):
    order = db.query(Order).filter(and_(Order.user_id==user_id, Order.product_id==product_id)).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()

    return {"message": f"Order for product ID {product_id} has been cancelled"}