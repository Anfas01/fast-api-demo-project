from pydantic import BaseModel
from typing import List





class OrderResponseModel(BaseModel):
    product_name: str
    quantity: int


    class Config:
        from_attributes = True

class OrderPlacementResponse(BaseModel):
    message: str
    order: List[OrderResponseModel]

    class Config:
        from_attributes = True
