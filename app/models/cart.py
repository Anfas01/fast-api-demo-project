from core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    owner_name = Column(String, ForeignKey("users.username"))
    product_name = Column(String, ForeignKey("products.name"))
    quantity = Column(Integer)

    owner = relationship("User")
    product = relationship("Product")