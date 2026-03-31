from fastapi import FastAPI
from core.database import Base, engine
from routers import user, product, authentication, cart, order


app = FastAPI()

Base.metadata.create_all(bind=engine)



app.include_router(authentication.router,prefix="/auth", tags=["Auth"])
app.include_router(user.router,prefix="/users",tags=["Users"])
app.include_router(product.router,prefix="/products",tags=["Products"])
app.include_router(cart.router,prefix="/cart",tags=["Cart"])
app.include_router(order.router,prefix="/order",tags=["Order"])
