from pydantic import BaseModel
from typing import List





class OrderResponseModel(BaseModel):
    product_id: int
    quantity: int


    class Config:
        from_attributes = True

class OrderPlacementResponse(BaseModel):
    message: str
    order: List[OrderResponseModel]

    class Config:
        from_attributes = True
