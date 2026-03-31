from pydantic import BaseModel
from typing import List
from schemas.product import ProductName



class UsersResponseModel(BaseModel):
    username: str
    products: List[ProductName] = []
    
    class Config:
        from_attributes = True


class UserResponseModel(BaseModel):
    username: str
    email: str
    products: List[ProductName] = []
    
    class Config:
        from_attributes = True