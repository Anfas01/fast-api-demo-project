from core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, ForeignKey("users.username"))
    product_name = Column(String, ForeignKey("products.name"))
    quantity = Column(Integer)

    user = relationship("User")
    product = relationship("Product")