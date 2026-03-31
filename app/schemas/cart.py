from pydantic import BaseModel


class CartCreate(BaseModel):
    product_name: str
    quantity: int


class CartResponseModel(BaseModel):
    product_name: str
    quantity: int

    class Config:
        from_attributes = True