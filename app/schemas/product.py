from pydantic import BaseModel



class ProductCreate(BaseModel):
    name: str
  

class ProductsResponseModel(BaseModel):
    name: str
    user_id: str
    
    class Config:
        from_attributes = True

class ProductName(BaseModel):
    name: str 

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    product_name: str | None = None



    class Config:
        from_attributes = True
