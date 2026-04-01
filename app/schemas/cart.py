from pydantic import BaseModel


class CartCreate(BaseModel):
    product_id: int
    quantity: int


class CartResponseModel(BaseModel):
    product_id: int
    quantity: int

    class Config:
        from_attributes = True