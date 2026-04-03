from pydantic import BaseModel



class ProductCreate(BaseModel):
    name: str
  

class ProductsResponseModel(BaseModel):
    name: str
    owner_id: int
    
    class Config:
        from_attributes = True

class ProductName(BaseModel):
    name: str 

    class Config:
        from_attributes = True


